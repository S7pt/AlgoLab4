from collections import defaultdict
from typing import List, Tuple

INPUT_FILE_NAME = "ijones_in.txt"
OUTPUT_FILE_NAME = "ijones_out.txt"


def read_input_data() -> Tuple[List[List[str]], int, int]:
    with open(INPUT_FILE_NAME, "r") as input_file:
        width, height = [int(parameter) for parameter in input_file.readline().strip().split()]
        corridor = [[letter for letter in row.strip()] for row in input_file.readlines()]
    return corridor, width, height


def ijones(grid: List[List[str]], width: int, height: int) -> int:
    number_of_paths_to_tile = [[0 for tile in range(width)] for row in range(height)]
    number_of_paths_to_letter = defaultdict(int)

    for i in range(height):
        letter = grid[i][0]
        number_of_paths_to_tile[i][0] = 1
        number_of_paths_to_letter[letter] += 1

    for j in range(1, width):
        current_column_ways_to_letter = defaultdict(int)
        for i in range(height):
            letter = grid[i][j]
            paths = number_of_paths_to_letter[letter]
            if letter != grid[i][j - 1]:
                paths += number_of_paths_to_tile[i][j - 1]
            number_of_paths_to_tile[i][j] = paths
            current_column_ways_to_letter[letter] += paths
        for tile_letter in current_column_ways_to_letter:
            number_of_paths_to_letter[tile_letter] += current_column_ways_to_letter[tile_letter]
    if height == 1:
        return number_of_paths_to_tile[0][width - 1]
    else:
        return number_of_paths_to_tile[0][width - 1] + number_of_paths_to_tile[height - 1][width - 1]


def write_output_data(paths: int) -> None:
    with open(OUTPUT_FILE_NAME, "w") as output_file:
        output_file.write(str(paths))


if __name__ == '__main__':
    tile_map, width, height = read_input_data();
    write_output_data(ijones(tile_map, width, height))
