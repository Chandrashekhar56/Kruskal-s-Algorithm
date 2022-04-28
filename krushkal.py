class Graph_for_krushkal:
    def __init__(self, total_vertex_in_graph):
        self.Vertices = total_vertex_in_graph
        self.graph_data = []

    def add_new_edge(self,source_vertex, destination_vertex, weight_of_edge):
        self.graph_data.append([source_vertex, destination_vertex,weight_of_edge])
        
    def function_of_kruskal_algorithm(self):
        final_result = []
        j, k = 0, 0
        self.graph_data= sorted(self.graph_data, key=lambda i: i[2])
        parent_node = []
        rank_of_node = []
        for node in range(self.Vertices):
            parent_node.append(node)
            rank_of_node.append(0)
        while k < self.Vertices- 1:
            source_vertex, destination_vertex,weight_of_edge= self.graph_data[j]
            j = j + 1
            m = self.search(parent_node, source_vertex)
            n = self.search(parent_node, destination_vertex)
            if m != n:
                k = k + 1
                final_result.append([source_vertex, destination_vertex,weight_of_edge])
                self.function_union(parent_node, rank_of_node, m, n)
        for source_vertex, destination_vertex, weight_of_edge in final_result:
            print("%d - %d: %d" % (source_vertex, destination_vertex, weight_of_edge))

    def search(self, parent_node, x):
        if parent_node[x] == x:
            return x
        return self.search(parent_node, parent_node[x])
   
    def function_union(self, parent_node, rank_of_node, m, n):
        m_root_node = self.search(parent_node, m)
        n_root_node = self.search(parent_node, n)
        if rank_of_node[ m_root_node] < rank_of_node[n_root_node]:
            parent_node[ m_root_node] = n_root_node
        elif rank_of_node[ m_root_node] > rank_of_node[n_root_node]:
            parent_node[n_root_node] =  m_root_node
        else:
            parent_node[n_root_node] =  m_root_node
            rank_of_node[ m_root_node] += 1
            
ob = Graph_for_krushkal(6)
ob.add_new_edge(0, 1, 4)
ob.add_new_edge(0, 2, 1)
ob.add_new_edge(0, 3, 2)
ob.add_new_edge(1, 3, 1)
ob.add_new_edge(3, 4, 5)
ob.add_new_edge(2, 4, 6)
ob.add_new_edge(2, 5, 10)
ob.add_new_edge(4, 5, 2)
ob.function_of_kruskal_algorithm()
