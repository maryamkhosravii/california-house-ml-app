from db import models
from sqlalchemy.orm import Session

def save_prediction (db: Session, user: str, features:str, prediction:float):
    record = models.PredictionRecord (user=user, features=features, prediction=prediction)
    db.add(record)
    db.commit()
    db.refresh(record)
    return {record}