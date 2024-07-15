import os
import json

from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

#To Add RAG
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings 
from langchain_community.vectorstores.chroma import Chroma

import bs4
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
llm = ChatOpenAI(model="gpt-3.5-turbo")

def researchAgent(query, llm):
    tools = load_tools(['ddg-search', 'wikipedia'], llm = llm)
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, promot=prompt, verbose=False)
    webContext = agent_executor.invoke({"input":query})
    return webContext['output']

def loadData():
    loader = WebBaseLoader(
        web_paths= ("https://www.dicasdeviagem.com/inglaterra/",), 
        bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_= ("postcontentwrap", "pagetitleloading background-imaged loading-dark")))  #inspecionamos a pagina para pegarmos as pts do site que queremos importar e usar (textos e titulo)
    )
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap = 200) #método que faz a separação de tudo que é texto dentro da página em pedaços/docs de 1000 tokens cujos 200 primeiros tokens são iguais ao doc anterior
    splits = text_splitter.split_documents(docs)
    vector_store = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
    retriever = vector_store.as_retriever()
    return retriever

def getRelevantDocs (query): #captura os elementos importantes desses docs
    retriever = loadData()
    relevant_documents = retriever.invoke(query)
    return relevant_documents

def supervisorAgent (query, llm, webContext, relevant_documents):
    prompt_template = """" Você é o gerente de uma agência de viagens. 
    Sua resposta final deve ser um roteiro de viagem completo e detalhado. 
    Utilize o contexto de eventos, os preços de passagens, o input do usuário e os documentos relevantes para elaborar o roteiro.
    Contexto: {webContext}
    Documento relevante: {relevant_documents}
    Usuario: {query}
    Assistente:
    """
    prompt = PromptTemplate(
        input_variables=['webContext', 'relevant_documents', 'query'],
        template=prompt_template
    )

    sequence = RunnableSequence(prompt | llm)
    response = sequence.invoke({"webContext":webContext, "relevant_documents":relevant_documents, "query":query})
    return response

def getResponse (query, llm):
    webContext = researchAgent (query, llm)
    relevant_documents = getRelevantDocs(query)
    response = supervisorAgent (query, llm, webContext, relevant_documents)
    return response

def lambda_handler (event, context):
    body = json.loads(event.get('body', {}))
    query = body.get('question', 'Parâmetro question não fornecido')
    response = getResponse(query, llm).content
    return {
        "statusCode":200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps ({
            "message": "Tarefa concluída com sucesso.",
            "detais": response,
        })      
    }