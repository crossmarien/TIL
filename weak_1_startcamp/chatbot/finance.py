from iexfinance.stocks import Stock
corps=Stock(['TSLA', 'AAPL', 'GOOGL', 'FB', 'AMZN'])
dataset=corps.get_price()
print (dataset["TSLA"])