FROM tensorflow/tensorflow:latest-gpu-jupyter

ARG NB_USER="Oring-AI"

ENV password 12345

ENV SHELL=/bin/bash 

WORKDIR /

USER root 

RUN apt-get update &&\
    /usr/bin/python3 -m pip install --upgrade pip &&\
	pip install torch==1.5.1+cu101 torchvision==0.6.1+cu101 -f https://download.pytorch.org/whl/torch_stable.html &&\
	pip install jupyterlab 
	

RUN apt-get -y install sudo 

CMD ["/bin/bash"]
