FROM python:3.11-slim as envs
LABEL platform_name="spheres"

# Set arguments to be used throughout the image
ARG SPHERES_HOME="/home/spheres"
ARG SPHERES_USER="spheres"
ARG SPHERES_UID="50000"

# Add environment variables based on arguments
ENV SPHERES_HOME ${SPHERES_HOME}
ENV SPHERES_USER ${SPHERES_USER}
ENV SPHERES_UID ${SPHERES_UID}
ENV BUCKET_NAME ${BUCKET_NAME}
ENV S3_ENDPOINT ${S3_ENDPOINT}
ENV ACCESS_KEY_ID ${ACCESS_KEY_ID}
ENV SECRET_ACCESS_KEY ${SECRET_ACCESS_KEY}

# Add spheres user
RUN useradd -ms /bin/bash -d ${SPHERES_HOME} --uid ${SPHERES_UID} ${SPHERES_USER}

# Start of the second layer
FROM envs as dist

# Installing prerequisite packages
RUN DEBIAN_FRONTEND="noninteractive" apt-get update && apt-get install -y tzdata keyboard-configuration
RUN apt-get -y install curl unzip groff less

# install s3fs
RUN set -ex && \
    apt-get update && \
    apt install s3fs -y

# install docker
RUN apt install docker.io -y
RUN docker --version

# container work directory
WORKDIR ${SPHERES_HOME}

# dependencies
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# AWS CLI installation
RUN	curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN	unzip awscliv2.zip && ./aws/install
RUN mkdir ${SPHERES_HOME}/.aws
RUN echo "[default]" > ${SPHERES_HOME}/.aws/config
RUN echo "region=us-east-1" >> ${SPHERES_HOME}/.aws/config

# write script to mount s3 bucket, execute docker daemon and run python script
RUN printf '#!/usr/bin/env bash  \n\
echo "ENVIRONMENT PREPARATION (10 second to go)..." \n\
nohup dockerd >/dev/null 2>&1 & sleep 10 && echo initiation \n\
echo "s3fs#${BUCKET_NAME} ${SPHERES_HOME}/s3_bucket fuse _netdev,allow_other,nonempty,umask=000,uid=${SPHERES_UID},gid=${SPHERES_UID},passwd_file=${SPHERES_HOME}/.s3fs-creds,use_cache=/tmp,url=${S3_ENDPOINT} 0 0" >> /etc/fstab  \n\
sed -i "/user_allow_other/s/^#//g" /etc/fuse.conf  \n\
printf "${ACCESS_KEY_ID}\n${SECRET_ACCESS_KEY}\nus-east-1\ntext\n" | aws configure \n\
echo ${ACCESS_KEY_ID}:${SECRET_ACCESS_KEY} > ${SPHERES_HOME}/.s3fs-creds \n\
chmod 400 ${SPHERES_HOME}/.s3fs-creds \n\
mkdir ${SPHERES_HOME}/s3_bucket \n\
mount -a \n\
cd ${SPHERES_HOME}/s3_bucket/docker-hello-world \n\
exec python ${SPHERES_HOME}/deploy/main.py \
' >> ${SPHERES_HOME}/entrypoint.sh

RUN chmod 700 ${SPHERES_HOME}/entrypoint.sh
ENTRYPOINT [ "/home/spheres/entrypoint.sh" ]