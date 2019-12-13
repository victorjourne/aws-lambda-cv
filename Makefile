venv:
	python3 -m venv venv
	venv/bin/pip install -U -r requirements.txt

tests:
	venv/bin/pytest -v

layers:
	mkdir -p layers

build: layers
	mkdir -p layers/pillow/python
	pip install Pillow==6.2.1 numpy==1.17.4 -t layers/pillow/python
	cd layers/pillow; zip -r pillow.zip python;cd ../..
	aws lambda publish-layer-version --layer-name pillow --zip-file fileb://layers/pillow/pillow.zip --compatible-runtimes python3.6

dev:
	sam build
	@echo "Test it with: \n"
	@echo "curl \"http://127.0.0.1:3000/shape\" -H \"Content-Type: image/jpg\" --data-binary \"@test/cat.jpg\""
	sam local start-api

deploy:
	sam package --s3-bucket aws-lambda-cv
	aws cloudformation delete-stack --stack-name aws-lambda-cv;sleep 15;
	aws cloudformation deploy --template-file packaged.yaml --stack-name aws-lambda-cv

clean:
	rm -Rf venv layers
