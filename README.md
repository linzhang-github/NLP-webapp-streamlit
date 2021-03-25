# NLP-webapp-streamlit 
# Deploy a NLP model into a web app with streamlit, docker, and AWS.  

As a data scientist, I work on different data science/data analytics projects on daily basis. Recently I designed and implemented a NLP model to reinvent the digital subcription strategy for a digital journal. We aim to help journalists/writers to create better content and approach right readers. In this NLP model, I automated the text mining process for over 20,000 articles and performed in-depth sentiments analysis and readability metrics analysis.  In order to enable our end-users to use our NLP model to evaluate their content -- they don't need to be a programer to run the codes, I deployed this NLP model into a web application and delivered this prototype with Streamlit, Docker, and AWS.  

### 1. Deploy the data app with Streamlit 
Stream is an open-source app framework for data scientist and machine learning engineers to deploy their data app in a short period of time.  
Check their webiste for documents and all the demos: https://streamlit.io/ 

### 2. Containerizing a Streamlit web app with Docker 
Docker is powerful tool for maintaining reproducible work and portability of the compute environment, enables you to separate your applications from your infrastructure so you can deliver software quickly. Docker documents: https://docs.docker.com/ 

### 3. Push the Streamlit web app on the cloud   
I pushed this streamlit app docker image on an EC2 instance on AWS. I set up docker on a clean EC2 instance, you can find a EC2 with a docker installed already. Here's the guide about docker installation on AWS instances: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html
