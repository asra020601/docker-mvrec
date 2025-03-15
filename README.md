# Docker MvRec - Movie Recommendation Website

## Overview
Docker MvRec is a simple, containerized movie recommendation website that suggests movies based on user input. Users can enter a movie they like, and the system will recommend similar movies they might enjoy.

## Features
- Single-input movie recommendation system
- Clean, user-friendly interface
- Quick response with relevant movie suggestions
- Dockerized deployment for easy setup

## Technologies
- Docker
- Python
- FastAPI (Backend)
- HTML/CSS/JavaScript (Frontend)
- Movie database API integration

## Installation

### Prerequisites
- Docker and Docker Compose
- Git

### Setup
1. Clone the repository:
```bash
git clone https://github.com/asra020601/docker-mvrec.git
cd docker-mvrec
```

2. Build and run the container:
```bash
docker-compose up -d
```

3. Access the website:
```
http://localhost:8000
```

## Usage
1. Visit the website
2. Enter the name of a movie you enjoy
3. Click "Get Recommendations"
4. View the list of recommended movies based on your input

## Development
To modify or extend the functionality:
1. Make changes to the source code
2. Rebuild the Docker container
3. Test your changes

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

