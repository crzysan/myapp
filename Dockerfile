FROM python:3.8-slim-buster

ENV ROOTAPP=/opt
ENV HOMEDIR=/opt/app
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

EXPOSE 8000
ENV PYTHONUNBUFFERED=1

RUN mkdir $HOMEDIR

COPY requirements.txt $HOMEDIR
COPY . $HOMEDIR

RUN chgrp -R 0 $ROOTAPP && \
    chmod -R g=u $ROOTAPP && \
    apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install python3-dev gcc g++ unixodbc-dev && \
    apt-get clean && \
    apt-get autoclean
    
USER 1001
RUN python3 -m venv $VIRTUAL_ENV && \
    pip --no-cache-dir install --upgrade pip && \
    pip --no-cache-dir install -r $HOMEDIR/requirements.txt

WORKDIR $HOMEDIR

CMD ["/bin/bash", "start-server.sh"]

