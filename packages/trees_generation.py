# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Génère les arbres dans le plateau
# -----------------------------
# CONTENU :
# - generate_trees(board)
# - possible_to_place_tree(board, encyclopedia, x, y)
# - put_tree(board, encyclopedia, x, y)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# ==========================================================

import random
from packages.short_class_import import Box, Tree, Encyclopedia, Position


###############################################################
####################### GENERATE_TREES ########################
###############################################################
def generate_trees(board: list, encyclopedia: Encyclopedia) -> list:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Place les arbres dans board
    # -----------------------------
    # PRECONDITIONS :
    # - encyclopedia a un dictionnaire de
    #   biomes comprend une liste d'au moins un arbre par biome
    # -----------------------------
    # DÉPEND DE :
    # - classes.Box
    # - classes.Tree
    # - classes.Encyclopedia
    # - random
    # - trees_generation.possible_to_place_tree()
    # - trees_generation.put_tree()
    # -----------------------------
    # UTILISÉ PAR :
    # - procedural_generation_2D.py
    # =============================
    width = len(board[0])
    # Car on ne traite que les arbres de la premiere partie :
    height = int(len(board) / 2)

    for line in range(height):

        for column in range(width):

            if board[line][column].biome.name != "tree":

                # Creation d'une liste à ordre aléatoire des arbres possibles
                trees_list = list(
                    encyclopedia.biomes[board[line][column].biome.name].trees
                )

                random.shuffle(trees_list)

                counter = 0
                placed = False

                while counter < len(trees_list) and not placed:

                    if (
                        possible_to_place_tree(
                            board,
                            trees_list[counter],
                            column,
                            line
                        )
                        and random.random() < trees_list[counter].spawn_probability
                    ):

                        put_tree(
                            board,
                            encyclopedia,
                            trees_list[counter],
                            column,
                            line
                        )

                        placed = True

                    counter += 1

    return board


###############################################################
################### POSSIBLE_TO_PLACE_TREE ####################
###############################################################
def possible_to_place_tree(board: list, tree: Tree, x: int, y: int):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Renvoie si il est possible de placer l'arbre
    # -----------------------------
    # DEPEND DE :
    # - classes.Box
    # - classes.Tree
    # - random
    # -----------------------------
    # UTILISE PAR :
    # - trees_creation.generate_trees()
    # =============================

    if x >= len(board[0]) or y >= len(board):
        print("Warning from p_trees_generation.possible_to_place_tree:")
        print("Attempting to look if a tree can be put outside the board.")
        return False

    type_of_source_box = board[y][x].biome.name

    tree_height = tree.get_height()
    tree_width = tree.get_width()

    # Traitement des cas où l'arbre est en bordure d'image :
    # on coupe le modèle à la bordure (pour ne pas placer de case en dehors du tableau)

    if y + tree_height > len(board):
        tree_height = len(board) - y

    if x + tree_width > len(board[0]):
        tree_width = len(board[0]) - x

    line = 0
    column = 0
    possible = True

    while line < tree_height and possible:

        while column < tree_width and possible:

            possible = (
                board[y + line][x + column].biome.name == type_of_source_box
                and board[y + line][x + column].tree == None
            )
            column += 1

        line += 1
        column = 0

    return possible


###############################################################
######################### PUT_TREE ############################
###############################################################
def put_tree(board: list, encyclopedia: Encyclopedia, tree: Tree, x, y):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Place un arbre depuis le point board[y][x]
    # -----------------------------
    # DÉPEND DE :
    # - classes.Box
    # - classes.Tree
    # - classes.Encyclopedia
    # -----------------------------
    # UTILISÉ PAR :
    # - trees_creation.generate_trees()
    # =============================

    if x >= len(board[0]) or y >= len(board):
        print("Warning from p_trees_generation.put_tree:")
        print("  Attempting to put a tree outside the board: ")
        print("    X:", x)
        print("    Y:", y)
        print("    Width of the board:", len(board[0]))
        print("    Height of the board:", len(board))

    else:

        tree_height = tree.get_height()
        tree_width = tree.get_width()

        # Traitement des cas où l'arbre est en bordure d'image :
        # on coupe le modèle à la bordure (pour ne pas placer de case en dehors du tableau)

        if y + tree_height > len(board):
            tree_height = len(board) - y

        if x + tree_width > len(board[0]):
            tree_width = len(board[0]) - x

        # Placement de l'arbre
        for line in range(tree_height):

            for column in range(tree_width):

                if tree.body.get_element(column, line) != None:
                    board[y + line][x + column].tree = tree
                    board[y + line][x +
                                    column].position_in_tree = Position(column, line)
