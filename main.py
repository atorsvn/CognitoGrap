from cognitograph import CognitoGraph
from PIL import Image

def main():
    cg = CognitoGraph()
    
    # 1. Add a node manually with textual information.
    cg.add_node("node1", text="This is a sample node representing a concept.")
    
    # 2. Query the LLM.
    try:
        llm_response = cg.llm_query("What is the capital of France?")
        print("LLM response:", llm_response)
    except Exception as e:
        print("Error querying LLM:", e)
    
    # 3. Perform a semantic search.
    search_results = cg.semantic_search_query("sample concept")
    print("Semantic search results:", search_results)
    
    # 4. Augment the graph with new entities extracted from text.
    new_entity_id = cg.augment_graph_from_text("A breakthrough in AI was achieved at a major conference.")
    print("Added new entity with ID:", new_entity_id)
    
    # 5. (Optional) If you have an image, augment the graph using visual data.
    # image = Image.open("path_to_image.jpg")
    # image_entity_id = cg.augment_graph_from_image(image, image_url="http://example.com/image.jpg")
    # print("Added image entity with ID:", image_entity_id)
    
    # 6. Visualize the current state of the knowledge graph.
    cg.visualize_graph()

if __name__ == "__main__":
    main()
