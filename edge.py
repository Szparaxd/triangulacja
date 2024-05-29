from vertex import Vertex


class Edge:
    def __init__(self, vertex1, vertex2, order=0):
        self.start = vertex1
        self.end = vertex2
        self.helper = None
        self.order_no = order

    def __repr__(self):
        #return f"Edge(start={self.start.point}, end={self.end.point}, helper={self.helper.point if self.helper else 'None'})"

        if self.order_no == 0:
            return f'|{self.start.name}{self.end.name}|'
        else:
            return f'e{self.order_no}'
    

def build_edges_list(vertices: list[Vertex]):
    edges = []

    for i in range(0, len(vertices)):
        start_v = vertices[i]

        if i != len(vertices)-1:
            end_v = vertices[i+1]
        else:
            end_v = vertices[0] 

        edges.append(Edge(start_v, end_v, start_v.order_no ))
    
    return edges