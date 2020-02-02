from .p_classes import cl_biome, cl_tree

# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Créer le dictionnaire v_dic_biomes
# et le dicionnaire v_dic_arbres
# -----------------------------
# CONTENU :
# - f_add_in_dic(v_dic, v_classe)
# - f_dic_biomes_creation()
# - f_dic_trees_creation()
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# - p_image_creation.py
# - p_trees_generation.py
# =============================



###############################################################
####################### F_ADD_IN_DIC ##########################
###############################################################
def f_add_in_dic(v_dic, v_classe):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Ajoute v_classe dans le dicionnaire v_dic avec
	# v_classe.nom_biome comme référence
	# -----------------------------
	# PRECONDITIONS :
	# - v_dic est un dictionnaire
	# - v_classe est un objet qui possède une caractéristique nom_biome
	# -----------------------------
	# DEPEND DE :
	# - p_classes.cl_biome
	# - p_classes.cl_tree
	# -----------------------------
	# UTILISE PAR :
	# - p_biomes_dic_creation.f_dic_biomes_creation()
	# - p_biomes_dic_creation.f_dic_trees_creation()
	# =============================

	v_dic[v_classe.nom_biome] = v_classe



###############################################################
################### F_DIC_BIOMES_CREATION #####################
###############################################################
def f_dic_biomes_creation():
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Remplit v_dic_conditions_biomes de classes cl_biome
	# -----------------------------
	# PRECONDITIONS :
	# - NONE
	# -----------------------------
	# DEPEND DE :
	# - p_creation_biomes_dic.f_add_in_dic()
	# - p_classes.cl_biome
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================

	v_dic_conditions_biomes = {}
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Desert_Cool",              0,  1, -4, -3, "193 165 133"))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Desert_Tropical",          2,  3, -4, -3, "247 210 165"))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Desert_Warm",              1,  2, -4, -3, "207 151 100"))

	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Desert_Scub_Cool",         0,  1, -3, -2, "187 158 126"))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Desert_Scub_Tropical",     2,  3, -3, -2, "251 224 181"))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Desert_Scub_Warm",         1,  2, -3, -2, "193 161 122"))

	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Dry_Forest_Tropical",      2,  3,  0,  1, "177 148 108"))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Dry_Forest_Warm",          1,  2, -1,  0, "167 138 104"))

	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Moist_Forest_Cool",        0,  1, -1,  0, "78 105 36"  ))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Moist_Forest_Tropical",    2,  3,  1,  2, "93 84 51"   ))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Moist_Forest_Warm",        1,  2,  0,  1, "86 104 56"  ))

	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Rain_Forest",              0,  1,  1,  2, "89 93 66"   ))

	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Rocks_and_ice",           -3, -2, -4, -1, "190 220 255"))

	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Steppe",                   0,  1, -2, -1, "160 173 120"))

	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Steppe_Woodland_Thorn",    1,  2, -2, -1, "160 173 120"))

	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Taiga_Desert",            -1,  0, -4, -3, "146 126 101"))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Taiga_Dry",               -1,  0, -3, -2, "167 175 120"))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Taiga_Moist",             -1,  0, -2, -1, "86 104 56"  ))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Taiga_Rain",              -1,  0,  0,  1, "57 102 21"  ))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Taiga_Wet",               -1,  0, -1,  0, "75 102 44"  ))

	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Toundra_Dry",             -2, -1, -4, -3, "167 175 120"))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Toundra_Moist",           -2, -1, -3, -2, "86 104 56"  ))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Toundra_Rain",            -2, -1, -1,  0, "57 102 21"  ))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Toundra_Wet",             -2, -1, -2, -1, "75 102 44"  ))

	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Tropical_Forest_Tropical", 2,  3,  3,  4, "71 94 12"   ))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Tropical_Forest_Warm",     1,  2,  2,  3, "94 124 16"  ))

	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Very_Dry_Forest",          2,  3, -1,  0, "191 168 124"))

	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Wet_Forest_Cool",          0,  1,  0,  1, "128 168 104"))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Wet_Forest_Tropical",      2,  3,  2,  3, "128 168 104"))
	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Wet_Forest_Warm",          1,  2,  1,  2, "128 168 104"))

	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Woodland_Thorn",           2,  3, -2, -1, "149 163 140"))

	f_add_in_dic(v_dic_conditions_biomes, cl_biome("Water",                    0,  0,  0,  0, "0 0 255"    ))

	return v_dic_conditions_biomes



###############################################################
################### F_DIC_TREES_CREATION ######################
###############################################################

