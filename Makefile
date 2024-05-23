clean-pycache:
	find ./ -type d -name '__pycache__' -exec rm -rf {} +

lint:
	poetry run ruff check src/* --fix

format:
	poetry run ruff format src/*

imports:
	poetry run ruff check src/* --select I --fix

pretty:
	$(MAKE) lint
	$(MAKE) format
	$(MAKE) imports