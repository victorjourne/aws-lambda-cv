import sys, os
import pytest
import io

from requests_toolbelt.multipart.encoder import MultipartEncoder
# Import lambda_function outside
sys.path.append(os.path.join(os.path.dirname(__file__),'aws_lambda'))

from lambda_function import lambda_handler

def test_handler(apigateway_event):

    resp = lambda_handler(apigateway_event, None)
    body = resp['body']
    print(body)
    assert resp['statusCode'] == 200
    assert eval(body)== [[600, 400, 3]], "size of image is : %s"% eval(body)
