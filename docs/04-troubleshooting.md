# Troubleshooting Guide

## Overview

During Docker and Kubernetes deployment of the Secure Event Management Platform, multiple real-world infrastructure and networking issues were encountered.

This document records:

* Error symptoms
* Root causes
* Resolution steps
* Key learnings

The purpose of this guide is to ensure the environment can be reproduced and debugged efficiently in future deployments.

---

# Issue 1 — Docker Compose Not Starting Containers Correctly

## Problem

After running Docker Compose, expected containers were not running properly.

Example validation:

```bash id="mpk1me"
docker ps
```

Output showed missing containers or exited containers.

---

## Symptoms

* Backend container missing
* Containers exited unexpectedly
* Application inaccessible

---

## Root Cause

Docker Compose startup order alone did not guarantee service readiness.

Even if PostgreSQL container started first, the database service inside container was not fully ready when backend attempted connection.

---

## Resolution

Check all containers:

```bash id="r6grut"
docker ps -a
```

Inspect logs:

```bash id="uexzrn"
docker logs secure-event-backend
```

This revealed backend startup failure due to database readiness timing.

---

## Learning

Container startup order does not guarantee application readiness.

Production systems should use:

* health checks
* readiness checks
* wait-for-db logic

---

# Issue 2 — PostgreSQL Connection Refused

## Problem

Backend container failed during startup.

Error:

```text id="hm5gbr"
connection refused
```

---

## Symptoms

Backend exited with status code 1.

Logs showed SQLAlchemy connection failure.

---

## Root Cause

Backend attempted database connection before PostgreSQL finished initialization.

---

## Resolution

Temporary startup delay added in backend.

Example:

```python id="rk0mbs"
import time
time.sleep(20)
```

This allowed PostgreSQL enough time to become ready before backend executed:

```python id="u3djzq"
db.create_all()
```

---

## Learning

Applications with hard dependencies need readiness handling.

Better long-term solutions:

* Docker health checks
* retry logic
* orchestration readiness probes

---

# Issue 3 — Backend Container Exiting Immediately

## Problem

Backend container repeatedly exited.

Validation:

```bash id="nox73u"
docker ps -a
```

Example:

```text id="dzhjz5"
Exited (1)
```

---

## Root Cause

Application startup failed because database connection failed during initialization.

The failure happened before Flask server could start.

---

## Resolution

Investigated using:

```bash id="h0rmmt"
docker logs secure-event-backend
```

Resolved database connectivity first.

---

## Learning

Always inspect container logs before debugging application code.

---

# Issue 4 — Docker Network / Host IP Confusion

## Problem

Frontend JavaScript API endpoint stopped working after network changes.

Example old configuration:

```javascript id="mjlwmz"
const API_URL = "http://192.168.x.x:5000/api";
```

---

## Symptoms

Frontend loaded successfully but API calls failed.

---

## Root Cause

Machine IP changed due to location/network change.

Static IP references inside frontend became invalid.

---

## Resolution

Update frontend API endpoint to current host/VM IP.

Rebuild frontend image.

---

## Learning

Hardcoded IP addresses create operational issues.

Production environments should use:

* DNS
* reverse proxy
* ingress routing

---

# Issue 5 — Missing Kubernetes Tools

## Problem

Required Kubernetes tools were missing.

Errors:

```text id="k79l33"
kubectl: command not found
kind: command not found
```

---

## Root Cause

Local environment not prepared for Kubernetes workflow.

---

## Resolution

Installed:

* kubectl
* kind

Validated installation:

```bash id="wdg79n"
kubectl version --client
kind version
```

---

## Learning

Always validate tooling before cluster deployment.

---

# Issue 6 — Namespace Not Found

## Problem

Kubernetes resources failed to deploy.

Error:

```text id="z8htjf"
namespaces "secure-event" not found
```

---

## Root Cause

Deployment manifests referenced namespace before namespace resource existed.

