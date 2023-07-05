# Create a virtual environment
echo "Creating a virtual environment..."
python3.9 -m venv venv
venv\Scripts\activate

echo "Installing the latest version of pip..."
python -m pip install --upgrade pip

# Build the project
echo "Building the project..."
python -m pip install -r requirements.txt

# Collect static files
echo "Running..."
python index.py