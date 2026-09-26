balance = 0.93
year = 0.022
for i in range(1000):
    balance += balance * year
    print(balance)