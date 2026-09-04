from ollama import chat
from ollama import ChatResponse
from retrieving_info import Retriever

class PDFChatAssistant:
    def __init__(self, question, filename):
        self.question = question
        self.filename = filename

    def pdf_llm_response(self):
        query = Retriever(self.question, self.filename)
        question, content_chunks = query.retrieved_info()

        response: ChatResponse = chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': f"{question}, {content_chunks}",
        },
        ])

        return response['message']['content']

class NormalChatAssistant:

    def __init__(self, question):
        self.question = question

    def normal_llm_response(self):
        response: ChatResponse = chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': f"{self.question}",
        },
        ])

        return response['message']['content']
