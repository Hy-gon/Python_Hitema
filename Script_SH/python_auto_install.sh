#!/bin/bash
echo "version : $OSTYPE"

apt-get update &&
    apt-get install -y python3.6 &&
    apt-get install -y python3-pip &&
    pip3 install --upgrade pip &&

    # installation des composants
    pip3 install numpy \
	 notebook \
	 pandas \
	 scikit-learn \
	 seaborn \
	 joblib \
	 matplotlib \
	 stop-words \
	 streamlit \
	 flask &&

    # installation de docker
    apt-get remove docker docker-engine docker.io containerd runc &&
    apt-get install apt-transport-https \
	    ca-certificates \
	    curl \
	    gnupg-agent \
	    software-properties-common &&

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) \
stable" &&
    apt-get update &&
    apt-get install -y docker-ce docker-ce-cli containerd.io &&
    apt-get install -y docker-ce=5:20.10.0~3-0~ubuntu-xenial docker-ce-cli=5:20.10.0~3-0~ubuntu-xenial containerd.io &&
    docker run hello-world
