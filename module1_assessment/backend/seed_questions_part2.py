from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['placement_readiness_module1']

# Logical Reasoning - 30 Questions
reasoning_questions = [
    {'category': 'reasoning', 'question_text': 'If all roses are flowers and some flowers are red, then:', 'option_a': 'All roses are red', 'option_b': 'Some roses may be red', 'option_c': 'No roses are red', 'option_d': 'All flowers are roses', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'Find the odd one out: 2, 4, 6, 9, 10', 'option_a': '2', 'option_b': '4', 'option_c': '9', 'option_d': '10', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'Complete the series: 2, 4, 8, 16, __', 'option_a': '20', 'option_b': '24', 'option_c': '28', 'option_d': '32', 'correct_answer': 'D'},
    {'category': 'reasoning', 'question_text': 'If A is taller than B, and B is taller than C, then:', 'option_a': 'C is tallest', 'option_b': 'A is tallest', 'option_c': 'B is tallest', 'option_d': 'Cannot determine', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'Find the next number: 1, 4, 9, 16, __', 'option_a': '20', 'option_b': '25', 'option_c': '30', 'option_d': '36', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'If CAT = 24, DOG = 26, then BAT = ?', 'option_a': '20', 'option_b': '22', 'option_c': '23', 'option_d': '24', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'Complete: ACE, BDF, CEG, __', 'option_a': 'DFH', 'option_b': 'DEF', 'option_c': 'EFG', 'option_d': 'FGH', 'correct_answer': 'A'},
    {'category': 'reasoning', 'question_text': 'If BOOK is coded as CPPL, then WORD is:', 'option_a': 'XPSE', 'option_b': 'XQSE', 'option_c': 'WQSE', 'option_d': 'WPRD', 'correct_answer': 'A'},
    {'category': 'reasoning', 'question_text': 'Find odd one: Apple, Banana, Carrot, Mango', 'option_a': 'Apple', 'option_b': 'Banana', 'option_c': 'Carrot', 'option_d': 'Mango', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'Complete: 5, 10, 20, 40, __', 'option_a': '60', 'option_b': '70', 'option_c': '80', 'option_d': '90', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'If Monday is 2 days after today, what day is today?', 'option_a': 'Wednesday', 'option_b': 'Thursday', 'option_c': 'Friday', 'option_d': 'Saturday', 'correct_answer': 'D'},
    {'category': 'reasoning', 'question_text': 'Find the missing number: 3, 6, 12, 24, __', 'option_a': '36', 'option_b': '42', 'option_c': '48', 'option_d': '54', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'If RAIN is coded as 1234, then TRAIN is:', 'option_a': '51234', 'option_b': '61234', 'option_c': '71234', 'option_d': '81234', 'correct_answer': 'A'},
    {'category': 'reasoning', 'question_text': 'Complete: AB, CD, EF, __', 'option_a': 'FG', 'option_b': 'GH', 'option_c': 'HI', 'option_d': 'IJ', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'Find odd one: 11, 13, 17, 18, 19', 'option_a': '11', 'option_b': '13', 'option_c': '17', 'option_d': '18', 'correct_answer': 'D'},
    {'category': 'reasoning', 'question_text': 'If 2 + 3 = 10, 3 + 4 = 14, then 4 + 5 = ?', 'option_a': '18', 'option_b': '20', 'option_c': '22', 'option_d': '24', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'Complete: 1, 1, 2, 3, 5, 8, __', 'option_a': '11', 'option_b': '12', 'option_c': '13', 'option_d': '14', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'If BLUE is coded as CMVF, then RED is:', 'option_a': 'SFE', 'option_b': 'SDE', 'option_c': 'TFE', 'option_d': 'TDE', 'correct_answer': 'A'},
    {'category': 'reasoning', 'question_text': 'Find the next: 100, 50, 25, __', 'option_a': '10', 'option_b': '12.5', 'option_c': '15', 'option_d': '20', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'If all birds can fly and penguin is a bird, then:', 'option_a': 'Penguin can fly', 'option_b': 'Penguin cannot fly', 'option_c': 'Statement is contradictory', 'option_d': 'Cannot determine', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'Complete: 2, 6, 12, 20, __', 'option_a': '28', 'option_b': '30', 'option_c': '32', 'option_d': '34', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'Find odd one: Circle, Square, Triangle, Rectangle', 'option_a': 'Circle', 'option_b': 'Square', 'option_c': 'Triangle', 'option_d': 'Rectangle', 'correct_answer': 'A'},
    {'category': 'reasoning', 'question_text': 'If A = 1, B = 2, then Z = ?', 'option_a': '24', 'option_b': '25', 'option_c': '26', 'option_d': '27', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'Complete: 10, 20, 30, 40, __', 'option_a': '45', 'option_b': '50', 'option_c': '55', 'option_d': '60', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'If MOTHER is coded as NPUIFS, then FATHER is:', 'option_a': 'GBUIFS', 'option_b': 'GBUIFS', 'option_c': 'GBUIFS', 'option_d': 'GBUIFS', 'correct_answer': 'A'},
    {'category': 'reasoning', 'question_text': 'Find the next: 3, 9, 27, 81, __', 'option_a': '162', 'option_b': '243', 'option_c': '324', 'option_d': '405', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'Complete: A1, B2, C3, __', 'option_a': 'D3', 'option_b': 'D4', 'option_c': 'E4', 'option_d': 'E5', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'Find odd one: 5, 10, 15, 22, 25', 'option_a': '5', 'option_b': '10', 'option_c': '22', 'option_d': '25', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'If DESK is coded as EFSL, then CHAIR is:', 'option_a': 'DIBJS', 'option_b': 'DIBJR', 'option_c': 'CIBJS', 'option_d': 'CIBJR', 'correct_answer': 'A'},
    {'category': 'reasoning', 'question_text': 'Complete: 7, 14, 28, 56, __', 'option_a': '84', 'option_b': '98', 'option_c': '112', 'option_d': '126', 'correct_answer': 'C'}
]

