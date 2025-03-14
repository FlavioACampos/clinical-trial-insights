# Clinical Trial Insights

A web application for browsing, saving, and receiving updates on clinical trials. Built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**, running in **Docker**.

## 🚀 Features

- Search for clinical trials by keywords
- Save favorite studies
- Receive email updates for saved trials
- Fully containerized with Docker

## 🛠 Tech Stack

- **Backend**: FastAPI, SQLAlchemy
- **Database**: PostgreSQL (via Docker)
- **Web Scraping**: Scrapy (for data ingestion)
- **Deployment**: Docker & Docker Compose

## 🔧 Setup & Installation

### 1️⃣ Clone the repository

```sh
git clone https://github.com/YOUR-USERNAME/clinical-trial-insights.git
cd clinical-trial-insights
```

### 2️⃣ Set up environment variables

Create a `.env` file with:

```
DB_USER=your-user
DB_PASSWORD=your-password
DB_NAME=cti
DATABASE_URL=postgresql://$DB_USER:$DB_PASSWORD@localhost/$DB_NAME
SECRET_KEY=your-secret-key
```

### 3️⃣ Start the project (Docker)

```sh
docker-compose up --build
```

### 4️⃣ Access the API

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) for interactive API documentation.

## 📌 Project Structure

```
/app
  ├── main.py          # FastAPI entry point
/models
  ├── database.py      # Database setup
  ├── models.py        # Database models
/docker
  ├── dockerfile
  ├── docker-compose.yml
```
