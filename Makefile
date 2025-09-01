.PHONY: install install-dev test clean

VENV := .venv
PY := $(VENV)/bin/python
PIP := $(PY) -m pip

# Install product environment
install:
	@echo "🔧 Performing initial setup for start (not for development)..."
	@echo "🔧 Creating virtual environment if needed..."
	@test -d $(VENV) || python3 -m venv $(VENV)
	@echo "✅ Virtual environment is ready."
	$(PIP) install -U pip
	$(PIP) install -e .
	@echo "✅System is ready for work. "
	@echo "⚠️Don't forget activate the environment."
	@echo "⚠️ source venv/bin/activate	# bash/zsh"
	@echo  ⚠️source venv/bin/activate.fish	# fish"


# Development environment setup
install-dev:
	@echo "🔧 Performing initial setup for development..."
	@echo "🔧 Creating virtual environment if needed..."
	@test -d $(VENV) || python3 -m venv $(VENV)
	@echo "✅ Virtual environment is ready."
	$(PIP) install -U pip
	$(PIP) install -e .[dev]
	@echo "✅System is ready for development. "
	@echo "⚠️Don't forget activate the environment."
	@echo "⚠️source venv/bin/activate	# bash/zsh"
	@echo "⚠️source venv/bin/activate.fish	# fish"

test:
# 	$(PY) -m pytest -q
	$(PY) -m pytest -v

clean:
	rm -rf $(VENV) .pytest_cache **/__pycache__