---

## Resolution

Create namespace first.

```bash id="g74g7o"
kubectl apply -f kubernetes/namespace.yaml
```

Verify:

```bash id="gcx94m"
kubectl get namespaces
```

---

## Learning

Namespace resources must be created before namespace-scoped workloads.

---

# Issue 7 — KIND Image Availability Problem

## Problem

Kubernetes deployment could not start backend/frontend pods.

---

## Symptoms

Pods stuck in image pull errors or failed startup.

---

## Root Cause

Locally built Docker images are not automatically available inside KIND nodes.

KIND runs Kubernetes nodes inside separate Docker containers.

---

## Resolution

Load images manually.

Backend:

```bash id="a2f9t0"
kind load docker-image secure-event-backend:v1 --name secure-event-cluster
```

Frontend:

```bash id="agf0pw"
kind load docker-image secure-event-frontend:v1 --name secure-event-cluster
```

---

## Learning

KIND requires explicit image loading for locally built images.

Cloud clusters use container registries instead.

---

# Issue 8 — IPv6 Networking Problems

## Problem

Network operations showed delays or connectivity issues.

Example:

```bash id="b4g6gx"
ping google.com
```

IPv6 resolution caused problems.

---

## Symptoms

* Failed ping
* Delayed connectivity
* Image pull issues

---

## Root Cause

System preferred IPv6 routes while local environment worked better over IPv4.

---

## Resolution

Temporarily disabled IPv6 via system configuration.

---

## Learning

Dual-stack networking can introduce unexpected routing issues in lab environments.

---

# Issue 9 — Hyper-V Disk Space Exhaustion

## Problem

Ubuntu VM disk usage became critically high.

Validation:

```bash id="d3r0jt"
df -h
```

Disk usage exceeded safe threshold.

---

## Symptoms

* Limited free space
* Image pull issues
* Build issues
* Cluster instability risk

---

## Root Cause

Disk consumed by:

* Docker images
* Volumes
* Build cache
* KIND node image

---

## Resolution

Checked disk usage:

```bash id="hh9vau"
docker system df
```

Expanded VM storage and cleaned unused Docker artifacts.

---

## Learning

Container-based lab environments consume storage rapidly.

Regular cleanup is essential.

---

# Issue 10 — KIND NodePort Not Reachable

## Problem

Backend service exposed using NodePort but remained inaccessible.

Service example:

```text id="sdj28h"
5000:30050/TCP
```

---

## Symptoms

Requests failed:

```bash id="me94m1"
curl http://VM-IP:30050/health
```

Connection refused.

---

## Root Cause

KIND networking differs from standard Kubernetes clusters.

NodePort traffic was not automatically exposed through:

* Docker
* Hyper-V
* Nested networking

---

## Resolution

Used port forwarding instead of NodePort.

Backend:

```bash id="zsv0r8"
kubectl port-forward service/backend-service 5000:5000 -n secure-event --address 0.0.0.0
```

Frontend:

```bash id="z63x3z"
kubectl port-forward service/frontend-service 8080:80 -n secure-event --address 0.0.0.0
```

---

## Learning

KIND is excellent for learning Kubernetes internals but has external networking limitations.

Production clusters typically use:

* LoadBalancer
* Ingress
* ALB / NLB

---

# Final Lessons

The troubleshooting process provided critical hands-on experience in:

* Container debugging
* Log analysis
* Service dependency handling
* Kubernetes networking
* Infrastructure diagnostics
* Storage management
* Real-world problem solving

These troubleshooting exercises were as valuable as the successful deployment itself.

---

# Summary

This troubleshooting journey demonstrated that successful infrastructure engineering is not only about deployment.

It requires the ability to:

* observe failures
* identify root causes
* validate hypotheses
* implement fixes
* document lessons learned

This debugging process significantly improved practical understanding of Docker, Kubernetes, networking, and cloud-native infrastructure behavior.
