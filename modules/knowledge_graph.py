import networkx as nx

class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node_id, text=None, image_url=None, embedding=None):
        """
        Adds a node with attributes such as text, image URL, and embedding.
        """
        self.graph.add_node(node_id, text=text, image_url=image_url, embedding=embedding)

    def add_edge(self, source_id, target_id, relation=None):
        """
        Adds an edge between nodes with an optional relation type.
        """
        self.graph.add_edge(source_id, target_id, relation=relation)

    def query_nodes(self, query_func):
        """
        Returns node IDs where the node attributes satisfy the provided query function.
        """
        return [node for node, attrs in self.graph.nodes(data=True) if query_func(attrs)]

    def visualize(self):
        """
        Prints out the nodes and edges of the graph.
        """
        print("Nodes:")
        for n, data in self.graph.nodes(data=True):
            print(f"  {n}: {data}")
        print("Edges:")
        for u, v, data in self.graph.edges(data=True):
            print(f"  {u} <-> {v}: {data}")
