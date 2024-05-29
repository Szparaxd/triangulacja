import math

C_START = 'Początkowy'
C_END = 'Końcowy'
C_REGULAR = 'Prawidlowy'
C_SPLIT = 'Dzielący'
C_MERGE = 'Łączący'

class Vertex:
    def __init__(self, name, point):
        self.name = name
        self.point = point  # Point as a tuple (x, y)
        self.type = 'undefind'  # 'start', 'end', 'regular', 'split', 'merge'
        self.order_no = 0 
        self.prev = None
        self.next = None
        self.angle = 0

    def __str__(self) -> str:
        return f'{self.name}: ({self.point[0]}, {self.point[1]}) - {self.type} - v{self.order_no}             prev={self.prev.name}  next={self.next.name}   angle={self.angle}'  
    
    def is_interior_right(self, x_mid):
        return self.point[0] < x_mid


     
def find_right_vertex(vertices: list[Vertex]):
    right_vertex = vertices[0]
    for vertex in vertices:
        if vertex.point[0] > right_vertex.point[0] or (vertex.point[0] == right_vertex.point[0] and vertex.point[1] > right_vertex.point[1]):
            right_vertex = vertex
    return right_vertex

def set_order_no_for_vertex(first_vertex: Vertex):
    counter = 1
    v = first_vertex
    v.order_no = counter

    while v.next.order_no == 0:
        counter+=1
        v = v.next
        v.order_no = counter

def build_vertex_list(data): 
    vertexs = []
    for label, (x, y) in data:
        v = Vertex(label, (x,y))
        
        if(len(vertexs) > 0):
            prev = vertexs[len(vertexs)-1]
            prev.next = v
            v.prev = prev

        vertexs.append(v)

    vertexs[0].prev = vertexs[len(vertexs)-1]
    vertexs[len(vertexs)-1].next = vertexs[0]

    return vertexs

def calculate_internal_angle(vertex: Vertex):
    prev_vertex = vertex.prev
    next_vertex = vertex.next

    vector1 = (prev_vertex.point[0] - vertex.point[0], prev_vertex.point[1] - vertex.point[1])
    vector2 = (next_vertex.point[0] - vertex.point[0], next_vertex.point[1] - vertex.point[1])

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

def classify_vertex(vertex: Vertex):
    prev_vertex = vertex.prev
    next_vertex = vertex.next

    internal_angle, angle_degrees = calculate_internal_angle(vertex)

    vertex.angle = angle_degrees

    if prev_vertex.point[1] < vertex.point[1] and next_vertex.point[1] < vertex.point[1]:
        if internal_angle < math.pi:
            vertex.type = C_START
        elif internal_angle > math.pi:
            vertex.type = C_SPLIT

    elif prev_vertex.point[1] > vertex.point[1] and next_vertex.point[1] > vertex.point[1]:
        if internal_angle < math.pi:
            vertex.type = C_END
        elif internal_angle > math.pi:
            vertex.type = C_MERGE

    else:
        vertex.type = C_REGULAR

def set_vertex_type(vertices: list[Vertex]):
    for v in vertices:
        classify_vertex(v)







