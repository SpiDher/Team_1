#!/bin/bash

# Ensure the backend directory is correct
cd Backend

# Install Python dependencies from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# Ensure any additional setup steps are here
# For example, collect static files if needed
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Any other steps like migrations can be added here if necessary
# echo "Running migrations..."
# python manage.py migrate

# Now, go back to the root directory and finish the build
cd ..

# Additional steps if necessary (e.g., build frontend)
