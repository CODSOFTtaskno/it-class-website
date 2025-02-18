from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
COURSE_LIST = [

    {
        'id': 1,
        'name': 'Introduction to Programming',
        'description': 'Learn the basics of programming with Python.',
        'duration': '8 weeks'
    },
    {
        'id': 2,
        'name': 'Web Development',
        'description': 'Build modern websites using HTML, CSS, and JavaScript.',
        'duration': '12 weeks'
    },
    {
        'id': 3,
        'name': 'Database Management',
        'description': 'Understand databases and SQL.',
        'duration': '10 weeks'
    },
    {
        'id': 4,
        'name': 'Data Science & AI',
        'description': 'Explore data science techniques, machine learning, and artificial intelligence concepts.',
        'duration': '16 weeks'
    },
    {
        'id': 5,
        'name': 'Python Development',
        'description': 'Learn the basics of programming with Python and build foundational skills for software development.',
        'duration': '8 weeks'
    },
    {
        'id': 6,
        'name': 'Java Development',
        'description': 'Master core Java programming concepts, object-oriented programming, and application development.',
        'duration': '10 weeks'
    },
    {
        'id': 7,
        'name': 'Full Stack Development',
        'description': 'Learn to build complete web applications, covering both front-end and back-end technologies.',
        'duration': '16 weeks'
    },
    {
        'id': 8,
        'name': 'Data Science',
        'description': 'Learn key data science techniques, including data cleaning, exploratory data analysis, and machine learning algorithms.',
        'duration': '14 weeks'
    }
]

@app.route('/')
def home():
    return render_template('home.html', title="Home")

@app.route('/courses')
def courses():
    return render_template('courses.html', title="Courses", courses=COURSE_LIST)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(f"Received contact form submission: Name: {name}, Email: {email}, Message: {message}")
        return redirect(url_for('home'))
    return render_template('contact.html', title="Contact")
@app.route('/enroll/<int:course_id>', methods=['GET', 'POST'])
def enroll(course_id):
    course = next((c for c in COURSE_LIST if c['id'] == course_id), None)
    if not course:
        return "Course not found", 404
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        print(f"Enrollment received: Name: {name}, Email: {email}, Course: {course['name']}")
        return redirect(url_for('enrollment_success'))

    return render_template('enroll.html', course=course)
@app.route('/enrollment_success')
def enrollment_success():
    return render_template('enrollment_success.html')

if __name__ == '__main__':
    app.run(debug=True)
