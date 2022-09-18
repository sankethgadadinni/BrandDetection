# Use/extend python3.9-slim-buster image
FROM python:3.8

WORKDIR /app

# Copy app.py, README.md, requirements.txt and config.toml
# COPY ["app.py", "detect.py", "requirements.txt", "./"]
COPY requirements.txt ./requirements.txt

# Install python dependencies
RUN pip3 install -r requirements.txt

# Expose the streamlit port
EXPOSE 8501

COPY . /app

# Set entrypoint and cmd
ENTRYPOINT ["streamlit", "run"]
CMD [ "app.py" ]



