price = [57.8, 46.51, 97, 11, 34.10, 34.78, 56, 9911, 10, 22]

for prices in price:
    rub = int(prices)
    kk = (prices - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')