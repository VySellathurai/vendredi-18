.DEFAULT_GOAL: help

help:
	@awk -F ':|##' '/^[^\t].+?:.*?##/ {printf "\033[36m%-30s\033[0m %s\n", $$1, $$NF}' $(MAKEFILE_LIST)

show-platform: ##show plateform infos
	@echo "Platform: $(shell uname -s)"
	@echo "Architecture: $(shell uname -m)"
	@echo "OS Version: $(shell uname -r)"
	@echo "Kernel Version: $(shell uname -v)"
	@echo "System Name: $(shell uname -n)"
	@echo "System Type: $(shell uname -o)"

check-requirements: ##check requirements
	@echo "Checking requirements..."
	@command -v python3 >/dev/null 2>&1 || { echo >&2 "Python3 is required but it's not installed. Aborting."; exit 1; }
	@command -v pip3 >/dev/null 2>&1 || { echo >&2 "pip3 is required but it's not installed. Aborting."; exit 1; }
	@echo "All requirements are met."

install: check-requirements ##install requirements
	@echo "Installing requirements..."
	@python3 -m venv venv
	@pip3 install -r requirements.txt
	@echo "All requirements are installed."

fix-macos-install: ##fixing issue on sentencepiece lib
	@echo "Fixing macOS install..."
	@brew install protobuf
	@pip install sentencepiece
	@echo "All fixes are applied."

run: install ##run the app
	@echo "Running the app..."
	@. venv/bin/activate
	@streamlit run app.py
	@echo "App is running."