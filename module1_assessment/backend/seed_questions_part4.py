from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['placement_readiness_module1']

# Operating Systems - 30 Questions
os_questions = [
    {'category': 'os', 'question_text': 'Which is not an OS?', 'option_a': 'Windows', 'option_b': 'Linux', 'option_c': 'Oracle', 'option_d': 'macOS', 'correct_answer': 'C'},
    {'category': 'os', 'question_text': 'Process is:', 'option_a': 'Program in execution', 'option_b': 'Program on disk', 'option_c': 'Compiled code', 'option_d': 'Source code', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which scheduling algorithm is non-preemptive?', 'option_a': 'Round Robin', 'option_b': 'FCFS', 'option_c': 'Priority', 'option_d': 'Multilevel', 'correct_answer': 'B'},
    {'category': 'os', 'question_text': 'Deadlock occurs when:', 'option_a': 'Mutual exclusion', 'option_b': 'Hold and wait', 'option_c': 'No preemption', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Virtual memory uses:', 'option_a': 'RAM only', 'option_b': 'Disk only', 'option_c': 'RAM and Disk', 'option_d': 'Cache only', 'correct_answer': 'C'},
    {'category': 'os', 'question_text': 'Page fault occurs when:', 'option_a': 'Page is in memory', 'option_b': 'Page is not in memory', 'option_c': 'Page is deleted', 'option_d': 'Page is created', 'correct_answer': 'B'},
    {'category': 'os', 'question_text': 'Semaphore is used for:', 'option_a': 'Synchronization', 'option_b': 'Scheduling', 'option_c': 'Memory management', 'option_d': 'File management', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which is not a process state?', 'option_a': 'Ready', 'option_b': 'Running', 'option_c': 'Waiting', 'option_d': 'Sleeping', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Context switching is:', 'option_a': 'Switching between processes', 'option_b': 'Switching between threads', 'option_c': 'Switching between users', 'option_d': 'Both A and B', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Which is a memory allocation technique?', 'option_a': 'First Fit', 'option_b': 'Best Fit', 'option_c': 'Worst Fit', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Thrashing occurs when:', 'option_a': 'Too many page faults', 'option_b': 'Too few page faults', 'option_c': 'No page faults', 'option_d': 'Page is loaded', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which is not a file access method?', 'option_a': 'Sequential', 'option_b': 'Direct', 'option_c': 'Indexed', 'option_d': 'Parallel', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Kernel is:', 'option_a': 'Core of OS', 'option_b': 'Application', 'option_c': 'User interface', 'option_d': 'File system', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which is a real-time OS?', 'option_a': 'Windows', 'option_b': 'VxWorks', 'option_c': 'Ubuntu', 'option_d': 'macOS', 'correct_answer': 'B'},
    {'category': 'os', 'question_text': 'Spooling is used for:', 'option_a': 'CPU scheduling', 'option_b': 'I/O operations', 'option_c': 'Memory management', 'option_d': 'Process creation', 'correct_answer': 'B'},
    {'category': 'os', 'question_text': 'Which is not a deadlock prevention method?', 'option_a': 'Mutual exclusion', 'option_b': 'Hold and wait', 'option_c': 'Circular wait', 'option_d': 'Aging', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'PCB stands for:', 'option_a': 'Process Control Block', 'option_b': 'Program Control Block', 'option_c': 'Process Code Block', 'option_d': 'Program Code Block', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which scheduling gives minimum average waiting time?', 'option_a': 'FCFS', 'option_b': 'SJF', 'option_c': 'Round Robin', 'option_d': 'Priority', 'correct_answer': 'B'},
    {'category': 'os', 'question_text': 'Paging is a:', 'option_a': 'Memory management technique', 'option_b': 'Scheduling technique', 'option_c': 'File management technique', 'option_d': 'I/O technique', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which is not an IPC mechanism?', 'option_a': 'Pipe', 'option_b': 'Message Queue', 'option_c': 'Shared Memory', 'option_d': 'Cache', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Critical section is:', 'option_a': 'Code accessing shared resource', 'option_b': 'Code with errors', 'option_c': 'Code with loops', 'option_d': 'Code with functions', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which is a disk scheduling algorithm?', 'option_a': 'FCFS', 'option_b': 'SCAN', 'option_c': 'C-SCAN', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Fragmentation is of how many types?', 'option_a': '1', 'option_b': '2', 'option_c': '3', 'option_d': '4', 'correct_answer': 'B'},
    {'category': 'os', 'question_text': 'Which is not a thread type?', 'option_a': 'User thread', 'option_b': 'Kernel thread', 'option_c': 'Hybrid thread', 'option_d': 'Virtual thread', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Mutex is used for:', 'option_a': 'Mutual exclusion', 'option_b': 'Scheduling', 'option_c': 'Memory allocation', 'option_d': 'File access', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which is not a file attribute?', 'option_a': 'Name', 'option_b': 'Type', 'option_c': 'Size', 'option_d': 'Speed', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Interrupt is:', 'option_a': 'Signal to CPU', 'option_b': 'Error', 'option_c': 'Process', 'option_d': 'Thread', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which is a page replacement algorithm?', 'option_a': 'FIFO', 'option_b': 'LRU', 'option_c': 'Optimal', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Belady anomaly occurs in:', 'option_a': 'FIFO', 'option_b': 'LRU', 'option_c': 'Optimal', 'option_d': 'All', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which is not a system call?', 'option_a': 'fork()', 'option_b': 'exec()', 'option_c': 'wait()', 'option_d': 'print()', 'correct_answer': 'D'}
]

# Coding - 30 Questions
coding_questions = [
    {'category': 'coding', 'question_text': 'What is the output of: print(2 ** 3)?', 'option_a': '6', 'option_b': '8', 'option_c': '9', 'option_d': '5', 'correct_answer': 'B'},
    {'category': 'coding', 'question_text': 'Which loop is entry-controlled?', 'option_a': 'for', 'option_b': 'while', 'option_c': 'do-while', 'option_d': 'Both A and B', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Array index starts from:', 'option_a': '0', 'option_b': '1', 'option_c': '-1', 'option_d': 'Depends on language', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Which is not a data type?', 'option_a': 'int', 'option_b': 'float', 'option_c': 'char', 'option_d': 'loop', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Function returns:', 'option_a': 'Value', 'option_b': 'Nothing', 'option_c': 'Both A and B', 'option_d': 'Error', 'correct_answer': 'C'},
    {'category': 'coding', 'question_text': 'Which is a comparison operator?', 'option_a': '=', 'option_b': '==', 'option_c': '===', 'option_d': 'Both B and C', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Recursion uses:', 'option_a': 'Stack', 'option_b': 'Queue', 'option_c': 'Array', 'option_d': 'List', 'correct_answer': 'A'},
    {'category': 'coding', 'question_text': 'Which is not a loop?', 'option_a': 'for', 'option_b': 'while', 'option_c': 'if', 'option_d': 'do-while', 'correct_answer': 'C'},
    {'category': 'coding', 'question_text': 'String is:', 'option_a': 'Mutable', 'option_b': 'Immutable', 'option_c': 'Both', 'option_d': 'Depends on language', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Which is a logical operator?', 'option_a': 'AND', 'option_b': 'OR', 'option_c': 'NOT', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Exception handling uses:', 'option_a': 'try-catch', 'option_b': 'if-else', 'option_c': 'switch', 'option_d': 'loop', 'correct_answer': 'A'},
    {'category': 'coding', 'question_text': 'Which is not a programming paradigm?', 'option_a': 'OOP', 'option_b': 'Functional', 'option_c': 'Procedural', 'option_d': 'Sequential', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Variable scope can be:', 'option_a': 'Local', 'option_b': 'Global', 'option_c': 'Both A and B', 'option_d': 'None', 'correct_answer': 'C'},
    {'category': 'coding', 'question_text': 'Which is a conditional statement?', 'option_a': 'if', 'option_b': 'switch', 'option_c': 'Both A and B', 'option_d': 'for', 'correct_answer': 'C'},
    {'category': 'coding', 'question_text': 'Pointer stores:', 'option_a': 'Value', 'option_b': 'Address', 'option_c': 'Both', 'option_d': 'None', 'correct_answer': 'B'},
    {'category': 'coding', 'question_text': 'Which is not an OOP concept?', 'option_a': 'Encapsulation', 'option_b': 'Inheritance', 'option_c': 'Polymorphism', 'option_d': 'Compilation', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Constructor is called when:', 'option_a': 'Object is created', 'option_b': 'Object is destroyed', 'option_c': 'Method is called', 'option_d': 'Class is defined', 'correct_answer': 'A'},
    {'category': 'coding', 'question_text': 'Which is a bitwise operator?', 'option_a': '&', 'option_b': '|', 'option_c': '^', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Static variable is:', 'option_a': 'Shared by all instances', 'option_b': 'Unique to each instance', 'option_c': 'Local to function', 'option_d': 'None', 'correct_answer': 'A'},
    {'category': 'coding', 'question_text': 'Which is not a sorting algorithm?', 'option_a': 'Bubble Sort', 'option_b': 'Quick Sort', 'option_c': 'Merge Sort', 'option_d': 'Linear Sort', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Time complexity of linear search is:', 'option_a': 'O(1)', 'option_b': 'O(n)', 'option_c': 'O(log n)', 'option_d': 'O(n²)', 'correct_answer': 'B'},
    {'category': 'coding', 'question_text': 'Which is a searching algorithm?', 'option_a': 'Binary Search', 'option_b': 'Linear Search', 'option_c': 'Both A and B', 'option_d': 'None', 'correct_answer': 'C'},
    {'category': 'coding', 'question_text': 'Abstract class can have:', 'option_a': 'Abstract methods', 'option_b': 'Concrete methods', 'option_c': 'Both A and B', 'option_d': 'None', 'correct_answer': 'C'},
    {'category': 'coding', 'question_text': 'Interface can have:', 'option_a': 'Only abstract methods', 'option_b': 'Only concrete methods', 'option_c': 'Both', 'option_d': 'Depends on language', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Which is not a collection?', 'option_a': 'List', 'option_b': 'Set', 'option_c': 'Map', 'option_d': 'Loop', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Garbage collection is:', 'option_a': 'Automatic memory management', 'option_b': 'Manual memory management', 'option_c': 'Error handling', 'option_d': 'None', 'correct_answer': 'A'},
    {'category': 'coding', 'question_text': 'Which is a wrapper class?', 'option_a': 'Integer', 'option_b': 'Float', 'option_c': 'Boolean', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Method overloading is:', 'option_a': 'Same name, different parameters', 'option_b': 'Different name, same parameters', 'option_c': 'Same name, same parameters', 'option_d': 'None', 'correct_answer': 'A'},
    {'category': 'coding', 'question_text': 'Method overriding is:', 'option_a': 'In same class', 'option_b': 'In parent-child class', 'option_c': 'In interface', 'option_d': 'None', 'correct_answer': 'B'},
    {'category': 'coding', 'question_text': 'Which is not a access modifier?', 'option_a': 'public', 'option_b': 'private', 'option_c': 'protected', 'option_d': 'hidden', 'correct_answer': 'D'}
]

db.questions.insert_many(os_questions)
db.questions.insert_many(coding_questions)

print(f"✅ Inserted {len(os_questions)} Operating Systems questions")
print(f"✅ Inserted {len(coding_questions)} Coding questions")
print("\n🎯 Total questions inserted so far: 210")
