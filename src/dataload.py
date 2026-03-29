import pandas as pd
def load_data(sent_path,trade_path):
    sentiment=pd.read_csv(sent_path)
    trades=pd.read_csv(trade_path)
    return sentiment,trades
