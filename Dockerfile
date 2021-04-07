# We're using Ubuntu 20.10
FROM liualvinas24/docker:groovy
#
# Clone repo and prepare working directory
#
RUN git clone -b Virus-UserBot https://github.com/tungauicipiyey/Virus-UserBot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/tungauicipiyey/Virus-UserBot/Virus-UserBot/requirements.txt

CMD ["python3","-m","userbot"]
