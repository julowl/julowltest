
def solve (n: int) -> list:
    solve_massive = []
    for i in range(0, n):
        is_good = True
        for k in [2, 3, 5]:
            if i % k == 0:
                is_good = False
        if is_good:
            solve_massive.append(i)
    return solve_massive




print(solve(100))









