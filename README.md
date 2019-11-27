# aws-lambda-cv
Toy example to illustrate how aws-lambda may be used in computer vision applications. This serveless API returns the size of an image.

The API deployment with sam-cli is included in this repository.

## Installation
1. To run the example, AWS account is needed.
2. Clone the repo.
3. Create and activate python 3 virtual environment.
- `python3 -m venv ./lambda-env`
- `source lambda-env/bin/activate`
- `pip install -r requirements.txt`
4. Sam-cli has just been installed, check it inside the virtual env and init:
- `sam --version`
- `sam init --runtime python3.6`
5. Run :
- `sam package --template-file src/template.yaml  --output-template-file packaged.yaml`
## Utilisation
curl ....
