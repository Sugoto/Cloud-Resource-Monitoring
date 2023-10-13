# Cloud Resource Monitoring Application

![Docker](https://img.shields.io/badge/Docker-✔-blue?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-✔-blue?logo=kubernetes)
![Amazon ECR](https://img.shields.io/badge/Amazon%20ECR-✔-blue?logo=amazon-aws)
![Amazon EKS](https://img.shields.io/badge/Amazon%20EKS-✔-blue?logo=amazon-aws)

Monitor and manage server resource utilization in the cloud with our Cloud Resource Monitoring Application. This application is designed to accurately measure the system resource usage of a server, leveraging Docker, Kubernetes, Amazon ECR, and Amazon EKS.

## Features

- 🐳 Utilizes Docker for containerization to ensure consistency and portability.
- ☸️ Uses Kubernetes for orchestration and scaling of monitoring components.
- 🌐 Integrates with Amazon ECR for secure and efficient container image storage.
- ☁️ Leverages Amazon EKS for a managed Kubernetes service, ensuring high availability and ease of management.

## Getting Started

### Prerequisites

Before you begin, make sure you have the following prerequisites:

- Docker installed: [Docker Installation Guide](https://docs.docker.com/get-docker/)
- Kubernetes cluster (Amazon EKS or other): [Amazon EKS Getting Started](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)
- Access to Amazon ECR for container image storage: [Amazon ECR Documentation](https://aws.amazon.com/ecr/)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Sugoto/cloud-resource-monitoring.git
   ```

2. Build and deploy the application using your Kubernetes cluster.

   ```sh
   kubectl apply -f deployment.yaml
   ```

3. Access the monitoring dashboard.

## Usage

- Provide instructions on how to use the application.
- Include code samples and configuration details.
- Explain how to interpret the monitoring data.
