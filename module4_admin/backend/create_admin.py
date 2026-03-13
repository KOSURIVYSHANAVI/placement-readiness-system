from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['placement_readiness_module4']

admin = {
    'name': 'Admin',
    'email': 'admin@placement.com',
    'password': generate_password_hash('admin123'),
    'created_at': datetime.utcnow()
}

db.admins.insert_one(admin)
print("✅ Admin created successfully!")
print("Email: admin@placement.com")
print("Password: admin123")
