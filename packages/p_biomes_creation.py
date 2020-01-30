from .p_classes import cl_biome

# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Créer le dictionnaire v_dic_biomes
# -----------------------------
# CONTENU :
# - f_ajout_biome(v_dic_biomes, v_le_biome)
# - f_creation_constantes_biomes()
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# =============================



###############################################################
######################### AJOUT_BIOME #########################
###############################################################
def f_ajout_biome(v_dic_biomes, v_le_biome):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Ajoute v_le_biome dans le dicionnaire v_dic_biomes avec
	# v_le_biome.nom_biome comme référence
	# -----------------------------
	# PRECONDITIONS :
	# - v_dic_biomes est un dictionnaire
	# -----------------------------
	# DEPEND DE :
	# - p_classes.cl_biome
	# -----------------------------
	# UTILISE PAR :
	# - p_biomes_creation.f_creation_constantes_biomes()
	# =============================

	v_dic_biomes[v_le_biome.nom_biome] = v_le_biome



###############################################################
################# CREATION_CONSTANTES_BIOMES ##################
###############################################################
def f_creation_constantes_biomes():
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Remplit v_dic_biomes de classes cl_biome
	# -----------------------------
	# PRECONDITIONS :
	# - NONE
	# -----------------------------
	# DEPEND DE :
	# - p_biomes_creation.f_ajout_biome()
	# - p_classes.cl_biome
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================

	v_dic_biomes = {}
	f_ajout_biome(v_dic_biomes, cl_biome("Desert_Cool", 0, 1, -4, -3))
	f_ajout_biome(v_dic_biomes, cl_biome("Desert_Tropical", 2, 3, -4, -3))
	f_ajout_biome(v_dic_biomes, cl_biome("Desert_Warm", 1, 2, -4, -3))

	f_ajout_biome(v_dic_biomes, cl_biome("Desert_Scub_Cool", 0, 1, -3, -2))
	f_ajout_biome(v_dic_biomes, cl_biome("Desert_Scub_Tropical", 2, 3, -3, -2))
	f_ajout_biome(v_dic_biomes, cl_biome("Desert_Scub_Warm", 1, 2, -3, -2))

	f_ajout_biome(v_dic_biomes, cl_biome("Dry_Forest_Tropical", 2, 3, 0, 1))
	f_ajout_biome(v_dic_biomes, cl_biome("Dry_Forest_Warm", 1, 2, -1, 0))

	f_ajout_biome(v_dic_biomes, cl_biome("Moist_Forest_Cool", 0, 1, -1, 0))
	f_ajout_biome(v_dic_biomes, cl_biome("Moist_Forest_Tropical", 2, 3, 1, 2))
	f_ajout_biome(v_dic_biomes, cl_biome("Moist_Forest_Warm", 1, 2, 0, 1))

	f_ajout_biome(v_dic_biomes, cl_biome("Rain_Forest", 0, 1, 1, 2))

	f_ajout_biome(v_dic_biomes, cl_biome("Rocks_and_ice", -3, -2, -4, -1))

	f_ajout_biome(v_dic_biomes, cl_biome("Steppe", 0, 1, -2, -1))

	f_ajout_biome(v_dic_biomes, cl_biome("Steppe_Woodland_Thorn", 1, 2, -2, -1))

	f_ajout_biome(v_dic_biomes, cl_biome("Taiga_Desert", -1, 0, -4, -3))
	f_ajout_biome(v_dic_biomes, cl_biome("Taiga_Dry", -1, 0, -3, -2))
	f_ajout_biome(v_dic_biomes, cl_biome("Taiga_Moist", -1, 0, -2, -1))
	f_ajout_biome(v_dic_biomes, cl_biome("Taiga_Rain", -1, 0, 0, 1))
	f_ajout_biome(v_dic_biomes, cl_biome("Taiga_Wet", -1, 0, -1, 0))

	f_ajout_biome(v_dic_biomes, cl_biome("Toundra_Dry", -2, -1, -4, -3))
	f_ajout_biome(v_dic_biomes, cl_biome("Toundra_Moist", -2, -1, -3, -2))
	f_ajout_biome(v_dic_biomes, cl_biome("Toundra_Rain", -2, -1, -1, 0))
	f_ajout_biome(v_dic_biomes, cl_biome("Toundra_Wet", -2, -1, -2, -1))

	f_ajout_biome(v_dic_biomes, cl_biome("Tropical_Forest_Tropical", 2, 3, 3, 4))
	f_ajout_biome(v_dic_biomes, cl_biome("Tropical_Forest_Warm", 1, 2, 2, 3))

	f_ajout_biome(v_dic_biomes, cl_biome("Very_Dry_Forest", 2, 3, -1, 0))

	f_ajout_biome(v_dic_biomes, cl_biome("Wet_Forest_Cool", 0, 1, 0, 1))
	f_ajout_biome(v_dic_biomes, cl_biome("Wet_Forest_Tropical", 2, 3, 2, 3))
	f_ajout_biome(v_dic_biomes, cl_biome("Wet_Forest_Warm", 1, 2, 1, 2))

	f_ajout_biome(v_dic_biomes, cl_biome("Woodland_Thorn", 2, 3, -2, -1))


	return v_dic_biomes
