# Masters Cloud Project  
E-Commerce Microservices Application 

## Project Overview  
This project demonstrates a simple e-commerce backend built using a microservices architecture. It consists of two independently deployable services—User Serviceand Product Service 
and a shared PostgreSQL database.
The application is designed for containerized deployment on Kubernetes, with each service exposing a REST API (documented using Swagger).

## Features  
- User Service: CRUD operations (GET, PUT, DELETE) for user data via Swagger-documented REST API  
- Product Service: CRUD operations (GET, PUT, DELETE) for product catalog via Swagger REST API  
- PostgreSQL Database: Stores user and product information, backed by a Kubernetes Persistent Volume Claim (PVC) so data persists across restarts  
- Kubernetes Deployment: Containerised microservices with Docker images, Kubernetes Deployments for services, Services for networking, Ingress/LoadBalancer for external access  
- Horizontal scalability: Each microservice can be scaled independently (adjust replica count or use Horizontal Pod Autoscaler)  
- Swagger UI: API documentation and interactive testing interface for both microservices  

## Architecture  
1. External client (web UI, REST client) → Ingress (or Service) routes requests  
2. Requests go to either User Service or Product Service depending on path  
3. Both services communicate with the PostgreSQL database for persistent storage  
4. Kubernetes Services provide discovery and load balancing; Deployments manage replicas; PVC ensures data persistence  

## Tech Stack  
- Programming languages: Python Flask,Html  
- API documentation: Swagger / OpenAPI  
- Database: PostgreSQL  
- Containerization: Docker (images pushed to Docker Hub)  
- Orchestration/Infrastructure: Kubernetes (Deployments, Services, Ingress, PVC)  
