# Secure Event Management Platform

A production-style **3-tier web application** built to simulate real-world cloud-native deployment and security practices.

This project demonstrates the end-to-end journey of deploying a modern application across multiple stages:

* Local containerized development using Docker Compose
* Kubernetes orchestration using KIND (Kubernetes in Docker)
* Future cloud deployment on AWS EKS using Terraform and GitHub Actions
* Security hardening using Kubernetes security best practices and DevSecOps tooling

The application consists of three main layers:

* **Frontend** — Nginx-based static UI (HTML/CSS/JavaScript)
* **Backend** — Flask REST API
* **Database** — PostgreSQL

## Project Goals

This project was built to gain hands-on experience in:

* Containerization with Docker
* Multi-container orchestration with Docker Compose
* Kubernetes deployments and service networking
* Cloud-native application architecture
* DevSecOps and Kubernetes security hardening
* Infrastructure as Code (Terraform)
* CI/CD automation using GitHub Actions

## Current Project Status

### Phase 0 — Local Docker Deployment ✅

* Dockerized frontend, backend, and database
* Multi-container orchestration using Docker Compose
* Internal service communication via Docker network

### Phase 1 — Local Kubernetes Deployment (KIND) ✅

* Kubernetes cluster setup using KIND
* Deployments and Services for all application tiers
* Pod networking and service discovery
* External access using port forwarding

### Phase 1.1 — AWS EKS Deployment ⏳

Planned:

* Terraform-based AWS infrastructure
* EKS cluster provisioning
* Amazon ECR image registry
* GitHub Actions CI/CD pipeline
* ALB / Ingress integration

### Phase 2 — Kubernetes Security Hardening ⏳

Planned:

* Secrets management
* ConfigMaps
* RBAC
* Network Policies
* SecurityContext hardening

### Phase 3 — DevSecOps Security Automation ⏳

Planned:

* Container image scanning
* Kubernetes CIS benchmark checks
* Runtime threat detection
* Security monitoring integration

---

## Architecture Overview

### Phase 0 — Docker Compose Architecture

The application was initially deployed locally using Docker Compose with three isolated containers:

* Frontend Container (Nginx)
* Backend Container (Flask API)
* Database Container (PostgreSQL)

Request flow:

```text
Browser → Frontend Container → Backend Container → PostgreSQL
```

Architecture Diagram:

```text
architecture/phase-0-docker-architecture.png
```

---

### Phase 1 — Kubernetes (KIND) Architecture

The application was later migrated to Kubernetes using **KIND (Kubernetes in Docker)**.

Components deployed in Kubernetes:

* Namespace: `secure-event`
* PostgreSQL Deployment + Service
* Backend Deployment + Service
* Frontend Deployment + Service

Request flow:

```text
Browser → Frontend Pod → Backend Pod → PostgreSQL Pod
```

Architecture Diagram:

```text
architecture/phase-1-kind-architecture.png
```

---

## Repository Structure

```text
secure-event-management-platform/
│
├── architecture/         # Architecture diagrams and screenshots
├── backend/              # Flask backend application
├── frontend/             # Nginx frontend application
├── kubernetes/           # Kubernetes manifests
├── docs/                 # Detailed project documentation
├── terraform/            # Reserved for Phase 1.1 (AWS EKS)
├── docker-compose.yml
└── README.md
```

---

## Documentation Index

Detailed documentation is available in the `docs/` directory.

### Project Documentation

* `docs/01-project-overview.md`
* `docs/02-docker-deployment.md`
* `docs/03-kind-kubernetes-deployment.md`
* `docs/04-troubleshooting.md`
* `docs/05-lessons-learned.md`
* `docs/06-roadmap.md`

---

## Skills Demonstrated

This project demonstrates practical experience with:

### Cloud & Infrastructure

* AWS Architecture Planning
* Infrastructure Design
* Terraform (planned for Phase 1.1)

### Containers & Orchestration

* Docker
* Docker Compose
* Kubernetes
* KIND

### DevOps / Automation

* Git
* GitHub
* CI/CD Pipeline Design
* GitHub Actions (planned)

### Security / DevSecOps

* Container Security
* Kubernetes Security
* Network Segmentation
* Security Hardening

---

## Quick Start

### Clone Repository

```bash
git clone <repository-url>
cd secure-event-management-platform
```

---

### Run Using Docker Compose

```bash
docker compose up --build
```

Application access:

* Frontend: `http://localhost:8080`
* Backend API: `http://localhost:5000`
* PostgreSQL: `localhost:5432`

---

### Run Using Kubernetes (KIND)

Create cluster:

```bash
kind create cluster --name secure-event-cluster
```

Deploy application:

```bash
kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/postgres/
kubectl apply -f kubernetes/backend/
kubectl apply -f kubernetes/frontend/
```

Port forward services:

```bash
kubectl port-forward service/backend-service 5000:5000 -n secure-event --address 0.0.0.0

kubectl port-forward service/frontend-service 8080:80 -n secure-event --address 0.0.0.0
```

Access application:

* Frontend: `http://<VM-IP>:8080`
* Backend Health Check: `http://<VM-IP>:5000/health`

---

## Future Enhancements

Planned improvements for upcoming phases:

* AWS EKS production deployment
* Terraform infrastructure automation
* Amazon ECR integration
* GitHub Actions CI/CD pipeline
* Kubernetes Secrets and ConfigMaps
* Network Policies
* RBAC implementation
* Security scanning using Trivy / kube-bench
* Runtime security monitoring

---

## Key Learning Outcomes

Through this project, the following practical concepts were implemented and validated:

* Multi-container application architecture
* Service-to-service communication
* Kubernetes networking and service discovery
* Container image management
* Local cluster orchestration using KIND
* Troubleshooting real-world infrastructure issues
* Production deployment planning on AWS

---

## Author

**Karan Singh Rajawat**

Cloud • DevOps • Security Engineering • DevSecOps

This project is part of a hands-on cloud security and DevSecOps learning journey focused on building production-style infrastructure and security-focused engineering practices.
