import my_token
import pyEX

c = pyEX.Client(api_token=my_token.token)

symbol = input("Enter the ticker: ")

income_statement = c.incomeStatement(symbol, 'annual', 2)
balance_sheet = c.balanceSheet(symbol, 'annual', 2)
adv_fundamentals = c.fundamentals(symbol, 'annual')
cash_flow = c.cashFlow(symbol, 'annual')

def net_income(income_statement):
  ni = income_statement[0]['netIncome']

  if ni > 0:
    return 1
  else:
    return 0

def positive_roa(income_statement, balance_sheet):
  ni = income_statement[0]['netIncome']
  assets = balance_sheet[0]['totalAssets']

  if ni / assets > 0:
    return 1
  else:
    return 0

def cfo_greater_than_ni(adv_fundamentals, income_statement):
  cfo = adv_fundamentals[0]['cashFlowOperating']
  ni = income_statement[0]['netIncome']

  if cfo > ni:
    return 1
  else:
    return 0

def positive_ocf(adv_fundamentals):
  cfo = adv_fundamentals[0]['cashFlowOperating']

  if cfo > 0:
    return 1
  else:
    return 0

def long_term_debt(balance_sheet):
  this_year = balance_sheet[0]['longTermDebt']
  last_year = balance_sheet[1]['longTermDebt']

  if this_year < last_year:
    return 1
  else:
    return 0

def current_ratio_improving(balance_sheet):
  this_year = balance_sheet[0]['currentAssets'] / balance_sheet[0]['totalCurrentLiabilities']
  last_year = balance_sheet[1]['currentAssets'] / balance_sheet[1]['totalCurrentLiabilities']

  if this_year > last_year:
    return 1
  else:
    return 0

def negative_cff(cash_flow):
  cff = cash_flow[0]['cashFlowFinancing']

  if cff < 0:
    return 1
  else:
    return 0

def higher_gm(income_statement):
  this_year = income_statement[0]['grossProfit'] / income_statement[0]['totalRevenue']
  last_year = income_statement[1]['grossProfit'] / income_statement[1]['totalRevenue']
  
  if this_year > last_year:
    return 1
  else:
    return 0

def asset_turnover_improving(income_statement, balance_sheet):
  this_year = income_statement[0]['totalRevenue'] / balance_sheet[0]['totalAssets']
  last_year = income_statement[1]['totalRevenue'] / balance_sheet[1]['totalAssets']

  if this_year > last_year:
    return 1
  else:
    return 0

score = net_income(income_statement) + positive_roa(income_statement, balance_sheet) + cfo_greater_than_ni(adv_fundamentals, income_statement) + positive_ocf(adv_fundamentals) + long_term_debt(balance_sheet) + current_ratio_improving(balance_sheet) + negative_cff(cash_flow) + higher_gm(income_statement) + asset_turnover_improving(income_statement, balance_sheet)

print(score)