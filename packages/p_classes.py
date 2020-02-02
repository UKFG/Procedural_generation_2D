# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Définir les classes utilisées dans le programme
# -----------------------------
# CONTENU :
# - class cl_box
# - class cl_biome
# - class cl_tree
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - p_board_functions.py
# - p_decisional.py
# - p_dic_creation.py
# - p_image_creation.py
# - p_decisional.py
# =============================



##############################################################
######################### CL_CASE ############################
##############################################################
class cl_box:

	def __init__(self, v_nom_biome, v_temp, v_pluv, v_coul):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Crée la classe définissant une case, caractérisée par :
		# - son type
		# - sa température moyenne
		# - sa pluviométrie annuelle
		# - le string de sa couleur rgb de forme r g b
		# -----------------------------
		# UTILISE PAR :
		# - p_board_functions.f_creer_plateau_vide()
		# - p_board_functions.f_afficher_plateau()
		# - p_decisional.f_choix_biome()
		# - p_image_creation.f_image_creation()
		# - p_trees_creation.f_possible_to_place_tree
		# - p_trees_creation.f_put_tree()
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - NONE
		# =============================

		self.nom_biome = v_nom_biome
		self.temp = v_temp
		self.pluv = v_pluv
		self.coul = v_coul


###############################################################
######################### CL_BIOME ############################
###############################################################
class cl_biome:

	def __init__(self, v_nom, v_temp_min, v_temp_max, v_pluv_min, v_pluv_max, v_coul):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Crée la classe définisant un biome, caractérisé par :
		# - son nom
		# - sa température moyenne minimale
		# - sa température moyenne maximale
		# - sa pluviometrie annuelle minimale
		# - sa pluviometrie annuelle maximale
		# - sa couleur
		# -----------------------------
		# UTILISE PAR :
		# - p_biomes_creation.f_dic_biomes_creation()
		# - p_decisional.f_choix_biome()
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - NONE
		# =============================

		self.nom_biome = v_nom
		self.temp_min = v_temp_min
		self.temp_max = v_temp_max
		self.pluv_min = v_pluv_min
		self.pluv_max = v_pluv_max
		self.coul = v_coul


	def f_in_range(self, v_temp, v_pluv):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Renvoit True si la temperature et la pluviométrie
		# correspondent à celles de ce biome
		# -----------------------------
		# UTILISE PAR :
		# - p_decisional.f_choix_biome()
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - p_classes.cl_cond_biome.__init__()
		# =============================

		return self.temp_min <= v_temp <= self.temp_max and self.pluv_min <= v_pluv < self.pluv_max



##############################################################
######################### CL_TREE ############################
##############################################################
class cl_tree:
	def __init__(self, v_nom_biome, v_body):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Crée la classe définisant l'arbre d'un biome,
		# caractérisé par :
		# - le nom du biome
		# - le body de sa représentation ppm avec None pour les pixels vides
		# -----------------------------
		# UTILISE PAR :
		# - p_dic_creation.f_dic_trees_creation()
		# - p_trees_generation.f_possible_to_place_tree()
		# - p_trees_generation.f_put_tree()
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - NONE
		# =============================

		self.nom_biome = v_nom_biome
		self.body = v_body
