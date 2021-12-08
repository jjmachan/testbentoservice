# hello.py
import bentoml
from bentoml.io import JSON

SERVICE_NAME = "testservice"
svc = bentoml.Service(SERVICE_NAME)


@svc.api(input=JSON(), output=JSON())
async def classify(input_json):
    return {"input_received": input_json, "foo": "bar"}


# make sure to expose the asgi_app from the service instance
# app = svc.asgi_app
