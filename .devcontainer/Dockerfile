ARG PYTHON_VERSION
FROM mcr.microsoft.com/devcontainers/python:0-${PYTHON_VERSION}

# One way of installing requirements is to copy them into a temporary dir, install them using pip and then removing them
# Another way is using "postCreateCommand", inside devcontainer.json, which is what we are currently doing
# COPY app/requirements.txt /tmp/pip-tmp/
# RUN pip3 install -r /tmp/pip-tmp/requirements.txt && rm -rf /tmp/pip-tmp