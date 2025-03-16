FROM docker.elastic.co/logstash/logstash:7.17.16

COPY config/ /usr/share/logstash/pipeline/

ARG DOCKER_GID=998
RUN usermod -aG ${DOCKER_GID} logstash


# Set the user to logstash
USER logstash