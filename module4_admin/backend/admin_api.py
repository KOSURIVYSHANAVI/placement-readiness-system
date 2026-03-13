from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
CORS(app)

# MongoDB Connection with pooling
client = MongoClient('mongodb://localhost:27017/', maxPoolSize=50, minPoolSize=10)
db = client['placement_readiness_module4']
admins_collection = db['admins']

# Create indexes
admins_collection.create_index('email', unique=True)

# Access other modules' databases
module1_db = client['placement_readiness_module1']
students_collection = module1_db['students']
questions_collection = module1_db['questions']
test_results_collection = module1_db['test_results']

module2_db = client['placement_readiness_module2']
roadmaps_collection = module2_db['roadmaps']
company_eligibility_collection = module2_db['company_eligibility']

# Admin Authentication
@app.route('/api/admin/register', methods=['POST'])
def register_admin():
    data = request.json
    if admins_collection.find_one({'email': data['email']}):
        return jsonify({'message': 'Email already exists'}), 400
    
    admin = {
        'name': data['name'],
        'email': data['email'],
        'password': generate_password_hash(data['password']),
        'created_at': datetime.utcnow()
    }
    result = admins_collection.insert_one(admin)
    return jsonify({'message': 'Admin registered successfully'}), 201

@app.route('/api/admin/login', methods=['POST'])
def login_admin():
    data = request.json
    
    # HARDCODED ADMIN CREDENTIALS - Only this email/password works
    ADMIN_EMAIL = 'admin@placement.com'
    ADMIN_PASSWORD = 'admin123'
    
    if data['email'] == ADMIN_EMAIL and data['password'] == ADMIN_PASSWORD:
        return jsonify({
            'message': 'Login successful',
            'admin_id': 'admin_001',
            'name': 'Admin'
        }), 200
    
    return jsonify({'error': 'Invalid credentials'}), 401

# Monitor Student Readiness
@app.route('/api/admin/students', methods=['GET'])
def get_all_students():
    # OPTIMIZED: Use aggregation with lookup
    pipeline = [
        {'$lookup': {
            'from': 'test_results',
            'localField': '_id',
            'foreignField': 'student_id',
            'as': 'results',
            'pipeline': [{'$project': {'percentage': 1}}]
        }},
        {'$project': {
            'name': 1,
            'email': 1,
            'created_at': 1,
            'tests_taken': {'$size': '$results'},
            'average_score': {'$avg': '$results.percentage'}
        }}
    ]
    
    students = list(students_collection.aggregate(pipeline))
    
    student_data = [{
        'id': str(s['_id']),
        'name': s['name'],
        'email': s['email'],
        'tests_taken': s.get('tests_taken', 0),
        'average_score': round(s.get('average_score', 0), 2),
        'readiness_status': 'Ready' if s.get('average_score', 0) >= 70 else 'Needs Improvement',
        'registered_at': s['created_at'].strftime('%Y-%m-%d')
    } for s in students]
    
    return jsonify({'students': student_data, 'total': len(student_data)})

# System Analytics
@app.route('/api/admin/analytics', methods=['GET'])
def get_system_analytics():
    total_students = students_collection.count_documents({})
    total_tests = test_results_collection.count_documents({})
    total_questions = questions_collection.count_documents({})
    total_roadmaps = roadmaps_collection.count_documents({})
    
    pipeline = [{'$group': {'_id': None, 'avg_percentage': {'$avg': '$percentage'}}}]
    result = list(test_results_collection.aggregate(pipeline))
    avg_performance = result[0]['avg_percentage'] if result else 0
    
    # Category-wise performance
    category_pipeline = [
        {'$group': {'_id': '$category', 'avg_score': {'$avg': '$percentage'}, 'count': {'$sum': 1}}}
    ]
    category_stats = list(test_results_collection.aggregate(category_pipeline))
    
    return jsonify({
        'total_students': total_students,
        'total_tests': total_tests,
        'total_questions': total_questions,
        'total_roadmaps': total_roadmaps,
        'avg_performance': round(avg_performance, 2),
        'category_stats': [{
            'category': stat['_id'],
            'avg_score': round(stat['avg_score'], 2),
            'attempts': stat['count']
        } for stat in category_stats]
    })

