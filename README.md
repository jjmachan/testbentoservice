# Prototype Service - Bentoml 1.0

This a prototype service that I build to test out all the features of bentoml
1.0 and bentoctl.


## Project Structure

`service.py` - This is the bento service contains the logic of our service.

`bentofile.yaml` - The build file for bento service.

`build.py` - Build script for bento. This will build and export the bento into
`./saved_dir`

`ec2_config.yaml` - bentoctl config for AWS-EC2 deployment.

## Building this Bento

Run `python build.py` and this will create the bento and export it to `saved_dir` for you.

Else you can do `bentoml build` to build and save it into the local store.
