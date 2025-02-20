import functools
from typing import Any, Callable, Dict, Set


# Create a class to hold our coverage data
class CoverageData:
    def __init__(self):
        self.data: Dict[str, Dict[str, Set[int]]] = {}


# Single global instance of the above class
_COVERAGE = CoverageData()


def initialize_coverage() -> None:
    _COVERAGE.data.clear()


def track_branch(function_name: str, branch_number: int) -> None:
    if function_name not in _COVERAGE.data:
        _COVERAGE.data[function_name] = {
            "branches": {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12},
            "hit_branches": set(),
        }

    _COVERAGE.data[function_name]["hit_branches"].add(branch_number)


def instrument_function(branch_points_num: int) -> Callable:
    """Decorator to instrument functions for branch coverage"""

    def decorator(func):
        func_name = func.__name__

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Initialize coverage tracking for this function
            if func_name not in _COVERAGE.data:
                _COVERAGE.data[func_name] = {
                    "branches": set(range(1, branch_points_num + 1)),
                    "hit_branches": set(),
                }
            return func(*args, **kwargs)

        return wrapper

    return decorator


def report_coverage() -> None:
    print("\n=== Coverage Report ===")
    if not _COVERAGE.data:
        print("No coverage data collected! :(")
        return

    for func_name, data in _COVERAGE.data.items():
        branches = data["branches"]
        hit_branches = data["hit_branches"]
        coverage = len(hit_branches) / len(branches) * 100
        print(f"\nFunction: {func_name}")
        print(f"Branches: {branches}")
        print(f"Hit branches: {hit_branches}")
        print(f"Branch coverage: {coverage:.1f}%")
        print(f"Missing branches: {sorted(branches - hit_branches)}")
