# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Box, une case
# -----------------------------
# CONTENU :
# - __slots__
# - __init__()
# - getters
# - setters
# - get_color()
# ==========================================================

from typing import Optional

from packages.classes.Biome import Biome
from packages.classes.Color import Color


class Box:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_biome"
    )

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            biome: Biome
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Box (case), caractérisé par :
        # - son biome
        # =============================
        self._biome = None
        self.set_biome(biome)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_biome(self) -> Optional[Biome]:
        return self._biome

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_biome(self, biome: Optional[Biome]) -> None:
        if isinstance(biome, Biome):
            self._biome = biome
        else:
            raise Exception(
                "Error: impossible to set _biome for a " + type(self).__name__ + ":" +
                "\n_biome must be a Biome, but a " + type(biome).__name__ + " is given."
            )

    ###############################################################
    ########################## GET_COLOR ##########################
    ###############################################################
    def get_color(self) -> Color:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Revoie la couleur de la case,
        # donc celle du sol puisque il n'y a pas d'arbre
        # =============================
        if self.get_biome() is None:
            raise Exception("Error: trying to get the color of a " + type(self).__name__ + " but it biome is None.")
        else:
            return self.get_biome().get_ground_color()
