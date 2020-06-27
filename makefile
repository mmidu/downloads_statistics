.env:
	@cp .env.dev .env
include .env
export

app: 
	@yarn --cwd ./src/client/
	@yarn --cwd ./src/client/ build
	@docker-compose up --build -d
	@sleep 1
	@curl localhost:$(PYTHON_PORT)/seed | jq

seed:
	@curl localhost:$(PYTHON_PORT)/seed | jq

test:
	@docker exec -t $(PYTHON_CONTAINER_NAME) pytest
