import openai
from typing import List, Dict
import numpy as np
from config import OPENAI_API_KEY , OPENAI_API_MODEL, OPENAI_EMBEDDING_MODEL
from sklearn.metrics.pairwise import cosine_similarity

openai.api_key = OPENAI_API_KEY

class QAEngine:
    def __init__(self, model: str = OPENAI_API_MODEL):
        self.model = model
        self.client = openai.OpenAI(api_key= OPENAI_API_KEY)

    def get_embedding(self, text: str) -> List[float]:
        """
        Get the embedding for a given text using OpenAI's API.
        """
        response = self.client.embeddings.create(
            input=text,
            model= OPENAI_EMBEDDING_MODEL
        )
        return response.data[0].embedding

    def cosine_similarity(self, a: List[float], b: List[float]) -> float:
        """
        Calculate the cosine similarity between two vectors.
        """
       
        a = np.array(a).reshape(1, -1)
        b = np.array(b).reshape(1, -1)
        
        return cosine_similarity(a, b)[0][0]



    def find_most_relevant_chunk(self, question: str, chunks: List[str]) -> str:
        """ 
        Find the most relevant chunk of text to a given question.
        """
        question_embedding = self.get_embedding(question)
        chunk_embeddings = [self.get_embedding(chunk) for chunk in chunks]
        similarities = [self.cosine_similarity(question_embedding, chunk_embedding) for chunk_embedding in chunk_embeddings]
        most_relevant_index = similarities.index(max(similarities))
        return chunks[most_relevant_index]

    def generate_answer(self, question: str, context: str) -> str:
        """
        Send the question and context to the OpenAI API to generate an answer
        """
        prompt = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions based on the given context"
                                              "Remember answers should be word to word match if the question is a word to word match "
                                              "If you can't find a relevant answer in the context, reply with 'Data Not Available'."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.0,
        )
        return response.choices[0].message.content.strip()

    def answer_questions(self, questions: List[str], chunks: List[str]) -> Dict[str, str]:
        """
        Answer a list of questions based on a list of text chunks
        """
        answers = {}
        for question in questions:
            if question.strip() != '':
                relevant_chunk = self.find_most_relevant_chunk(question, chunks)
                answer = self.generate_answer(question, relevant_chunk)
                answers[question] = answer
        return answers