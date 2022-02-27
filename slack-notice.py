from slack_sdk import WebClient
import yaml

class SlackApi:
    def __init__(self, token):
        self.client = WebClient(token)

    def post_message(self, text):
        result = self.client.chat_postMessage(
            channel="#solved-ac-streak-notice",
            text=text,
        )

        return result

def main():
    with open('./secrets.yml') as yml:
        config = yaml.load(yml, Loader=yaml.BaseLoader)
        bot_token = config['bot-token']

    slack = SlackApi(token=bot_token)
    response = slack.post_message('test message')

if __name__ == '__main__':
    main()