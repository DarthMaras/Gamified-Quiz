# my_quiz_project/myquiz/views.py
from django.shortcuts import render
from quiz_logic import generate_pseudoname

# Sample data for questions, answers, and correct answers
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

def quiz(request):
    if request.method == 'POST':
        # Handle form submission and quiz logic here
        # This code will be executed when the user submits the quiz form

        # Get the user's selected answers from the form
        user_answers = [
            request.POST.get('q1'),
            request.POST.get('q2'),
            request.POST.get('q3'),
            request.POST.get('q4'),
            request.POST.get('q5'),
            request.POST.get('q6'),
            request.POST.get('q7'),
            request.POST.get('q8'),
            request.POST.get('q9'),
            request.POST.get('q10'),
        ]

        # Check the user's answers against the correct answers
        score = 0
        for i in range(len(correct_answers)):
            if user_answers[i] == correct_answers[i]:
                score += 10

        # Store the score in the database or perform other actions as needed

        # Render the result page with the user's score
        return render(request, 'myquiz/result.html', {'score': score})

    else:
        # Generate the unique pseudoname for the user
        username = generate_pseudoname()

        # Combine questions and answers into a list of tuples
        quiz_data = zip(questions, answers)

        # Rest of your introduction and rendering the quiz form...
        return render(request, 'myquiz/quiz_form.html', {'username': username, 'quiz_data': quiz_data})
