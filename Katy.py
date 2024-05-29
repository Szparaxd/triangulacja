import math
import dane

def calculate_internal_angle(prev_vertex, vertex, next_vertex):
    # Wektory z wierzchołka do jego sąsiadów
    vector1 = (prev_vertex[0] - vertex[0], prev_vertex[1] - vertex[1])
    vector2 = (next_vertex[0] - vertex[0], next_vertex[1] - vertex[1])

    # Składowe wektorów
    x1, y1 = vector1
    x2, y2 = vector2

    # Iloczyn skalarny i normy wektorów
    dot_product = x1 * x2 + y1 * y2
    norm1 = math.sqrt(x1**2 + y1**2)
    norm2 = math.sqrt(x2**2 + y2**2)

    # Kąt między wektorami
    cos_theta = dot_product / (norm1 * norm2)
    angle = math.acos(cos_theta)

    # Iloczyn wektorowy
    cross_product = x1 * y2 - y1 * x2

    # Ustalenie, czy kąt jest wewnętrzny czy zewnętrzny
    if cross_product > 0:
        angle = 2 * math.pi - angle

    # Zamiana radianów na stopnie
    angle_degrees = math.degrees(angle)

    return angle, angle_degrees

def classify_vertex(prev_vertex, vertex, next_vertex):
    # Obliczanie kąta wewnętrznego w radianach i stopniach
    internal_angle, angle_degrees = calculate_internal_angle(prev_vertex, vertex, next_vertex)

    # Wyświetlenie kąta w stopniach
    # print(f"Kąt wewnętrzny: {angle_degrees} stopni")

    # Sprawdzamy położenie sąsiadów
    if prev_vertex[1] < vertex[1] and next_vertex[1] < vertex[1]:
        if internal_angle < math.pi:
            return "wierzchołek początkowy" , angle_degrees
        elif internal_angle > math.pi:
            return "wierzchołek dzielący", angle_degrees

    elif prev_vertex[1] > vertex[1] and next_vertex[1] > vertex[1]:
        if internal_angle < math.pi:
            return "wierzchołek końcowy", angle_degrees
        elif internal_angle > math.pi:
            return "wierzchołek łączący" , angle_degrees

    return "wierzchołek prawidłowy", angle_degrees

# Przykładowe dane:
vertex = (1, 2)
prev_vertex = (0, 1)
next_vertex = (2, 1)


for i in range(len(dane.cw_)):
    
    _data = dane.me_

    ptk, vertex = _data[i]
    if i == 0:
        prev_ptk, prev_vertex = _data[len(_data)-1]
    else:
        prev_ptk, prev_vertex = _data[i-1]

    if i == len(_data)-1:
        next_ptk, next_vertex = _data[0]
    else:
        next_ptk, next_vertex = _data[i+1]

    result, rec = classify_vertex(prev_vertex, vertex, next_vertex)
    print(f'Typ wierzchołka {ptk} = ({vertex[0]},{vertex[1]}): {result} {rec}')


# Wywołanie funkcji
# result = classify_vertex(prev_vertex, vertex, next_vertex)
# print("Typ wierzchołka:", result)
