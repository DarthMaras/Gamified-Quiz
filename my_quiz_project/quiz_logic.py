# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 23:22:53 2023

@author: Maragkos Andreas
"""

import hashlib
import random 
import time

def generate_pseudoname():
    timestamp = str(time.time()).encode()
    pseudoname = hashlib.sha256(timestamp).hexdigest()
    return pseudoname

#introduction of the game
username = generate_pseudoname()
print("This is your unique pseudoname for this quiz:", username) #the user should enter a username 
print("Hello!", username, "\nYou have selected the general category for personal finance.", "\nThis category consists of savings, credit, investing, insurance, income, and purchases as the main topics of the questions.", "\nYou will have to answer to 10 questions. 10 points will be awarded for every correct answer, there is no point deduction for any wrong answers.", "Answer correctly to 7/10 questions, and you will receive a badge of completion.", "\nAnswer correctly to 10/10 questions, and you will receive £10.", "\nYou can try as many times as you want to receive the rewards, but the rewards can be claimed only once.")
#that was the general information about the quiz
 
 
#these are the 10 questions asked      
questions = ["Question 1. What is a personal budget?", 
             "Question 2. What are the main things to keep truck on a budget?",
             "Question 3. What needs to be considered before making a big purchase?",
             "Question 4. You have £10000 and thinking of investing them as a long-term low risk invest, which is the more appropriate to invest?",
             "Question 5. What % of your income you should save?",
             "Question 6. What is a portfolio diversification strategy?",
             "Question 7. What is the best way to save for retirement in the UK?",
             "Question 8. What is the purpose of a credit score?",
             "Question 9. What is an emergency fund?",
             "Question 10. What is the concept of Opportunity Cost when it comes to spending?"]

#these are the 4 answers for each question
answers = [["A. A system to maximise debt", "B. A system, to reduce income and increase excpenses", "C. A system to track income, spending and goals", "D. A system to consume more money"],
           ["A. Assets and wants", "B. Costs and benefits", "C. Loans and payments", "D. Income and expenses"],
           ["A. Friends and family opinions", "B. Personal goals and budgeting", "C. Borrowing money from the bank", "D. Fashion trends and attractiveness"],
           ["A. Invest in cryptocurrencies", "B. Purchasing a car", "C. Gambling", "D. Government bonds"],
           ["A. 25%", "B. Depending on your personal goals", "C. 10%", "D. Above 25%"],
           ["A. Decide to invest within only in a single class", "B.Invest in a lot of stocks which are promising", "C.Invest in a company you believe in", "D. Spread money across different sectors, asset classes, and regions."],
           ["A. Save as much as possible in the savings account", "B. Pension schemes", "C. Property investments only", "D. Reliant on winning the lottery for retirement"],
           ["A. To track expenditure", "B. To determine your creditworthiness", "C. Forecasting your net worth", "D. Assess ability to save money"],
           ["A. An account for only big purchases", "B. An account for unexpected obligations", "C. An investment portfolio", "D.An account dedicated for paying off debt"],
           ["A. The potential benefit of choosing a good/service instead of another", "B. Accumulating debt by spending a lot of money", "C. The amount of money spent on expenses in each period", "D. Value of time and effort of research and choosing between two products"]]

#the correct answers for each question
correct_answers = ["C", "D", "B", "D", "B", "D", "B", "B", "B", "A"]

#the wrong answers for each question
incorrect_answers = [["A", "B", "D"], ["A", "B", "C"], ["A", "C", "D"], ["A", "B", "C"], ["A", "C", "D"], ["A", "B", "C"],["A", "C", "D"], ["A", "C", "D"], ["A", "C", "D"], ["B", "C", "D"]]

#this is the extra information, regarding each answer the user gives, these are in order to each answer
extra_information = [["This is not the definition of a budget.", "This is not the definition of a budget.", "This is the definition of a budget.", "This is not the definition of a budget."], 
                     ["A budget estimates the expenses in the foreseable future, records expenses during a period, and then compares them! It gives a sense of planning ahead and control, keep that in mind as you want to buy a house in the future.", "A budget estimates the expenses in the foreseable future, records expenses during a period, and then compares them! It gives a sense of planning ahead and control, keep that in mind as you want to buy a house in the future.", "A budget estimates the expenses in the foreseable future, records expenses during a period, and then compares them! It gives a sense of planning ahead and control, keep that in mind as you want to buy a house in the future.", "A budget estimates the expenses in the foreseable future, records expenses during a period, and then compares them! It gives a sense of planning ahead and control, keep that in mind as you want to buy a house in the future."],
                     ["Friends and family are often the most trustworthy people around us,nevertheless, is preferable receiving paid financial assistance from a financial planner/advisor for investing decisions", "This option is the correct as it possesses the lowest risk between these choices!", "minimising the risk of making a poor decision", "To receive a loan from the bank easy, you need to establish creditworthiness and good history (credit score) and you need to have guarantors for a long-term loan, which is a longer commitment too!", "Although many people are attracted to fashion trends which predominantly caused by improvements in older models (phones, cars), one must take into consideration alternatives and the risk involved."],
                     ["Cryptocurrencies are very popular now, although there is high volatility associated with them, lot of scams and Ponzi schemes, therefore it is not classified as a low-risk investment", "Gambling is not a long-term investment. It is not encouraged in any form through this platform, although it has been very popular amongst young adults during covid-19.If you feel gambling is a safe investment, we encourage to visit a financial expert for guidance", "Government bonds are debt securities issued by governments to increase their capital. When there is a purchase of a government bond, it means that there is a lending of money to a government, with interest on it and fixed term repayments. They are considered low risk and safe investment, as they are backed by governments"],
                     ["Are you sure this is what you want to save according to your preferences?", "This is a reminder to save accordingly to your goals, and keep in mind that you want to buy a house!", "Are you sure this is what you want to save according to your preferences?", "Are you sure this is what you want to save according to your preferences?"],
                     ["This is not the definition of a portfolio diversification strategy.", "This is not the definition of a portfolio diversification strategy.", "This is not the definition of a portfolio diversification strategy.", "This is a definition of portfolio diversification strategy!"],
                     ["Savings account will not provide a sufficient return on the investment for retirement, and having money saved in the bank is not such a great idea as only up to 85000£ are insured. Cyprus haircut is a great case to check", "Pension schemes are retirement plans which allow people to enjoy income even after retirement. There are 4 pension plans: ccupational, work, company, work-based, provided to the public, which grow through a monthly payment from the salary of the individual, the person might also enjoy tax relief from this activity. If you do not own one, we encourage you to have a conversation with your employer about this.", "Although having invested in a property that will generate your money in the future is generally a good idea, relaying only one asset class specifically as a retirement income is not an ideal plan.", "Gambling is not a long-term investment. It is not encouraged in any form through this platform, although it has been very popular amongst young adults during covid-19. If you feel gambling is a safe investment, we encourage to visit a financial expert for guidance."],
                     ["Bugeting is usually the best way to track your expenses", "Credit score is the main element of accessing money. Having a good credit score, indicates that an individual can be trustworthy to repay its debt obligations, therefore is more trusted to gain a loan which is going to be repaid on time. Example a mortgage loan could be up to 25 years, the lender needs to see some previous experience of consistent repayments.","Net worth is usually referred to as an individual’s economic status, which is calculated by reducing total liabilities from total assets", "Budgeting is usually one way to discover saving money."],
                     ["This can be related to a savings account, but it is not related to emergencies", "This is what an emerency fund is for and why it is important to have!", "An investment portfolio, is an account that showcasing and allows the user to manage its investments in financial markets and financial assets.", "This is an account where money are saved to pay a specific obligation, debt"],
                     ["This question indicates what the term -opportunity cost- is.","This answer does not match the definition of opportunity cost.", "This answer does not match the definition of opportunity cost.", "This answer does not match the definition of opportunity cost."]]

#some encouranging messages after each answer to motivate the user

encouraging_messages = ["You're doing great! Keep it up!", "Well done! You are making progress", "Keep pushing, you got this!", "I am impressed by your dedication, you are awesome!", "Magnificent! Your knowledge is on point!", "You rock!! Amazing work!!"]
random_encouraging_messages = random.choice(encouraging_messages)

#these are other encouraging messeges given in case of an incorrect answer to motivate the user
incorrect_answer_messages = ["Believe you can and you are halfway there!", "Never give up, you got this lets keep pushing!", "There is no success without failure! Lets gooo..", "The moment you give up is the moment you lose! I believe in you keep going!", "Its not failure, its a step towards success! Don't give up now!"]
random_incorrect_answer_messages = random.choice(incorrect_answer_messages)
#the scoring for the quiz
score = 0

#lists to store the data
question_answers = []
scores = []
influenced_by_features = []
feedback_features = []


#the loops for the quiz
for i in range(len(questions)):
        print(questions[i])
        print(answers[i])
    
#we are going to allow the user to input an answer for each question appearing   
        user_answer = input("Please select an answer between (A, B, C, or D): ").upper()

        if user_answer == correct_answers[i]:
            print(random_encouraging_messages)
            score += 10
            print(extra_information[i][correct_answers[i].index(user_answer)])
        else:
            print(random_incorrect_answer_messages)         
            print(extra_information[i][incorrect_answers[i].index(user_answer)])  
        
             
#this will appear at the end of the quiz    
print("Congratulations!!! You have completed the general categgory's quiz!")
print("Your scored:", score, "out of 100")
    
#if the user scores a specific score then he is eligible for awards, if not encourages to try again.
if score >= 70:
    print("You can claim your badge!", "\nPlay again for a chance to win a 10£ reward!")
elif score == 100:
    print("Congratulations you can claim your badge and your 10£ reward once you exit!")
else:
    print("You should try again for a chance to claim the rewards!")
  

# Feedback
print("\nPlease Provide your feedback:")
features_feedback = int(input("How much did the gamification features such as points, badges, and encouraging messages motivate your progress through the quiz? Rate from 1-10 (1 being the least):"))
overall_experience = int(input("How would you rate this type of experience of financial educational content? Rate from 1-10 (1 being the worst ever):"))
the_future = int(input("How pleased would you be if similar gamification features were applied in financial services platforms? Rate from 1-10 (1 being the least):"))
open_ended_feedback = input("Any additional thoughts or suggestions for improvement of your experience? Please share:")


    



