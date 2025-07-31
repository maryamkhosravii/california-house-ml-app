from pydantic import BaseModel

class InputData (BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_bedrooms: float
    population: float
    median_income: float
    ocean_proximity: str


class PredictionOut (BaseModel):
    prediction: float