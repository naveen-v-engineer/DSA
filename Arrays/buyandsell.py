prices = [7, 1, 5, 8, 3, 6, 4]

count = 0
max_profit = 0

while count < len(prices):
    i = count + 1

    while i < len(prices):
        profit = prices[i] - prices[count]

        if profit > max_profit:
            max_profit = profit

        i += 1

    count += 1

print(max_profit)


# prices=[7,1,5,8,3,6,4]


# max=prices[0]
# min=prices[0]
# index=0
# count=0
# i=1
# while i<len(prices):
#     if max<prices[i]:
#         max=prices[i]
#     if min>prices[i]:
#         min=prices[i]
#     i+=1


# buyingday=prices.index(min)
# sellingday=prices.index(max)

# profit=max-min

# print(profit)









