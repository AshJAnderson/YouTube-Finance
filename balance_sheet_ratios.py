import my_token
import pyEX

c = pyEX.Client(api_token=my_token.token)

symbol = input("Enter the ticker: ")

company = c.company(symbol)
bs = c.balanceSheet(symbol)[0]

print("=" * 64)
print("%s (%s) Report" % (company['companyName'], company['symbol']))
print("-" * 64)

#### Quick Ratio

quick_ratio = (bs['currentAssets'] - bs['inventory']) / bs['totalCurrentLiabilities']

#### Current Ratio

current_ratio = bs['currentAssets'] / bs['totalCurrentLiabilities']

#### Long-term debt / equity

lt_debt_equity = bs['longTermDebt'] / bs['shareholderEquity']

#### long-term debt as a % of invested capital

invested_capital = bs['shareholderEquity'] + bs['totalLiabilities'] - bs['totalCurrentLiabilities'] - bs['currentCash']
lt_debt_ic = bs['longTermDebt'] / invested_capital

print("Quick Ratio: %f" % quick_ratio)
print("Current Ratio: %f" % current_ratio)
print("LT Debt / Equity: %f" % lt_debt_equity)
print("Invested Capital: %i" % invested_capital)
print("LT Debt / IC: %f" % lt_debt_ic )
print("=" * 64)