from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.responses import JSONResponse

# Load the model from the file
model = joblib.load('model.pkl')

# Create a FastAPI instance
app = FastAPI()

# Define the request body schema using Pydantic
class Features(BaseModel):
    ALL_WorstPaymentStatusActiveAccounts:float
    Amount:float
    ALL_CountOpenedLast12Months:float
    ALL_CountDefaultAccounts:float
    ALL_SumCurrentOutstandingBalExcMtg:float
    ALL_AgeOfOldestAccount:float
    ALL_CountActive:float
    ALL_SumCurrentOutstandingBal:float
    DebtRatio:float
    Term:float

@app.post('/predict')
async def predict(features: Features):
    print(features)
    input_data = np.array([[features.ALL_WorstPaymentStatusActiveAccounts, features.Amount, features.ALL_CountOpenedLast12Months,
                            features.ALL_CountDefaultAccounts, features.ALL_SumCurrentOutstandingBalExcMtg, features.ALL_AgeOfOldestAccount,
                            features.ALL_CountActive, features.ALL_SumCurrentOutstandingBal, features.DebtRatio,
                            features.Term]])
    prediction = model.predict(input_data)

    return JSONResponse({'prediction': int(prediction[0])})
