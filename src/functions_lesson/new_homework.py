
def solve (n: int) -> list:
    solve_massive = list(range(n))
    for k in [2, 3, 5]:
        new_solve_massive = []
        for i in solve_massive:
            is_good = True
            if i % k == 0:
                is_good = False
            if is_good:
                new_solve_massive.append(i)
        solve_massive = new_solve_massive
    return solve_massive
print(solve(100))









