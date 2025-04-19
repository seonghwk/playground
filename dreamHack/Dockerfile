FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# 필수 도구 설치
RUN apt update && apt install -y \
  gdb git python3 python3-pip curl tmux unzip \
  libc6-i386 lib32z1 lib32stdc++6 \
  && rm -rf /var/lib/apt/lists/*

# pwndbg 설치
RUN git clone https://github.com/pwndbg/pwndbg /opt/pwndbg && \
    cd /opt/pwndbg && ./setup.sh

# pwntools 설치
RUN python3 -m pip install --upgrade pip && pip install pwntools

WORKDIR /app

CMD ["/bin/bash"]
