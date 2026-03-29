def merge_datasets(daily_metrics,sentiment):
    final_df=daily_metrics.merge(
        sentiment[['date','classification']],
        on='date',
        how='inner'
    )
    return final_df