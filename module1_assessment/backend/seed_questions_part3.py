from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['placement_readiness_module1']

# DBMS - 30 Questions
dbms_questions = [
    {'category': 'dbms', 'question_text': 'What does DBMS stand for?', 'option_a': 'Data Base Management System', 'option_b': 'Database Management Software', 'option_c': 'Data Binary Management System', 'option_d': 'Database Manipulation System', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which SQL command is used to retrieve data?', 'option_a': 'GET', 'option_b': 'SELECT', 'option_c': 'RETRIEVE', 'option_d': 'FETCH', 'correct_answer': 'B'},
    {'category': 'dbms', 'question_text': 'Primary key must be:', 'option_a': 'Unique', 'option_b': 'Null', 'option_c': 'Duplicate', 'option_d': 'Optional', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which is not a DDL command?', 'option_a': 'CREATE', 'option_b': 'ALTER', 'option_c': 'SELECT', 'option_d': 'DROP', 'correct_answer': 'C'},
    {'category': 'dbms', 'question_text': 'Foreign key is used for:', 'option_a': 'Uniqueness', 'option_b': 'Referential integrity', 'option_c': 'Indexing', 'option_d': 'Sorting', 'correct_answer': 'B'},
    {'category': 'dbms', 'question_text': 'Which normal form removes transitive dependency?', 'option_a': '1NF', 'option_b': '2NF', 'option_c': '3NF', 'option_d': 'BCNF', 'correct_answer': 'C'},
    {'category': 'dbms', 'question_text': 'ACID properties include:', 'option_a': 'Atomicity', 'option_b': 'Consistency', 'option_c': 'Isolation', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'dbms', 'question_text': 'Which command is used to delete a table?', 'option_a': 'DELETE', 'option_b': 'REMOVE', 'option_c': 'DROP', 'option_d': 'TRUNCATE', 'correct_answer': 'C'},
    {'category': 'dbms', 'question_text': 'JOIN is used to:', 'option_a': 'Combine rows from tables', 'option_b': 'Delete rows', 'option_c': 'Update rows', 'option_d': 'Create tables', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which is not a type of JOIN?', 'option_a': 'INNER JOIN', 'option_b': 'OUTER JOIN', 'option_c': 'CROSS JOIN', 'option_d': 'PARALLEL JOIN', 'correct_answer': 'D'},
    {'category': 'dbms', 'question_text': 'Index is used for:', 'option_a': 'Faster retrieval', 'option_b': 'Data storage', 'option_c': 'Data deletion', 'option_d': 'Data backup', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which is a DML command?', 'option_a': 'CREATE', 'option_b': 'INSERT', 'option_c': 'ALTER', 'option_d': 'DROP', 'correct_answer': 'B'},
    {'category': 'dbms', 'question_text': 'Candidate key is:', 'option_a': 'Minimal superkey', 'option_b': 'Foreign key', 'option_c': 'Composite key', 'option_d': 'Alternate key', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which clause is used with SELECT to filter?', 'option_a': 'FILTER', 'option_b': 'WHERE', 'option_c': 'HAVING', 'option_d': 'CONDITION', 'correct_answer': 'B'},
    {'category': 'dbms', 'question_text': 'GROUP BY is used with:', 'option_a': 'Aggregate functions', 'option_b': 'JOIN', 'option_c': 'INDEX', 'option_d': 'VIEW', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which is not an aggregate function?', 'option_a': 'COUNT', 'option_b': 'SUM', 'option_c': 'AVG', 'option_d': 'SELECT', 'correct_answer': 'D'},
    {'category': 'dbms', 'question_text': 'Transaction ends with:', 'option_a': 'COMMIT or ROLLBACK', 'option_b': 'START', 'option_c': 'BEGIN', 'option_d': 'END', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'View is a:', 'option_a': 'Physical table', 'option_b': 'Virtual table', 'option_c': 'Index', 'option_d': 'Key', 'correct_answer': 'B'},
    {'category': 'dbms', 'question_text': 'Which key can have NULL values?', 'option_a': 'Primary key', 'option_b': 'Foreign key', 'option_c': 'Candidate key', 'option_d': 'Super key', 'correct_answer': 'B'},
    {'category': 'dbms', 'question_text': 'Normalization is used to:', 'option_a': 'Reduce redundancy', 'option_b': 'Increase redundancy', 'option_c': 'Delete data', 'option_d': 'Backup data', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which is not a constraint?', 'option_a': 'NOT NULL', 'option_b': 'UNIQUE', 'option_c': 'CHECK', 'option_d': 'VERIFY', 'correct_answer': 'D'},
    {'category': 'dbms', 'question_text': 'TRUNCATE command:', 'option_a': 'Deletes all rows', 'option_b': 'Deletes table structure', 'option_c': 'Updates rows', 'option_d': 'Creates table', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which isolation level is highest?', 'option_a': 'READ UNCOMMITTED', 'option_b': 'READ COMMITTED', 'option_c': 'REPEATABLE READ', 'option_d': 'SERIALIZABLE', 'correct_answer': 'D'},
    {'category': 'dbms', 'question_text': 'Deadlock occurs when:', 'option_a': 'Two transactions wait for each other', 'option_b': 'Transaction commits', 'option_c': 'Transaction rolls back', 'option_d': 'Database starts', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which is not a database model?', 'option_a': 'Relational', 'option_b': 'Hierarchical', 'option_c': 'Network', 'option_d': 'Sequential', 'correct_answer': 'D'},
    {'category': 'dbms', 'question_text': 'ER diagram stands for:', 'option_a': 'Entity Relationship', 'option_b': 'Entity Record', 'option_c': 'Entry Relationship', 'option_d': 'Entry Record', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Cardinality refers to:', 'option_a': 'Number of rows', 'option_b': 'Number of columns', 'option_c': 'Number of tables', 'option_d': 'Number of databases', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which command saves changes?', 'option_a': 'SAVE', 'option_b': 'COMMIT', 'option_c': 'STORE', 'option_d': 'PERSIST', 'correct_answer': 'B'},
    {'category': 'dbms', 'question_text': 'Stored procedure is:', 'option_a': 'Precompiled SQL code', 'option_b': 'Table', 'option_c': 'Index', 'option_d': 'View', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which is fastest to retrieve data?', 'option_a': 'Full table scan', 'option_b': 'Index scan', 'option_c': 'Sequential scan', 'option_d': 'Random scan', 'correct_answer': 'B'}
]

# Computer Networks - 30 Questions
cn_questions = [
    {'category': 'cn', 'question_text': 'OSI model has how many layers?', 'option_a': '5', 'option_b': '6', 'option_c': '7', 'option_d': '8', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'Which layer is responsible for routing?', 'option_a': 'Physical', 'option_b': 'Data Link', 'option_c': 'Network', 'option_d': 'Transport', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'TCP is a:', 'option_a': 'Connection-oriented protocol', 'option_b': 'Connectionless protocol', 'option_c': 'Physical layer protocol', 'option_d': 'Application protocol', 'correct_answer': 'A'},
    {'category': 'cn', 'question_text': 'IP address version 4 is:', 'option_a': '16-bit', 'option_b': '32-bit', 'option_c': '64-bit', 'option_d': '128-bit', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Which protocol is used for email?', 'option_a': 'HTTP', 'option_b': 'FTP', 'option_c': 'SMTP', 'option_d': 'DNS', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'Default port for HTTP is:', 'option_a': '21', 'option_b': '22', 'option_c': '80', 'option_d': '443', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'MAC address is:', 'option_a': '32-bit', 'option_b': '48-bit', 'option_c': '64-bit', 'option_d': '128-bit', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Which device works at Network layer?', 'option_a': 'Hub', 'option_b': 'Switch', 'option_c': 'Router', 'option_d': 'Repeater', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'DNS stands for:', 'option_a': 'Domain Name System', 'option_b': 'Domain Network System', 'option_c': 'Data Name System', 'option_d': 'Data Network System', 'correct_answer': 'A'},
    {'category': 'cn', 'question_text': 'Which is not a network topology?', 'option_a': 'Star', 'option_b': 'Ring', 'option_c': 'Bus', 'option_d': 'Square', 'correct_answer': 'D'},
    {'category': 'cn', 'question_text': 'FTP uses which port?', 'option_a': '20', 'option_b': '21', 'option_c': '22', 'option_d': '23', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Which protocol is connectionless?', 'option_a': 'TCP', 'option_b': 'UDP', 'option_c': 'HTTP', 'option_d': 'FTP', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Subnet mask is used for:', 'option_a': 'Network identification', 'option_b': 'Host identification', 'option_c': 'Both A and B', 'option_d': 'None', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'Which layer handles encryption?', 'option_a': 'Physical', 'option_b': 'Data Link', 'option_c': 'Presentation', 'option_d': 'Application', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'HTTPS uses port:', 'option_a': '80', 'option_b': '443', 'option_c': '8080', 'option_d': '8443', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Which is a private IP range?', 'option_a': '192.168.x.x', 'option_b': '8.8.8.8', 'option_c': '1.1.1.1', 'option_d': '4.4.4.4', 'correct_answer': 'A'},
    {'category': 'cn', 'question_text': 'ARP stands for:', 'option_a': 'Address Resolution Protocol', 'option_b': 'Address Routing Protocol', 'option_c': 'Application Resolution Protocol', 'option_d': 'Application Routing Protocol', 'correct_answer': 'A'},
    {'category': 'cn', 'question_text': 'Which device works at Data Link layer?', 'option_a': 'Hub', 'option_b': 'Switch', 'option_c': 'Router', 'option_d': 'Gateway', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Ping uses which protocol?', 'option_a': 'TCP', 'option_b': 'UDP', 'option_c': 'ICMP', 'option_d': 'HTTP', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'Which is not a routing protocol?', 'option_a': 'RIP', 'option_b': 'OSPF', 'option_c': 'BGP', 'option_d': 'HTTP', 'correct_answer': 'D'},
    {'category': 'cn', 'question_text': 'Bandwidth is measured in:', 'option_a': 'Bytes', 'option_b': 'Bits per second', 'option_c': 'Packets', 'option_d': 'Frames', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Which is a connection-oriented protocol?', 'option_a': 'UDP', 'option_b': 'IP', 'option_c': 'TCP', 'option_d': 'ICMP', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'NAT stands for:', 'option_a': 'Network Address Translation', 'option_b': 'Network Application Translation', 'option_c': 'Node Address Translation', 'option_d': 'Node Application Translation', 'correct_answer': 'A'},
    {'category': 'cn', 'question_text': 'Which layer is closest to user?', 'option_a': 'Physical', 'option_b': 'Network', 'option_c': 'Transport', 'option_d': 'Application', 'correct_answer': 'D'},
    {'category': 'cn', 'question_text': 'Firewall works at which layer?', 'option_a': 'Physical', 'option_b': 'Network', 'option_c': 'Transport', 'option_d': 'All layers', 'correct_answer': 'D'},
    {'category': 'cn', 'question_text': 'Which protocol is used for file transfer?', 'option_a': 'HTTP', 'option_b': 'FTP', 'option_c': 'SMTP', 'option_d': 'DNS', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Loopback address is:', 'option_a': '192.168.1.1', 'option_b': '127.0.0.1', 'option_c': '10.0.0.1', 'option_d': '172.16.0.1', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Which is not a network device?', 'option_a': 'Router', 'option_b': 'Switch', 'option_c': 'Hub', 'option_d': 'Compiler', 'correct_answer': 'D'},
    {'category': 'cn', 'question_text': 'DHCP is used for:', 'option_a': 'Dynamic IP allocation', 'option_b': 'Static IP allocation', 'option_c': 'DNS resolution', 'option_d': 'Routing', 'correct_answer': 'A'},
    {'category': 'cn', 'question_text': 'Which protocol is secure?', 'option_a': 'HTTP', 'option_b': 'FTP', 'option_c': 'HTTPS', 'option_d': 'Telnet', 'correct_answer': 'C'}
]

db.questions.insert_many(dbms_questions)
db.questions.insert_many(cn_questions)

print(f"✅ Inserted {len(dbms_questions)} DBMS questions")
print(f"✅ Inserted {len(cn_questions)} Computer Networks questions")
