# Project Roadmap

## Overview

The Secure Event Management Platform is intentionally designed as a multi-phase engineering project.

Rather than stopping after a successful local deployment, the platform will continue evolving toward a production-grade cloud-native architecture with strong security and DevSecOps controls.

This roadmap defines the planned future phases.

---

# Completed Phases

## Phase 0 — Local Docker Deployment ✅

Completed objectives:

* Containerized frontend application
* Containerized backend application
* Deployed PostgreSQL database
* Validated multi-container communication
* Tested end-to-end user registration

Outcome:

A fully functional local 3-tier application running via Docker Compose.

---

## Phase 1 — Local Kubernetes Deployment Using KIND ✅

Completed objectives:

* Installed Kubernetes tooling
* Created KIND cluster
* Deployed PostgreSQL on Kubernetes
* Deployed backend workload
* Deployed frontend workload
* Validated inter-service communication
* Verified end-to-end workflow

Outcome:

Successfully migrated the application from Docker Compose to Kubernetes.

---

# Upcoming Phases

## Phase 1.1 — AWS EKS Production Deployment

### Objective

Migrate the local Kubernetes deployment to a production-style AWS environment.

---

## Planned Infrastructure

AWS resources to be provisioned using Terraform:

### Networking

* VPC
* Public subnets
* Private subnets
* Internet Gateway
* Route Tables
* NAT Gateway

### Security

* Security Groups
* IAM Roles
* IAM Policies

### Compute / Containers

* Amazon EKS Cluster
* Managed Node Groups
* Worker Nodes

### Container Registry

* Amazon ECR for frontend images
* Amazon ECR for backend images

### Application Exposure

* AWS Load Balancer
* Kubernetes Ingress
* DNS routing

### Optional Managed Services

* Amazon RDS PostgreSQL
* AWS Secrets Manager

---

## Phase 1.1 Deliverables

Expected deliverables:

* Terraform modules
* Infrastructure diagrams
* EKS cluster deployment
* Kubernetes deployment on EKS
* Public application access
* Cloud architecture documentation

---

## Skills Focus

This phase will strengthen:

* AWS networking
* EKS administration
* Terraform IaC
* Cloud architecture design
* Production Kubernetes deployment

---

# Phase 2 — Kubernetes Security Hardening

### Objective

Transform the Kubernetes deployment into a security-hardened environment using production best practices.

---

## Planned Security Controls

### Secrets Management

Replace plaintext credentials with Kubernetes Secrets.

Examples:

* Database passwords
* API secrets
* Sensitive configuration

---

### ConfigMaps

Externalize non-sensitive configuration.

Examples:

* Environment variables
* Application configuration
* Runtime settings

---

### Resource Constraints

Add workload resource limits.

Examples:

* CPU limits
* Memory limits
* Requests

Benefits:

* Prevent resource abuse
* Improve scheduling reliability

---

### Health Probes

Add:

* liveness probes
* readiness probes

Benefits:

* Self-healing workloads
* Better availability

---

### Security Context

Harden container execution.

Examples:

* non-root containers
* privilege reduction
* filesystem controls

---

### RBAC

Implement role-based access control.

Goals:

* Least privilege
* Controlled cluster access
* Reduced attack surface

---

### Network Policies

Restrict pod-to-pod communication.

Desired communication model:

Frontend → Backend allowed
Backend → PostgreSQL allowed
All other traffic denied

Benefits:

* Zero-trust networking
* Reduced lateral movement

---

## Phase 2 Deliverables

Expected deliverables:

* Hardened Kubernetes manifests
* Security policy documentation
* Access control design
* Security validation report

---

## Skills Focus

This phase strengthens:

* Kubernetes security
* Security engineering
* Zero-trust architecture
* Cluster hardening

---

# Phase 3 — DevSecOps Automation

### Objective

Integrate security controls into CI/CD workflows and automate continuous validation.

---

## Planned Security Automation

### Container Image Scanning

Scan images for:

* vulnerabilities
* CVEs
* misconfigurations

Potential tool:

* [Trivy](https://trivy.dev?utm_source=chatgpt.com)

---

### Kubernetes Benchmark Validation

Validate cluster against CIS benchmarks.

Potential tool:

* [kube-bench](https://github.com/aquasecurity/kube-bench?utm_source=chatgpt.com)

---

### Kubernetes Attack Surface Analysis

Identify exposed attack paths.

Potential tool:

* [kube-hunter](https://github.com/aquasecurity/kube-hunter?utm_source=chatgpt.com)

---

### Runtime Security Monitoring

Monitor runtime behavior for suspicious activity.

Potential integration:

* Wazuh
* Falco

---

### CI/CD Security Gates

Pipeline stages:

Code Commit
→ Build
→ Security Scan
→ Policy Validation
→ Deploy

Security checks must pass before deployment.

---

## Phase 3 Deliverables

Expected deliverables:

* GitHub Actions pipeline
* Security scan reports
* Automated policy validation
* Runtime monitoring dashboard

---

## Skills Focus

This phase strengthens:

* DevSecOps
* Security automation
* Continuous compliance
* Shift-left security

---

# Long-Term Vision

The long-term goal of this project is to evolve from a learning lab into a realistic production-grade reference architecture that demonstrates:

* Cloud infrastructure engineering
* Kubernetes operations
* Security engineering
* DevSecOps automation
* Production deployment workflows

This project will serve as a continuously evolving portfolio artifact for demonstrating practical engineering capability across cloud, security, and automation domains.

---

# Final Roadmap Summary

Project evolution:

Local Development
→ Docker Containerization
→ Local Kubernetes (KIND)
→ AWS EKS Deployment
→ Security Hardening
→ DevSecOps Automation
→ Production-Grade Cloud Security Platform
