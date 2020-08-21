# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe BoardBox, un tableau de Box en 2D
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + create_empty_board()
# ==========================================================

from __future__ import annotations
from typing import List, Optional, cast

from packages.classes.Board import Board
from packages.classes.Box import Box


class BoardBox(Board):
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    TYPE_OF_ELEMENTS: Optional = Optional[Box]

    ###############################################################
    ########################### __INIT__ ##########################
    ###############################################################
    def __init__(self, elements: Optional[List[List[Box]]] = None) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet BoardBox, héritant de Board,
        # caractérisé par :
        # - ses éléments (une liste de liste de Box)
        # =============================
        super().__init__(elements)

    ###############################################################
    ##################### CREATE_EMPTY_BOARD ######################
    ###############################################################
    @classmethod
    def create_empty_board(cls, width: int, height: int) -> BoardBox:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un BoardBox rempli de None, de dimension height x width
        # =============================
        return cast(BoardBox, super(BoardBox, cls).create_empty_board(width, height))
