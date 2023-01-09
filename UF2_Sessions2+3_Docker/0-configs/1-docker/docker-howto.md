# Docker HowTo
-------------------------------------------------------------------------------

# 1. Docker installation
- sudo apt install docker.io
- sudo apt install docker-compose
- sudo usermod -aG docker $USER
- poweroff --reboot
- groups


# 2. Create an image: Manual method
- The Dockerfile method is preferred, but here is how to do it manually:
- docker image pull ubuntu
- docker run -it --name CONTAINER_NAME ubuntu bash
  Example: docker run -it --name bio ubuntu bash
- (As root inside the container)
  apt update
  apt upgrade
  apt install dialog apt-utils
  apt install nano
  apt install zip
  apt install git
  apt install lynx
  apt install curl
  apt install sqlite3

  apt install python3 python3-pip python3-venv python-is-python3

  python -m venv /opt/bio-venv

  pip install -Ur requirements.txt
  [Ctrl-D]

- docker container commit CONTAINER_NAME IMAGE_NAME
  Example: docker container commit bio bio


# 3. Create an image: Dockerfile method (recommended)
- Command: docker image build --tag IMAGE-NAME:TAG --file Dockerfile     .
- Example: docker image build --tag bio            --file dev.Dockerfile .
- Dockerfile reference: https://docs.docker.com/engine/reference/builder/


# 4. Run new container with shared folder
docker container prune

docker run \
-it \
--name bio \
--mount src=DIR_OUTSIDE,target=DIR_INSIDE,type=bind \
bio bash

- (Run web server inside the container)
- python -m http.server

- (Open web browser pop-os to localhost:8000)


# 5. Ports
- Publish ports:
  - https://www.mend.io/free-developer-tools/blog/docker-expose-port/


# 6. Volumes
- Volumes:
  - https://earthly.dev/blog/docker-mysql/
  - https://docs.docker.com/storage/volumes/

- Volume backups:
  - https://onelinerhub.com/docker/how-to-extract-file-from-docker-image
  - https://www.howtogeek.com/devops/how-to-back-up-your-docker-volumes/


# 7. VS Code configuration
- Extensions to install on VSCode
  - 'Docker' by Microsoft
  - 'Dev Containers' by Microsoft
- Extensions to install on the container
  - 'Python' by Microsoft


-------------------------------------------------------------------------------

