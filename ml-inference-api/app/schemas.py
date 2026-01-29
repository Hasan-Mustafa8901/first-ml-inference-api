from pydantic import BaseModel, Field

class IrisRequest(BaseModel):
    sepal_length: float = Field(..., gt=0)
    sepal_width: float = Field(..., gt=0)
    petal_length: float = Field(..., gt=0)
    petal_width: float = Field(..., gt=0)

class IrisResponse(BaseModel):
    prediction: int
    probability: float
    model_version: str