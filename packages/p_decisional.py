# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Gèrer l'évolution du terrain et
# prendre la décisison du type de case à placer en (v_y, v_x)
# -----------------------------
# CONTENU :
# - f_genererate_box(v_encyclopedie, v_x, v_y, v_seed, v_intensite_variation)
# - f_choice_biome(v_encyclopedie, v_temp, v_pluv)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# =============================

###############################################################
###################### F_GENERATE_BOX #########################
###############################################################
def f_genererate_box(v_encyclopedie, v_x, v_y, v_seed, v_intensite_variation):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITE :
    # Génère une case en pour la case en (v_y, v_x)
    # -----------------------------
    # PRECONDITIONS :
    # - v_x, v_y : integers not null
    # - v_seed["Tx"], v_seed["Ty"] : integers not null
    # - v_seed["Px"], v_seed["Py"] : integers not null
    # -----------------------------
    # DEPEND DE :
    # - p_perlin_noise.py
    # - f_choice_biome()
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py
    # =============================
    from .p_perlin_noise import SimplexNoise

    # Calcul du bruit de perlin v_pluv et v_temp de la case
    cl_noise = SimplexNoise()

    v_temp = 0
    v_pluv = 0


    for i in range(1,9):
        v_puissance = 2**i
        v_temp += cl_noise.noise2(v_seed["Tx"] + 100000*i + v_x/(v_intensite_variation * v_puissance) , v_seed["Ty"] + 100000*i +  v_y/(v_intensite_variation * v_puissance)) * v_puissance
        v_pluv += cl_noise.noise2(v_seed["Px"] + 100000*i + v_x/(v_intensite_variation * v_puissance) , v_seed["Py"] + 100000*i + v_y/(v_intensite_variation * v_puissance)) * v_puissance

    v_temp *= 0.00587    # v_temp = v_temp * 3 / (2**9 - 1)
    v_pluv *= 0.00783    # v_pluv = v_pluv * 4 / (2**9 - 1)


    return f_choice_biome(v_encyclopedie, v_temp, v_pluv)


###############################################################
######################## F_CHOICE_BIOME #######################
###############################################################
def f_choice_biome(v_encyclopedie, v_temp, v_pluv):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITE :
    # Renvoit l'id du biome qui a les caracteristiques
    # v_temp et v_pluv correspondantes.
    # -----------------------------
    # PRECONDITIONS :
    # - v_encyclopedie : cl_encyclopedia
    # - v_temp : integer not null
    # - v_pluv : integer not null
    # -----------------------------
    # DEPEND DE :
    # - p_classes.cl_box
    # -----------------------------
    # UTILISE PAR :
    # - p_decisional.f_genererate_box(v_encyclopedie, v_x, v_y, v_seed)
    # =============================
    from .p_classes import cl_box

    for v_biome in v_encyclopedie.biomes.values():

        if v_biome.m_in_range(v_temp, v_pluv):

            return cl_box(v_biome.nom_biome)

    return cl_box("Water")
