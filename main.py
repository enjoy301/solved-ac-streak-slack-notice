import slack_notice
import get_streak

is_solved = get_streak.main()

if not is_solved:
    slack_notice.main(['NOT SOLVED TODAY', 'https://solved.ac/'])
