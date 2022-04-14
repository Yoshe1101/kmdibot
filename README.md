# kmdibot
bot to check embassy appointments


#How to use it 

##1- add your credentials to the json_data.json
telegram_token = your telegram bot token
telegram_chat_id = the id of your user chat or group
web_id = request number?
web_cd = code?

##2- install the python libraries
run: pip3 install -r requirements.txt

##3- Run the python sript
run: python3 main.py


# How to use it (DOCKER)

##1- add your credentials to the json_data.json
telegram_token = your telegram bot token
telegram_chat_id = the id of your user chat or group
web_id = request number?
web_cd = code?

##2- build the docker image

go to the folder where the Dockerfile is and run:
sudo docker build .

##3-  Run the created docker image

sudo docker run 'imageID' 


#Notes

So far this image only works with a telegram integration, feel free to use it stand alone with the command line

## interest links

pytesseract algoritms:
https://stackoverflow.com/questions/65930463/how-to-process-this-captcha-image-for-pytesseract
create requirements.txt:
https://stackoverflow.com/questions/31684375/automatically-create-requirements-txt
usegull selenium:
https://stackoverflow.com/questions/18557275/how-to-locate-and-insert-a-value-in-a-text-box-input-using-python-selenium
install chromedriver in dockerfile:
https://gist.github.com/varyonic/dea40abcf3dd891d204ef235c6e8dd79
