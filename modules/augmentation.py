class AugmentationModule:
    def __init__(self, llm_module, vlm_module, knowledge_graph):
        self.llm = llm_module
        self.vlm = vlm_module
        self.kg = knowledge_graph

    def augment_from_text(self, text):
        """
        Uses the LLM to extract entities/relationships from text and adds them as a new node.
        """
        prompt = f"Extract entities and relationships from the following text:\n\n{text}"
        response = self.llm.generate_text(prompt)
        # For simplicity, we add the text as a new node.
        entity_id = f"entity_{len(self.kg.graph.nodes()) + 1}"
        self.kg.add_node(entity_id, text=text)
        return entity_id

    def augment_from_image(self, image, image_url=None):
        """
        Uses the VLM to get an image embedding and adds it as a new node.
        """
        embedding = self.vlm.get_image_embedding(image)
        entity_id = f"image_entity_{len(self.kg.graph.nodes()) + 1}"
        self.kg.add_node(entity_id, text="extracted from image", image_url=image_url, embedding=embedding)
        return entity_id
