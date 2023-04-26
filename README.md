# DevContainers + FastAPI + MongoDB

Microsoft Dev Containers allow you to create isolated development environments, which makes it easier to develop and collaborate, without worrying about compatibility issues.

In this template, we have two services:

- The main application, which is developed in Python using FastAPI framework.
- The database with which the main application will communicate.

Here, both the Python service and the dababase are containerized, using the help of a docker-compose file. This emulates a scenario where the user can comfortably do <code>docker-compose up</code>, and launch the whole app with all its dependencies.

## What does the app do?

I created a simple CRUD
