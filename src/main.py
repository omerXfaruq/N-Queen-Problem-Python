from queen import ChessProblemSolver

if __name__ == "__main__":
    solver = ChessProblemSolver(4, 4)
    solver.solve_problem()
    print(solver.map)
