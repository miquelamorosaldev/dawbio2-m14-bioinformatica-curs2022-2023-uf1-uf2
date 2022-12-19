# Docker HowTo
-------------------------------------------------------------------------------

# 1. Docker installation
- sudo apt install docker.io
- sudo apt install docker-compose
- sudo usermod -aG docker $USER
- poweroff --reboot
- groups


# 2. Create an image with PHP environment
- Use the Dockerfile!
- But if you want to do it manually:
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


# 3. Run new container with shared folder and published port
docker container prune

docker run \
-it \
--name bio \
--mount src=DIR_OUTSIDE,target=DIR_INSIDE,type=bind \
bio bash

- (Run web server inside the container)
- python -m http.server

- (Open web browser pop-os to localhost:8000)


# 4. VS Code configuration
- Extensions to install on VSCode
  - 'Docker' by Microsoft
  - 'Dev Containers' by Microsoft
- Extensions to install on the container
  - 'Python' by Microsoft


-------------------------------------------------------------------------------

