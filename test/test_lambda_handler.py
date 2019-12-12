import sys, os
import pytest
import io

from requests_toolbelt.multipart.encoder import MultipartEncoder
# Import lambda_function
import imp
util = imp.load_source("lambda_function", "lambda_function.py")

from lambda_function import lambda_handler


def test_handler(apigateway_event):

    resp = lambda_handler(apigateway_event, None)
    body = resp['body']
    print(body)
    assert resp['statusCode'] == 200
    assert eval(body)== [[600, 400, 3]], "size of image is : %s"% eval(body)
