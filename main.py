import os
from subprocess import Popen
import datetime
import random

def run(commands):
    Popen(commands).wait()


# end_date          :   end date
# total_days        :   commit period
# commit_frequency  :   commit time per day
# repo_link         :   repository link
# for 8+ year
end_date = datetime.datetime(2024, 9, 18)
total_days = 33
commit_frequency = 7 #daily commit count
repo_link = "https://github.com/AleksandaryPetkovic/Django-House-rental-site.git"

##################

f = open("commit.txt", "w")
os.system("git config user.name")
os.system("git config user.email")
os.system("git init")

pointer = 0
commit_line = 1

while total_days > 0:
    current_date = end_date + datetime.timedelta(days= -pointer)
    format_date = current_date.strftime("%Y-%m-%d")

    random_number = random.randint(0, 10)

    commit_count = random.randint(1, commit_frequency)

    # Common Days Relax Conditions
    if random_number > 9:
        commit_count = 0

    # Saturday Relax Conditions
    if current_date.weekday() == 5 and random_number <= 7:
        commit_count = random.randint(1, 4)
    if current_date.weekday() == 5 and random_number > 7:
        commit_count = 0

    # Sunday Relax Conditions
    if current_date.weekday() == 6 and random_number <= 5:
        commit_count = random.randint(0, 3)
    if current_date.weekday() == 6 and random_number > 5:
        commit_count = 0

    # Jan 1 - Jan 5 Relax Conditions
    if current_date.month == 1 and current_date.day <= 5:
        commit_count = 0

    num_days = (current_date - datetime.datetime(current_date.year, 1, 1)).days + 1
    divide_num = (current_date.year - 2000) * 3 / 2 + 7
    if num_days % divide_num == 0:
        commit_count = random.randint(12, 30)


    print(f"-----------------------{format_date} commits: {commit_count} times-----------------------")
    while commit_count > 0:
        with open("commit.txt", 'a+') as file:
            file.write(f"commit line {commit_line}: {format_date}\n")
        run(['git', 'add', '.'])
        run(['git', 'commit', '-m', '"commit line %s"' % {commit_line},
            '--date', format_date])
    
        print(f"commit line {commit_line}: {format_date}")
        commit_count -= 1
        commit_line += 1
    pointer += 1
    total_days -= 1


print(repo_link)
os.system(f"git remote add origin {repo_link}")
os.system("git branch -M main")
os.system("git push -u origin main -f")
