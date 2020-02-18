import pytest
import base64
from requests_toolbelt.multipart.encoder import MultipartEncoder

path_cat = 'test/cat.jpg'
@pytest.fixture
def apigateway_event():

    mp_encoder = MultipartEncoder(
        fields={'image': ('filename',open(path_cat, "rb"),'image/png'),
                'other' : 'babar'
                })
    body = mp_encoder.to_string()
    print('form-data is :')
    print(body[:100])
    body = base64.b64encode(body)
    print('It is encoded in base64')

    def _apigateway_event(route):
        event = dict(httpMethod = 'POST',
                     path = '/%s'%route,
                     headers = {'content-type': mp_encoder.content_type},
                     body = body)


        return event

    return _apigateway_event
