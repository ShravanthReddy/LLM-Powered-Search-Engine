from gpt import GPT

class LLM:
    def __init__(self):
        self.available_llms = ["gpt-3.5-turbo-0125", "gpt-4-0125-preview", "Gemini Pro"]
        self.currently_active_llm = self.available_llms[0]
        self.llm_objs = {self.available_llms[0]: GPT(self.currently_active_llm), self.available_llms[1]: GPT(self.available_llms[1]), self.available_llms[2]: ""}
    def process_query(self, query):
        return self.llm_objs[self.currently_active_llm].process_query(query)
    
    def answer_query(self, query, data):
        return self.llm_objs[self.currently_active_llm].api_call(query, data)