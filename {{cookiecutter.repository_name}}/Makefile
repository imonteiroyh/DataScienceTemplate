.PHONY: help
help:			## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets: "
	@fgrep "##" Makefile | fgrep -v fgrep


.PHONY: clean
clean:			## Clean unused files.
	@echo "Cleaning up..."
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -delete
	@rm -f .coverage
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@rm -rf {{ cookiecutter.project_name }}/*.egg-info
	@rm -rf htmlcov
	@rm -rf docs/_build
	@rm -rf docs/_static


.PHONY: install
install:		## Install in development mode.
	pip install -e .[test]


.PHONY: format
format:			## Format code using isort and black
	isort notebooks/
	isort scripts/
	isort {{ cookiecutter.project_name }}/
	isort tests/
	black -l 110 notebooks/
	black -l 110 scripts/
	black -l 110 {{ cookiecutter.project_name }}/
	black -l 110 tests/


.PHONY: lint
lint:			## Run linters
	flake8 {{ cookiecutter.project_name }}/
	black -l 110 --check {{ cookiecutter.project_name }}/
	mypy {{ cookiecutter.project_name }}/


.PHONY: test
test: lint		## Run tests and generate coverage report
	pytest tests/
	coverage html


.PHONY: docs
docs:			## Build documentation
	@echo "Building documentation..."
	pdoc {{ cookiecutter.project_name }} -o docs
	@echo "Serving API documentation..." 
	pdoc {{ cookiecutter.project_name }} --host localhost --port 8080
