# NLP-webapp-streamlit | Deploy a NLP model into a web app with streamlit, docker, and AWS.  

As a data scientist, I work on different data science/data analytics projects on daiy basis. Recently I am working on a NLP project and thought that would be cool to deploy a data science project into a product -- a web app. After talking with some SDE friends, doing online research, I decided to make a protype with Streamlit, Docker, and AWS. That's the whole story behind this product. 

### 1. Deploy the data app with Streamlit 
Stream is an open-source app framework for data scientist and machine learning engineers to deploy their data app in a short period of time.  
Check their webiste for documents and all the demos: https://streamlit.io/ 

### 2. Containerizing a Streamlit web app with Docker 
Docker is powerful tool for maintaining reproducible work and portability of the compute environment, enables you to separate your applications from your infrastructure so you can deliver software quickly. Docker documents: https://docs.docker.com/ 

### 3. Push the Streamlit web app on the cloud   
I pushed this streamlit app docker image on an EC2 instance on AWS. I set up docker on a clean EC2 instance, you can find a EC2 with a docker installed already. 
