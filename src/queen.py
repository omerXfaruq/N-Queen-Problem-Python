import numpy


class ChessProblemSolver:
    def __init__(
        self,
        column_count: int = 4,
        row_count: int = 4,
        map: [numpy.ndarray, numpy.ndarray] = None,
        verbose: bool = False,
    ):
        self.column_count = column_count
        self.row_count = row_count
        if map is None:
            self.map = numpy.zeros((row_count, column_count))
        self.step_count = 0
        self.verbose = verbose

    def solve_problem(self, row: int = 0) -> bool:
        """
        Recursive, backtracking solver.

        Args:print
            row: row value

        Returns:
            bool: If problem is solvable or not

        """
        if row >= self.row_count:
            return False
        for column in range(self.column_count):
            if not self.is_coordinate_eligible(row, column):
                continue
            self.map[row, column] = 1
            self.step_count += 1
            if self.verbose:
                print(self.step_count, "\n", self.map)
            if row == self.row_count - 1:
                return True
            else:
                if self.solve_problem(row=row + 1):
                    return True
                else:
                    self.map[row, column] = 0
        return False

    def is_coordinate_eligible(self, row: int, column: int) -> bool:
        """
        Checks whether if the coordinate is threatened by any other queen.

        Args:
            row:
            column:

        Returns:
            bool:

        """
        if any(self.map[row, :] == 1):
            return False
        if any(self.map[:, column] == 1):
            return False

        current_row = row
        current_column = column
        while current_row >= 0 and current_column >= 0:
            if self.map[current_row, current_column] == 1:
                return False
            current_row += -1
            current_column += -1

        current_row = row
        current_column = column
        while (
            current_row <= self.row_count - 1
            and current_column <= self.column_count - 1
        ):
            if self.map[current_row, current_column] == 1:
                return False
            current_row += +1
            current_column += +1

        current_row = row
        current_column = column
        while current_row <= self.row_count - 1 and current_column >= 0:
            if self.map[current_row, current_column] == 1:
                return False
            current_row += +1
            current_column += -1

        current_row = row
        current_column = column
        while current_row >= 0 and current_column <= self.column_count - 1:
            if self.map[current_row, current_column] == 1:
                return False
            current_row += -1
            current_column += +1

        return True


if __name__ == "__main__":
    solver = ChessProblemSolver(4, 4)
    solver.solve_problem()
    print(solver.map)
