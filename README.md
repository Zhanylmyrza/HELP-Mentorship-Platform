# HELP - Mentorship Platform

## Overview
HELP - Mentorship Platform is a full-stack web application that connects students and early-career professionals with mentors. The platform facilitates knowledge sharing and professional development through mentorship relationships, real-time chat, and secure user authentication.

## Features
- **Responsive Frontend**: Built with React.js and integrated with a Django backend via REST API.
- **Authentication System**: Implements JWT-based authentication, email verification, and Google OAuth2 login.
- **Real-time Communication**: Utilizes Django Channels and Redis for instant chat functionality.
- **Cloud-based Media Storage**: AWS S3 is used for scalable and efficient media handling.
- **Database Management**: PostgreSQL is the primary database for handling user profiles, mentorship relationships, and messaging.
- **Secure API**: Built with Django REST Framework, featuring robust permission systems and token blacklisting.
- **Scalable Deployment**: Hosted on AWS with EC2, RDS, and IAM role-based security measures.
- **Reverse Proxy and Web Servers**: Nginx is used as a reverse proxy, Gunicorn as a WSGI server, and Daphne for ASGI support.
- **System Monitoring**: Configured with systemd services and journalctl logging for maintenance.
- **Automated CI/CD**: GitHub Actions with SSH key authentication streamlines deployment through WSL.
- **Message Broker**: Upstash Redis is integrated for handling real-time communications efficiently.

## Tech Stack
- **Backend**: Python, Django, Django REST Framework, PostgreSQL, Redis, AWS (EC2, RDS, S3).
- **Frontend**: React.js, Redux, Bootstrap.
- **Infrastructure**: AWS, Nginx, Gunicorn, Daphne, Upstash, Redis, systemd, SSH, GitHub Actions.

## Installation
### Prerequisites
- Python 3.10+
- Node.js and npm
- PostgreSQL
- Redis
- AWS credentials (for S3, RDS, EC2 access)

### Backend Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/Zhanylmyrza/HELP-Mentorship-Platform.git
   cd HELP-Mentorship-Platform
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Copy `.env.example` to `.env` and fill in the required credentials.

5. Apply database migrations:
   ```sh
   python manage.py migrate
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm start
   ```
4. Build the frontend on backend:
   ```sh
   npm run build
   ```
   

## Deployment
### AWS Deployment Steps
1. Deploy backend to AWS EC2 using Gunicorn, Nginx, and Daphne.
2. Set up PostgreSQL on AWS RDS and configure security groups.
3. Configure AWS S3 for media storage.
4. Use GitHub Actions for CI/CD with SSH authentication.
5. Ensure Redis is running for real-time chat (Upstash Redis recommended for scalability).

## API Documentation
The API endpoints are built using Django REST Framework. To explore available endpoints, you can use:
```sh
http://localhost:8000/api/docs/
```

## Links

- **Technical Thesis: https://drive.google.com/drive/folders/1TH414MMkCnlQz8YqiZtsd-ywD9VWazCQ?usp=sharing
- **Project Demo: https://www.youtube.com/watch?v=F4uLV9qbzY4
- **Deployed link to web application: https://34.132.9.23/


---
This README provides a comprehensive overview of the HELP - Mentorship Platform, covering its features, setup, deployment, and API documentation. 🚀

