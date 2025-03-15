from models.database import Base, engine
from models.models import ClinicalTrial

# Create the tables in the database
Base.metadata.create_all(bind=engine)
