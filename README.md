# UI automated tests
This project contains code for user interface (UI) automated tests made
 with Python, Pytest and Selenium for [this website](https://www.podium.com/). 
 Tests can run locally or inside a Docker container which is included and based 
 on the [official Selenium Chrome debugging Docker
  image](https://github.com/SeleniumHQ/docker-selenium/tree/selenium-3#debugging).
 The debugging image was chosen because it allows visual inspection with a VNC client 
 while tests are running. 

## Requirements

You must have Google Chrome 86, Chrome Webdriver for Chrome 86, Python 3.8 and
 Pytest 6.1.2 installed on your system and administrator privileges to run the 
 tests locally. To run them on the Docker container, you must have Docker installed.

## Instructions to run the tests locally
1. On the directory you pulled this project, run the tests with `pytest -v`.
 If Pytest is not on the path environment variable of your system, append the
  Python interpreter to the command and run Pytest as a module, with 
  `python -m pytest -v` or `python3 -m pytest -v`, depending on how Python
   is configured on your system.

## Instructions to run the tests with Docker

1. Build image with `docker build -t selenium/standalone-chrome-debug:podium .`.
1. Run it with `docker run -d -p 4444:4444 -p 5900:5900 -v 
/dev/shm:/dev/shm --name podium selenium/standalone-chrome-debug:podium`.
1. Enter the container with `docker exec -it podium /bin/bash`.
1. Connect your VNC client on the **0.0.0.0:5900** address if you wish to 
visualize the tests while they run.
1. Run the tests with `python3 -m pytest -v`.
