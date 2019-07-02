#!/bin/bash

docker build -q -f Dockerfile -t cocotb-performance .
docker run -it -v$PWD:$PWD -w$PWD cocotb-performance $@
