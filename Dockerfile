# LORD USERBOT
FROM koala21/kampangbot:buster

#
# LORD
#
RUN git clone -b Virus-UserBot https://github.com/tungauicipiyey/Virus-UserBot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/tungauicipiyey/Virus-UserBot/Virus-UserBot/requirements.txt

CMD ["python3","-m","userbot"]
