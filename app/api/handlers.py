from fastapi import APIRouter, HTTPException
from app.data.data_manager import DataManager
from app.schemas.schemas import PredictRequest
import train_model

router = APIRouter()



@router.get("/test")
def test():
    return {"status": "OK"}

@router.post("/predict")
async def get_prediction(request: PredictRequest):

    data_manager = DataManager(ticker=request.ticker,
                               start_date=request.start_date,
                               end_date=request.end_date)

    try:
        data = data_manager.get_ticker_dataframe()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

    
    #ToDo Дописать логику обращения к модели для расчета предсказания