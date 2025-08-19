# 1. Base Image: Start with an official Python slim image for a smaller footprint.
FROM python:3.11-slim

# 2. Working Directory: Set the working directory inside the container.
WORKDIR /app

# 3. Copy Dependencies: Copy the requirements file into the container.
COPY requirements.txt .

# 4. Install Dependencies: Install the Python libraries needed for the app.
# --no-cache-dir is used to keep the image size smaller.
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy Application Code: Copy the rest of your project files into the container.
COPY . .

# 6. Expose Port: Tell Docker that the container listens on port 8501 (the default for Streamlit).
EXPOSE 8501

# 7. Run Command: Specify the command to execute when the container starts.
# We need to specify the server address to allow external access.
CMD ["streamlit", "run", "dashboard1.py", "--server.port=8501", "--server.address=0.0.0.0"]