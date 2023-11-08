#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
from collections import deque

def generate_maze(n, wall_prob=0.25):
    return [[1 if random.random() < wall_prob else 0 for _ in range(n)] for _ in range(n)]

def print_maze(maze, path=[]):
    RED='\033[31m'
    BLUE='\033[34m'
    GREEN = '\033[92m'  # ANSI code for green color
    END_COLOR = '\033[0m'  # ANSI code to reset color
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) == (0, 0):
                print('S', end=' ')
            elif (i, j) == (len(maze)-1, len(maze)-1):
                print('E', end=' ')
            elif (i, j) in path:
                print(GREEN + '◍' + END_COLOR, end=' ')
            elif cell == 1:
                print(RED + '▓' + END_COLOR, end=' ')
            else:
                print(BLUE +'◌' + END_COLOR, end=' ')
        print()


def bfs(maze):
    start = (0, 0)
    end = (len(maze) - 1, len(maze) - 1)
    queue = deque([start])
    visited = set([start])
    prev = {start: None}

    while queue:
        current = queue.popleft()
        if current == end:
            break
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_cell = (current[0] + dx, current[1] + dy)
            if 0 <= next_cell[0] < len(maze) and 0 <= next_cell[1] < len(maze) and maze[next_cell[0]][next_cell[1]] == 0 and next_cell not in visited:
                queue.append(next_cell)
                visited.add(next_cell)
                prev[next_cell] = current

    path = []
    at = end
    if at in prev:
        while at:
            path.append(at)
            at = prev[at]
        return path[::-1]
    else:
        print("No path found from start to end.")
        return []


def get_maze_size():
    try:
        n = int(input("Enter the size of the maze (n x n): "))
        print("Generated Maze: ")
        if n <= 0:
            raise ValueError
        return n
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return None

def main_menu(maze, path):
    while True:
        print("\n1. Print the path")
        print("2. Generate another puzzle")
        print("3. Exit the Game")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("Maze with path: ")
            print_maze(maze, path)
        elif choice == '2':
            size = get_maze_size()
            if size:
                maze = generate_maze(size)
                path = bfs(maze)
                print_maze(maze)
        elif choice == '3':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Initial setup
n = get_maze_size()
if n:
    maze = generate_maze(n)
    path = bfs(maze)
    print_maze(maze)
    main_menu(maze, path)


# In[ ]:





# In[ ]:




