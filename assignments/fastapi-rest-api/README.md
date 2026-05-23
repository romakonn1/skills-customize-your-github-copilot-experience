# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using FastAPI by defining routes, validating request data, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description

Set up a FastAPI app and define the main API endpoints for managing a simple in-memory resource.

#### Requirements
Completed program should:

- Initialize a FastAPI application in a Python file
- Define a root endpoint (`GET /`) that returns a welcome JSON message
- Define a `GET /items/{item_id}` endpoint that retrieves an item by ID
- Define a `POST /items` endpoint that creates a new item from request data

### 🛠️ Add Request Validation and Response Models

#### Description

Use Pydantic models to validate incoming request payloads and format outgoing JSON responses.

#### Requirements
Completed program should:

- Define a Pydantic model for item data with fields such as `name`, `description`, and `price`
- Validate POST request bodies using the Pydantic model
- Return created items with an assigned `id`
- Use typed response models for endpoint return values

### 🛠️ Implement Error Handling and Data Storage

#### Description

Add simple application logic to store items in memory and return proper errors when requested resources are missing.

#### Requirements
Completed program should:

- Store created items in an in-memory list or dictionary
- Return a 404 error when an item is not found
- Return a success message when a new item is created
- Include example request/response behavior in comments or docstrings
