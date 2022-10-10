#Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        openssh-server \
        vim \
        curl \
        wget \
        tcptraceroute \
    && pip install --upgrade pip \
    && pip install subprocess32 \
    && pip install gunicorn \ 
    && pip install virtualenv \
    && pip install beautifulsoup4 \
    && pip install bs4 \
    && pip install tkinter \
    && pip install django \
    && pip install django-allauth \
    && pip install django-rest-auth \
    && pip install djangorestframework \
    && pip install drf-spectacular \
    && pip install html5lib \
    && pip install itsdangerous \
    && pip install prettytable \
    && pip install termcolor \
    && pip install xmltodict \
    && pip install lxml

# Open ports for SSH access
EXPOSE 8000
ENV PORT 8000
ENV SSH_PORT 2222
ENV SSH_PORT1 22

# setup SSH
RUN mkdir -p /home/LogFiles \
     && echo "root:Docker!" | chpasswd \
     && echo "cd /home" >> /etc/bash.bashrc 

COPY sshd_config /etc/ssh/
RUN mkdir -p /opt/startup
COPY init_container.sh /opt/startup/init_container.sh

# setup default site
RUN mkdir /opt/defaultsite
COPY hostingstart.html /opt/defaultsite
COPY application.py /opt/defaultsite

# configure startup
RUN chmod -R 777 /opt/startup
COPY entrypoint.py /usr/local/bin

ENTRYPOINT ["/opt/startup/init_container.sh"]