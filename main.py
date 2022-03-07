import slack_notice
from get_streak import Streak


streak = Streak()
streak.get_id()
streak.html_parse()
streak.get_last_solved_time()
streak.is_solved_today()

slack_notice.main(['NOT SOLVED TODAY', 'https://solved.ac/', streak.is_solved, streak.last_solved_time.strftime("%Y/%m/%d, %H:%M:%S"), streak.standard_time.strftime("%Y/%m/%d, %H:%M:%S")])
