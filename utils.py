import joblib
import numpy as np
import json
from datetime import date, timedelta
from train_model import idx_current_date

def load_model():
    return joblib.load('models/model.joblib')

def make_response(model, days=1):
    X = np.arange((date.today() + timedelta(days=1)).toordinal(), (date.today() + timedelta(days=days+1)).toordinal()).reshape(-1,1)
    print(X)

    preds = model.predict(X)

    dict = {str(date.today() + timedelta(days=day+1)):preds[day-1] for day in range(days)}

    json_response = json.dumps(dict)

    return json_response