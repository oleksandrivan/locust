# Project Benchmarking

This project aims to benchmark different solutions for a master thesis project. The benchmarking process is facilitated using Locust.

## Prerequisites

Before you can build and run the benchmarking project, make sure you have the following prerequisites installed on your machine:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)

## Building the Project

To build the project, follow these steps:

Build the Docker image using the provided Dockerfile:

```shell
docker build -t load-tests .
```

This command will build the Docker image with the name `load-tests`.

## Running the Benchmark

To run the benchmark, execute the following command within the container running:

```shell
./run.sh legacy-load # alternatively `proxy-load`
```
