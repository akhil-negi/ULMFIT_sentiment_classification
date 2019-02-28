FROM ubuntu:18.04

LABEL maintainer="Akhil <writetoakhilnegi@gmail.com>"

RUN apt-get update && apt-get install -y python3.6 python3-pip libsm6 libxrender-dev libxext6 libgl1-mesa-glx
RUN apt-get install -y python3-pip
    
RUN mkdir /opt/app

WORKDIR /opt/app    
ADD requirements.txt .

RUN pip3 install -r requirements.txt
RUN python3 -m spacy download en

ADD . .

EXPOSE 8889
ENV FLASK_APP=app.py

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
