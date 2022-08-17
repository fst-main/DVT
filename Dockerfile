# Install OpenSSH and set the password for root to "Docker!". In this example, "apk add" is the install instruction for an Alpine Linux-based image.
RUN apk add openssh \
     && echo "root:Docker!" | chpasswd 
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

# Copy the sshd_config file to the /etc/ssh/ directory
COPY sshd_config /etc/ssh/

# Copy and configure the ssh_setup file
RUN mkdir -p /tmp
COPY ssh_setup.sh /tmp
RUN chmod +x /tmp/ssh_setup.sh \
    && (sleep 1;/tmp/ssh_setup.sh 2>&1 > /dev/null)

# Open port 2222 for SSH access
EXPOSE 8080 2222
# EXPOSE 80/tcp
# EXPOSE 80/udp
# EXPOSE 22/tcp