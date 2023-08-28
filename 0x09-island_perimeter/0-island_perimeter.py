#!/usr/bin/python3
""" island perimeter"""


def island_perimeter(grid):
    """ calculating the perimeter of an island"""
    island, neighbours = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                island += 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    neighbours += 1
                if j < len(grid[i]) - 1 and grid[i][j + 1]:
                    neighbours += 1
    perimeter = (island * 4) - (neighbours * 2)
    return perimeter