# Verbal Ability - 30 Questions
verbal_questions = [
    {'category': 'verbal', 'question_text': 'Synonym of HAPPY:', 'option_a': 'Sad', 'option_b': 'Joyful', 'option_c': 'Angry', 'option_d': 'Tired', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Antonym of DIFFICULT:', 'option_a': 'Hard', 'option_b': 'Tough', 'option_c': 'Easy', 'option_d': 'Complex', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Choose correct spelling:', 'option_a': 'Accomodate', 'option_b': 'Accommodate', 'option_c': 'Acomodate', 'option_d': 'Acommodate', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of BRAVE:', 'option_a': 'Coward', 'option_b': 'Fearful', 'option_c': 'Courageous', 'option_d': 'Weak', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Antonym of ANCIENT:', 'option_a': 'Old', 'option_b': 'Modern', 'option_c': 'Historic', 'option_d': 'Traditional', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Fill in the blank: She is good __ mathematics.', 'option_a': 'in', 'option_b': 'at', 'option_c': 'on', 'option_d': 'with', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of QUICK:', 'option_a': 'Slow', 'option_b': 'Fast', 'option_c': 'Lazy', 'option_d': 'Tired', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Antonym of BEAUTIFUL:', 'option_a': 'Pretty', 'option_b': 'Lovely', 'option_c': 'Ugly', 'option_d': 'Attractive', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Choose correct sentence:', 'option_a': 'He go to school', 'option_b': 'He goes to school', 'option_c': 'He going to school', 'option_d': 'He gone to school', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of INTELLIGENT:', 'option_a': 'Dumb', 'option_b': 'Smart', 'option_c': 'Foolish', 'option_d': 'Stupid', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Antonym of STRONG:', 'option_a': 'Powerful', 'option_b': 'Mighty', 'option_c': 'Weak', 'option_d': 'Robust', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Fill in: I have been waiting __ two hours.', 'option_a': 'since', 'option_b': 'for', 'option_c': 'from', 'option_d': 'at', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of LARGE:', 'option_a': 'Small', 'option_b': 'Tiny', 'option_c': 'Big', 'option_d': 'Little', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Antonym of RICH:', 'option_a': 'Wealthy', 'option_b': 'Poor', 'option_c': 'Affluent', 'option_d': 'Prosperous', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Choose correct: Neither of them __ present.', 'option_a': 'are', 'option_b': 'is', 'option_c': 'were', 'option_d': 'been', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of ANGRY:', 'option_a': 'Happy', 'option_b': 'Furious', 'option_c': 'Calm', 'option_d': 'Peaceful', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Antonym of HOT:', 'option_a': 'Warm', 'option_b': 'Burning', 'option_c': 'Cold', 'option_d': 'Heated', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Fill in: She is afraid __ dogs.', 'option_a': 'from', 'option_b': 'of', 'option_c': 'with', 'option_d': 'by', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of FAMOUS:', 'option_a': 'Unknown', 'option_b': 'Renowned', 'option_c': 'Obscure', 'option_d': 'Hidden', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Antonym of LOVE:', 'option_a': 'Like', 'option_b': 'Adore', 'option_c': 'Hate', 'option_d': 'Cherish', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Choose correct: The news __ good.', 'option_a': 'are', 'option_b': 'is', 'option_c': 'were', 'option_d': 'been', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of CLEAN:', 'option_a': 'Dirty', 'option_b': 'Spotless', 'option_c': 'Messy', 'option_d': 'Filthy', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Antonym of DARK:', 'option_a': 'Black', 'option_b': 'Dim', 'option_c': 'Light', 'option_d': 'Shadowy', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Fill in: He is senior __ me.', 'option_a': 'than', 'option_b': 'to', 'option_c': 'from', 'option_d': 'with', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of SMALL:', 'option_a': 'Large', 'option_b': 'Tiny', 'option_c': 'Big', 'option_d': 'Huge', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Antonym of EARLY:', 'option_a': 'Soon', 'option_b': 'Prompt', 'option_c': 'Late', 'option_d': 'Quick', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Choose correct: One of the boys __ absent.', 'option_a': 'are', 'option_b': 'is', 'option_c': 'were', 'option_d': 'been', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of QUIET:', 'option_a': 'Loud', 'option_b': 'Noisy', 'option_c': 'Silent', 'option_d': 'Boisterous', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Antonym of TRUE:', 'option_a': 'Correct', 'option_b': 'Right', 'option_c': 'False', 'option_d': 'Accurate', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Fill in: I am looking forward __ meeting you.', 'option_a': 'for', 'option_b': 'to', 'option_c': 'at', 'option_d': 'in', 'correct_answer': 'B'}
]

db.questions.insert_many(reasoning_questions)
db.questions.insert_many(verbal_questions)

print(f"✅ Inserted {len(reasoning_questions)} Logical Reasoning questions")
print(f"✅ Inserted {len(verbal_questions)} Verbal Ability questions")
