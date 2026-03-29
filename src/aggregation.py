def create_daily_metrics(trades):
    daily = trades.groupby('date').agg({
        'pnl': 'sum',
        'is_win': 'mean',
        'trade_size': 'mean',
        'Account': 'count',
        'is_long': 'mean'
    }).reset_index()
    daily.columns = [
        'date',
        'daily_pnl',
        'win_rate',
        'avg_trade_size',
        'num_trades',
        'long_ratio'
    ]
    return daily