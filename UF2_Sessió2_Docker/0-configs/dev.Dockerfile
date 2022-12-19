# Dockerfile for building DawBio2 M14 Bio Development Image
# -----------------------------------------------------------------------------
# Tutorial:       https://geekflare.com/dockerfile-tutorial/
# Best practices: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
# Reference:      https://docs.docker.com/engine/reference/builder/

# Clean previous: docker container stop -t 1 bio
#                 docker container rm bio
#                 docker image     rm bio

# Build Cmdline:  docker image     build --tag IMAGE-NAME:TAG --file Dockerfile     .
# Example:        docker image     build --tag bio            --file dev.Dockerfile .
# Beware:         The dot at the end is the build context.

# Run:            docker container run   -it --name bio --mount src=DIR_OUTSIDE,target=DIR_INSIDE,type=bind bio bash
# Note:           Directories must be absolute paths

# VSCode:         Remember to install Python extensions in each container.



# Commands for building the development image
# -----------------------------------------------------------------------------

# Set the base image to Ubuntu latest LTS
FROM ubuntu

# Temporary environment variables so that apt does not complain
# https://github.com/phusion/baseimage-docker/issues/319
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NOWARNINGS="yes"

# Apt: Update the repository sources list, install apt-utils (complains otherwise) and upgrade packages
# 'apt-get' has a stable CLI interface. Do not use 'apt' as it does not.
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get upgrade -y

# Basic system utilities
RUN apt-get install -y dialog nano tree zip git sqlite3 curl lynx

# Python packages. python3 is already installed but write it for completeness.
RUN apt-get install -y python3 python3-venv python3-pip python-is-python3

# Python Virtual Environment
# - https://docs.python.org/3/library/venv.html
# - https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
# - Not strictly necessary inside a container, but can avoid conflicts. Pip complains.
ENV VIRTUAL_ENV=/opt/bio-venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install python dependencies
COPY requirements.txt /
RUN  pip install -Ur requirements.txt
RUN  rm /requirements.txt

# Python configs
ENV PYTHONDONTWRITEBYTECODE=1



# Additional commands for app deployment
# -----------------------------------------------------------------------------

# Expose a port to communicate
# EXPOSE 8080

# Create the default app directory
# RUN mkdir -p /app

# Copy the application
# COPY . /app/

# Run the application:
# WORKDIR /app/
# CMD ["python", "app.py"]

# -----------------------------------------------------------------------------
