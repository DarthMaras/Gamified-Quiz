from django.shortcuts import render, redirect, get_object_or_404
from django.http import request
from .models import Question, Answer
from django.template.loader import get_template


        #question and answer lists
questions = ["Question_1. What is a personal budget?", 
             "Question_2. What are the main things to keep truck on a budget?",
             "Question_3. What needs to be considered before making a big purchase?",
             "Question_4. You have £10000 and thinking of investing them as a long-term low risk invest, which is the more appropriate to invest?",
             "Question_5. What % of your income you should save?",
             "Question_6. What is a portfolio diversification strategy?",
             "Question_7. What is the best way to save for retirement in the UK?",
             "Question_8. What is the purpose of a credit score?",
             "Question_9. What is an emergency fund?",
             "Question10. What is the concept of Opportunity Cost when it comes to spending?"
                ]
answers = [["A. A system to maximise debt", "B. A system, to reduce income and increase excpenses", "C. A system to track income, spending and goals", "D. A system to consume more money"],
           ["A. Assets and wants", "B. Costs and benefits", "C. Loans and payments", "D. Income and expenses"],
           ["A. Friends and family opinions", "B. Personal goals and budgeting", "C. Borrowing money from the bank", "D. Fashion trends and attractiveness"],
           ["A. Invest in cryptocurrencies", "B. Purchasing a car", "C. Gambling", "D. Government bonds"],
           ["A. 25%", "B. Depending on your personal goals", "C. 10%", "D. Above 25%"],
           ["A. Decide to invest within only in a single class", "B.Invest in a lot of stocks which are promising", "C.Invest in a company you believe in", "D. Spread money across different sectors, asset classes, and regions."],
           ["A. Save as much as possible in the savings account", "B. Pension schemes", "C. Property investments only", "D. Reliant on winning the lottery for retirement"],
           ["A. To track expenditure", "B. To determine your creditworthiness", "C. Forecasting your net worth", "D. Assess ability to save money"],
           ["A. An account for only big purchases", "B. An account for unexpected obligations", "C. An investment portfolio", "D.An account dedicated for paying off debt"],
           ["A. The potential benefit of choosing a good/service instead of another", "B. Accumulating debt by spending a lot of money", "C. The amount of money spent on expenses in each period", "D. Value of time and effort of research and choosing between two products"]
            ]
