# Dockerfile for checking local changes made to the oss2018 site using hugo.

# Run the following commands to setup this docker
# docker pull ubuntu:16.04
# git clone https://github.com/OpenSecuritySummit/oss2021.git 
# cd oss2018 && git clone https://github.com/devcows/hugo-universal-theme.git themes/oss-owasp
# docker build -t oss2021 . 
# docker run -it -p 1313:1313 -v $(pwd):/opt/oss2021 oss2021:latest 

FROM ubuntu:20.04
MAINTAINER Mohammed A. Imran <imran.mohammed@owasp.org>

ENV HUGO_VERSION="0.72"
ENV SRC_DIR="/opt/oss2021"

RUN apt-get update \
    && apt-get install -y curl git \
    && adduser --disabled-password --gecos "oss" oss  \
    && curl -Ls https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz -o /tmp/hugo.tar.gz \
    && tar xf /tmp/hugo.tar.gz -C /usr/local/bin \
    && mkdir -p $SRC_DIR

WORKDIR $SRC_DIR
ADD --chown=oss:oss .. $SRC_DIR

USER oss:oss

ENTRYPOINT hugo server --bind="0.0.0.0"
