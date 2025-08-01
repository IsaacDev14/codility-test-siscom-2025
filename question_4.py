# question_4.py
"""
Overview

You need to help Bob be a good businessman and not charge people too much for his signs.
Description

Bob is running a business that creates signs for people. He can charge much less than his competitors because he charges by letter instead by the entire sign. He can take a sign and change a few letters to make a new sign much more cheaply than a competitor can make a sign from scratch.

The only problem is Bob is not very good at pricing these changes. He wants to be able to look at a sign and a customer's request and quickly be able to give the customer an estimate for the total cost.
Task

Define a function estimate(add_cost, remove_cost, old_sign, new_sign) -> minimum_cost that is adaptable to changes in the market, and can help Bob estimate prices quickly.

The first 2 arguments are the costs of doing an operation, of adding and removing a letter respectively.
The last 2 arguments are the old sign of the customer, and their request.

It should return the cost of changing the sign from the old message to the new message. If there are multiple ways to change the sign, it should return the cheapest way.

"""


def estimate(add_cost, remove_cost, old_sign, new_sign):
    m = len(old_sign)
    n = len(new_sign)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i * remove_cost  
    for j in range(n + 1):
        dp[0][j] = j * add_cost   

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if old_sign[i - 1] == new_sign[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                cost_remove = dp[i - 1][j] + remove_cost
                cost_add = dp[i][j - 1] + add_cost
                cost_substitute = dp[i - 1][j - 1] + remove_cost + add_cost
                dp[i][j] = min(cost_remove, cost_add, cost_substitute) # We take the minimum of the three possible operations.

    return dp[m][n]