# Manage Questions
@app.route('/api/admin/questions', methods=['POST'])
def add_question():
    data = request.json
    question = {
        'category': data['category'],
        'question_text': data['question_text'],
        'option_a': data['option_a'],
        'option_b': data['option_b'],
        'option_c': data['option_c'],
        'option_d': data['option_d'],
        'correct_answer': data['correct_answer'],
        'created_at': datetime.utcnow()
    }
    questions_collection.insert_one(question)
    return jsonify({'message': 'Question added successfully'}), 201

@app.route('/api/admin/questions', methods=['GET'])
def get_all_questions():
    questions = list(questions_collection.find())
    return jsonify([{
        'id': str(q['_id']),
        'category': q['category'],
        'question_text': q['question_text'],
        'correct_answer': q['correct_answer']
    } for q in questions])

# Manage Roadmaps
@app.route('/api/admin/roadmaps', methods=['POST'])
def add_roadmap():
    data = request.json
    roadmap = {
        'category': data['category'],
        'title': data['title'],
        'description': data['description'],
        'resources': data['resources'],
        'duration': data['duration'],
        'created_at': datetime.utcnow()
    }
    roadmaps_collection.insert_one(roadmap)
    return jsonify({'message': 'Roadmap added successfully'}), 201

@app.route('/api/admin/roadmaps', methods=['GET'])
def get_all_roadmaps():
    roadmaps = list(roadmaps_collection.find())
    return jsonify([{
        'id': str(r['_id']),
        'category': r['category'],
        'title': r['title'],
        'description': r['description'],
        'resources': r['resources'],
        'duration': r['duration']
    } for r in roadmaps])

# Manage Company Eligibility
@app.route('/api/admin/companies', methods=['POST'])
def add_company():
    data = request.json
    company = {
        'name': data['name'],
        'min_score': data['min_score'],
        'roles': data['roles'],
        'package': data['package'],
        'created_at': datetime.utcnow()
    }
    company_eligibility_collection.insert_one(company)
    return jsonify({'message': 'Company added successfully'}), 201

# Add New Subject/Category
@app.route('/api/admin/subjects', methods=['POST'])
def add_subject():
    data = request.json
    subject = {
        'key': data['key'],
        'name': data['name'],
        'icon': data.get('icon', '📚'),
        'created_at': datetime.utcnow()
    }
    db['subjects'].insert_one(subject)
    return jsonify({'message': 'Subject added successfully', 'subject': subject}), 201

# Get All Subjects
@app.route('/api/admin/subjects', methods=['GET'])
def get_all_subjects():
    subjects = list(db['subjects'].find())
    return jsonify([{
        'id': str(s['_id']),
        'key': s['key'],
        'name': s['name'],
        'icon': s.get('icon', '📚')
    } for s in subjects])

# Get Question Count by Category
@app.route('/api/admin/questions/count', methods=['GET'])
def get_question_counts():
    pipeline = [
        {'$group': {'_id': '$category', 'count': {'$sum': 1}}}
    ]
    counts = list(questions_collection.aggregate(pipeline))
    return jsonify([{
        'category': c['_id'],
        'count': c['count']
    } for c in counts])

# Generate Reports
@app.route('/api/admin/reports/placement-readiness', methods=['GET'])
def generate_placement_report():
    students = list(students_collection.find())
    
    report = []
    for student in students:
        results = list(test_results_collection.find({'student_id': str(student['_id'])}))
        if results:
            avg_score = sum([r['percentage'] for r in results]) / len(results)
            report.append({
                'student_name': student['name'],
                'email': student['email'],
                'tests_completed': len(results),
                'average_score': round(avg_score, 2),
                'placement_ready': 'Yes' if avg_score >= 70 else 'No',
                'recommendation': 'Ready for placements' if avg_score >= 70 else 'Needs more preparation'
            })
    
    return jsonify({
        'report_date': datetime.utcnow().strftime('%Y-%m-%d'),
        'total_students': len(report),
        'ready_students': len([s for s in report if s['placement_ready'] == 'Yes']),
        'students': report
    })

if __name__ == '__main__':
    app.run(debug=True, port=5004)
