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
  GET /
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
  git clone https://github.com/yourusername/new-repo-name.git # https
  git clone git@github.com:yourusername/new-repo-name.git # SSH
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

## Acknowledgments

HNG Internship program links:
- [Python Developers](https://hng.tech/hire/python-developers)
- [C# Developers](https://hng.tech/hire/csharp-developers)
- [Golang Developers](https://hng.tech/hire/golang-developers)
- [PHP Developers](https://hng.tech/hire/php-developers)
- [Java Developers](https://hng.tech/hire/java-developers)
- [NodeJS Developers](https://hng.tech/hire/nodejs-developers)