extra_information = [["This is not the definition of a budget.", "This is not the definition of a budget.", "This is the definition of a budget.", "This is not the definition of a budget."], 
                     ["A budget estimates the expenses in the foreseable future, records expenses during a period, and then compares them! It gives a sense of planning ahead and control, keep that in mind as you want to buy a house in the future.", "A budget estimates the expenses in the foreseable future, records expenses during a period, and then compares them! It gives a sense of planning ahead and control, keep that in mind as you want to buy a house in the future.", "A budget estimates the expenses in the foreseable future, records expenses during a period, and then compares them! It gives a sense of planning ahead and control, keep that in mind as you want to buy a house in the future.", "A budget estimates the expenses in the foreseable future, records expenses during a period, and then compares them! It gives a sense of planning ahead and control, keep that in mind as you want to buy a house in the future."],
                     ["Friends and family are often the most trustworthy people around us,nevertheless, is preferable receiving paid financial assistance from a financial planner/advisor for investing decisions", "This option is the correct as it possesses the lowest risk between these choices!", "minimising the risk of making a poor decision", "To receive a loan from the bank easy, you need to establish creditworthiness and good history (credit score) and you need to have guarantors for a long-term loan, which is a longer commitment too!", "Although many people are attracted to fashion trends which predominantly caused by improvements in older models (phones, cars), one must take into consideration alternatives and the risk involved."],
                     ["Cryptocurrencies are very popular now, although there is high volatility associated with them, lot of scams and Ponzi schemes, therefore it is not classified as a low-risk investment", "Purchasing a depriciated asset, such as a vehicle, is not a good investment option for the future", "Gambling is not a long-term investment. It is not encouraged in any form through this platform, although it has been very popular amongst young adults during covid-19.If you feel gambling is a safe investment, we encourage to visit a financial expert for guidance", "Government bonds are debt securities issued by governments to increase their capital. When there is a purchase of a government bond, it means that there is a lending of money to a government, with interest on it and fixed term repayments. They are considered low risk and safe investment, as they are backed by governments"],
                     ["Are you sure this is what you want to save according to your preferences?", "This is a reminder to save accordingly to your goals, and keep in mind that you want to buy a house!", "Are you sure this is what you want to save according to your preferences?", "Are you sure this is what you want to save according to your preferences?"],
                     ["This is not the definition of a portfolio diversification strategy.", "This is not the definition of a portfolio diversification strategy.", "This is not the definition of a portfolio diversification strategy.", "This is a definition of portfolio diversification strategy!"],
                     ["Savings account will not provide a sufficient return on the investment for retirement, and having money saved in the bank is not such a great idea as only up to 85000£ are insured. Cyprus haircut is a great case to check", "Pension schemes are retirement plans which allow people to enjoy income even after retirement. There are 4 pension plans: ccupational, work, company, work-based, provided to the public, which grow through a monthly payment from the salary of the individual, the person might also enjoy tax relief from this activity. If you do not own one, we encourage you to have a conversation with your employer about this.", "Although having invested in a property that will generate your money in the future is generally a good idea, relaying only one asset class specifically as a retirement income is not an ideal plan.", "Gambling is not a long-term investment. It is not encouraged in any form through this platform, although it has been very popular amongst young adults during covid-19. If you feel gambling is a safe investment, we encourage to visit a financial expert for guidance."],
                     ["Bugeting is usually the best way to track your expenses", "Credit score is the main element of accessing money. Having a good credit score, indicates that an individual can be trustworthy to repay its debt obligations, therefore is more trusted to gain a loan which is going to be repaid on time. Example a mortgage loan could be up to 25 years, the lender needs to see some previous experience of consistent repayments.","Net worth is usually referred to as an individual’s economic status, which is calculated by reducing total liabilities from total assets", "Budgeting is usually one way to discover saving money."],
                     ["This can be related to a savings account, but it is not related to emergencies", "This is what an emerency fund is for and why it is important to have!", "An investment portfolio, is an account that showcasing and allows the user to manage its investments in financial markets and financial assets.", "This is an account where money are saved to pay a specific obligation, debt"],
                     ["This question indicates what the term -opportunity cost- is.","This answer does not match the definition of opportunity cost.", "This answer does not match the definition of opportunity cost.", "This answer does not match the definition of opportunity cost."]
                     ]
        #the correct answers for each question
correct_answers = ["C", "D", "B", "D", "B", "D", "B", "B", "B", "A"]

        #the wrong answers for each question
incorrect_answers = [["A", "B", "D"], ["A", "B", "C"], ["A", "C", "D"], ["A", "B", "C"], ["A", "C", "D"], ["A", "B", "C"],["A", "C", "D"], ["A", "C", "D"], ["A", "C", "D"], ["B", "C", "D"]]

        #messages based on the answers
encouraging_messages = ["You're doing great! Keep it up!", "Well done! You are making progress", "Keep pushing, you got this!", "I am impressed by your dedication, you are awesome!", "Magnificent! Your knowledge is on point!", "You rock!! Amazing work!!"]
incorrect_answer_messages = ["Believe you can and you are halfway there!", "Never give up, you got this lets keep pushing!", "There is no success without failure! Lets gooo..", "The moment you give up is the moment you lose! I believe in you keep going!", "Its not failure, its a step towards success! Don't give up now!"]




def start_quiz(request): 
    #introduction message
    introduction = "Hello, \nYou have selected the general category for personal finance.\nThis category consists of savings, credit, investing, insurance, income, and purchases as the main topics of the questions.\nYou will have to answer 10 questions. 10 points will be awarded for every correct answer, and there is no point deduction for wrong answers.\nAnswer correctly to 7/10 questions, and you will receive a badge of completion.\nAnswer correctly to all 10 questions, and you will receive £10.\nYou can try as many times as you want to receive the rewards, but the rewards can be claimed only once.\n you can navigate through the questions by pressing the 'next or 'previous' and press 'submit' to submit your answer." 
    
    
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            request.session['username'] = username
            #initialize score and question index
            request.session['score'] = 0
            request.session['current_question_index'] = 0
            return redirect('GamifQuiz:quiz_question', question_number=1)


    return render(request, 'start_quiz.html', {
             'introduction': introduction,})
    


