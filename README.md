## Overview
This repo contains a FastAPI / SQL DB project, the purpose of which is to create a way for users to search for all inclusive resorts matching their parameters. 

## Running the Project
This project is run from your local machine in a venv. 

1. Navigate to a directory where you wish to create a venv (this should not be in the project directory).
2. Run the command "python3 -m venv vacation_resort_app".
3. Once the venv has been created, activate the venv. 
    - On a Mac, from the ../vacation_resort_app venv directory, run the command "source ./bin/activate" from the terminal. Ensure that your terminal session's active command line now shows (vacation_resort_app) at the beginning of the command line. 
    - On a Windows machine, from the ../vacation_resport_app directory, run the command ".\Scripts\activate". Ensure that your terminal session's active command line now shows (vacation_resort_app) at the beginning of the command line. 
4. Now, with the venv activated, navigate to the vacation_resort_app project folder and run the command "pip install -r requirements.txt" to download all necessary pip packages. If you are prompted to upgrade pip at the end of the installation, do so. 
5. Now that the venv has been set up, you can run the application from the same location via "python ./app/main.py". You will see output in the terminal session indicating that the uvicorn server is live. 

## Collaboration Instructions
This project is being set up with the intention for engineers to collaborate and add code, open PRs, and conduct code reviews. As such, a standardized process should be adhered to by all members of the repo to keep the project workflow organized. 

- The Git branching strategy is **trunk based**, centered on the **develop** branch. The general strategy to be followed is:
    1. The master branch will update the prod environment. 
    2. The develop branch will be created off of the prod branch. 
    3. The develop branch will be merged directly into master when code updates to prod need to be made. Feature branches to prod are not currently allowed in this project.
    4. Each user will create a named branch off of the develop branch, e.g. **git checkout -b Jimmy**. This developer branch will be where code updates are made before being merged into develop via the PR process. 
    5. Once a PR is created from the developer's branch to develop, a PR will be conducted. Once merged and tested in the lower environment, a PR to master may be opened. Updates to prod via this process will take place during scheduled change windows to minimize disruption to users. 
 