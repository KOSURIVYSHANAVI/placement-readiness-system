from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

# MongoDB Connection with pooling
client = MongoClient('mongodb://localhost:27017/', maxPoolSize=50, minPoolSize=10)
module1_db = client['placement_readiness_module1']
test_results_collection = module1_db['test_results']
students_collection = module1_db['students']

# Create indexes
test_results_collection.create_index([('student_id', 1), ('completed_at', -1)])

# Get Student Progress Over Time
@app.route('/api/analytics/progress/<student_id>', methods=['GET'])
def get_student_progress(student_id):
    results = list(test_results_collection.find({'student_id': student_id}).sort('completed_at', 1))
    
    progress_data = []
    for result in results:
        progress_data.append({
            'category': result['category'],
            'percentage': result['percentage'],
            'date': result['completed_at'].strftime('%Y-%m-%d'),
            'readiness_score': result.get('readiness_score', 0)
        })
    
    return jsonify({
        'total_tests': len(results),
        'progress_data': progress_data
    })

# Compare Current vs Previous Scores
@app.route('/api/analytics/comparison/<student_id>', methods=['GET'])
def compare_scores(student_id):
    results = list(test_results_collection.find({'student_id': student_id}).sort('completed_at', -1))
    
    comparisons = {}
    for result in results:
        category = result['category']
        if category not in comparisons:
            comparisons[category] = {
                'current': result['percentage'],
                'previous': None,
                'improvement': 0
            }
        else:
            comparisons[category]['previous'] = result['percentage']
            comparisons[category]['improvement'] = comparisons[category]['current'] - result['percentage']
    
    return jsonify({
        'comparisons': comparisons
    })

# Get Performance Chart Data
@app.route('/api/analytics/chart/<student_id>', methods=['GET'])
def get_chart_data(student_id):
    results = list(test_results_collection.find({'student_id': student_id}))
    
    categories = []
    scores = []
    
    for result in results:
        if result['category'] not in categories:
            categories.append(result['category'])
            scores.append(result['percentage'])
    
    return jsonify({
        'categories': categories,
        'scores': scores,
        'chart_type': 'bar'
    })

# Get Overall Analytics Dashboard
@app.route('/api/analytics/dashboard/<student_id>', methods=['GET'])
def get_analytics_dashboard(student_id):
    # OPTIMIZED: Use aggregation pipeline
    pipeline = [
        {'$match': {'student_id': student_id}},
        {'$group': {
            '_id': None,
            'total_tests': {'$sum': 1},
            'average_score': {'$avg': '$percentage'},
            'highest_score': {'$max': '$percentage'},
            'lowest_score': {'$min': '$percentage'},
            'categories': {'$addToSet': '$category'}
        }}
    ]
    result = list(test_results_collection.aggregate(pipeline))
    
    if not result:
        return jsonify({
            'message': 'No data available',
            'total_tests': 0,
            'average_score': 0,
            'highest_score': 0,
            'lowest_score': 0
        })
    
    data = result[0]
    return jsonify({
        'total_tests': data['total_tests'],
        'average_score': round(data['average_score'], 2),
        'highest_score': round(data['highest_score'], 2),
        'lowest_score': round(data['lowest_score'], 2),
        'categories_attempted': len(data['categories'])
    })

# Get Readiness Improvement Timeline
@app.route('/api/analytics/timeline/<student_id>', methods=['GET'])
def get_readiness_timeline(student_id):
    results = list(test_results_collection.find({'student_id': student_id}).sort('completed_at', 1))
    
    timeline = []
    for result in results:
        timeline.append({
            'date': result['completed_at'].strftime('%Y-%m-%d %H:%M'),
            'category': result['category'],
            'readiness_score': result.get('readiness_score', 0),
            'percentage': result['percentage']
        })
    
    return jsonify({
        'timeline': timeline
    })

if __name__ == '__main__':
    app.run(debug=True, port=5003)
