#Import all the modules 
import time
import random
import game

#this will generate a random number that will be used later after certain questions
random_number = random.randint(30, 100)

#store the users name
user_name = input("Please enter your name: ")

#call game.
game.display_rules()

def welcome():
    print('Welcome to the Ethics game ' + user_name + '!')
    print('----------------------------')
    print('Time to put you to the test!')
    print(' ')

# Global score variable
score = 0


def question_one():
    global score
    while True:
        try:
            ans = input(' Q1: Would you ruin a family buisness to win the lottery for millions of dollars ? (y/n): ')
            if ans.lower() not in ('y', 'n'):
                raise ValueError(f"Please enter 'y' or 'n'. ")
            break
        except ValueError as e:
            print(e)


    if ans.lower() == 'y':
        print(f"You destroyed the income of {random_number} family members. Wow, heartless.")
        print(' ')
        score -= 1  # Optionally, you can decrease the score if the action is considered unethical
    elif ans.lower() == 'n':
        random_money = random.randint(1000, 5000)  # Random amount of money they could have won
        print(f"You won the hearts of {random_number} family members!")
        print(' ')
        score += 1  # Optionally, increase the score for making an ethical choice



def question_two():
    global score
    #list!
    job_offers = [
        ("a prestigious tech company", "another person who mistakenly didn’t receive the offer due to an admin error"),
        ("a small startup", "a friend who was supposed to get the offer but their email was missed"),
        ("a well-known corporation", "a highly qualified candidate who was overlooked because of a typo in their email address")
    ]

    # Randomly selects one job offer scenario
    company, situation = random.choice(job_offers)

    while True:
        try:
            ans = input(f'Q2: You got offered a job at {company} that was originally intended for {situation}. Do you take the job? (y/n): ')
            if ans.lower() not in ('y', 'n'):
                raise ValueError("Please enter 'y' or 'n'. ")
            break
        except ValueError as e:
            print(e)
        print(' ')

    if ans.lower() == 'y':
        print(f"Good for you, you got the job at {company}! And the award for biggest jerk!!")
        print(' ')
        score -= 1  # decrease the score if the action is considered unethical
    elif ans.lower() == 'n':
        print(f"Amazing job! The team at {company} appreciated your honesty and is keeping you in mind :)")
        print(' ')
        score += 1  # increase the score for making an ethical choice
 
# Loop this question 2 times
def question_three():
    global score
    for i in range(2):  # Looping the question 2 times
        while True:
            try:
                ans = input(f'Q3: your crush left their diary at your house by accident. Do you open it up and read? (y/n): ')
                print(' ')
                if ans.lower() not in ('y', 'n'):
                    raise ValueError("Please enter 'y' or 'n'. ")
                print(' ')
                break
            except ValueError as e:
                print(e)

        if ans.lower() == 'y':
            print("Ever heard of privacy! Your crush is not talking to you anymore.")
            print(' ')
            score -= 1  # Decrease the score if the action is considered unethical
        elif ans.lower() == 'n':
            print("Good job you have basic decency!!")
            print(' ')
            score += 1  # Increase the score for making an ethical choice


def finalscreen():
    print('Hello, user :) This concludes our game. Thank you for playing!')
    time.sleep(1)
   
    print('Please, allow for a brief rolling of our credits, before we reveal your final score!')
    time.sleep(1)
   
    print('Credits:')
    print(' ')
    print('Creative Director: Inaya Siddiqi')
    time.sleep(0.5)
    print('Lead Developers: Inayah Siddiqi & Mahad Khan')
    time.sleep(0.5)
    print('VSCode Debugger: Mahad Khan')


welcome()
time.sleep(2)  # Waits for 2 seconds before moving to the next question
question_one()
time.sleep(5)  # Waits for 3 seconds before moving to the next question
question_two()
time.sleep(3)  # Waits for 3 seconds before moving to the next question
question_three()
time.sleep(3)  # Waits for 3 seconds before printing the final score


finalscreen()


time.sleep(3)
# Print the final score after all questions
print('Here is your final score:', score)

