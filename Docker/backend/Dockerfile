# Use official Python slim base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy your app file
COPY app.py .

# (Optional) Copy requirements if you create one
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Install Flask manually since requirements.txt is optional
RUN pip install flask==2.2.5

# Expose the port your app runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
