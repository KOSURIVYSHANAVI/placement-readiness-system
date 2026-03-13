from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['placement_readiness_module1']

# DSA (Data Structures & Algorithms) - 30 Questions
dsa_questions = [
    {'category': 'dsa', 'question_text': 'Time complexity of binary search is:', 'option_a': 'O(n)', 'option_b': 'O(log n)', 'option_c': 'O(n²)', 'option_d': 'O(1)', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Which data structure uses LIFO?', 'option_a': 'Queue', 'option_b': 'Stack', 'option_c': 'Tree', 'option_d': 'Graph', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Which data structure uses FIFO?', 'option_a': 'Stack', 'option_b': 'Queue', 'option_c': 'Tree', 'option_d': 'Graph', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Array elements are stored in:', 'option_a': 'Contiguous memory', 'option_b': 'Random memory', 'option_c': 'Heap', 'option_d': 'Stack', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Linked list node contains:', 'option_a': 'Data only', 'option_b': 'Pointer only', 'option_c': 'Data and pointer', 'option_d': 'None', 'correct_answer': 'C'},
    {'category': 'dsa', 'question_text': 'Time complexity of insertion in array at end is:', 'option_a': 'O(1)', 'option_b': 'O(n)', 'option_c': 'O(log n)', 'option_d': 'O(n²)', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Which is not a tree traversal?', 'option_a': 'Inorder', 'option_b': 'Preorder', 'option_c': 'Postorder', 'option_d': 'Sideorder', 'correct_answer': 'D'},
    {'category': 'dsa', 'question_text': 'Binary tree has maximum how many children?', 'option_a': '1', 'option_b': '2', 'option_c': '3', 'option_d': 'Unlimited', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'BST stands for:', 'option_a': 'Binary Search Tree', 'option_b': 'Best Search Tree', 'option_c': 'Binary Sort Tree', 'option_d': 'Basic Search Tree', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Hash table uses:', 'option_a': 'Hash function', 'option_b': 'Sort function', 'option_c': 'Search function', 'option_d': 'None', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Time complexity of bubble sort is:', 'option_a': 'O(n)', 'option_b': 'O(n log n)', 'option_c': 'O(n²)', 'option_d': 'O(log n)', 'correct_answer': 'C'},
    {'category': 'dsa', 'question_text': 'Quick sort uses:', 'option_a': 'Divide and conquer', 'option_b': 'Greedy', 'option_c': 'Dynamic programming', 'option_d': 'Backtracking', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Merge sort time complexity is:', 'option_a': 'O(n)', 'option_b': 'O(n log n)', 'option_c': 'O(n²)', 'option_d': 'O(log n)', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Heap is a:', 'option_a': 'Complete binary tree', 'option_b': 'Incomplete binary tree', 'option_c': 'Graph', 'option_d': 'List', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'DFS uses:', 'option_a': 'Stack', 'option_b': 'Queue', 'option_c': 'Array', 'option_d': 'Tree', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'BFS uses:', 'option_a': 'Stack', 'option_b': 'Queue', 'option_c': 'Array', 'option_d': 'Tree', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Graph can be represented using:', 'option_a': 'Adjacency matrix', 'option_b': 'Adjacency list', 'option_c': 'Both A and B', 'option_d': 'None', 'correct_answer': 'C'},
    {'category': 'dsa', 'question_text': 'Dijkstra algorithm is used for:', 'option_a': 'Shortest path', 'option_b': 'Longest path', 'option_c': 'Sorting', 'option_d': 'Searching', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'AVL tree is:', 'option_a': 'Balanced BST', 'option_b': 'Unbalanced BST', 'option_c': 'Binary tree', 'option_d': 'Graph', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Trie is used for:', 'option_a': 'String operations', 'option_b': 'Number operations', 'option_c': 'Sorting', 'option_d': 'Searching', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Priority queue can be implemented using:', 'option_a': 'Heap', 'option_b': 'Array', 'option_c': 'Linked list', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'dsa', 'question_text': 'Circular queue overcomes:', 'option_a': 'Memory wastage', 'option_b': 'Time complexity', 'option_c': 'Space complexity', 'option_d': 'None', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Doubly linked list has:', 'option_a': 'One pointer', 'option_b': 'Two pointers', 'option_c': 'Three pointers', 'option_d': 'No pointer', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Recursion uses which data structure internally?', 'option_a': 'Queue', 'option_b': 'Stack', 'option_c': 'Array', 'option_d': 'Tree', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Dynamic programming uses:', 'option_a': 'Memoization', 'option_b': 'Tabulation', 'option_c': 'Both A and B', 'option_d': 'None', 'correct_answer': 'C'},
    {'category': 'dsa', 'question_text': 'Greedy algorithm always gives:', 'option_a': 'Optimal solution', 'option_b': 'Local optimal solution', 'option_c': 'No solution', 'option_d': 'Wrong solution', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Space complexity of recursive fibonacci is:', 'option_a': 'O(1)', 'option_b': 'O(n)', 'option_c': 'O(log n)', 'option_d': 'O(n²)', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Which is not a graph algorithm?', 'option_a': 'Dijkstra', 'option_b': 'Bellman-Ford', 'option_c': 'Floyd-Warshall', 'option_d': 'Bubble Sort', 'correct_answer': 'D'},
    {'category': 'dsa', 'question_text': 'Topological sort is used in:', 'option_a': 'DAG', 'option_b': 'Cyclic graph', 'option_c': 'Tree', 'option_d': 'Array', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Kruskal algorithm is used for:', 'option_a': 'Minimum spanning tree', 'option_b': 'Maximum spanning tree', 'option_c': 'Shortest path', 'option_d': 'Sorting', 'correct_answer': 'A'}
]

# Python Programming - 30 Questions
python_questions = [
    {'category': 'python', 'question_text': 'Python is:', 'option_a': 'Compiled', 'option_b': 'Interpreted', 'option_c': 'Both', 'option_d': 'None', 'correct_answer': 'B'},
    {'category': 'python', 'question_text': 'Which is not a Python data type?', 'option_a': 'list', 'option_b': 'tuple', 'option_c': 'array', 'option_d': 'dict', 'correct_answer': 'C'},
    {'category': 'python', 'question_text': 'List is:', 'option_a': 'Mutable', 'option_b': 'Immutable', 'option_c': 'Both', 'option_d': 'None', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Tuple is:', 'option_a': 'Mutable', 'option_b': 'Immutable', 'option_c': 'Both', 'option_d': 'None', 'correct_answer': 'B'},
    {'category': 'python', 'question_text': 'Dictionary stores data as:', 'option_a': 'Key-value pairs', 'option_b': 'Only values', 'option_c': 'Only keys', 'option_d': 'Array', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which keyword is used to define a function?', 'option_a': 'function', 'option_b': 'def', 'option_c': 'func', 'option_d': 'define', 'correct_answer': 'B'},
    {'category': 'python', 'question_text': 'Python file extension is:', 'option_a': '.py', 'option_b': '.python', 'option_c': '.pt', 'option_d': '.p', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is used for comments?', 'option_a': '//', 'option_b': '/* */', 'option_c': '#', 'option_d': '--', 'correct_answer': 'C'},
    {'category': 'python', 'question_text': 'Range(5) generates:', 'option_a': '1,2,3,4,5', 'option_b': '0,1,2,3,4', 'option_c': '0,1,2,3,4,5', 'option_d': '1,2,3,4', 'correct_answer': 'B'},
    {'category': 'python', 'question_text': 'Which is not a loop in Python?', 'option_a': 'for', 'option_b': 'while', 'option_c': 'do-while', 'option_d': 'None', 'correct_answer': 'C'},
    {'category': 'python', 'question_text': 'Lambda function is:', 'option_a': 'Anonymous function', 'option_b': 'Named function', 'option_c': 'Class', 'option_d': 'Module', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is used to handle exceptions?', 'option_a': 'try-except', 'option_b': 'if-else', 'option_c': 'switch', 'option_d': 'loop', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Self keyword is used in:', 'option_a': 'Functions', 'option_b': 'Classes', 'option_c': 'Loops', 'option_d': 'Conditions', 'correct_answer': 'B'},
    {'category': 'python', 'question_text': '__init__ is:', 'option_a': 'Constructor', 'option_b': 'Destructor', 'option_c': 'Method', 'option_d': 'Variable', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is not a Python framework?', 'option_a': 'Django', 'option_b': 'Flask', 'option_c': 'FastAPI', 'option_d': 'React', 'correct_answer': 'D'},
    {'category': 'python', 'question_text': 'Pip is used for:', 'option_a': 'Package management', 'option_b': 'Compilation', 'option_c': 'Debugging', 'option_d': 'Testing', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is used to import modules?', 'option_a': 'include', 'option_b': 'import', 'option_c': 'require', 'option_d': 'use', 'correct_answer': 'B'},
    {'category': 'python', 'question_text': 'List comprehension syntax is:', 'option_a': '[x for x in range(5)]', 'option_b': '{x for x in range(5)}', 'option_c': '(x for x in range(5))', 'option_d': 'All', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is not a string method?', 'option_a': 'upper()', 'option_b': 'lower()', 'option_c': 'split()', 'option_d': 'push()', 'correct_answer': 'D'},
    {'category': 'python', 'question_text': 'Len() function returns:', 'option_a': 'Length', 'option_b': 'Size', 'option_c': 'Count', 'option_d': 'All', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is used for type conversion?', 'option_a': 'int()', 'option_b': 'str()', 'option_c': 'float()', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'python', 'question_text': 'None is:', 'option_a': 'Null value', 'option_b': 'Zero', 'option_c': 'Empty string', 'option_d': 'False', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is not a comparison operator?', 'option_a': '==', 'option_b': '!=', 'option_c': '=', 'option_d': '>=', 'correct_answer': 'C'},
    {'category': 'python', 'question_text': 'Global keyword is used to:', 'option_a': 'Access global variable', 'option_b': 'Create global variable', 'option_c': 'Modify global variable', 'option_d': 'All', 'correct_answer': 'D'},
    {'category': 'python', 'question_text': 'Which is used for file handling?', 'option_a': 'open()', 'option_b': 'read()', 'option_c': 'write()', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'python', 'question_text': 'Inheritance is implemented using:', 'option_a': 'class Child(Parent):', 'option_b': 'class Child extends Parent:', 'option_c': 'class Child inherits Parent:', 'option_d': 'None', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is not a Python keyword?', 'option_a': 'pass', 'option_b': 'break', 'option_c': 'continue', 'option_d': 'exit', 'correct_answer': 'D'},
    {'category': 'python', 'question_text': 'Decorator is denoted by:', 'option_a': '@', 'option_b': '#', 'option_c': '$', 'option_d': '%', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is used for multiple inheritance?', 'option_a': 'class Child(Parent1, Parent2):', 'option_b': 'class Child extends Parent1, Parent2:', 'option_c': 'class Child inherits Parent1, Parent2:', 'option_d': 'None', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Yield keyword is used in:', 'option_a': 'Generators', 'option_b': 'Functions', 'option_c': 'Classes', 'option_d': 'Loops', 'correct_answer': 'A'}
]

db.questions.insert_many(dsa_questions)
db.questions.insert_many(python_questions)

print(f"✅ Inserted {len(dsa_questions)} DSA questions")
print(f"✅ Inserted {len(python_questions)} Python questions")
print("\n🎉 DSA and Python questions added successfully!")
print("Total new questions: 60")
