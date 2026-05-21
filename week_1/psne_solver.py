def solve_psne(payoff_matrix1, payoff_matrix2):
    m = len(payoff_matrix1)
    n = len(payoff_matrix1[0])
    max_payoff1 = [max(payoff_matrix1[i][j] for i in range(m)) for j in range(n)]
    max_payoff2 = [max(payoff_matrix2[i][j] for j in range(n)) for i in range(m)]
    nash_coords = []
    for i in range(m):
        for j in range(n):
            if payoff_matrix1[i][j] == max_payoff1[j] and payoff_matrix2[i][j] == max_payoff2[i]:
                nash_coords.append((i, j))
    return nash_coords


example_payoff1 = [[3, 0], [5, 1]]
example_payoff2 = [[3, 5], [0, 1]]
nash_equilibria = solve_psne(example_payoff1, example_payoff2)
print("All nash equilibria: ", nash_equilibria)