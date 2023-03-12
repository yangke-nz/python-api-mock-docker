# python-api-mock-docker

## generate requirement.txt 
pip install pipreqs
pipreqs  .
or 
python -m  pipreqs.pipreqs


## to run locally
python ./view.py

## docker cmd
docker image build -t restapi_mock_app .
docker run --name=restapi_mock -e PYTHONUNBUFFERED=1 -p 5000:5000 -d restapi_mock_app

