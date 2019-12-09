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
- `mkdir -p layers/pillow/python`
- `pip install Pillow==6.2.1 numpy==1.17.4 -t layers/pillow/python`
- `cd layers/pillow; zip -r pillow.zip python;cd ../..`
- `aws lambda publish-layer-version --layer-name pillow --zip-file fileb://layers/pillow/pillow.zip --compatible-runtimes python3.6`
7. Test it locally :
- Build package `sam build`
- Run API : `sam local start-api`
- Send image : `curl "http://127.0.0.1:3000/shape" -H "Content-Type: image/jpg" --data-binary "@test/cat.jpg"`
8. Package and deploy aws lambda :
- `sam package --s3-bucket aws-lambda-cv`
- `aws cloudformation delete-stack --stack-name aws-lambda-cv;sleep 15;`
- `aws cloudformation deploy --template-file packaged.yaml --stack-name aws-lambda-cv`

## Utilisation
`curl "https://8b1gvs25v5.execute-api.eu-west-1.amazonaws.com/Prod/shape"  -H "Content-Type: image/jpg" --data-binary "@test/cat.jpg"`
