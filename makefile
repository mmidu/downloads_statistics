.env:
	@cp .env.dev .env
include .env
export

app: 
	@docker-compose up --build -d
	@yarn --cwd ./src/now-ui-dashboard-react/
	@yarn --cwd ./src/now-ui-dashboard-react/ build
	@curl localhost:$(PYTHON_PORT)/seed | jq

seed:
	@curl localhost:$(PYTHON_PORT)/seed | jq

test:
	@docker exec -t $(PYTHON_CONTAINER_NAME) pytest
