import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config import SLACK_BOT_TOKEN, SLACK_CHANNEL

class SlackPoster:
    def __init__(self):
        self.client = WebClient(token=SLACK_BOT_TOKEN)
        self.channel = SLACK_CHANNEL

    def post_message(self, message: str):
        """
        Post a message to the specified Slack channel.
        """
        try:
            response = self.client.chat_postMessage(
                channel=self.channel,
                text=message
            )
            print(f"Message posted: {response['ts']}")
        except SlackApiError as e:
            print(f"Error posting message: {e}")

    def post_qa_results(self, qa_results: dict,json_format : bool = True):
        """
        Post Q&A results to Slack in a formatted message.
        """
        message = "Q&A Results:\n\n"
        if not json_format:
            for question, answer in qa_results.items():
                message += f"Q: {question}\nA: {answer}\n\n"
            self.post_message(message)
            
        else:
            json_blob = json.dumps(qa_results, indent=2)
            self.post_message(message + f"\n```{json_blob}```")