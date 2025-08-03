# Life Tracker

## Overview

**Life Tracker** is a Django-based application that allows users to track their life in weeks. Users can sign up, log in, and view a visual representation of their life, with weeks passed and weeks remaining. The application is containerized using **Docker** and served with **Nginx** for easy and efficient deployment.

---

## Features

- **User Authentication**: Sign up, login, and logout functionality using **session-based authentication**.
- **Profile Management**: View and edit your user profile, including first name, last name, birth date, and expected death date.
- **Life in Weeks**: Visualize your life in weeks, with a grid of weeks passed and weeks remaining.
- **API Endpoints**: A DRF-powered API to manage user data and customer details.

---

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: SQLite
- **Authentication**: djoser
- **Containerization**: Docker, Docker Compose

---

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/meGQD/life](https://github.com/meGQD/life)
    cd life
    ```
2.  **Create a `.env` file** for the database configuration. You can copy the example file:
    ```bash
    cp .env.example .env
    ```
    Update the `.env` file with your SECRET_KEY.
3.  **Build and run the application using Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    The application will be available at `http://localhost:8000`.

---

## API Endpoints

Here are the available API endpoints:

- `auth/`: Authentication-related endpoints (login, logout, signup).
- `life/me/`: View and update your profile information.
- `life/remainingWeeks/`: Get the number of weeks you have left.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/megqd/life/issues) if you'd like to contribute.

## Contact

[MohammadReza Karimi] - [mrk272727mrk@gmail.com]

Project Link: [https://github.com/megqd/life](https://github.com/megqd/life)
