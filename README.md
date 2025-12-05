## Overview
This repo contains a FastAPI / SQL DB project, the purpose of which is to create a way for users to search for all inclusive resorts matching their parameters. 

## Running the Project
This project is run with Docker. In the near future, the project will be updated to a Docker Compose project to handle orchestration of various micro-services. 

The steps for running this project are:

1. From the project directory, run the command **docker build -t resort_app .**

2. Run the command **docker run -d -p 80:80 resort_app**

3. Navigate to your browser and go to **localhost:80**. You should see the message: {"Hello":"World"}

## Collaboration Instructions
This project is being set up with the intention for engineers to collaborate and add code, open PRs, and conduct code reviews. As such, a standardized process should be adhered to by all members of the repo to keep the project workflow organized. 

- The Git branching strategy is **trunk based**, centered on the **develop** branch. The general strategy to be followed is:
    1. The master branch will update the prod environment. 
    2. The develop branch will be created off of the prod branch. 
    3. The develop branch will be merged directly into master when code updates to prod need to be made. Feature branches to prod are not currently allowed in this project.
    4. Each user will create a named branch off of the develop branch, e.g. **git checkout -b Jimmy**. This developer branch will be where code updates are made before being merged into develop via the PR process. 
    5. Once a PR is created from the developer's branch to develop, a PR will be conducted. Once merged and tested in the lower environment, a PR to master may be opened. Updates to prod via this process will take place during scheduled change windows to minimize disruption to users. 
 