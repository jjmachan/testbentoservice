# Prototype Service - Bentoml 1.0

This a prototype service that I build to test out all the features of bentoml
1.0 and bentoctl.


## Project Structure

./service.py - This is the bento service contains the logic of our service.

./build.py - Build script for bento. This will build and export the bento into
./saved_dir

./ec2_config.yaml - bentoctl config for AWS-EC2 deployment.


## Building Docker Container

1. Modify docker file

2. from inside saved_dir. `docker build -f env/docker/Dockerfile -t testbento`

3. `docker run -p 5000:5000 testbento`
