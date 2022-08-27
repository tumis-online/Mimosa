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

DarkOrange="\033[38;5;202m"   # DarkOrange
Orange="\033[38;5;220m"   # Orange

# Background
On_Black="\033[40m"       # Black
On_Red="\033[41m"         # Red
On_Green="\033[42m"       # Green
On_Yellow="\033[43m"      # Yellow
On_Blue="\033[44m"        # Blue
On_Purple="\033[45m"      # Purple
On_Cyan="\033[46m"        # Cyan
On_White="\033[47m"       # White

On_Orange="\033[48;5;220m"  # Orange

# apt install portaudio19-dev python3-pyaudio

# ENV Variables
export PYTHONPATH="${PYTHONPATH}:/RASA"
SAPHIR_DIR="$(pwd)"
export SAPHIR_DIR
export PROJECT_GROUP="mimosa"

echo -e "************************"
echo -e "************************"
echo -e "********${On_White}        ${Color_Off}********"
echo -e "********${On_White}        ${Color_Off}********"
echo -e "********${On_White}${Orange}~MIMOSA~${Color_Off}********"
echo -e "********${On_Orange}     °  ${Color_Off}********"
echo -e "********${On_Orange}      ° ${Color_Off}********"
echo -e "********${On_Orange}  o     ${Color_Off}********"
echo -e "*********${On_Orange}   °  ${Color_Off}*********"
echo -e "**********${On_Orange}    ${Color_Off}**********"
echo -e "***********${On_Orange}  ${Color_Off}***********"
echo -e "***********${On_White}  ${Color_Off}***********"
echo -e "********${On_White}        ${Color_Off}********"
echo -e "************************"
echo -e "************************"

check_status() {
  if [ $? -eq 0 ]; then
   echo -e "${Green}OK${Color_Off}"
  else
     echo -e "${Red}FAILED${Color_Off}"
  fi
}

# Add group, add user to group and grant permission to user and group
groupadd $PROJECT_GROUP
usermod -aG $PROJECT_GROUP "$(whoami)"
chgrp -R -v $PROJECT_GROUP -

#echo "Building Docker images..."
#echo "Building RASA NLU Server Docker Image..."
#docker build . -t rasa-nlu-server:${RASA_NLU_SERVER_TAG} \
#               -f docker/Dockerfile.rasa_nlu_server
#check_status
#

echo "Building Base Cube One Docker Containers..."
# TODO build bco docker containers according to doc

check_status

# Generate secure Token for the application admin at start and store persistently in .bashrc
# TODO: Generate individual token, https://pypi.org/project/secrets/,
#       https://blog.miguelgrinberg.com/post/the-new-way-to-generate-secure-tokens-in-python
echo "Creating auth token for the application..."
if [[ -z "${SAPHIR_AUTH_TOKEN}" ]]; then
  echo "export SAPHIR_AUTH_TOKEN='PbnveAR7aAY-M5Cw1cIvyDZDvO8'" >> ~/.bashrc
fi
check_status

echo "Starting Docker containers via Docker Compose..."
# Start Docker Containers via docker-compose

  # --build
check_status
