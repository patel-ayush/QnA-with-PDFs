import argparse
import logging
from pdf_processor import PDFProcessor
from qa_engine import QAEngine
from slack_poster import SlackPoster
import re

def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s', 
                        filename='pdf_qa_agent.log',
                        filemode='w')  

    print("Starting PDF Q&A Agent")

    parser = argparse.ArgumentParser(description="PDF Q&A Agent")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("questions_pdf_path", help="Path to the Question PDF file")
    args = parser.parse_args()

    # Extracting and processing the main PDF
    try:
        logging.info(f"Processing main PDF: {args.pdf_path}")
        pdf_processor = PDFProcessor(args.pdf_path)
        text = pdf_processor.extract_text()  
        chunks = pdf_processor.chunk_text(text)  
        logging.info("Text extraction and chunking completed for main PDF.")
    except Exception as e:
        logging.error(f"Failed to process main PDF: {e}")
        return

    # Extracting and processing the questions PDF
    try:
        logging.info(f"Processing questions PDF: {args.questions_pdf_path}")
        questions_pdf_processor = PDFProcessor(args.questions_pdf_path)
        questions_text = questions_pdf_processor.extract_text()  
        questions = questions_text.split('\n') 
        logging.info(f"Extracted questions: {questions}")
    except Exception as e:
        logging.error(f"Failed to process questions PDF: {e}")
        return

    # Answering questions
    try:
        logging.info("Starting question answering process.")
        qa_engine = QAEngine()
        answers = qa_engine.answer_questions(questions, chunks)
        logging.info("Questions answered successfully.")
    except Exception as e:
        logging.error(f"Error during question answering: {e}")
        return

    # Sending the results to Slack
    try:
        logging.info("Posting Q&A results to Slack.")
        slack_poster = SlackPoster()
        slack_poster.post_qa_results(answers)
        logging.info("Q&A results have been posted to Slack.")
    except Exception as e:
        logging.error(f"Failed to post results to Slack: {e}")
        return

    logging.info("PDF Q&A Agent completed successfully.")

if __name__ == "__main__":
    main()
