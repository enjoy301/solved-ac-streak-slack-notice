from slack_notice import SlackApi
from get_streak import Streak


streak = Streak()
streak.get_id()
streak.html_parse()
streak.get_last_solved_time()
streak.is_solved_today()

slack = SlackApi()
slack.get_bot_token()
slack.create_instance()

if not streak.is_solved:
    slack.post_messages(['NOT SOLVED TODAY!!', 'https://solved.ac/'])
