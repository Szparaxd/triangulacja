from vertex import *
from edge import *
from dane import cw_, me_

def main(dane):
    messages = []
    vertexs = build_vertex_list(dane)    
    first_vertext = find_right_vertex(vertexs)
    set_order_no_for_vertex(first_vertext)
    set_vertex_type(vertexs)

    edges = build_edges_list(vertexs)
    quene = sorted(vertexs, key=lambda v: (-v.point[1], v.point[0]))

    x_sorted = sorted(vertexs, key=lambda v: (-v.point[0], v.point[1]))
    x_mid = (x_sorted[0].point[0] + x_sorted[len(x_sorted)-1].point[0])/2 

    T = []
    D = []

    def find_ej(v):
        t_reverse = sorted(T, key=lambda e: (e.order_no))
        ej = next((e for e in t_reverse if (e.start.point[0] < v.point[0]) and (e.end.point[0] < v.point[0])), None)
        messages.append(f'ej={ej}')
        return ej

    def pomocnik(e, v):
        if e is None:
            return
        
        e.helper = v
        messages.append(f'pomocnik({e}) = v{v.order_no}')

    def handle_start_vertex(v):
        edge = next(e for e in edges if e.order_no == v.order_no)
        T.append(edge)
        pomocnik(edge, v)    

    def handle_merge_vertex(v):
        edge = next(e for e in edges if e.order_no == v.order_no-1)

        if edge.helper and edge.helper.type == C_MERGE:
            D.append(Edge(v, edge.helper))
        
        if(edge in T):
            T.remove(edge)
            messages.append(f'T= {T}')

        ej = find_ej(v)

        if ej and ej.helper and ej.helper.type == 'merge':
            D.append(Edge(v, ej.helper))
        
        pomocnik(ej, v)
    # todo sprawdzic
    def handle_regular_vertex(v):
        messages.append(f'is_interior_right = {v.is_interior_right(x_mid)}')
        if v.is_interior_right(x_mid):
            edge = next(e for e in edges if e.order_no == v.order_no-1)
            if edge and edge.helper and edge.helper.type == C_MERGE:
                D.append(Edge(v, edge.helper))
            
            if(edge in T):
                T.remove(edge)
                messages.append(f'T= {T}')

            edge = next(e for e in edges if e.order_no == v.order_no)
            T.append(edge)
            pomocnik(edge, v)
        else:
            ej = next((e for e in T if (e.start.point[0] < v.point[0]) and (e.end.point[0] < v.point[0])), None)

            if ej and ej.helper and ej.helper.type == C_MERGE:
                D.append(Edge(v, ej.helper))
            
            pomocnik(ej, v)

    def handle_split_vertex(v):
        ej = find_ej(v)
        if ej and ej.helper and ej.helper:
            D.append(Edge(v, ej.helper))

        pomocnik(ej, v)

        edge = next(e for e in edges if e.order_no == v.order_no)

        T.append(edge)
        pomocnik(edge, v)

    def handle_end_vertex(v):
        edge = next((e for e in edges if e.order_no == v.order_no-1), None)
        if edge and edge.helper and edge.helper.type == C_MERGE:
            D.append(Edge(v,edge))

        if(edge in T):
            T.remove(edge)
            messages.append(f'T= {T}')

    for i in range(len(quene)):
        messages.append('')
        v = quene[i]
        messages.append(f'{i+1}. Badamy v{v.order_no} = {v.name} - {v.type}')
        
        
        if v.type == C_START:
            handle_start_vertex(v)
        elif v.type == C_MERGE:
            handle_merge_vertex(v)
        elif v.type == C_REGULAR:
            handle_regular_vertex(v)
        elif v.type == C_SPLIT:
            handle_split_vertex(v)
        elif v.type == C_END:
            handle_end_vertex(v)
        
        T.sort(key=lambda e: (e.order_no), reverse=True)

        messages.append(f'T= {T}')
        messages.append(f'D= {D}')

    return messages

def converHttpToStandard(daneHttp):
    linie = daneHttp.strip().split('\n')
    dane = []

    for line in linie:
        nazwa, x, y = line.strip().split(' ')
        dane.append((nazwa, (int(x),int(y))))

    return dane
    


def httpTringulate(daneHttp):
    dane = converHttpToStandard(daneHttp)
    print(dane)
    return main(dane)

    # messages.append('###############')
    # main(cw_)

if __name__ == '__main__':
    main(cw_)