FROM python:3.10

# Set the working directory
WORKDIR /app

COPY requirements.txt ./requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Run the application

# CMD ["python", "app.py"]
# to keep the container running
 CMD ["tail", "-f", "/dev/null"]