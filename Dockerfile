FROM python:3.8

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True
ENV PORT 5000

EXPOSE 5000


# Copy local code to the container image.
COPY . /src
WORKDIR /src

# Install Python Requirements
RUN pip install -r requirements/requirements.txt

# Run the web service on container startup.
CMD exec flask run