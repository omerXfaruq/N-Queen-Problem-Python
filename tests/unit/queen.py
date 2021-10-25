import pytest
from src.queen import ChessProblemSolver


def test_is_eligible():
    solver = ChessProblemSolver()
    print(solver.map)
    assert solver.is_coordinate_eligible(0, 0)


def test_is_eligible_1():
    solver = ChessProblemSolver()
    solver.map[1, 2] = 1
    print(solver.map)
    assert not solver.is_coordinate_eligible(1, 1)


def test_is_eligible_2():
    solver = ChessProblemSolver()
    solver.map[1, 2] = 1
    print(solver.map)
    assert solver.is_coordinate_eligible(3, 3)
