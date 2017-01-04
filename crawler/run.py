from yahoo_finance import Share
import csv

symbol_list = [
    'YHOO',
    'AAPL',
    'GOOGL.SW',
    '005930.KS'
]
'''
for symbol in symbol_list:
    item = Share(symbol)

    print(item.get_name() + '(' + symbol + ')')
    print('currency : ' + item.get_currency())
    print('open : ' + item.get_open())
    print('price : ' + item.get_price())
    print('high(yr) : ' + item.get_year_high())
    print('low(yr) : ' + item.get_year_low())
    print('')
'''
with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow([
        'date',
        'name',
        'currency',
        'open',
        'close',
        'high',
        'low',
        'volume'
    ])

    for symbol in symbol_list:
        item = Share(symbol)
        historical = item.get_historical('2016-01-01', '2016-02-01')

        for data in historical:
            writer.writerow([
                data['Date'],
                item.get_name(),
                item.get_currency(),
                data['Open'],
                data['Close'],
                data['High'],
                data['Low'],
                data['Volume']
            ])