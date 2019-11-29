# aws-lambda-cv
Toy example to illustrate how aws-lambda may be used in computer vision applications. This serveless API returns the size of an image.

The API deployment with sam-cli is included in this repository.

## Installation
1. To run the example, AWS account is needed.
2. Clone the repo.
3. Create python virtaul environment:
- `python3 -m venv ./lambda-env`
- `pip install -r requirements.txt`

4. Sam cli has just been installed. Test it:
- `sam --version`
5. Test locally with pytest. The test consists to send to lambda function cat.jpg and check the image shape.
`pytest test -v`
6. Build lambda layer 
- `mkdir -p layers/mylayer/python`
- `pip install requests-toolbelt==0.9.1 Pillow==6.2.1 numpy==1.17.4 -t layers/mylayer/python`
- `cd layers/mylayer; zip -r mylayer.zip python;cd ../..`
- `aws lambda publish-layer-version --layer-name mylayer --zip-file fileb://layers/mylayer/mylayer.zip --compatible-runtimes python3.6`
6. Test it locally :
- Run API : `sam local start-api`
- Send image : `curl "http://127.0.0.1:3000/shape" -H "Content-Type: multipart/form-data" -F "image=@test/cat.jpg"`
6. Build, package and deploy aws lambda :
- `sam build`
- `sam package --template-file template.yaml --s3-bucket aws-lambda-cv  --output-template-file packaged.yaml`
- `aws cloudformation deploy --template-file packaged.yaml --stack-name aws-lambda-cv`

- `sam package --template-file src/template.yaml  --output-template-file packaged.yaml`
## Utilisation
curl "https://0v2xflxovf.execute-api.eu-west-1.amazonaws.com/Prod/shape" -H "Content-Type: multipart/form-data" -F "image=@test/cat.jpg"
