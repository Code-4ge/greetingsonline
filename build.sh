# Create a virtual environment
# echo "Creating a virtual environment..."
# python3.9 -m venv venv
# venv\Scripts\activate

# echo "Installing the latest version of pip..."
# python -m pip install --upgrade pip

# Build the project
echo "Building the project..."
python3.9 -m pip install -r requirements.txt
echo "Build end"
# Collect static files
echo "Running..."
python3.9 index.py