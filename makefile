.PHONY: tests
tests: ## run tests with poetry (isort, black, pflake8, mypy)
	@echo "🚀 Launching the tests..."
	poetry run black python-desgin-pattern
	poetry run isort python-desgin-pattern
	poetry run pflake8 python-desgin-pattern
	poetry run mypy python-desgin-pattern
	@echo "\033[33;45mAll tests passed! ✨🍾🥳🍾✨\033[0m"


.PHONY: tests_strict
tests_strict: ## run tests with poetry (isort, black, pflake8, mypy)
	@echo "🚀 Launching the strict tests..."
	poetry run isort python-desgin-pattern
	poetry run black python-desgin-pattern
	poetry run pflake8 python-desgin-pattern
	poetry run mypy python-desgin-pattern --strict
	@echo "\033[33;45mAll strict tests passed! ✨🍾🤩🍾✨\033[0m"