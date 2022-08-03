from sample_python_binary.modules.settings import MODEL_LOCATION

class ModelReader:
    def __init__(self, model_path: str=None):
        self.name = "Model Reader"
        if model_path is None:
            model_path = MODEL_LOCATION
        self.model_path = model_path
    
    def _read_model_file(self) -> None:
        with open(self.model_path, "r") as model_file:
            model_content = model_file.readlines()
            for content in model_content:
                print(content)
