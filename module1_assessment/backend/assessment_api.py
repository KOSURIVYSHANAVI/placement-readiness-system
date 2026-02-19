from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import bcrypt
from datetime import datetime

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['placement_readiness_module1']

@app.route('/api/student/register', methods=['POST'])
def register():
    data = request.json
    if db.students.find_one({'email': data['email']}):
        return jsonify({'error': 'Email already exists'}), 400
    
    hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    student = {
        'name': data['name'],
        'email': data['email'],
        'password': hashed,
        'created_at': datetime.now()
    }
    result = db.students.insert_one(student)
    return jsonify({'message': 'Registration successful', 'student_id': str(result.inserted_id)}), 201

@app.route('/api/student/login', methods=['POST'])
def login():
    data = request.json
    student = db.students.find_one({'email': data['email']})
    if not student or not bcrypt.checkpw(data['password'].encode('utf-8'), student['password']):
        return jsonify({'error': 'Invalid credentials'}), 401
    
    return jsonify({'message': 'Login successful', 'student_id': str(student['_id']), 'name': student['name']}), 200

@app.route('/api/questions/<category>', methods=['GET'])
def get_questions(category):
    questions = list(db.questions.find({'category': category}))
    for q in questions:
        q['id'] = str(q['_id'])
        del q['_id']
    return jsonify(questions), 200

@app.route('/api/test/submit', methods=['POST'])
def submit_test():
    data = request.json
    student_id = data['student_id']
    category = data['category']
    answers = data['answers']
    
    score = 0
    total = len(answers)
    
    for ans in answers:
        question = db.questions.find_one({'_id': ObjectId(ans['question_id'])})
        if question and question['correct_answer'] == ans['selected_answer']:
            score += 1
    
    percentage = (score / total * 100) if total > 0 else 0
    readiness_score = percentage * 0.8
    
    result = {
        'student_id': student_id,
        'category': category,
        'score': score,
        'total': total,
        'percentage': percentage,
        'readiness_score': readiness_score,
        'submitted_at': datetime.now()
    }
    db.test_results.insert_one(result)
    
    return jsonify({
        'score': score,
        'total': total,
        'percentage': percentage,
        'readiness_score': readiness_score
    }), 200

@app.route('/api/results/<student_id>', methods=['GET'])
def get_results(student_id):
    results = list(db.test_results.find({'student_id': student_id}))
    for r in results:
        r['id'] = str(r['_id'])
        del r['_id']
        r['submitted_at'] = r['submitted_at'].strftime('%Y-%m-%d %H:%M:%S')
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
