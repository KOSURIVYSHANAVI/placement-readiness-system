from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['placement_readiness_module1']

# Clear existing questions
db.questions.delete_many({})

# Quantitative Aptitude - 30 Questions
quantitative_questions = [
    {
        'category': 'quantitative',
        'question_text': 'If 20% of a number is 50, what is the number?',
        'option_a': '200',
        'option_b': '250',
        'option_c': '300',
        'option_d': '350',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'A train travels 120 km in 2 hours. What is its speed?',
        'option_a': '50 km/h',
        'option_b': '60 km/h',
        'option_c': '70 km/h',
        'option_d': '80 km/h',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is 15% of 200?',
        'option_a': '25',
        'option_b': '30',
        'option_c': '35',
        'option_d': '40',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'If x + 5 = 12, what is x?',
        'option_a': '5',
        'option_b': '6',
        'option_c': '7',
        'option_d': '8',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'The average of 10, 20, and 30 is:',
        'option_a': '15',
        'option_b': '20',
        'option_c': '25',
        'option_d': '30',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is the square root of 144?',
        'option_a': '10',
        'option_b': '11',
        'option_c': '12',
        'option_d': '13',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'If a product costs $80 after a 20% discount, what was the original price?',
        'option_a': '$90',
        'option_b': '$95',
        'option_c': '$100',
        'option_d': '$105',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is 25% of 80?',
        'option_a': '15',
        'option_b': '20',
        'option_c': '25',
        'option_d': '30',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'If 3x = 27, what is x?',
        'option_a': '7',
        'option_b': '8',
        'option_c': '9',
        'option_d': '10',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'The ratio of 15 to 45 is:',
        'option_a': '1:2',
        'option_b': '1:3',
        'option_c': '1:4',
        'option_d': '1:5',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is 10% of 500?',
        'option_a': '40',
        'option_b': '45',
        'option_c': '50',
        'option_d': '55',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'If a = 5 and b = 3, what is 2a + 3b?',
        'option_a': '17',
        'option_b': '18',
        'option_c': '19',
        'option_d': '20',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is the value of 5²?',
        'option_a': '20',
        'option_b': '25',
        'option_c': '30',
        'option_d': '35',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'If 40% of a number is 80, what is the number?',
        'option_a': '180',
        'option_b': '200',
        'option_c': '220',
        'option_d': '240',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is 30% of 150?',
        'option_a': '40',
        'option_b': '45',
        'option_c': '50',
        'option_d': '55',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'The sum of angles in a triangle is:',
        'option_a': '90°',
        'option_b': '180°',
        'option_c': '270°',
        'option_d': '360°',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'If x - 8 = 15, what is x?',
        'option_a': '21',
        'option_b': '22',
        'option_c': '23',
        'option_d': '24',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is 50% of 200?',
        'option_a': '90',
        'option_b': '95',
        'option_c': '100',
        'option_d': '105',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'The LCM of 4 and 6 is:',
        'option_a': '10',
        'option_b': '12',
        'option_c': '14',
        'option_d': '16',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'If 2x + 5 = 15, what is x?',
        'option_a': '3',
        'option_b': '4',
        'option_c': '5',
        'option_d': '6',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is the cube of 3?',
        'option_a': '9',
        'option_b': '18',
        'option_c': '27',
        'option_d': '36',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'The perimeter of a square with side 5 cm is:',
        'option_a': '15 cm',
        'option_b': '20 cm',
        'option_c': '25 cm',
        'option_d': '30 cm',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is 75% of 80?',
        'option_a': '55',
        'option_b': '60',
        'option_c': '65',
        'option_d': '70',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'If 5x = 45, what is x?',
        'option_a': '7',
        'option_b': '8',
        'option_c': '9',
        'option_d': '10',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'The area of a rectangle with length 10 and width 5 is:',
        'option_a': '40',
        'option_b': '45',
        'option_c': '50',
        'option_d': '55',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is 20% of 250?',
        'option_a': '45',
        'option_b': '50',
        'option_c': '55',
        'option_d': '60',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'The HCF of 12 and 18 is:',
        'option_a': '4',
        'option_b': '6',
        'option_c': '8',
        'option_d': '10',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'If x/4 = 5, what is x?',
        'option_a': '15',
        'option_b': '20',
        'option_c': '25',
        'option_d': '30',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is 60% of 50?',
        'option_a': '25',
        'option_b': '30',
        'option_c': '35',
        'option_d': '40',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'The value of 8 × 7 is:',
        'option_a': '54',
        'option_b': '56',
        'option_c': '58',
        'option_d': '60',
        'correct_answer': 'B'
    }
]

db.questions.insert_many(quantitative_questions)
print(f"✅ Inserted {len(quantitative_questions)} Quantitative Aptitude questions")
