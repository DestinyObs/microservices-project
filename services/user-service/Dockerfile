# Use official Python image
FROM python:3.12

# Set working directory
WORKDIR /src

# Copy app files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5001

# Run the app
CMD ["python", "app.py"]
