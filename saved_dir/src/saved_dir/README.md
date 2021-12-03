# BentoML Service "testservice"

This is a Machine Learning Service created with BentoML. 

## Inference APIs:

It contains the following inference APIs:

### /classify

* Input: JSON
* Output: JSON


## Customize This Message

This is the default generated `bentoml.Service` doc. You may customize it in your Bento
build file:

```yaml
service: "image_classifier.py:svc"
description: "./readme.md"
labels:
  foo: bar
  team: abc
docker:
  distro: slim
  gpu: True
python:
  packages:
    - tensorflow
    - numpy
```
