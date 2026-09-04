from pypdf import PdfReader

class ReadingPdf:
    def __init__(self, filename):
        self.filename = filename
        self.reader = PdfReader(filename)

    def extracting_text(self):
        pdf_info = []

        for page in self.reader.pages:
            page_info = page.extract_text()
            pdf_info.append(page_info)

        return pdf_info

    def chunking(self, text, chunking_size= 500):
        chunks = []

        for i in range(0, len(text), chunking_size):
            chunks.append(text[i:i+chunking_size])

        return chunks

    def chunked_list(self):
        all_chunks = []
        pages_of_pdf = self.extracting_text()

        for page in pages_of_pdf:
            all_chunks.extend(self.chunking(page))

        return all_chunks
