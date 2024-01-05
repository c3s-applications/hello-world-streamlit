# Set the base image
FROM continuumio/miniconda3

# Set the working directory
WORKDIR /app

# Copy the application code
COPY requirements.txt /app
COPY hello-world.py /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port on which the application will run, by default streamlit runs on port 8501
EXPOSE 8501

# Start the application
CMD ["streamlit", "run", "hello-world.py"]
