# My Flask App

A Python Flask web application containerized with Docker and automated via GitHub Actions. This project demonstrates secure use of environment variables, containerization, automated builds, and dependency management with Dependabot.

# Features
- Displays a customizable message on the home page (`/`) via the `APP_MESSAGE` environment variable.
- Shows application health on `/health` via the `APP_HEALTH` environment variable.
- Fully containerized using Docker.
- Automated build and deployment workflow using GitHub Actions.
- Dependabot keeps dependencies up-to-date for `pip`, Docker, and GitHub Actions.

# Getting Started

# Prerequisites
- Docker and Docker Compose installed locally.
- Python 3.14+ installed (optional if you only use Docker).

# Setup
1. Copy the example environment file:
   bash
   cp .env.example .env
