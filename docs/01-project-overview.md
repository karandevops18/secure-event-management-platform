# Project Overview

## Introduction

The **Secure Event Management Platform** is a production-style cloud-native application designed to simulate how modern enterprise applications are developed, containerized, deployed, secured, and operated.

The project was created as a hands-on engineering lab to gain practical experience across multiple domains:

* Application containerization
* Kubernetes orchestration
* Cloud infrastructure
* DevSecOps automation
* Security hardening

Rather than treating deployment as a single step, this project follows a phased engineering approach that gradually evolves the platform from local development to cloud-scale production infrastructure.

---

## Problem Statement

Modern applications are no longer deployed as single monolithic services running on standalone servers.

Organizations increasingly rely on:

* Containers
* Kubernetes
* Infrastructure as Code
* CI/CD pipelines
* Cloud-native security controls

To build practical expertise in these areas, a real-world multi-tier application was required that could simulate production deployment patterns and security challenges.

The Secure Event Management Platform serves as that learning environment.

---

## Project Objective

The primary objectives of this project are:

### Application Deployment

Deploy a complete 3-tier web application consisting of frontend, backend, and database layers.

### Containerization

Package each application component into isolated Docker containers.

### Kubernetes Orchestration

Deploy and manage the application using Kubernetes resources such as:

* Deployments
* Services
* Namespaces
* Pod networking

### Cloud Deployment

Prepare the application for production deployment on AWS using managed Kubernetes services.

### Security Hardening

Apply security best practices for containers and Kubernetes workloads.

### DevSecOps Integration

Integrate security scanning and automation into CI/CD pipelines.

---

## Application Overview

The platform is designed as a 3-tier architecture.

### Frontend Layer

The frontend provides the user interface for interacting with the application.

Responsibilities:

* User registration
* User interaction
* Sending API requests to backend
* Rendering responses

Technology used:

* HTML
* CSS
* JavaScript
* Nginx

---

### Backend Layer

The backend exposes REST API endpoints for application logic.

Responsibilities:

* User registration processing
* API request handling
* Business logic execution
* Database interaction

Technology used:

* Python
* Flask
* SQLAlchemy

---

### Database Layer

The database stores persistent application data.

Responsibilities:

* Store users
* Store events
* Store booking records

Technology used:

* PostgreSQL

---

## Architecture Evolution

This project is intentionally built in multiple phases to simulate how applications evolve in real environments.

---

## Phase 0 — Local Docker Deployment

In Phase 0, the application was containerized and executed locally using Docker Compose.

Goals:

* Build Docker images
* Validate container communication
* Test application locally
* Understand container networking

Key components:

* Frontend container
* Backend container
* PostgreSQL container
* Docker bridge network
* Docker volumes

Outcome:

A fully functional local multi-container application.

Status: Completed

---

## Phase 1 — Local Kubernetes Deployment Using KIND

In Phase 1, the application was migrated from Docker Compose to Kubernetes using KIND (Kubernetes in Docker).

Goals:

* Learn Kubernetes fundamentals
* Deploy workloads using manifests
* Understand Services and networking
* Validate inter-pod communication

Implemented resources:

* Namespace
* Deployments
* Services
* Pods
* Port forwarding

Challenges addressed:

* Service discovery
* KIND networking limitations
* External service exposure
* NodePort limitations in nested virtualization

Outcome:

Successfully deployed the entire application stack on a local Kubernetes cluster.

Status: Completed

---

## Phase 1.1 — AWS EKS Production Deployment

Phase 1.1 will migrate the application from local Kubernetes to AWS Elastic Kubernetes Service (EKS).

Goals:

* Build production-grade cloud infrastructure
* Provision EKS using Terraform
* Push images to Amazon ECR
* Deploy workloads to EKS
* Expose services via Load Balancer / Ingress

Planned infrastructure:

* VPC
* Public / Private subnets
* NAT Gateway
* Security Groups
* EKS cluster
* Worker nodes
* ECR repositories
* Optional RDS database

Status: Planned

---

## Phase 2 — Kubernetes Security Hardening

This phase focuses on strengthening workload and cluster security.

Planned controls:

* Kubernetes Secrets
* ConfigMaps
* SecurityContext
* RBAC
* Network Policies
* Least privilege access
* Pod security hardening

Status: Planned

---

## Phase 3 — DevSecOps Automation

Phase 3 focuses on automated security validation and continuous compliance.

Planned integrations:

* Container image scanning
* Kubernetes CIS benchmark checks
* Runtime security monitoring
* Security pipeline automation

Potential tools:

* Trivy
* kube-bench
* kube-hunter
* Wazuh

Status: Planned

---

## Technology Stack

### Application Stack

* HTML
* CSS
* JavaScript
* Python
* Flask
* PostgreSQL

### Containerization

* Docker
* Docker Compose

### Orchestration

* Kubernetes
* KIND

### Cloud / Infrastructure

* AWS
* Terraform

### CI/CD

* GitHub Actions

### Security

* Container Scanning
* Kubernetes Security Controls
* DevSecOps Tooling

---

## Key Learning Goals

This project helps build hands-on expertise in:

* Cloud-native architecture
* Container orchestration
* Infrastructure automation
* Security engineering
* DevSecOps practices
* Production deployment workflows

---

## Summary

The Secure Event Management Platform is more than a simple application deployment project.

It represents a complete engineering journey from:

Local Development
→ Containerization
→ Kubernetes
→ Cloud Deployment
→ Security Hardening
→ DevSecOps Automation

This phased approach ensures strong practical understanding of modern infrastructure engineering and security-focused cloud operations.
