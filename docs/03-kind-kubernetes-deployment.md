# Phase 1 — Local Kubernetes Deployment Using KIND

## Overview

After validating the application using Docker Compose, the next phase involved migrating the Secure Event Management Platform to Kubernetes.

A local Kubernetes environment was created using **KIND (Kubernetes IN Docker)**.

This phase focused on understanding how production-style Kubernetes deployments work while keeping infrastructure lightweight and reproducible on a local machine.

---

## Objective

The primary goals of this phase were:

* Learn Kubernetes fundamentals
* Deploy a multi-tier application on Kubernetes
* Understand pod networking and service discovery
* Replace Docker Compose orchestration with Kubernetes manifests
* Prepare application for future AWS EKS migration

---

## Why KIND?

KIND (Kubernetes in Docker) was selected because it provides a lightweight local Kubernetes cluster suitable for development and testing.

Benefits:

* Lightweight
* Easy setup
* Fast cluster creation
* Ideal for Kubernetes learning labs
* Runs locally without cloud cost

Important limitation:

KIND runs Kubernetes nodes inside Docker containers, which introduces networking differences compared to cloud-managed clusters such as AWS EKS.

---

## Prerequisites

Required tools:

### Docker

Verify:

```bash id="k1p9vq"
docker --version
```

---

### kubectl

Verify:

```bash id="n3x6lt"
kubectl version --client
```

---

### KIND

Verify:

```bash id="m4r7qs"
kind version
```

---

## Cluster Creation

Create Kubernetes cluster:

```bash id="p2v8wd"
kind create cluster --name secure-event-cluster
```

Expected output:

* Node image download
* Control plane creation
* CNI installation
* StorageClass installation

Verify cluster:

```bash id="t6m2ky"
kubectl cluster-info
```

Check nodes:

```bash id="x9q4rv"
kubectl get nodes
```

Expected:

```text id="79f1az"
secure-event-cluster-control-plane   Ready
```

---

# Namespace Creation

A dedicated namespace was created for workload isolation.

Namespace manifest:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: secure-event
```

Apply:

```bash id="d4w7qn"
kubectl apply -f kubernetes/namespace.yaml
```

Verify:

```bash id="u5r9mc"
kubectl get namespaces
```

Expected namespace:

```text id="q1l8sv"
secure-event
```

---

# Kubernetes Resource Layout

Project manifests were organized as follows:

```text id="k7p1xz"
kubernetes/
│
├── namespace.yaml
│
├── postgres/
│   ├── deployment.yaml
│   └── service.yaml
│
├── backend/
│   ├── deployment.yaml
│   └── service.yaml
│
└── frontend/
    ├── deployment.yaml
    └── service.yaml
