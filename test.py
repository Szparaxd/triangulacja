def is_interior_right(v_prev, v, v_next):
    # Obliczamy wektory
    vector1 = (v[0] - v_prev[0], v[1] - v_prev[1])
    vector2 = (v_next[0] - v[0], v_next[1] - v[1])
    
    # Iloczyn wektorowy
    cross_product = vector1[0] * vector2[1] - vector1[1] * vector2[0]
    
    # Sprawdzamy znak iloczynu wektorowego
    return cross_product > 0

# Przykładowe punkty
v_prev = (1, 1)
v = (2, 2)
v_next = (3, 1)

# Sprawdzenie
interior_right = is_interior_right(v_next,  v_prev, v )
print("Interior is on the right:", interior_right)