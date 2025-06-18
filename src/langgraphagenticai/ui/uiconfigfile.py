# configparser will help parse all the text file (uiconfigfile.ini)
from configparser import ConfigParser

class Config:
    def __init__(self, confile_file = "./src/langgraphagenticai/ui/uiconfigs.ini"):
        self.config = ConfigParser()
        self.config.read(confile_file)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")