```

---

# PostgreSQL Deployment

PostgreSQL was deployed first because backend depends on database availability.

---

## Deployment

Responsibilities:

* Run PostgreSQL container
* Persist application data
* Accept internal Kubernetes traffic

Deploy:

```bash id="v8n3px"
kubectl apply -f kubernetes/postgres/deployment.yaml
```

---

## Service

A ClusterIP service was created for internal database access.

Deploy:

```bash id="f2m6tw"
kubectl apply -f kubernetes/postgres/service.yaml
```

Verify:

```bash id="c4r1qp"
kubectl get pods -n secure-event
kubectl get svc -n secure-event
```

Expected service:

```text id="n7x5mz"
postgres-service   ClusterIP   5432
```

---

# Backend Deployment

The backend Flask application was deployed after PostgreSQL.

---

## Backend Image Preparation

Since KIND uses internal Docker nodes, locally built images must be loaded into the cluster manually.

Build backend image:

```bash id="w3k8ny"
cd backend
docker build -t secure-event-backend:v1 .
```

Load image into KIND:

```bash id="r5m1qv"
kind load docker-image secure-event-backend:v1 --name secure-event-cluster
```

---

## Backend Deployment

Deploy backend:

```bash id="j9p2tr"
kubectl apply -f kubernetes/backend/deployment.yaml
```

---

## Backend Service

Deploy service:

```bash id="h4n8kx"
kubectl apply -f kubernetes/backend/service.yaml
```

Verify:

```bash id="b1v6qw"
kubectl get pods -n secure-event
kubectl get svc -n secure-event
```

Expected:

```text id="m6r3px"
backend-service
```

---

# Backend Health Validation

Verify backend health:

```bash id="k8w4tz"
kubectl port-forward service/backend-service 5000:5000 -n secure-event --address 0.0.0.0
```

Test:

```bash id="d3n7qy"
curl http://localhost:5000/health
```

Expected:

```json
{"status":"healthy"}
```

This confirmed:

* backend pod running
* service routing functional
* database connection successful

---

# Frontend Deployment

The frontend application was deployed after backend validation.

---

## Frontend Image Preparation

Build image:

```bash id="q7r1mv"
cd frontend
docker build -t secure-event-frontend:v1 .
```

Load image:

```bash id="u2m8pk"
kind load docker-image secure-event-frontend:v1 --name secure-event-cluster
```

---

## Frontend Deployment

Deploy:

```bash id="n5w2rx"
kubectl apply -f kubernetes/frontend/deployment.yaml
```

Deploy service:

```bash id="l1q8vm"
kubectl apply -f kubernetes/frontend/service.yaml
```

Verify:

```bash id="x3m6kt"
kubectl get pods -n secure-event
```

Expected:

```text id="j2v7pr"
frontend   Running
backend    Running
postgres   Running
```

---

# Service Exposure

Since KIND runs inside Docker, external access differs from normal Kubernetes clusters.

Initial attempt:

* NodePort service
* Host IP access

Issue:

NodePort was not directly accessible because KIND node networking differs from standard VM/bare-metal clusters.

---

## Port Forwarding Solution

Port forwarding was used for external access.

### Backend

```bash id="z8p4tx"
kubectl port-forward service/backend-service 5000:5000 -n secure-event --address 0.0.0.0
```

---

### Frontend

```bash id="g4r9kw"
kubectl port-forward service/frontend-service 8080:80 -n secure-event --address 0.0.0.0
```

---

# Application Validation

Frontend access:

```text id="u7n3qs"
http://<VM-IP>:8080
```

Backend health:

```text id="t5p8mv"
http://<VM-IP>:5000/health
```

---

# Functional Testing

The following validations were performed.

### Pod Status Validation

All workloads reached running state.

### Service Communication

Validated:

* frontend → backend
* backend → postgres

### User Registration Test

A test user was registered successfully.

This confirmed full end-to-end application flow.

Application flow:

Browser
→ Frontend Pod
→ Backend Pod
→ PostgreSQL Pod

---

# Key Challenges Encountered

Several practical issues were encountered during deployment.

Examples:

* Missing kubectl
* Missing KIND
* Namespace missing errors
* Backend image unavailable inside KIND
* PostgreSQL startup delays
* NodePort access failure
* IPv6 networking issues
* Hyper-V storage constraints

Detailed troubleshooting:

```text id="f8r2ny"
docs/04-troubleshooting.md
```

---

# Key Learning Outcomes

This phase provided practical understanding of:

* Kubernetes architecture
* Namespaces
* Deployments
* Services
* Pod lifecycle
* Service discovery
* Port forwarding
* Local cluster limitations
* Production migration planning

---

# KIND vs Production Kubernetes

Important distinction:

### KIND

Best for:

* Learning
* Local testing
* CI pipelines

Limitations:

* Complex external networking
* No managed load balancers
* Limited production realism

---

### Production Kubernetes (EKS)

Provides:

* Managed control plane
* Real networking
* Load Balancers
* IAM integration
* Autoscaling
* Cloud-native security

This makes Phase 1 a critical stepping stone toward Phase 1.1 (AWS EKS).

---

# Summary

Phase 1 successfully migrated the application from Docker Compose to Kubernetes.

Outcome:

✔ KIND cluster created
✔ Namespace configured
✔ PostgreSQL deployed
✔ Backend deployed
✔ Frontend deployed
✔ Inter-service networking validated
✔ End-to-end user registration verified

This completed the first Kubernetes deployment milestone and established the foundation for cloud-native production deployment.

