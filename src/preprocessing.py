import pandas as pd
def preprocess_data(sentiment, trades):  
    sentiment= sentiment.drop_duplicates()
    trades=trades.drop_duplicates()

    sentiment['date']=pd.to_datetime(sentiment['date'])
    trades['time']=pd.to_datetime(trades['Timestamp IST'],dayfirst=True,errors='coerce')
    sentiment['date']=sentiment['date'].dt.date
    trades['date']=trades['time'].dt.date
    
    return sentiment,trades
