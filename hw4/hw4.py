file = open("/workspaces/DATA_3500_Shawn_Robbins/hw4/TLSA.txt")

lines = file.readlines()

prices = []
for line in lines:
    price = float(line)
    price = round(price, 2) # to round the price to 2 decimals
    print(price)
    prices.append(price)

profit = 0
buy = 0
first_buy = True
first_buy_price = 0
i = 0
for price in prices:
    if i >= 5:
        current_price = prices[i]
        avg_price = (prices[i-5] + prices[i-4] + prices[i-3] + prices[i-2] + prices[i-1]) / 5

        if current_price < avg_price * 0.98:
            #buy
            print("Buying at:\t\t", current_price)
            #update buy variable
            buy = current_price
            #update first_buy variable if this is the first time you buy
            if first_buy:
                first_buy = False
                first_buy_price = current_price

        elif current_price > avg_price * 1.02:
            #sell
            print("Selling at:\t\t", current_price)
            #calculate profit of this individual trade
            trade_profit = current_price - buy
            #keep a running total of all profit

        else: 
            # do nothing this iteration
    i += 1