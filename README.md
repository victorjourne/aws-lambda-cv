# aws-lambda-cv
Toy example to illustrate how aws-lambda may be used in computer vision applications. This serveless API returns the bytes size of an image and its shape. The images are sent inside a form.

The API deployment with sam-cli is included in this repository.

## Installation
1. To run the example, AWS account is needed.
2. Clone the repo.
3. Create python virtual environment:
- `make venv`

4. Sam cli has just been installed. Test it:
- `sam --version`
5. Test locally with pytest. The test consists to send to lambda function cat.jpg and check the image shape.
- `make tests`
6. Build lambda layer
- `make build`
7. Test it locally :
- `make dev`
8. Package and deploy aws lambda :
- `make deploy`

## Utilisation
`curl "https://7w26u0d56g.execute-api.eu-west-1.amazonaws.com/Prod/shape"  -H "Content-Type: multipart/form-data" -F "image=@test/cat.jpg"`
