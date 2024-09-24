# PDF Q&A Agent

This project implements an AI agent that can extract answers from a PDF document based on given questions and post the results on Slack.

## Features

- Extract text and questions from the PDF documents
- Answer questions based on the content of the PDF using OpenAI's language model
- Post results to a specified Slack channel

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/pdf-qa-agent.git
   cd pdf-qa-agent
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Build the docker 
   ```
   docker build -t qna_app .
   ```

## Usage

Run the script using docker container with the following command:

   ```
   docker run qna_app path/to/your/document.pdf  path/to/your/questions.pdf 
   ```

Replace `path/to/your/document.pdf` and `path/to/your/questions.pdf`  with the path to your PDF files

## Configuration

Edit the `.env` file and add your OpenAI API key and Slack bot token:

```
OPENAI_API_KEY=your_openai_api_key
SLACK_BOT_TOKEN=your_slack_bot_token
SLACK_CHANNEL=your_slack_channel_name
```
