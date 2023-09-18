import cs50

# Ask how many cents the customer is owed
while True:
    sum_from_user = cs50.get_float("Change owed: ")
    if sum_from_user > 0:
        break

coin_values = [0.25, 0.1, 0.05, 0.01]
coins = [0, 0, 0, 0]

for i in range(len(coin_values)):
    coins[i] = sum_from_user // coin_values[i]
    sum_from_user = sum_from_user - coins[i] * coin_values[i]
    sum_from_user = round(sum_from_user, 2)

coins_sum = int(sum(coins))

print(coins_sum)
