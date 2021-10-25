# N-Queen-Problem-Python
A recursive backtracking approach to the generalized version of the https://en.wikipedia.org/wiki/Eight_queens_puzzle
 
_By FarukOzderim_

```
from queen import ChessProblemSolver

if __name__ == "__main__":
    solver = ChessProblemSolver(4, 4)
    solver.solve_problem()
    print(solver.map)
```