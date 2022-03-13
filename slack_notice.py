from slack_sdk import WebClient
import yaml


class SlackApi:
    def __init__(self):
        self.client = None
        self.bot_token = None

    def get_bot_token(self):
        with open('./secrets.yml') as yml:
            config = yaml.load(yml, Loader=yaml.BaseLoader)
            self.bot_token = config['bot-token']

    def create_instance(self):
        self.client = WebClient(self.bot_token)

    def post_messages(self, messages):
        for message in messages:
            self.client.chat_postMessage(
                channel="#solved-ac-streak-notice",
                text=message,
            )
