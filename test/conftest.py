import pytest
import base64

path_cat = 'test/cat.jpg'
@pytest.fixture
def apigateway_event():

    with open(path_cat, "rb") as image_file:
        body = base64.b64encode(image_file.read())
        event = dict(httpMethod = 'POST',
                     path = '/shape',
                     headers = {'Content-Type': 'image/jpg'},
                     body = body)


    yield event
