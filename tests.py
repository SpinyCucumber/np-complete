from typing import TextIO
from timeit import timeit
from np_complete import *
import click

solvers_to_test = [
    "find_subset_exhaustive",
    "find_subset_optimized",
    "find_subset_greedy"
]

@click.command()
@click.argument("data", type=click.File("r"))
@click.argument("num_iterations", default=10000)
def run_tests(data: TextIO, num_iterations: int):
    # Construct test namespace
    namespace = {
        "p": read_subset_sum(data),
        **{name: getattr(solvers, name) for name in solvers_to_test}
    }
    click.echo(f"Running {num_iterations} tests for each function")
    for name in solvers_to_test:
        time = timeit(f"{name}(p)", globals=namespace, number=num_iterations)
        print(f"{name}: {time}")

if __name__ == "__main__":
    run_tests()