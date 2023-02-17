# Update Termux packages
upgrade:
	apt update && apt upgrade -y

# Install Rust
rust:
	curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Install Python
python:
	apt install python3.11

# Create Python virtual environment
venv:
	python3.11 -m venv venv

# Activate the virtual environment
activate: venv
	source venv/bin/activate

# Install Python dependencies
install:
	pip install -r requirements.txt

# Start the application using granian
gstart:
	granian --interface asgi app.main:app

# Start the application using uvicorn
ustart:
	uvicorn app.main:app

# Default target, install everything
all: upgrade rust python venv activate install

.PHONY: upgrade rust python venv activate install gstart ustart all
