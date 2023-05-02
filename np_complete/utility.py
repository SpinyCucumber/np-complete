from typing import TextIO, Generator, Callable, Union, Iterable
from sympy import Symbol
from sympy.logic.boolalg import Not, BooleanFunction
from .definitions import SubsetSum, Partition, Sat

FileOrPath = Union[TextIO, str]

def read_lines(file_or_path: FileOrPath) -> Generator[str, None, None]:
    """
    Yields each line of a file until encountering a line with a single '$' character or EOF

    Accepts either a file object or a path, which will be opened as a file object
    """
    # Convert to file if necessary
    if isinstance(file_or_path, str):
        with open(file_or_path, "r") as file:
            yield from read_lines(file)
    else:
        file = file_or_path
        while True:
            line = file.readline()
            if line == "": break # Detect EOF
            line = line[:-1] # Strip trailing newline
            if line == "$": break # Detect $
            yield line

def write_lines(file_or_path: FileOrPath, lines: Iterable[str]):
    """
    Writes a sequence of lines to a file

    Accepts either a file object or a path, which will be opened as a file object
    """
    # Convert to file if necessary
    if isinstance(file_or_path, str):
        with open(file_or_path, "w") as file:
            return write_lines(file, lines)
    # Output lines
    file = file_or_path
    for line in lines:
        print(line, file=file)

def read_subset_sum(file_or_path: FileOrPath) -> SubsetSum:
    """
    Parses an instance of the subset sum problem from a file

    The first line defines the target sum, while each consecutive line defines a number in the set.
    Accepts either a file object or a path.
    """

    lines = read_lines(file_or_path)
    target = int(next(lines)) # Read target sum
    numbers = [int(line) for line in lines] # Read remaining numbers
    return SubsetSum(target, numbers)

def read_partition(file_or_path: FileOrPath) -> Partition:
    """
    Parses an instance of the partition problem from a file

    Each line defines a number in the set.
    Accepts either a file object or a path.
    """

    numbers = [int(line) for line in read_lines(file_or_path)]
    return Partition(numbers)

def write_subset_sum(file_or_path, subset_sum: SubsetSum):
    """
    Serializes an instance of the subset sum problem and writes it to a file

    The target sum is output as the first line, followed by each number on a consecutive line.
    Accepts either a file object or a path.
    """

    def generate_lines() -> Generator[str, None, None]:
        yield str(subset_sum.target)
        for num in subset_sum.numbers:
            yield num
    
    write_lines(file_or_path, generate_lines())

def write_sat(file_or_path: FileOrPath, sat: Sat, to_index: Callable[[Symbol], int]):
    """
    Serializes an instance of the SAT problem and writes it to a file

    Must provide a mapping between symbol and index, as variables are represented internally as symbols
    but must be serialized as indicies.
    Accepts either a file object or a path.
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

    def serialize_clause(clause: BooleanFunction):
        return " ".join(map(serialize_literal, clause.args))
    
    # Output each clause as a line
    write_lines(file_or_path, map(serialize_clause, sat.expression.args))