def f_dic_trees_creation():
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Remplit v_dic_arbres de classes cl_tree
	# -----------------------------
	# PRECONDITIONS :
	# - NONE
	# -----------------------------
	# DEPEND DE :
	# - p_trees_dic_create.f_add_in_dic(v_dic_arbres, v_l_arbre)
	# - p_classes.cl_tree
	# -----------------------------
	# UTILISE PAR :
	# - packages.p_trees_generation()
	# =============================

	v_dic_arbres = {}

	f_add_in_dic(v_dic_arbres, cl_tree("Desert_Cool", [
			[None,          "106 82 18",   None,          None,          "106 82 18"  ],

			["106 82 18",   "142 93 60",   None,          "127 85 63",   None         ],

			[None,          None,          "142 93 60",   "142 93 60",   "106 82 18"  ],

			[None,          "106 82 18",   "142 93 60",   None,          None         ],

			[None,          None,          "142 93 60",   None,          None         ]
		]))

	f_add_in_dic(v_dic_arbres, cl_tree("Desert_Tropical", [
			[None,          "106 82 18",   None,          None,          "106 82 18"  ],

			["106 82 18",   "142 93 60",   None,          "127 85 63",   None         ],

			[None,          None,          "142 93 60",   "142 93 60",   "106 82 18"  ],

			[None,          "106 82 18",   "142 93 60",   None,          None         ],

			[None,          None,          "142 93 60",   None,          None         ]
		]))

	f_add_in_dic(v_dic_arbres, cl_tree("Desert_Warm", [
			[None,          "106 82 18",   None,          None,          "106 82 18"  ],

			["106 82 18",   "142 93 60",   None,          "127 85 63",   None         ],

			[None,          None,          "142 93 60",   "142 93 60",   "106 82 18"  ],

			[None,          "106 82 18",   "142 93 60",   None,          None         ],

			[None,          None,          "142 93 60",   None,          None         ]
		]))


	f_add_in_dic(v_dic_arbres, cl_tree("Desert_Scub_Cool", [
			["156 152 107", "156 152 107", None         ],
			["156 152 107", "118 115 98",  "156 152 107"],
			[None         , "118 115 98",  None         ]
		]))
	f_add_in_dic(v_dic_arbres, cl_tree("Desert_Scub_Tropical", [
			["156 152 107", "156 152 107", None         ],

			["156 152 107", "118 115 98",  "156 152 107"],

			[None,          "118 115 98",  None         ]
		]))

	f_add_in_dic(v_dic_arbres, cl_tree("Desert_Scub_Warm", [
			["156 152 107", "156 152 107", None         ],

			["156 152 107", "118 115 98",  "156 152 107"],

			[None,          "118 115 98",  None         ]
		]))


	f_add_in_dic(v_dic_arbres, cl_tree("Dry_Forest_Tropical", [

			[None,          None,          "121 105 56",  None,          None,          None,          None         ],

			[None,          None,          None,          "133 103 69",  None,          "133 103 69",  "121 105 56" ],

			["121 105 56",  "133 103 69",  "133 103 69",  "133 103 69",  "133 103 69",  None,          None         ],

			[None,          "121 105 56",  None,          "133 103 69",  None,          None,          None         ],

			[None,          None,          None,          "133 103 69",  None,          None,          None         ],

			[None,          None,          None,          "133 103 69",  None,          None,          None         ]
		]))

	f_add_in_dic(v_dic_arbres, cl_tree("Dry_Forest_Warm", [
			[None,          None,          "121 105 56",  None,          None,          None,          None         ],

			[None,          None,          None,          "133 103 69",  None,          "133 103 69",  "121 105 56" ],

			["121 105 56",  "133 103 69",  "133 103 69",  "133 103 69",  "133 103 69",  None,          None         ],

			[None,          "121 105 56",  None,          "133 103 69",  None,          None,          None         ],

			[None,          None,          None,          "133 103 69",  None,          None,          None         ],

			[None,          None,          None,          "133 103 69",  None,          None,          None         ]
		]))


	f_add_in_dic(v_dic_arbres, cl_tree("Moist_Forest_Cool", [
			[None,          "54 62 15",    "34 46 10",    "34 46 10",    None         ],

			["65 71 23",    "34 46 10",    "34 46 10",    "34 46 10",    None         ],

			["34 46 10",    "34 46 10",    "58 45 26",    "34 46 10",    "34 46 10"   ],

			[None,          None,          "58 45 26",    None,          None         ],

			[None,          None,          "58 45 26",    None,          None         ]
		]))

	f_add_in_dic(v_dic_arbres, cl_tree("Moist_Forest_Tropical", [
			[None,          "54 62 15",    "34 46 10",    "34 46 10",    None         ],

			["65 71 23",    "34 46 10",    "34 46 10",    "34 46 10",    None         ],

			["34 46 10",    "34 46 10",    "58 45 26",    "34 46 10",    "34 46 10"   ],

			[None,          None,          "58 45 26",    None,          None         ],

			[None,          None,          "58 45 26",    None,          None         ]
		]))

	f_add_in_dic(v_dic_arbres, cl_tree("Moist_Forest_Warm", [
			[None,          "54 62 15",    "34 46 10",    "34 46 10",    None         ],

			["65 71 23",    "34 46 10",    "34 46 10",    "34 46 10",    None         ],

			["34 46 10",    "34 46 10",    "58 45 26",    "34 46 10",    "34 46 10"   ],

			[None,          None,          "58 45 26",    None,          None         ],

			[None,          None,          "58 45 26",    None,          None         ]
		]))


	f_add_in_dic(v_dic_arbres, cl_tree("Rain_Forest", [
			[None,          "68 88 39",    "68 88 39",    "68 88 39",    None         ],

			["68 88 39",    "68 88 39",    "68 88 39",    "68 88 39",    "68 88 39"   ],

			[None,          "68 88 39",    "88 107 55",   "68 88 39",    "68 88 39"   ],

			[None,          None,          "111 129 74",  "68 88 39",    None         ],

			[None,          None,          "116 133 78",  None,          None         ],

			[None,          None,          "116 133 78",  None,          None         ],

			[None,          None,          "116 133 78",  None,          None         ],

			[None,          None,          "116 133 78",  None,          None         ],

			[None,          None,          "114 131 77",  None,          None         ]
		]))


	f_add_in_dic(v_dic_arbres, cl_tree("Steppe_Woodland_Thorn", [
			[None,          "34 58 26",    None         ],

			["34 58 26",    "34 58 26",    "34 58 26"   ],

			["34 58 26",    "34 58 26",    "34 58 26"   ],

			[None,          "88 73 50",    None         ]
		]))

	f_add_in_dic(v_dic_arbres, cl_tree("Taiga_Desert", [
			[None,          None,          "34 58 26",    None,          None         ],

			[None,          None,          "34 58 26",    None,          None         ],

			[None,          "34 58 26",    "34 58 26",    "34 58 26",    None         ],

			["34 58 26",    "34 58 26",    "88 73 50",    "34 58 26",    "34 58 26"   ],

			[None,          None,          "88 73 50",    None,          None         ]
		]))

	f_add_in_dic(v_dic_arbres, cl_tree("Taiga_Dry", [
			[None,          None,          "34 58 26",    None,          None         ],

			[None,          None,          "34 58 26",    None,          None         ],

			[None,          "34 58 26",    "34 58 26",    "34 58 26",    None         ],

			["34 58 26",    "34 58 26",    "88 73 50",    "34 58 26",    "34 58 26"   ],

			[None,          None,          "88 73 50",    None,          None         ]
		]))

	f_add_in_dic(v_dic_arbres, cl_tree("Taiga_Moist", [
			[None,          None,          "34 58 26",    None,          None         ],

			[None,          None,          "34 58 26",    None,          None         ],

			[None,          "34 58 26",    "34 58 26",    "34 58 26",    None         ],

			["34 58 26",    "34 58 26",    "88 73 50",    "34 58 26",    "34 58 26"   ],

			[None,          None,          "88 73 50",    None,          None         ]
		]))

	f_add_in_dic(v_dic_arbres, cl_tree("Taiga_Rain", [
			[None,          None,          "34 58 26",    None,          None         ],

			[None,          None,          "34 58 26",    None,          None         ],

			[None,          "34 58 26",    "34 58 26",    "34 58 26",    None         ],

			["34 58 26",    "34 58 26",    "88 73 50",    "34 58 26",    "34 58 26"   ],

			[None,          None,          "88 73 50",    None,          None         ]
		]))

	f_add_in_dic(v_dic_arbres, cl_tree("Taiga_Wet", [
			[None,          None,          "34 58 26",    None,          None         ],

			[None,          None,          "34 58 26",    None,          None         ],

			[None,          "34 58 26",    "34 58 26",    "34 58 26",    None         ],

			["34 58 26",    "34 58 26",    "88 73 50",    "34 58 26",    "34 58 26"   ],

			[None,          None,          "88 73 50",    None,          None         ]
		]))


	f_add_in_dic(v_dic_arbres, cl_tree("Toundra_Rain", [
			["34 58 26",    "34 58 26"   ]
		]))

	f_add_in_dic(v_dic_arbres, cl_tree("Toundra_Wet", [
			["34 58 26",    "34 58 26"   ]
		]))


	f_add_in_dic(v_dic_arbres, cl_tree("Tropical_Forest_Tropical", [
			[None,          "0 69 41",     "0 69 41",     "0 69 41",     "0 69 41",     "0 69 41",     None         ],

			["0 69 41",     "0 69 41",     "0 69 41",     "0 69 41",     "0 69 41",     "0 69 41",     "0 69 41"    ],

			[None,          None,          None,          "88 73 50",    None,          None,          None         ],

			[None,          None,          None,          "88 73 50",    None,          None,          None         ],

			[None,          None,          None,          "88 73 50",    None,          None,          None         ],

			[None,          None,          None,          "88 73 50",    None,          None,          None         ],

			[None,          None,          None,          None,          "88 73 50",    None,          None         ],

			[None,          None,          None,          "88 73 50",    "88 73 50",    None,          None         ],

			[None,          None,          None,          None,          "88 73 50",    None,          None         ]
		]))

	f_add_in_dic(v_dic_arbres, cl_tree("Tropical_Forest_Warm", [
			[None,          "0 69 41",     "0 69 41",     "0 69 41",     "0 69 41",     "0 69 41",     None         ],

			["0 69 41",     "0 69 41",     "0 69 41",     "0 69 41",     "0 69 41",     "0 69 41",     "0 69 41"    ],

			[None,          None,          None,          "88 73 50",    None,          None,          None         ],

			[None,          None,          None,          "88 73 50",    None,          None,          None         ],

			[None,          None,          None,          "88 73 50",    None,          None,          None         ],

			[None,          None,          None,          "88 73 50",    None,          None,          None         ],

			[None,          None,          None,          None,          "88 73 50",    None,          None         ],

			[None,          None,          None,          "88 73 50",    "88 73 50",    None,          None         ],

			[None,          None,          None,          None,          "88 73 50",    None,          None         ]
		]))

	f_add_in_dic(v_dic_arbres, cl_tree("Very_Dry_Forest", [
			[None,          None,          "121 105 56",  None,          None,          None,          None         ],

			[None,          None,          None,          "133 103 69",  None,          "133 103 69",  "121 105 56" ],

			["121 105 56",  "133 103 69",  "133 103 69",  "133 103 69",  "133 103 69",  None,          None         ],

			[None,          "121 105 56",  None,          "133 103 69",  None,          None,          None         ],

			[None,          None,          None,          "133 103 69",  None,          None,          None         ],

			[None,          None,          None,          "133 103 69",  None,          None,          None         ]
		]))


	f_add_in_dic(v_dic_arbres, cl_tree("Wet_Forest_Cool", [
			[None,          "38 127 0",    "38 127 0",    "38 127 0",    None         ],

			["38 127 0",    "38 127 0",    "38 127 0",    "38 127 0",    "38 127 0"   ],

			[None,          None,          "95 80 51",    None,          None         ],

			[None,          None,          "95 80 51",    None,          None         ],

			[None,          None,          "95 80 51",    None,          None         ],

			[None,          None,          "95 80 51",    None,          None         ],

			[None,          None,          "95 80 51",    None,          None         ],

			[None,          None,          "95 80 51",    None,          None         ]
		]))

	f_add_in_dic(v_dic_arbres, cl_tree("Wet_Forest_Tropical", [
			[None,          "38 127 0",    "38 127 0",    "38 127 0",    None         ],

			["38 127 0",    "38 127 0",    "38 127 0",    "38 127 0",    "38 127 0"   ],

			[None,          None,          "95 80 51",    None,          None         ],

			[None,          None,          "95 80 51",    None,          None         ],

			[None,          None,          "95 80 51",    None,          None         ],

			[None,          None,          "95 80 51",    None,          None         ],

			[None,          None,          "95 80 51",    None,          None         ],

			[None,          None,          "95 80 51",    None,          None         ]
		]))

	f_add_in_dic(v_dic_arbres, cl_tree("Wet_Forest_Warm", [
			[None,          "38 127 0",    "38 127 0",    "38 127 0",    None         ],

			["38 127 0",    "38 127 0",    "38 127 0",    "38 127 0",    "38 127 0"   ],

			[None,          None,          "95 80 51",    None,          None         ],

			[None,          None,          "95 80 51",    None,          None         ],

			[None,          None,          "95 80 51",    None,          None         ],

			[None,          None,          "95 80 51",    None,          None         ],

			[None,          None,          "95 80 51",    None,          None         ],

			[None,          None,          "95 80 51",    None,          None         ]
		]))


	f_add_in_dic(v_dic_arbres, cl_tree("Woodland_Thorn", [
			[None,          "39 67 0",     "39 67 0",     "39 67 0",     "39 67 0",     "39 67 0",     None         ],

			["39 67 0",     "39 67 0",     "39 67 0",     "39 67 0",     "39 67 0",     "39 67 0",     "39 67 0"    ],

			[None,          "138 127 99",  None,          "118 98 65",   None,          "138 127 99",  None         ],

			[None,          None,          None,          "118 98 65",   None,          "138 127 99",  None         ],

			[None,          None,          None,          None,          "118 98 65",   None,          None         ],

			[None,          None,          None,          None,          "118 98 65",   None,          None         ]
		]))



	return v_dic_arbres
