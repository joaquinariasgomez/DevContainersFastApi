# DevContainers + FastAPI + MongoDB

Microsoft Dev Containers allow you to create isolated development environments, which makes it easier to develop and collaborate, without worrying about compatibility issues.

In this template, we have two services:

- The main application, which is developed in Python using FastAPI framework.
- The database with which the main application will communicate.

Here, the Python service is not containerized by default. This emulates a scenario where application is developed locally, with all the dependencies controlled inside a Python virtual environment.

Even though this app makes it to production inside a Docker container, this is the usual way ot develop an application locally.

The database, however, is deployed inside a Docker container, using a docker-compose.yml file for simplicity. We are using MongoDB for this.

## What does the app do?

# TODO: poner gráfico de la app aqui

## Deploying the app, locally

In order to get this app up and running, we need to deploy the two services.

First, we need to deploy the database. A simple ```docker-compose``` command will do:
```
$ docker-compose up -d
```

Then, we can deploy the main service inside a Python virtual environment (to avoid dependency issues). We are using Python 3.10 for this app:
```
$ python -m venv venv
$ source venv/bin/activate
```

Now, we deploy the application inside the virtual environment one of two ways:
```
$(venv) pip install -r app/requirements.txt
$(venv) python app/main.py
```

Or do ```make all```, which will deploy the database, install the requirements and deploy our application for us.
```
$(venv) make all
```

## Deploying the app, using Dev Containers extension

In order to get this app up and running, we still need to deploy the two services.

First, we need to deploy the database, as before:
```
$ docker-compose up -d
```

Then, we now can open the environment inside a Development Container using the Dev Container extension shortcut: ```Open Folder in Container```. If you have opened this workspace before, you can click on the extension ```Reopen in Container```, which will remember your container.

Once inside the container, the dependencies must be installed due to *postCreateCommand* from *devcontainer.json*. Here, we don't need a Python virtual environment, since we are currently in one!

To launch the app service:
```
$ python app/main.py
```

Or
```
$ make run
```
