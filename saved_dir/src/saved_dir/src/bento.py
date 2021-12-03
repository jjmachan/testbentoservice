# bento.py
import bentoml
import bentoml.sklearn
import numpy as np

from bentoml.io import NumpyNdarray

# Load the runner for the latest ScikitLearn model we just saved
iris_clf_runner = bentoml.sklearn.load_runner("iris_classifier_model:latest")

# Create the iris_classifier_service with the ScikitLearn runner
svc = bentoml.Service("iris_classifier_service", runners=[iris_clf_runner])


# Create API function with pre- and post- processing logic
@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def predict(input_ndarray: np.ndarray) -> np.ndarray:
    # Define pre-processing logic
    result = iris_clf_runner.run(input_ndarray)
    # Define post-processing logic
    return result
