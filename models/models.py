from sqlalchemy import Column, Integer, String, Date
from .database import Base


class ClinicalTrial(Base):
    __tablename__ = "clinical_trials"

    id = Column(Integer, primary_key=True, index=True)
    study_title = Column(String, index=True)
    study_url = Column(String)
    conditions = Column(String)
    start_date = Column(Date)
    completion_date = Column(Date)
