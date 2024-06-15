# Makefile

# Name of the Docker image
IMAGE_NAME := kubernetes-singleton
# Tag for the Docker image
IMAGE_TAG := latest

# Default target
.PHONY: all
all: build

# Build the Docker image
.PHONY: build
build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

# Push the Docker image to a registry (optional)
.PHONY: push
push:
	docker push $(IMAGE_NAME):$(IMAGE_TAG)

# Run the Docker container (optional)
.PHONY: run
run:
	docker run -p 4000:80 $(IMAGE_NAME):$(IMAGE_TAG)

# Clean up (optional)
.PHONY: clean
clean:
	docker rmi $(IMAGE_NAME):$(IMAGE_TAG)
