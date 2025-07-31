from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import Integer, String, Float, DateTime

class PredictionRecord (Base):
    __tablename__ = 'predictions'

    id = Column (Integer, primary_key = True, index= True)
    user = Column (String, index=True)
    features = Column (String)
    prediction = Column (Float)
    timestamp = Column (DateTime(timezone=True), server_default=func.now())
    