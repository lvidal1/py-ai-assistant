# Assistant

## Run the app

pipenv install

pipenv shell

./boostrap.sh


## Run docker

### build the image
docker build -t ai_assistant .

### run a new docker container named ai_assistant
docker run --name ai_assistant -d -p 5000:5000 ai_assistant

### fetch transcript from the dockerized instance
curl http://localhost:5000/transcript/