from transformers import CLIPProcessor, CLIPModel
from PIL import Image

class VLMModule:
    def __init__(self, model_name="openai/clip-vit-base-patch32"):
        self.model_name = model_name
        self.processor = CLIPProcessor.from_pretrained(model_name)
        self.model = CLIPModel.from_pretrained(model_name)

    def get_image_embedding(self, image: Image.Image):
        """
        Given a PIL image, returns its embedding as a list.
        """
        inputs = self.processor(images=image, return_tensors="pt")
        outputs = self.model.get_image_features(**inputs)
        return outputs.detach().numpy().tolist()[0]
