#/bin/bash

source /etc/temp_controller.txt && echo "variables added!"

python3 main.py > /var/log/aquarium-temp-controller/"$(date +"%Y_%m_%d_%I_%M_%p").log"

