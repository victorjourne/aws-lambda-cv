venv:
	python3 -m venv venv
	venv/bin/pip install -U -r requirements.txt

tests:
	venv/bin/pytest test -v

layers:
	mkdir -p layers

build: layers
	mkdir -p layers/pillow-toolbeit/python
	venv/bin/pip install requests-toolbelt==0.9.1 Pillow==6.2.1 numpy==1.17.4 -t layers/pillow-toolbeit/python
	cd layers/pillow-toolbeit; zip -r pillow-toolbeit.zip python;cd ../..
	aws lambda publish-layer-version --layer-name pillow-toolbeit --zip-file fileb://layers/pillow-toolbeit/pillow-toolbeit.zip --compatible-runtimes python3.6

dev:
	sam build
	@echo "Test it with: \n"
	@echo "curl \"http://127.0.0.1:3000/shape\" -H \"Content-Type: multipart/form-data\" -F \"image=@test/cat.jpg\""
	sam local start-api

deploy:
	sam package --template-file template.yaml --s3-bucket aws-lambda-cv-form --output-template-file packaged.yaml
	aws cloudformation delete-stack --stack-name aws-lambda-cv-form;sleep 15;
	aws cloudformation deploy --template-file packaged.yaml --stack-name aws-lambda-cv-form

clean:
	rm -Rf venv layers
