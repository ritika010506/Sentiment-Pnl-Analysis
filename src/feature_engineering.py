def create_features(trades):
    trades['pnl']=trades['Closed PnL']
    trades['is_win']=trades['pnl']>0
    trades['trade_size'] = trades['Size USD']
    trades['is_long']=trades['Side'].apply(lambda x:1 if x=='BUY' else 0)
    return trades
