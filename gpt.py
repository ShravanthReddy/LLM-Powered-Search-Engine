from dotenv import load_dotenv
import os
import requests
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("GPT_API_KEY")

class GPT:
    def __init__(self, current_model) -> None:
        self.api_key = os.getenv("GPT_API_KEY")
        self.url = os.getenv("GPT_URL")
        self.doc_data = {}
        self.related_data = {}
        self.available_models = ["gpt-3.5-turbo-0125", "gpt-4-0125-preview"]
        self.currently_selected_model = current_model
        self.system_prompt = os.getenv("GPT_SYSTEM_PROMPT")
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=30, length_function=len, is_separator_regex=False)
        self.embeddings = OpenAIEmbeddings(api_key=self.api_key)
        self.history = [{"role": "system", "content": self.system_prompt}]
        self.headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        self.params = {
            'model': self.currently_selected_model,
            'temperature': 0.1,
            'messages': self.history
        }
        self.timer = 20

    def process_query(self, query):
        if len(self.history) < 2:
            return query
        
        prompt = f"Is the query: {query}, related to the previous conversation? Previous conversation: {self.history[-1]['content']}. If yes, rewrite the query to have all the context to make it easier for search engine. For ex: previous quesion was about 'Who is Narendra Modi' and the current query is 'What is his age' To have full context, the question should be re-written as 'What is Narendra Modi's age?'. If the question is not at all related to the previous convo, output the current query without any modifications. Only output the query and nothing else."

        response = requests.post(
            self.url,
            headers = self.headers,
            json = {
                'model': self.available_models[1],
                'temperature': 0.1,
                'messages': [{"role": "user", "content": prompt}]
            },
            timeout = self.timer  
        )

        if response.status_code == 200:
            data = response.json()
            query = data['choices'][0]['message']['content']
        
        return query
        
    def get_related_data(self, query):
        self.related_data = {}
        for key, value in self.doc_data.items():
            docs = value.similarity_search(query, k=2)
            self.related_data[key] = docs

    def data_processing(self, data, query):
        for key, value in data.items():
            if not value:
                continue
            doc = self.text_splitter.create_documents([value])
            vectordb = Chroma.from_documents(documents=doc, embedding=self.embeddings)
            self.doc_data[key] = vectordb

        self.get_related_data(query)

    def api_call(self, query, data):
        self.doc_data = {}
        while len(self.history) > 1:
            self.history.pop()

        self.data_processing(data, query)
        prompt = f"Here's the user's query: {query}\nHere's the text from the website related to the query given by Bing Search API: {str(self.related_data)}"
        self.history.append({"role": "user", "content": prompt})

        response = requests.post(
            self.url,
            headers = self.headers,
            json = self.params,
            timeout = self.timer  
        )

        if response.status_code == 200:
            data = response.json()
            output = data['choices'][0]['message']['content']
            self.history.append({"role": "assistant", "content": output})
            return output
        
        else:
            self.history.pop()
            return "An Error occured:", response.status_code, response.text