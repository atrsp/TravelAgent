# TravelAgent
#### -> An API that develops travel itineraries with contextual and real time informations.

## Technologies used: 
    - Docker
    - AWS Cloud
    - OpenAI GPT-3.5 Turbo
    - OpenAI Embedding Models

## The project:

![fluxograma3](https://github.com/user-attachments/assets/3f7ac6b5-61c9-4879-8aca-62f4f4e1e5b4)

## Libraries required: 
    bs4
    chromadb
    wikipedia
    langchain
    langchainhub
    langchain-core
    langchain-openai
    duckduckgo-search
    langchain-community
    langchain-text-splitters 
###### *Available on "requirements.txt"
    

## Tips:
> ###### Disclaimer: I developed this project on Windows 11.
> 
### 1. Virtual Environment
  I used a Virtual Environment to download all the libraries listed above.

  <details>
  <summary>a. Create a Virtual Environment:</summary>

  -     python -m venv .venv
</details> 

  <details>
  <summary>b. Change Command Prompt permissions:</summary>

  > This needs to be done before you activate the environment
  -     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
</details> 

<details>
  <summary>c. Activate the environment:</summary>
  -     .venv/Scripts/activate
</details> 
 
        
> PS: after these instructions, you terminal should have a "(.venv)" before "PS C:\\...\\_project_folder_" 

### 2. OpenAI Access Key

> To work with the OpenAI API, we need to have an access key, which I stored in a ".env" file (The .env file isn't in this repository because it should be kept private).
This way, we would need to run "source .env" before every time we wish to run our code. 

##### To automate this, I used the "dotenv" library:

 <details>
  <summary>a. Install dotenv:</summary>

  -     pip install python-dotenv
</details> 
                                                       
 <details>
  <summary>b. Import it in file:</summary>

  -     from dotenv import load_dotenv
</details> 

 <details>
  <summary>c. Add this function as the first code line:e</summary>
     
> This is what automatizes "source .env"
     
  -     load_dotenv()
  
</details> 

#

###### This project was taught during NLW Dev, an event hosted by Rocketseat on july 2024, by <a href="https://www.linkedin.com/in/daniel-omar-soria?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app">Daniel Omar Soria Santos</a>.
