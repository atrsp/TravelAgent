#Use the aws base image for python 3.12
FROM public.ecr.aws/lambda/python:3.12

#Install build-essential compiler and tools
RUN microdnf update -y && microdnf install -y gcc-c++ make

#Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

#Install packages
RUN pip install -r requirements.txt

#Copy function code
COPY travelAgentV4.py ${LAMBDA_TASK_ROOT}

#Set permissions to make this file executable
RUN chmod +x travelAgentV4.py

#Set the cmd
CMD ["travelAgentV4.lambda_handler"]
