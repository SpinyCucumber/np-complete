from typing import TextIO, Generator, Callable, Union
from sympy import Symbol
from sympy.logic import Not
from .definitions import SubsetSum, Partition, Sat

def read_lines(io: TextIO) -> Generator[str, None, None]:
    while True:
        line = io.readline()
        if line == "": break # Detect EOF
        line = line[:-1] # Strip trailing newline
        if line == "$": break # Detect $
        yield line

def read_subset_sum(io: TextIO) -> SubsetSum:
    lines = read_lines(io)
    target = int(next(lines)) # Read target sum
    numbers = [int(line) for line in lines] # Read remaining numbers
    return SubsetSum(target, numbers)

def read_partition(io: TextIO) -> Partition:
    numbers = [int(line) for line in read_lines(io)]
    return Partition(numbers)

def write_sat(io: TextIO, sat: Sat, to_index: Callable[[Symbol], int]):
    """
    Seralizes an instance of the SAT problem and writes it to a file
    Must provide a mapping between symbol and index
    """

    def serialize_literal(literal: Union[Symbol, Not]) -> str:
        result = ""
        if isinstance(literal, Not):
            symbol = literal.args[0]
            result += "-"
        else:
           symbol = literal 
        result += str(to_index(symbol))
        return result
    
    # Output each clause as a line
    for clause in sat.expression.args:
        print(" ".join(map(serialize_literal, clause.args)), file=io)
    
    # Output $
    print("$", file=io)