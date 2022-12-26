import yfinance as yf
from sklearn.linear_model import LinearRegression
from joblib import dump
import datetime as dt

BTC_Ticker = yf.Ticker("BTC-USD")
data = BTC_Ticker.history(period="max")

idx_current_date = data.shape[0]

def train_model():
    X = data.index.map(dt.datetime.toordinal).values

    reg = LinearRegression()
    reg.fit(X.reshape(-1,1), y=data['Close'].values)

    dump(reg, 'models/model.joblib')

if __name__ == '__main__':
    train_model()

    print("Modelo treinado")