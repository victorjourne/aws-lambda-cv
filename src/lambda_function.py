from PIL import Image
import base64
import io, re, json
import numpy as np
from requests_toolbelt.multipart import decoder
from urllib.request import urlopen

pattern = re.compile('(?<=form-data; name=").*?(?=")')

def nbytes(img):
    return img.nbytes / 1000 # in k bytes

def shape(img):
    return img.shape

def lambda_handler(event, context):
    """
    Lambda function
    """
    res = list()
    assert event.get('httpMethod') == 'POST'
    try :
        event['body'] = base64.b64decode(event['body'])
    except :
         return {
        'statusCode': 400,
        'body': json.dumps(res)
        }

    if event['path'] == '/nbytes' :
        function = nbytes
    elif event['path'] == '/shape' :
        function = shape
    else:
         return {
        'statusCode': 404,
        'body': json.dumps(res)
        }

    content_type = event.get('headers', {"content-type" : ''}).get('content-type')
    if not content_type: # Could be case sensitive...
            content_type = event.get('headers', {"Content-Type" : ''}).get('Content-Type')

    print(content_type)
    if 'multipart/form-data' in content_type  :

        # convert to bytes if need
        if type(event['body']) is str:
            event['body'] = bytes(event['body'],'utf-8')
        #   import pdb; pdb.set_trace()

        multipart_data = decoder.MultipartDecoder(event['body'], content_type)
        for part in multipart_data.parts:
            #
            content_disposition = part.headers.get(b'Content-Disposition',b'').decode('utf-8')
            search_field = pattern.search(content_disposition)
            print(search_field)
            #import pdb; pdb.set_trace()
            if search_field :
                if search_field.group(0) == 'image' :
                    try:
                        img_io = io.BytesIO(part.content)
                        img_io.seek(0)
                        img = Image.open(img_io)
                        img = np.array(img)
                        res.append(function(img))
                    except Exception as e:
                        print(e)
                        res.append([])

                else :
                    print('Bad field name in form-data')

    return {
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
                },
            'statusCode': 200,
            'body': json.dumps(res)
            }
