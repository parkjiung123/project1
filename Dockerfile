FROM python:3.9

RUN apt-get update && apt-get install -y \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /usr/src/app

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install pygame


CMD ["docker_main.py"]
ENTRYPOINT ["python3"]
