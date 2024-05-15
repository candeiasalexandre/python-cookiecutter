.PHONY: clean-env
clean-env:
	-rm -rf .venv


.PHONY: clean-build
clean-build:
	@rm -fr pip-wheel-metadata
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +


.PHONY: setup-dev
setup-dev:
	poetry config virtualenvs.in-project true 
	poetry install


.PHONY: tests
tests:
	poetry run pytest tests


.PHONY: format
format:
	poetry run black {{cookiecutter.__project_name_snake}} tests
	poetry run ruff check --fix {{cookiecutter.__project_name_snake}} tests


.PHONY: check
check:
	poetry run black --check {{cookiecutter.__project_name_snake}} tests
	poetry run ruff check {{cookiecutter.__project_name_snake}} tests
	poetry run mypy {{cookiecutter.__project_name_snake}} tests


.PHONY: build
build: clean-build
	poetry build -f wheel
	poetry export -f requirements.txt --output dist/requirements.txt --without-hashes


.PHONY: build-docker
build-docker:
	docker build -t {{cookiecutter.__project_name_kebab}} .