def quiz_question(request, question_number=None):
    if 'username' not in request.session:
         return redirect('GamifQuiz:start_quiz')
    
    if question_number is None:
        return redirect('GamifQuiz:start_quiz')
    
    current_question_index = int(question_number) - 1  # Subtract 1 to match the question index
    score = request.session.get('score', 0)
    username = request.session.get('username')

    if current_question_index >= len(questions):
        return redirect('GamifQuiz:quiz_result')
    
    current_question = questions[current_question_index]
    current_answers = answers[current_question_index]
    current_extra_info = extra_information[current_question_index]
    correct_answer = correct_answers[current_question_index]
    incorrect_answers_list = incorrect_answers[current_question_index]
    encouraging_message = encouraging_messages[current_question_index % len(encouraging_messages)]
    incorrect_message = incorrect_answer_messages[current_question_index % len(incorrect_answer_messages)]

    message = ''
    feedback = ''  

    if request.method == 'POST':
        selected_answer = request.POST.get('answer')
        selected_letter = selected_answer[0] if selected_answer else ''

        print(f"Selected answer: {selected_answer}")
        print(f"Current answers: {current_answers}")
        
        if selected_answer:
            if selected_letter == correct_answer:
                score += 10
                message = encouraging_message
                feedback = current_extra_info[current_answers.index(selected_answer)]
            else:
                if selected_letter in correct_answer:
                    feedback = current_extra_info[current_answers.index(selected_letter)]
                else:
                    try:
                        incorrect_index = incorrect_answers[current_question_index].index(selected_letter)
                        message = incorrect_message
                        feedback = current_extra_info[incorrect_index]
                    except ValueError:
                        feedback = current_extra_info[current_answers.index(correct_answer)]
        else:
            feedback = "Please select an answer before submitting."

        request.session['score'] = score
        request.session['current_question_index'] = current_question_index + 1

    context = {
        'username': username,
        'question': current_question,
        'answers': current_answers,
        'extra_info': current_extra_info,
        'message': message,
        'feedback': feedback,
        'score': score,
        'progress': int((current_question_index / len(questions)) * 100),
    }

    template_name = f'question_{question_number}.html'
    return render(request, template_name, context)




def quiz_result(request):
    print("Quiz result view accessed!")

    username = request.session.get('username')
    score = request.session.get('score', 0)
    progress = int((score/ (10 * len(questions))) *100)
    badge = ""
    reward = ""
    
 #prepare the messages based on the progress
    if progress >= 70:
            badge = "Completion Badge"
            message = "You can claim your badge! Play again for a chance to win a £10 reward!"
    elif progress == 100:
            reward = "£10"
            message = "Congratulations! You can claim your badge and your £10 reward once you exit!"
    else:
            message = "You should try again for a chance to claim the rewards!"
    
    if request.method == 'POST':
         if 'play-again' in request.POST:
              request.session['score']=0
              request.session['current_question_index']=0
              return redirect('GamifQuiz:start_quiz')
         elif 'submit-feedback' in request.POST:
            return redirect('GamifQuiz:submit_feedback')
    
    context = {
              'username': username,
              'score': score,
              'progress': progress,
              'badge': badge,
              'reward': reward, 
              'message' : message,
    }
    return render(request, 'quiz_result.html', context)




# Define the feedback questions and their corresponding names and rating options
feedback_questions = [
    {'name': 'features', 'question': 'How much did the gamification features such as points, badges and encouraging messages motivated your progress through the quiz?', 'rating_options': range(1, 11)},
    {'name': 'experience', 'question': 'How would you rate this type of experience of a financial educational content?', 'rating_options': range(1, 11)},
    {'name': 'future', 'question': 'How pleased would you be if similar gamification features would be applied in financial services platforms?', 'rating_options': range(1, 11)}
]

def submit_feedback(request):
    if request.method == 'POST':
        print("Submit feedback view accessed!")
        feedback_data = {}
        for question in feedback_questions:
            feedback_data[question['name']] = request.POST.get(question['name'])

        open_ended_feedback = request.POST.get('thoughts')
        if all(feedback_data.values()) and open_ended_feedback:
            return render(request, 'thank_you.html', {
                'feedback_data': feedback_data,
                'open_ended_feedback': open_ended_feedback,
            })

    return render(request, 'feedback.html', {
        'feedback_questions': feedback_questions
    })


def thank_you(request):      
    return render(request, 'thank_you.html')

def play_again(request):
     return render(request, 'play_again.html')

