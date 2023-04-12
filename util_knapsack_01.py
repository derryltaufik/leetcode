def foo(profits, weights, capacity):

    r, c = len(weights), capacity
    dp = [[0] * (c + 1) for _ in range(r)]

    # init first row
    for i in range(c + 1):
        if i >= weights[0]:
            dp[0][i] = profits[0]

    for cur_r in range(1, r):
        for cur_c in range(1, c + 1):
            # count the profit if we don't pick the weight
            profit_not_pick = dp[cur_r - 1][cur_c]
            profit_pick = 0
            if cur_c >= weights[cur_r]:
                profit_pick = profits[cur_r] + dp[cur_r - 1][cur_c - weights[cur_r]]
            dp[cur_r][cur_c] = max(profit_not_pick, profit_pick)

    return dp[-1][-1]


def read_input():
    profit = []
    weight = []
    num_lines, capacity = input().split()
    num_lines = int(num_lines)
    capacity = int(capacity)
    for i in range(num_lines):
        line = input().strip().split()
        p, w = map(int, line)
        profit.append(p)
        weight.append(w)
    return profit, weight, capacity


def start():

    profit, weight, capacity = read_input()

    ans = foo(profit, weight, capacity)
    print(ans)


start()
