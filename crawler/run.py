from yahoo_finance import Share
import csv

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

with open('file.csv', 'w') as file:
    writer = csv.writer(file)

    for symbol in symbol_list:
        item = Share(symbol)
        writer.writerow([item.get_name(),item.get_currency(),item.get_open(),item.get_price(),item.get_year_high(),item.get_year_low()])