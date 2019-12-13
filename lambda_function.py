import io
import json
import base64
import numpy as np
from PIL import Image


def sizeof(img):
    return img.size


def shape(img):
    return img.shape


def lambda_handler(event, context):
    """
    Lambda function
    """
    res = list()
    assert event.get('httpMethod') == 'POST'
    try:
        event['body'] = base64.b64decode(event['body'])
    except:
        return {
                'statusCode': 400,
                'body': json.dumps("bad encoding")
                }

    if event['path'] == '/size':
        function = sizeof
    elif event['path'] == '/shape':
        function = shape
    else:
        return {
                'statusCode': 404,
                'body': json.dumps("no path")
                }

    content_type = (event
                    .get('headers', {"content-type": ''})
                    .get('content-type')
                    )

    if not content_type:  # Could be case sensitive...
        content_type = (event
                        .get('headers', {"Content-Type": ''})
                        .get('Content-Type')
                        )

    print(content_type)
    if 'image/jpg' in content_type:

        # convert to bytes if need
        if type(event['body']) is str:
            event['body'] = bytes(event['body'], 'utf-8')

        try:
            img_io = io.BytesIO(event['body'])
            img_io.seek(0)
            img = Image.open(img_io)
            img = np.array(img)
            res.append(function(img))
        except Exception as e:
            print(e)
            res.append([])

    return {
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
                },
            'statusCode': 200,
            'body': json.dumps(res)
            }
