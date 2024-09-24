import PyPDF2
from typing import List

class PDFProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_text(self) -> str:
        """
        Take filepath as input and returns extracted text from the PDF file.
        """
        with open(self.file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
        return text

    def chunk_text(self, text: str, chunk_size: int = 1000) -> List[str]:
        """
        Splitting the text into chunks of approximately equal size.
        """
        words = text.split()
        chunks = []
        current_chunk = []
        current_size = 0

        for word in words:
            if current_size + len(word) > chunk_size and current_chunk:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_size = 0
            current_chunk.append(word)
            current_size += len(word) + 1 

        if current_chunk:
            chunks.append(' '.join(current_chunk))

        return chunks