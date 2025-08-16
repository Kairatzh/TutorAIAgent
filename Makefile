.PHONY: help install install-dev test lint format clean build run

help:
	@echo "Доступные команды:"
	@echo "  install      - Установка зависимостей"
	@echo "  install-dev  - Установка зависимостей для разработки"
	@echo "  test         - Запуск тестов"
	@echo "  lint         - Проверка кода линтерами"
	@echo "  format       - Форматирование кода"
	@echo "  clean        - Очистка временных файлов"
	@echo "  build        - Сборка пакета"
	@echo "  run          - Запуск агента"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

test:
	pytest tests/ -v --cov=tools --cov=utils --cov-report=html

lint:
	flake8 tools/ utils/ configs/ agent.py
	mypy tools/ utils/ configs/ agent.py
	black --check tools/ utils/ configs/ agent.py
	isort --check-only tools/ utils/ configs/ agent.py

format:
	black tools/ utils/ configs/ agent.py
	isort tools/ utils/ configs/ agent.py

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	rm -rf .coverage

build:
	python -m build

run:
	python agent.py

setup-hooks:
	pre-commit install

update-hooks:
	pre-commit autoupdate
