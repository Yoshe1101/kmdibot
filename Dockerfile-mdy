FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y ca-certificates
RUN apt-get update && \
    apt-get install -y gnupg wget curl unzip --no-install-recommends && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update -y && \
    apt-get install -y google-chrome-stable && \
    CHROMEVER=$(google-chrome --product-version | grep -o "[^\.]*\.[^\.]*\.[^\.]*") && \
    DRIVERVER=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROMEVER") && \
    wget -q --continue -P /chromedriver "http://chromedriver.storage.googleapis.com/$DRIVERVER/chromedriver_linux64.zip" && \
    unzip /chromedriver/chromedriver* -d /chromedriver

ENV CHROMEDRIVER_DIR /chromedriver
ENV PATH $CHROMEDRIVER_DIR:$PATH

RUN apt-get install -y libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1
RUN apt install -y tesseract-ocr
COPY . .
RUN apt-get install -y openjdk-11-jre-headless
ENV JDK_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JDK_HOME
RUN apt-get install -y xvfb

RUN apt install -y python3-pip
RUN pip3 install Cython
RUN pip3 install -r requirements.txt


CMD [ "python3", "main.py" ]