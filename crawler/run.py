from yahoo_finance import Share

symbol_list = [
    'YHOO',
    'AAPL',
    'GOOGL.SW',
    '005930.KS'
]

for symbol in symbol_list:
    item = Share(symbol)

    print(item.get_name() + '(' + symbol + ')')
    print('currency : ' + item.get_currency())
    print('open : ' + item.get_open())
    print('price : ' + item.get_price())
    print('high(yr) : ' + item.get_year_high())
    print('low(yr) : ' + item.get_year_low())
    print('')