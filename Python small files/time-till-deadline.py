import datetime


def get_input():
    goal_and_deadline = input('What is your goaln and the deadline?\n ').split(':')
    print(goal_and_deadline)

    goal = goal_and_deadline[0]
    deadline = goal_and_deadline[1]

    deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

    today = datetime.datetime.today()
    lefr_over_days = deadline_date - today

    print(f'{lefr_over_days.days} nap van hátra, hogy megvalósítsd a {goal}')

#get_input()
get_input()
