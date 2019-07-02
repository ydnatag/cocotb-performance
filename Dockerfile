from debian:stretch

RUN apt update && apt install -y python python3 python3-pip python-pip git iverilog

RUN pip3 install pyyaml
RUN pip2 install pillow
