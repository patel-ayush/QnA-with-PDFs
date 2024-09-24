FROM python:3.12-slim

# Setting the working directory in the container
WORKDIR /usr/src/app

# Copying the current directory contents into the container
COPY . .

# Installing any Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "src/main.py"]

# Build the Docker image
# docker build -t qna_app .

# Run the Docker container
# docker run qna_app data/handbook.pdf data/ques.pdf

