from sentence_transformers import SentenceTransformer, util
from pdf_reader import ReadingPdf

class Retriever:
    def __init__(self, query, filename):
        self.query = query
        self.filename = filename
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def retrieved_info(self):
        pdf = ReadingPdf(self.filename)
        documents = pdf.chunked_list()

        query_embedding = self.model.encode(self.query)
        doc_embeddings = self.model.encode(documents)

        results = util.semantic_search(query_embedding, doc_embeddings, top_k=3)
        most_similar_docs = [documents[results[0][i]['corpus_id']] for i in range(len(results[0]))]

        llm_feeding_docs = " ,".join(most_similar_docs)

        return self.query, llm_feeding_docs
