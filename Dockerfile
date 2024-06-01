FROM python:3.9

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN git clone https://github.com/parkjiung123/project1.git .

RUN pip install pygame


CMD ["python3", "docker_main.py"]