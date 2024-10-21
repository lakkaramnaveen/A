class Graph:
    def __init__(self, edges) -> None:
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph dict: ", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []


if __name__ == '__main__':
    # Tuple
    routes = [
        ("Mumbai","Paris"),
        ("Newyork","France"),
        ("Newyork","California"),
        ("Hyderabad","Dallas"),
        ("Banglore","Seattle"),
    ]
    route_graph = Graph(routes)

    start="Seattle"
    end="Mumbai"

    print(f"Paths between {start} and {end}: ", route_graph.get_paths(start, end))
