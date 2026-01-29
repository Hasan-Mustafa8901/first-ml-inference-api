from fastapi import FastAPI, HTTPException
import pandas as pd
from schemas import IrisRequest, IrisResponse
from contextlib import asynccontextmanager
from model import IrisModel


iris_model = IrisModel()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    iris_model.load()
    yield
    # shutdown
    print("Shutting down app")
    
app = FastAPI(title='Simple ML Inference API', lifespan=lifespan)

    
@app.post('/predict',response_model=IrisResponse)
async def classify(request: IrisRequest):
    try:
        df = pd.DataFrame([request.model_dump()])
        pred, prob = iris_model.predict(df)
        
        return IrisResponse(
            prediction=pred,
            probability=round(prob,4),
            model_version=iris_model.version
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def main():
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
    
if __name__ == '__main__':
    main()