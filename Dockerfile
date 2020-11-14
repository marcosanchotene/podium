FROM selenium/standalone-chrome-debug
RUN sudo apt-get update \
  && sudo apt-get install python3-pip -y
RUN pip3 install pytest \
  selenium
COPY . /podium
WORKDIR /podium