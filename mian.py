from vertex import Vertex
from edge import Edge

start = 'początkowy' 
end = 'końcowy'
regular = 'prawidłowy'
split = 'dzielący'
merge= 'łączący'


points = [
    ('A', (18, 8), end, 1), 
    ('B', (16, 13), start, 2), 
    ('C', (15, 11), merge, 3), 
    ('D', (13, 14), start, 4),
    ('E', (9, 11), merge, 5),
    ('F', (8, 13), start, 6),
    ('G', (6, 11), merge, 7),
    ('H', (4, 14), start, 8),
    ('I', (1, 7), regular, 9),
    ('J', (14, 2), end, 10),
    ('K', (13, 5), split, 11),
    ('L', (15, 4), end, 12),
    ('M', (13, 8), split, 13),
    ('N', (17, 6), end, 14),
    ('O', (16, 9), split, 15)
]

# Sort points by decreasing Y values and increasing X values in case of ties
sorted_points = sorted(points, key=lambda point: (-point[1][1], point[1][0]))






points_2 = []

for label, (x, y), name, v_name in points:
    v1 = Vertex(label, (x,y), name, v_name)
    points_2.append(v1)

quene = []
for label, (x, y), name,v_name in sorted_points:
    v = Vertex(label, (x,y), name, v_name)
    quene.append(v)


edges = [
    Edge(quene[0],quene[1], 8),
    Edge(quene[1],quene[2], 4),
    Edge(quene[2],quene[3], 6),
    Edge(quene[3],quene[4], 2),
    Edge(quene[4],quene[5], 7),
    Edge(quene[5],quene[6], 5),
    Edge(quene[6],quene[7], 3),
    Edge(quene[7],quene[8], 15),
    Edge(quene[8],quene[9], 13),
    Edge(quene[9],quene[10],1),
    Edge(quene[10],quene[11], 9),
    Edge(quene[11],quene[12], 14),
    Edge(quene[12],quene[13], 11),
    Edge(quene[13],quene[14], 12),
    Edge(quene[14],quene[0], 10),
]

T = []
D = []

def handle_end_vertex(vi, ei_minus1):
    if ei_minus1.helper and ei_minus1.helper.type == 'merge':
        D.append((vi.point, ei_minus1.helper.point))

    if(ei_minus1 in T):
        T.remove(ei_minus1)

def handle_merge_vertex(vi, ei_minus1):
    if ei_minus1.helper and ei_minus1.helper.type == 'merge':
        D.append((vi.point, ei_minus1.helper.point))
    
    if(ei_minus1 in T):
        T.remove(ei_minus1)

    for ej in T:
        if ej.start.point[0] < vi.point[0] < ej.end.point[0]:
            print('test')
            if ej.helper and ej.helper.type == 'merge':
                D.append((vi.point, ej.helper.point))
            ej.helper = vi
            break

def handle_start_vertex(vi, ei):
    T.append(ei)
    ei.helper = vi       
        
print(T)

for i in range(0,len(quene)):
    v = quene[i]
    e = edges[i]
    print(f'---------i={i+1}----------')
    print(v)
    print(e)

    if v.type == end:
        print('end')
        handle_end_vertex(v, e)
        print(T)
    
    if v.type == merge:
        print('merge')
        handle_merge_vertex(v,e)
        print(T)

    if v.type == start:
        print('start')
        handle_start_vertex(v,e)
        print(T)

