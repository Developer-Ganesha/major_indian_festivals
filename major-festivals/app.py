from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import json
import os
from datetime import datetime, timedelta
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', os.urandom(24))

# Load festival data
def load_festival_data():
    with open('data/festivals.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Timer management
def init_timer():
    session['start_time'] = datetime.now().timestamp()
    session['time_left'] = 600  # 10 minutes in seconds

def update_timer():
    if 'start_time' in session:
        elapsed = datetime.now().timestamp() - session['start_time']
        session['time_left'] = max(0, 600 - elapsed)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    festivals = load_festival_data()
    return render_template('home.html', festivals=festivals)

@app.route('/learn/<festival_id>')
def learn(festival_id):
    festivals = load_festival_data()
    festival = festivals.get(festival_id)
    if not festival:
        return redirect(url_for('home'))
    return render_template('learn.html', festival=festival)

@app.route('/save_answer', methods=['POST'])
def save_answer():
    data = request.get_json()
    question_index = data.get('question_index')
    answer = data.get('answer')
    
    if 'selected_answers' not in session:
        session['selected_answers'] = {}
    
    session['selected_answers'][question_index] = answer
    session.modified = True
    return jsonify({'status': 'success'})
@app.route('/quiz/<festival_id>', methods=['GET', 'POST'])
def quiz(festival_id):
    festivals = load_festival_data()
    festival = festivals.get(festival_id)
    if not festival:
        return redirect(url_for('home'))

    # Get questions for this festival
    questions = festival.get('quiz', [])
    
    if request.method == 'GET':
        # Initialize timer when quiz starts
        init_timer()
        # Clear any previous answers
        session.pop('selected_answers', None)
        # Store current question index
        session['current_question'] = 0
        return render_template('quiz.html', 
                             festival=festival, 
                             questions=questions,
                             current_question=0,
                             total_questions=len(questions))

    if request.method == 'POST':
        update_timer()
        form_data = request.form.to_dict()
        
        # Process answers and calculate score
        answers = []
        score = 0
        for i, question in enumerate(questions):
            answer = form_data.get(f'answer_{i}', '')
            answers.append(answer)
            if answer == question['correct']:
                score += 1
        
        # Store results in session
        session[f'quiz_{festival_id}_score'] = score
        session[f'quiz_{festival_id}_answers'] = answers
        session[f'quiz_{festival_id}_questions'] = questions
        session.pop('selected_answers', None)
        session.pop('current_question', None)
        
        return redirect(url_for('result', festival_id=festival_id))

@app.route('/result/<festival_id>')
def result(festival_id):
    update_timer()
    festivals = load_festival_data()
    festival = festivals.get(festival_id)
    if not festival:
        return redirect(url_for('home'))

    # Get quiz results from session
    score = session.get(f'quiz_{festival_id}_score', 0)
    answers = session.get(f'quiz_{festival_id}_answers', [])
    questions = session.get(f'quiz_{festival_id}_questions', [])

    # Calculate total questions and percentage
    total_questions = len(questions)
    percentage = (score / total_questions * 100) if total_questions > 0 else 0

    # Create a list of question-answer pairs for display
    quiz_results = []
    for i, (question, answer) in enumerate(zip(questions, answers)):
        quiz_results.append({
            'question': question['question'],
            'user_answer': answer,
            'correct_answer': question['correct'],
            'is_correct': answer == question['correct']
        })

    return render_template('result.html', 
                         festival=festival, 
                         score=score,
                         total_questions=total_questions,
                         percentage=percentage,
                         quiz_results=quiz_results)

@app.route('/quiz/all', methods=['GET', 'POST'])
def all_quiz():
    festivals = load_festival_data()
    
    # Get questions from each festival and combine them
    all_questions = []
    for fest in festivals.values():
        all_questions.extend(fest['quiz'])
    
    if request.method == 'GET':
        # Initialize timer when quiz starts
        init_timer()
        # Shuffle the questions to randomize the order
        random.shuffle(all_questions)
        # Store questions in session for later use
        session['quiz_questions'] = all_questions
        return render_template('all_quiz.html', questions=all_questions)
    
    if request.method == 'POST':
        update_timer()
        form_data = request.form.to_dict()
        
        # Get questions from session
        all_questions = session.get('quiz_questions', [])
        if not all_questions:
            return redirect(url_for('all_quiz'))
        
        # Process answers and calculate score
        answers = []
        score = 0
        
        # Collect answers and calculate score
        for i in range(len(all_questions)):
            answer = form_data.get(f'question_{i}', '')
            answers.append(answer)
            if answer == all_questions[i]['correct']:
                score += 1
        
        # Store results in session
        session['all_quiz_score'] = score
        session['all_quiz_answers'] = answers
        session['all_quiz_questions'] = all_questions
        
        # Clean up session
        session.pop('quiz_questions', None)
        session.pop('selected_answers', None)
        
        return redirect(url_for('all_result'))

@app.route('/result/all')
def all_result():
    update_timer()
    
    # Get quiz results from session
    questions = session.get('all_quiz_questions', [])
    score = session.get('all_quiz_score', 0)
    answers = session.get('all_quiz_answers', [])
    
    # If no quiz data in session, redirect to quiz
    if not questions or not answers:
        return redirect(url_for('all_quiz'))
    
    # Calculate total questions
    total_questions = len(questions)
    
    # Render template with results
    return render_template('all_result.html', 
                         questions=questions,
                         score=score,
                         answers=answers,
                         total_questions=total_questions)

@app.route('/api/timer')
def get_timer():
    update_timer()
    return jsonify({'time_left': session.get('time_left', 600)})

@app.route('/submit_quiz/<festival_id>', methods=['POST'])
def submit_quiz(festival_id):
    # Handle form submission logic here
    return redirect(url_for('quiz', festival_id=festival_id))

@app.route('/festival-flip')
def festival_flip():
    return render_template('festival_flip.html')

@app.route('/festival/regions')
def festival_regions():
    return render_template('festival_regions.html')

@app.route('/festival/timing')
def festival_timing():
    return render_template('festival_timing.html')

@app.route('/festival/significance')
def festival_significance():
    return render_template('festival_significance.html')

@app.route('/festival/customs')
def festival_customs():
    return render_template('festival_customs.html')

if __name__ == '__main__':
    # Use environment variables for host and port
    port = int(os.getenv('PORT', 5000))
    app.run(host='127.0.0.1', port=port, debug=True)