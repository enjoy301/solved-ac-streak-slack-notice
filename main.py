import slack_notice
from get_streak import Streak


streak = Streak()
streak.get_id()
streak.html_parse()
streak.get_last_solved_time()
streak.is_solved_today()

if not streak.is_solved:
    slack_notice.main(['NOT SOLVED TODAY!!', 'https://solved.ac/'])
