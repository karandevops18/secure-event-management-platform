# Phase 0 — Local Docker Deployment

## Overview

Before moving the application to Kubernetes, the Secure Event Management Platform was first containerized and deployed locally using Docker and Docker Compose.

This phase focused on validating:

* Application containerization
* Multi-container orchestration
* Service-to-service communication
* Local development workflow
* Container networking

This served as the foundation for the later Kubernetes migration.

---

## Objective

The primary goals of this phase were:

* Containerize frontend application
* Containerize backend application
* Deploy PostgreSQL as database container
* Enable communication between services
* Validate end-to-end functionality before Kubernetes

---

## Architecture

Phase 0 used a Docker-based 3-tier architecture.

Components:

### Frontend Container

Responsible for serving static UI files through Nginx.

### Backend Container

Runs Flask application and exposes REST API endpoints.

### Database Container

Runs PostgreSQL and stores persistent application data.

Application request flow:

Browser
→ Frontend Container
→ Backend Container
→ PostgreSQL Container

Architecture Diagram:

```text id="dqecbe"
architecture/phase-0-docker-architecture.png
```

---

## Prerequisites

Install required tools:

### Docker

Verify installation:

```bash id="x1hjlwm"
docker --version
```

---

### Docker Compose

Verify installation:

```bash id="ujn6bd"
docker compose version
```

---

## Project Structure During Docker Phase

```text id="rn3qq4"
secure-event-management-platform/
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│
├── frontend/
│   ├── Dockerfile
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── docker-compose.yml
```

---

# Backend Containerization

## Backend Dockerfile

The backend container was built using Python slim base image.

Responsibilities:

* Install dependencies
* Copy application code
* Create non-root user
* Expose Flask application port

Key features:

* Lightweight Python image
* Reduced attack surface
* Non-root container execution

Build backend image:

```bash id="9z3ahw"
cd backend
docker build -t secure-event-backend:v1 .
```

Verify image:

```bash id="6lz4ck"
docker images
```

---

# Frontend Containerization

## Frontend Dockerfile

Frontend container uses Nginx to serve static assets.

Responsibilities:

* Serve HTML
* Serve CSS
* Serve JavaScript
* Reverse proxy not used in Phase 0

Key features:

* Lightweight web server
* Fast static content delivery

Build frontend image:

```bash id="jl7c4v"
cd frontend
docker build -t secure-event-frontend:v1 .
```

Verify image:

```bash id="n8jlwm"
docker images
```

---

# Database Container

PostgreSQL was used as the relational database.

Database configuration:

* Database Name: `eventdb`
* Username: `eventadmin`
* Port: `5432`

Docker image used:

```text id="6oj9fk"
postgres:17
```

---

# Docker Compose Orchestration

Docker Compose was used to orchestrate all three services.

Services defined:

* postgres
* backend
* frontend

Responsibilities of Docker Compose:

* Create shared network
* Start services in order
* Manage container lifecycle
* Simplify multi-container deployment

---

## Start Application

Run:

```bash id="l10q8d"
docker compose up --build
```

Detached mode:

```bash id="8oosr4"
docker compose up -d
```

---

## Verify Containers

Check running containers:

```bash id="98w4ut"
docker ps
```

Expected containers:

* postgres-db
* secure-event-backend
* secure-event-frontend

Check all containers including exited:

```bash id="7k4wm7"
docker ps -a
```

---

# Container Networking

Docker Compose automatically created an internal bridge network.

Benefits:

* Containers communicate using service names
* No manual IP management
* Isolated application networking

Example backend database host:

Instead of:

```text id="pyn7cr"
localhost
```

Use:

```text id="k9xj1q"
postgres
```

This enabled backend-to-database communication.

---

# Database Configuration

Backend used environment variables for database connection.

Example configuration:

* DB_USER
* DB_PASSWORD
* DB_HOST
* DB_PORT
* DB_NAME

SQLAlchemy connection string pattern:

```text id="s5nghb"
postgresql+psycopg://user:password@host:port/database
```

---

# Application Validation

Frontend access:

```text id="75fq8t"
http://localhost:8080
```

Backend health endpoint:

```text id="g6oszk"
http://localhost:5000/health
```

Database access:

```bash id="2yw8h7"
docker exec -it postgres-db psql -U eventadmin -d eventdb
```

Validate users table:

```sql id="jcczzm"
SELECT * FROM users;
```

---

# Functional Testing

The following functionality was validated:

### Frontend Accessibility

Frontend UI loaded successfully.

### Backend API

Backend API returned healthy response.

### Database Connectivity

Backend successfully connected to PostgreSQL.

### User Registration

Users successfully inserted into database.

Example validation:

```sql id="uvj9j2"
SELECT id, name, email FROM users;
```

---


# Local Python Environment Setup
For local Python development, a virtual environment can optionally be created before installing backend dependencies.

Example:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


# Challenges Encountered

Several real-world issues were encountered during Docker deployment.

Examples:

* Backend container crash
* PostgreSQL connection refused
* Incorrect database host configuration
* Docker Compose service startup timing issues

These issues are documented in:

```text id="37sh7c"
docs/04-troubleshooting.md
```

---

# Key Learning Outcomes

This phase provided practical understanding of:

* Docker image creation
* Multi-container deployments
* Docker networking
* Service dependency management
* Container debugging
* Local infrastructure validation

---

# Summary

Phase 0 successfully transformed the application into a fully containerized system using Docker.

This phase established the deployment foundation required for the Kubernetes migration in Phase 1.

Outcome:

✔ Frontend containerized
✔ Backend containerized
✔ Database containerized
✔ Multi-container orchestration validated
✔ End-to-end workflow verified
