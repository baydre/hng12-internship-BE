# HNG Internship Backend

Welcome to my repository for the HNG Internship 12 Backend! This repository contains all my tasks for the period of my Internship.

## About HNG Internship

HNG Internship is a fast-paced bootcamp for learning digital skills. It's focused on advanced learners and those with some pre-knowledge, and it gets people into shape for job offers. In the HNG bootcamp, you work in teams to build apps and solve problems. 

# HNG Stage 0 Task

Develop a public API that returns the following information in JSON format:
- Your registered email address (used to register on the HNG12 Slack workspace).
- The current datetime as an ISO 8601 formatted timestamp.
- The GitHub URL of the project's codebase.

## Description

This is a simple REST API built with Python Flask that returns specific user information in JSON format. It was built as part of the HNG Internship Stage 0 task.

## Features

- Returns user information in JSON format
- Provides current datetime in ISO 8601 format
- Handles CORS
- Fast response time

## API Reference

### Get User Information

```http
  GET /basic-info
```

#### Response Format

```json
{
    "email": "your-email@example.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/yourusername/your-repo"
}
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/baydre/hng12-internship-BE # https
  git clone git@github.com:baydre/hng12-internship-BE.git # SSH
```

Go to the project directory

```bash
  cd stage0
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python main.py
```

## Tech Stack

- Python
- Flask
- Flask-CORS

## Deployment

This API is deployed on [Render](https://dashboard.render.com) and can be accessed at [Baydre-HNGInfoAPI](https://baydre-hnginfoapi.onrender.com)

## Authors

- [@baydre](https://github.com/baydre)

Open to coders, designers, product managers, and many more. Learn more at [HNG Internship](https://hng.tech).

## Backlinks
- [Hire Python Developers](https://hng.tech/hire/python-developers)
- [Hire C# Developers](https://hng.tech/hire/csharp-developers)
- [Hire Go Developers](https://hng.tech/hire/golang-developers)
- [Hire PHP Developers](https://hng.tech/hire/php-developers)
- [Hire Java Developers](https://hng.tech/hire/java-developers)
- [Hire Node.js Developers](https://hng.tech/hire/nodejs-developers)