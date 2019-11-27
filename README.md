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
4. Run :
- `sam package --template-file src/template.yaml  --output-template-file packaged.yaml`
## Utilisation
curl ....
