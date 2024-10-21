class Graph:
    def __init__(self, edges) -> None:
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:


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
    d = {
        "Mumbai": ["Paris", "Dubai"],
        "Paris": ["Dubai", "New York"]
    }
