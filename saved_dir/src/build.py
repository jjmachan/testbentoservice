import bentoml

from service import SERVICE_NAME

bentoml.build('./service.py:svc')
bentoml.export_bento(SERVICE_NAME, '../saved_dir')
