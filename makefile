.env:
	@cp .env.dev .env
include .env
export

app: 
ifeq (,$(wildcard ./src/client/src/conf.js))
	@cp src/client/src/conf.js.dev src/client/src/conf.js
endif
	@yarn --cwd ./src/client/
	@yarn --cwd ./src/client/ build
	@docker-compose up --build -d
	
seed:
	@curl localhost:$(PYTHON_PORT)/seed | jq

test:
	@docker exec -t $(PYTHON_CONTAINER_NAME) pytest
