FROM python:3.11-slim as envs
LABEL platform_name="spheres"

# Set arguments to be used throughout the image
ARG SPHERES_HOME="/home/spheres"
ARG SPHERES_USER="spheres"
ARG SPHERES_UID="50000"

# Set arguments for access s3 bucket to mount using s3fs
ARG BUCKET_NAME
ARG S3_ENDPOINT="https://s3.us-east-1.amazonaws.com"

# Add environment variables based on arguments
ENV SPHERES_HOME ${SPHERES_HOME}
ENV SPHERES_USER ${SPHERES_USER}
ENV SPHERES_UID ${SPHERES_UID}
ENV BUCKET_NAME ${BUCKET_NAME}
ENV S3_ENDPOINT ${S3_ENDPOINT}

# Add spheres user
RUN useradd -ms /bin/bash -d ${SPHERES_HOME} --uid ${SPHERES_UID} ${SPHERES_USER}

# Start of the second layer
FROM envs as dist

# install s3fs
RUN set -ex && \
    apt-get update && \
    apt install s3fs -y

# install docker
RUN apt install docker.io -y

# setup s3fs configs
RUN echo "s3fs#${BUCKET_NAME} ${SPHERES_HOME}/s3_bucket fuse _netdev,allow_other,nonempty,umask=000,uid=${SPHERES_UID},gid=${SPHERES_UID},passwd_file=${SPHERES_HOME}/.s3fs-creds,use_cache=/tmp,url=${S3_ENDPOINT} 0 0" >> /etc/fstab
RUN sed -i '/user_allow_other/s/^#//g' /etc/fuse.conf

# container work directory
WORKDIR ${SPHERES_HOME}

# dependencies
COPY . .
RUN pip install -r requirements.txt

# write script to mount s3 bucket via s3fs
RUN printf '#!/usr/bin/env bash  \n\
echo ${ACCESS_KEY_ID}:${SECRET_ACCESS_KEY} > ${SPHERES_HOME}/.s3fs-creds \n\
chmod 400 ${SPHERES_HOME}/.s3fs-creds \n\
mkdir ${SPHERES_HOME}/s3_bucket \n\
mount -a \n\
touch ${SPHERES_HOME}/s3_bucket/my-new-file-from-container.txt \n\
exec python ${SPHERES_HOME}/deploy/main.py \
' >> ${SPHERES_HOME}/entrypoint.sh

RUN chmod 700 ${SPHERES_HOME}/entrypoint.sh
ENTRYPOINT [ "/home/spheres/entrypoint.sh" ]