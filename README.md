## Overview
This repo contains a FastAPI / SQL DB project, the purpose of which is to create a way for users to search for all inclusive resorts matching their parameters. 

## Running the Project
This project is run with Docker. In the near future, the project will be updated to a Docker Compose project to handle orchestration of various micro-services. 

The steps for running this project are:

1. From the project directory, run the command **docker build -t resort_app .**

2. Run the command **docker run -d -p 80:80 resort_app**

3. Navigate to your browser and go to **localhost:80**. You should see the message: {"Hello":"World"}