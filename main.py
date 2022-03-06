import slack_notice
import get_streak


is_solved, last_solved_time, standard_time = get_streak.main()

slack_notice.main(['NOT SOLVED TODAY', 'https://solved.ac/', is_solved, last_solved_time.strftime("%Y/%m/%d, %H:%M:%S"), standard_time.strftime("%Y/%m/%d, %H:%M:%S")])
