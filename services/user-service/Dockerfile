# Use official Python image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy only necessary files to the container
COPY src/ /app/src/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose port
EXPOSE 5001

# Run the app
CMD ["python", "/app/src/app.py"]

