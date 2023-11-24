import pandas as pd
import statsmodels.api as sm
import os

market_df = pd.read_csv('market_data.csv')
market_df['Date'] = pd.to_datetime(market_df['Date'])
market_df.set_index('Date', inplace=True)

# BM ratio
market_df['BookToMarket'] = market_df['BookValue'] / market_df['Price']

# Factors from last date
latest_date = market_df.index.max()

# Filter the DataFrame for the latest date
latest_data = market_df.loc[latest_date]

# SMB
median_market_cap = latest_data['MarketCap'].median()
small_stocks = latest_data['MarketCap'] < median_market_cap
big_stocks = ~small_stocks
avg_small_return = latest_data.loc[small_stocks, 'Return'].mean()
avg_big_return = latest_data.loc[big_stocks, 'Return'].mean()
# factor value
SMB_value = avg_small_return - avg_big_return


# BM ratio
high_bm_threshold = latest_data['BookToMarket'].quantile(0.7)
low_bm_threshold = latest_data['BookToMarket'].quantile(0.3)

high_bm_stocks = latest_data['BookToMarket'] > high_bm_threshold
low_bm_stocks = latest_data['BookToMarket'] < low_bm_threshold
avg_high_bm_return = latest_data.loc[high_bm_stocks, 'Return'].mean()
avg_low_bm_return = latest_data.loc[low_bm_stocks, 'Return'].mean()
HML_value = avg_high_bm_return - avg_low_bm_return

# Regression
## random choice
selected_stock = '600691'

market_df['MarketReturn'] = market_df.groupby('Date')['Return'].transform('mean') # market return (average)
selected_stock_returns = market_df[market_df['StockID'] == selected_stock]['Return']
market_returns = market_df['MarketReturn'].loc[market_df['StockID'] == selected_stock]

risk_free_rate = 0.0025 # from mkt_shibor
excess_returns = selected_stock_returns - risk_free_rate
market_excess_returns = market_returns - risk_free_rate

# Regression data
regression_df = pd.DataFrame({
    'ExcessReturn': excess_returns,
    'MarketExcessReturn': market_excess_returns,
    'SMB': SMB_value, 
    'HML': HML_value   
})

X = sm.add_constant(regression_df[['MarketExcessReturn', 'SMB', 'HML']])
y = regression_df['ExcessReturn']

# fit model
model = sm.OLS(y, X).fit()

regression_summary = model.summary()
regression_summary
