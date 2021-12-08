import bentoml

from service import SERVICE_NAME

bentoml.build('./service.py:svc')
