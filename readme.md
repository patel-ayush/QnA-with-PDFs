# PDF Q&A Agent

This project implements an AI agent that can extract questions and answers from PDF documents and post the results on Slack.

## Features

- Extract text and questions from the PDF documents
- Answer questions based on the content of the PDF using OpenAI's language model
- Post results to a specified Slack channel

## Installation

#### 1. Clone this repository:
   ```
   git clone https://github.com/patel-ayush/QnA-with-PDFs.git
   cd QnA-with-PDFs
   ```

#### 2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

#### 3. Configuration

Create and edit the `.env` file and add your OpenAI API key and Slack bot token:

```
OPENAI_API_KEY=your_openai_api_key
SLACK_BOT_TOKEN=your_slack_bot_token
SLACK_CHANNEL=your_slack_channel_name
```

<details>
  <summary>How to get Slack bot token?</summary>

  To create your Slack bot token, follow these steps:

  1. Go to the [Slack API website](https://api.slack.com/).
  2. Log into your Slack workspace.
  3. Create a new app by navigating to **Your Apps** and selecting **Create New App**.
  4. In the **OAuth & Permissions** section, make sure to grant the necessary permissions, particularly the **chat:write** permission for your bot to send messages to your channel.
  5. Copy the generated **Bot User OAuth Token** and paste it into the `SLACK_BOT_TOKEN` field in your `.env` file.
  
</details>

#### 4. Build the docker 
   ```
   docker build -t qna_app .
   ```

## Usage

Run the script using docker container with the following command:

   ```
   docker run qna_app path/to/your/document.pdf  path/to/your/questions.pdf 
   ```

Replace `path/to/your/document.pdf` and `path/to/your/questions.pdf`  with the path to your PDF files


