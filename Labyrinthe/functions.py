# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 12:43:33 2015

@author: Mathieu Voisin
"""

import sys
import time


def load_level(level_name):
    """Returns a numpy array of the labyrinthe from the file 'level_name.py'"""
    # Convert the name in string and add ".txt"
    try:
        level_name = str(level_name)
    except:
        raise AttributeError("The level name should be a string")
    level_name += ".txt"
    # Create the numpy array
    tab = {}
    with open(level_name) as f:
        for i, row in enumerate(f):
            for j, sym in enumerate(row):
                tab[i, j] = sym
    return tab


# ==== Obsolete ====
def print_labyrinth(tab):
    """Print the labyrinth from the dict tab in user-friendly way"""
    # Get the dimensions of the table
    tab_dim = max([(i, j) for ((i, j), val) in tab.items()])
    i_max = int(tab_dim[0]) + 1
    j_max = int(tab_dim[1]) + 1
    for row in range(i_max):
        str_tmp = ""
        for col in range(j_max):
            str_tmp += tab[row, col]
        print(str_tmp, sep="", end="\n")
# =================


def generate_labyrinth(tab):
    """Returns a string in 2D of the labyrinth from the tab dict"""
    # Get the dimensions of the table
    tab_dim = max([(i, j) for ((i, j), val) in tab.items()])
    i_max = int(tab_dim[0]) + 1
    j_max = int(tab_dim[1]) + 1
    # Generate the string variable
    str_tmp = ""
    for row in range(i_max):
        for col in range(j_max):
            str_tmp += tab[row, col]
        str_tmp += "\n"
    return str_tmp


def main_loop(tab, position=[0, 1]):
    count = 0
    # Get the dimensions of the table
    tab_dim = max([(i, j) for ((i, j), val) in tab.items()])
    i_max = int(tab_dim[0]) + 1
    sys.stdout.write(generate_labyrinth(tab))
    while 1:
        sys.stdout.write('\b'*len(generate_labyrinth(tab))*i_max)
        count += 1
        if (count % 2) == 0:
            tab[position[0], position[1]] = "@"
        else:
            tab[position[0], position[1]] = " "
        sys.stdout.write(generate_labyrinth(tab))
        sys.stdout.flush()
        time.sleep(0.51)
