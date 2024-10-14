# Conversebot

Conversebot is a chat application built with Django and React, allowing users to interact with a bot through a chat interface. The application features user registration, chat message management, and CRUD operations for both users and chat messages.

## Features

- User registration and authentication
- Sending and receiving chat messages
- Chat message history retrieval
- Update and delete chat messages

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: React, Axios
- **Database**: SQLite (default), but can be configured to use other databases
- **Authentication**: JWT (JSON Web Tokens)

## Installation

### Prerequisites

- Python 3.x
- Node.js and npm

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/conversebot.git
   cd conversebot/conversebot-backend

2. Install the required packages:

    ```bash
    Copy code
    pip install -r requirements.txt

3. Run migrations:

    ```bash
    Copy code
    python manage.py migrate

4. Start the Django development server:

    ```bash
    Copy code
    python manage.py runserver
    Frontend Setup

5. Navigate to the frontend directory:

    ```bash
    Copy code
    cd ../conversebot-frontend

6. Install the required packages:

    ```bash
    Copy code
    npm install

7. Start the React development server:

    ```bash
    Copy code
    npm start

8. Usage
    Visit http://localhost:8000/ for the backend API documentation.
    Access the chat application at http://localhost:3000/.