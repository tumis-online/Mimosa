#!/bin/bash

# BASH Colors: https://gist.github.com/vratiu/9780109

# Reset
Color_Off="\033[0m"       # Text Reset

# Regular Colors
Black="\033[0;30m"        # Black
Red="\033[0;31m"          # Red
Green="\033[0;32m"        # Green
Yellow="\033[0;33m"       # Yellow
Blue="\033[0;34m"         # Blue
Purple="\033[0;35m"       # Purple
Cyan="\033[0;36m"         # Cyan
White="\033[0;37m"        # White

# Background
On_Black="\033[40m"       # Black
On_Red="\033[41m"         # Red
On_Green="\033[42m"       # Green
On_Yellow="\033[43m"      # Yellow
On_Blue="\033[44m"        # Blue
On_Purple="\033[45m"      # Purple
On_Cyan="\033[46m"        # Cyan
On_White="\033[47m"       # White

# apt install portaudio19-dev python3-pyaudio

# ENV Variables
export PYTHONPATH="${PYTHONPATH}:/RASA"
SAPHIR_DIR="$(pwd)"
export SAPHIR_DIR

echo -e "${On_Purple}****** SAPHIR ******${Color_Off}"

check_status() {
  if [ $? -eq 0 ]; then
   echo -e "${Green}OK${Color_Off}"
  else
     echo -e "${Red}FAILED${Color_Off}"
  fi
}

#echo "Building Docker images..."
#echo "Building RASA NLU Server Docker Image..."
#docker build . -t rasa-nlu-server:${RASA_NLU_SERVER_TAG} \
#               -f docker/Dockerfile.rasa_nlu_server
#check_status
#
export RASA_ACTION_SERVER_TAG=0.2
echo "Building RASA Action Server Docker Image..."
docker build . -t rasa-action-server:${RASA_ACTION_SERVER_TAG} \
               -f docker/Dockerfile.rasa_action_server
check_status

# Generate secure Token for the application admin at start and store persistently in .bashrc
# TODO: Generate individual token, https://pypi.org/project/secrets/,
#       https://blog.miguelgrinberg.com/post/the-new-way-to-generate-secure-tokens-in-python
echo "Creating auth token for the application..."
echo "export SAPHIR_AUTH_TOKEN='PbnveAR7aAY-M5Cw1cIvyDZDvO8'" >> ~/.bashrc
export SAPHIR_AUTH_TOKEN='PbnveAR7aAY-M5Cw1cIvyDZDvO8'
check_status

echo "Starting Docker containers via Docker Compose..."
# Start Docker Containers via docker-compose
docker compose --project-directory . --env-file .env --file docker/docker-compose.yml up \
  --detach \
  # --build
check_status
