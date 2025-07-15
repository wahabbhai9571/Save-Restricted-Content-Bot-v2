FROM python:3.10.4-slim-buster

# ✅ Point to Debian archive for Buster (EOL)
RUN sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list && \
    sed -i 's|http://security.debian.org/debian-security|http://archive.debian.org/debian-security|g' /etc/apt/sources.list && \
    apt update && apt upgrade -y

RUN apt-get install git curl python3-pip ffmpeg wget bash neofetch software-properties-common -y

COPY requirements.txt .
RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt

WORKDIR /app
COPY . .
EXPOSE 8000

CMD flask run -h 0.0.0.0 -p 8000 & python3 -m devgagan
