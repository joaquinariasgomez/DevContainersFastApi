# DevContainers + FastAPI + MongoDB

Microsoft Dev Containers allow you to create isolated development environments, which makes it easier to develop and collaborate, without worrying about compatibility issues.

In this template, we have two services:

- The main application, which is developed in Python using FastAPI framework.
- The database with which the main application will communicate.

Here, the Python service is not containerized by default. This emulates a scenario where application is developed locally, with all the dependencies controlled inside a Python virtual environment.

Even though this app makes it to production inside a Docker container, this is the usual way ot develop an application locally.

The database, however, is deployed inside a Docker container, using a docker-compose.yml file for simplicity. We are using MongoDB for this.

## What does the app do?

I created a simple CRUD