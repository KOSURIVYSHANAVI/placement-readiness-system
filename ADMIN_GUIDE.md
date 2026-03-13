# ADMIN PANEL QUICK GUIDE 🎯

## Login Credentials
- **Email:** admin@placement.com
- **Password:** admin123

## Admin Panel Features

### 1️⃣ Overview Tab
View system statistics:
- Total students registered
- Total tests completed
- Total questions in database
- Average student performance

### 2️⃣ Add Question Tab
Add new questions to any subject:
1. Select subject category from dropdown
2. Enter question text
3. Fill in options A, B, C, D
4. Select correct answer
5. Click "Add Question"

**Question Count Display:**
- Green background = 30+ questions (ready)
- Yellow background = Less than 30 questions (needs more)

### 3️⃣ Add Subject Tab
Create new subjects:
1. Enter subject key (lowercase, e.g., 'java')
2. Enter subject name (e.g., 'Java Programming')
3. Add emoji icon (e.g., ☕)
4. Click "Add Subject"

**Note:** After adding a new subject, you must manually update `AssessmentDashboard.jsx` to display it in the student interface.

### 4️⃣ Add Career Path Tab
Create learning roadmaps:
1. Select category from dropdown
2. Enter career path title
3. Add description
4. List learning resources
5. Set duration (e.g., '4 weeks')
6. Click "Add Career Path"

**View Existing Paths:**
- All career paths are displayed below the form
- Shows category, duration, description, and resources

### 5️⃣ Students Tab
Monitor student progress:
- View all registered students
- See number of tests taken
- Check average scores
- Green score = Ready (≥70%)
- Red score = Needs improvement (<70%)

---

## Quick Actions

### To Add 30 Questions to a Subject:
1. Go to "Add Question" tab
2. Check current question count
3. Add questions until count reaches 30
4. Green indicator shows subject is ready

### To Create a New Subject:
1. Go to "Add Subject" tab
2. Fill in key, name, and icon
3. Submit form
4. Go to "Add Question" tab
5. Add 30 questions for the new subject
6. Update AssessmentDashboard.jsx manually

### To Add Career Guidance:
1. Go to "Add Career Path" tab
2. Select relevant subject category
3. Fill in all fields
4. Submit form
5. Students will see this in Career Guidance section

---

## Tips
- Always add at least 30 questions per subject
- Use clear, concise question text
- Provide helpful resources in career paths
- Monitor student progress regularly
- Check question counts before launching new subjects

---

## Need Help?
- Check CHANGES_SUMMARY.md for technical details
- Review backend API endpoints in admin_api.py
- Frontend code in AdminManagement.jsx
