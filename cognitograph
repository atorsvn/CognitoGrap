from modules.llm_module import LLMModule
from modules.vlm_module import VLMModule
from modules.knowledge_graph import KnowledgeGraph
from modules.semantic_search import SemanticSearchEngine
from modules.augmentation import AugmentationModule

class CognitoGraph:
    def __init__(self):
        self.llm_module = LLMModule()
        self.vlm_module = VLMModule()
        self.knowledge_graph = KnowledgeGraph()
        self.semantic_search = SemanticSearchEngine()
        self.augmentation_module = AugmentationModule(self.llm_module, self.vlm_module, self.knowledge_graph)

    def add_node(self, node_id, text=None, image_url=None, embedding=None):
        """
        Adds a node to the knowledge graph and indexes its text for semantic search.
        """
        self.knowledge_graph.add_node(node_id, text, image_url, embedding)
        if text:
            self.semantic_search.add_document(node_id, text)

    def add_edge(self, source_id, target_id, relation=None):
        """
        Adds an edge between two nodes in the knowledge graph.
        """
        self.knowledge_graph.add_edge(source_id, target_id, relation)

    def semantic_search_query(self, query, limit=5):
        """
        Performs a semantic search using txtai.
        """
        return self.semantic_search.search(query, limit)

    def graph_query(self, query_func):
        """
        Queries the knowledge graph using a provided function.
        """
        return self.knowledge_graph.query_nodes(query_func)

    def llm_query(self, prompt):
        """
        Executes a query using the LLM module.
        """
        return self.llm_module.generate_text(prompt)

    def vlm_query(self, image):
        """
        Retrieves an image embedding using the VLM module.
        """
        return self.vlm_module.get_image_embedding(image)

    def augment_graph_from_text(self, text):
        """
        Augments the graph with entities extracted from text.
        """
        return self.augmentation_module.augment_from_text(text)

    def augment_graph_from_image(self, image, image_url=None):
        """
        Augments the graph with information from an image.
        """
        return self.augmentation_module.augment_from_image(image, image_url)

    def visualize_graph(self):
        """
        Prints out the current state of the knowledge graph.
        """
        self.knowledge_graph.visualize()
