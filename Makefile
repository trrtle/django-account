fail-if-no-virtualenv:
ifndef VIRTUAL_ENV # check for a virtualenv in development environment
$(error this makefile needs a virtualenv)
endif

lint: fail-if-no-virtualenv
	black --check --config pyproject.toml .
	find . -type f -name "*.py" | xargs pylint --load-plugins pylint_django

black: fail-if-no-virtualenv
	@black --exclude "migrations/*" .