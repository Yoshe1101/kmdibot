
FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y
RUN apt-get install -y apt
RUN apt-get install -y wget  
RUN apt-get install -y xvfb
RUN apt-get install -y unzip
RUN apt-get install -y gnupg
RUN apt-get install -y gnupg2
RUN apt-get install -y gnupg1
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

RUN apt-get update -y
RUN apt-get install -y google-chrome-stable
RUN apt install -y tesseract-ocr
ENV CHROMEDRIVER_VERSION 2.19
ENV CHROMEDRIVER_DIR /chromedriver
RUN mkdir $CHROMEDRIVER_DIR

RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR

# Put Chromedriver into the PATH
ENV PATH $CHROMEDRIVER_DIR:$PATH

COPY . .
RUN apt-get install -y openjdk-11-jre-headless
ENV JDK_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JDK_HOME

RUN apt install -y python3-pip
RUN pip3 install Cython
RUN pip3 install -r requirements.txt


CMD [ "python3", "main.py" ]