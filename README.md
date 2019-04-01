# DevOps Engineer Interview
This is an interview for the DevOps engineer role at BMO Capital Markets' Data Cognition Team. 

## Requirements 
1. Dockerize a given web application including both client-side and server-side code assets.
2. Set up a CI/CD pipeline to automate the procedure of building/deploying this application. 
3. You are free to use any framework/language to implement the CI/CD pipeline. Yet, we prefer to seeing your implementation in Cloud environment like AWS. 

## Code provided
We've provided code assets related to the web application. You don't need to add new functions to the application. 

We've provided: 
- front/index.html containing the front-end code of the application, which consumes data fed from a backend api.
- front/nginx.conf containing the configuration for nginx server, which defines port/route mappings of both front-end(:3000/) and back-end(:5000/api/) endpoints.
- back/run.py containing the back-end code of the application, which defines route and content of the backend api.
- back/requirements.txt containing the back-end libraries needed to be preinstalled. 
    
## Functionality
- Dockerfile/docker-compose scripts are expected to orchestrate the process of launch the application on a single server.
- Code Repository(s) is/are expected to accept code changes for front/back-end codes changes.
- When code changes are uploaded, tasks to build/deploy code changes are triggered automatically. 

## Challenge Scope
- High level description of design and technologies used
- Document all assumptions made
- Complete solutions aren't required, but what you do submit needs to run

## What are we looking for? What does this prove?
- Assumptions you make given limited requirements
- Technology and design choices
- Identify areas of your strengths
- This is not a pass or fail test, this will serve as a common ground that we can deep dive together into specific issues

## Scalability and production
- How would you bring the application to production? 
- How would you scale the application to support thousands of users?
- What considerations would you take into account to increase its scalablity and reliability?
