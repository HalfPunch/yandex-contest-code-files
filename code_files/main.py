# imports
from math import ceil
from sys import exit

# input
input_list = input().split(' ')
banknotes, coins = [int(input_list[i]) for i in (0, 1)]
input_list = input().split(' ')
price, vending_coins = [int(input_list[i]) for i in (0, 1)]
# processing
bottle_counter = 0
if price <= 0 or (banknotes == 0 and coins == 0):
    print(0)
    exit(0)
if coins + vending_coins >= 1000000:
    print((banknotes * 1000000 + coins)//price)
    exit(0)
transactions_list = []
transactions_were_not_shortened = True
while True:
    bought_amount_this_cycle = 0
    if price <= coins:
        bought_amount_this_cycle += coins // price
        coins -= price * bought_amount_this_cycle
        vending_coins += price * bought_amount_this_cycle
    min_banknote_amount = int(ceil((price - coins) / 1000000.0))
    min_banknote_value = min_banknote_amount * 1000000
    min_coin_amount = max(0, price - min_banknote_value)
    if (min_banknote_amount > banknotes
            or min_coin_amount > coins
            or min_banknote_value - price > vending_coins
            or min_banknote_value - price > vending_coins + coins):
        bottle_counter += bought_amount_this_cycle
        break
    change = max(0, min_banknote_value - price)
    coins += change - min_coin_amount
    vending_coins -= change - min_coin_amount
    banknotes -= min_banknote_amount
    bought_amount_this_cycle += 1
    bottle_counter += bought_amount_this_cycle
    if transactions_were_not_shortened:
        had_simular_transaction = False
        banknotes_spent_simular_way = 0
        bottles_bought_simular_way = 0
        for id_transaction in range(1, len(transactions_list)):
            if had_simular_transaction:
                banknotes_spent_simular_way += transactions_list[id_transaction][1]
                bottles_bought_simular_way += transactions_list[id_transaction][2]
            elif (transactions_list[id_transaction][0] == coins
                  and transactions_list[id_transaction][1] == min_banknote_amount):
                had_simular_transaction = True
                banknotes_spent_simular_way += transactions_list[id_transaction][1]
                bottles_bought_simular_way += transactions_list[id_transaction][2]
        if had_simular_transaction:
            bottle_counter += (banknotes//banknotes_spent_simular_way)*bottles_bought_simular_way
            banknotes -= (banknotes//banknotes_spent_simular_way)*banknotes_spent_simular_way

    transactions_list.append([coins, min_banknote_amount, bought_amount_this_cycle])
    # output
print(bottle_counter)
