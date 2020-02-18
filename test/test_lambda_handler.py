import sys, os
import pytest
import io

from requests_toolbelt.multipart.encoder import MultipartEncoder
# Import lambda_function
import imp
#lambda_function = importlib.import_module('.src', package='aws-lambda-cv')
util = imp.load_source("lambda_function", "src/lambda_function.py")

from lambda_function import lambda_handler


def test_handler(apigateway_event):

    resp = lambda_handler(apigateway_event('shape'), None)
    body = resp['body']
    print(body)
    assert resp['statusCode'] == 200
    assert eval(body)== [[600, 400, 3]], "shape of image is : %s"% eval(body)

    resp = lambda_handler(apigateway_event('nbytes'), None)
    body = resp['body']
    print(body)
    assert resp['statusCode'] == 200
    assert eval(body)== [720], "size of of image is : %sk bytes "% eval(body)
