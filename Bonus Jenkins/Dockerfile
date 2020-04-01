FROM jenkins/jenkins:lts-slim

EXPOSE 80/tcp
EXPOSE 8080/tcp
EXPOSE 443/tcp

USER root

RUN apt-get update
RUN apt-get install apt-utils apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
RUN apt-get update
RUN apt install docker.io -y

RUN usermod -a -G docker jenkins
RUN systemctl restart docker

USER jenkins