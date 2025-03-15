from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from models.database import get_db

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Clinical Trial Insights API!"}


@app.get("/db-test")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))  # Simple query to check DB connection
        return {"message": "Database connection successful!"}
    except Exception as e:
        return {"error": str(e)}
