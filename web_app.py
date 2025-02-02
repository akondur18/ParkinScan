from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime, timedelta
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a real secret key in production

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Dummy user class and database for demonstration
class User(UserMixin):
    def __init__(self, id):
        self.id = id

users = {'user@example.com': {'password': 'password123'}}

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email]['password'] == password:
            user = User(email)
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        flash('Invalid email or password', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users:
            flash('Email already registered', 'danger')
        else:
            users[email] = {'password': password}
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    # Dummy data for demonstration
    sleep_quality = random.randint(60, 95)
    exercise_progress = random.randint(40, 100)
    mood_level = random.randint(50, 90)
    
    upcoming_activities = [
        {'name': 'Morning Walk', 'time': '8:00 AM'},
        {'name': 'Speech Therapy', 'time': '10:30 AM'},
        {'name': 'Medication', 'time': '1:00 PM'}
    ]
    
    # Generate dummy data for charts
    dates = [(datetime.now() - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(7)]
    dates.reverse()
    
    speech_data = {
        'dates': dates,
        'scores': [random.randint(60, 95) for _ in range(7)]
    }
    
    sleep_data = {
        'dates': dates,
        'quality': [random.randint(50, 100) for _ in range(7)]
    }
    
    recommendations = {
        'Exercise': [
            'Take a 20-minute walk in the morning',
            'Do gentle stretching exercises',
            'Practice balance exercises'
        ],
        'Sleep': [
            'Maintain a consistent sleep schedule',
            'Create a relaxing bedtime routine',
            'Avoid screens before bedtime'
        ],
        'Mental Health': [
            'Practice deep breathing exercises',
            'Engage in a hobby you enjoy',
            'Connect with friends or family'
        ]
    }
    
    return render_template('dashboard.html',
                         sleep_quality=sleep_quality,
                         exercise_progress=exercise_progress,
                         mood_level=mood_level,
                         upcoming_activities=upcoming_activities,
                         speech_data=speech_data,
                         sleep_data=sleep_data,
                         recommendations=recommendations)

@app.route('/exercise')
@login_required
def exercise():
    exercises = {
        'Balance': [
            {'name': 'Single-Leg Stand', 'duration': '30 seconds each side', 'notes': 'Stand near a wall or chair for support'},
            {'name': 'Heel-to-Toe Walk', 'duration': '1 minute', 'notes': 'Walk in a straight line'},
            {'name': 'Sit-to-Stand', 'duration': '10 repetitions', 'notes': 'Use chair arms if needed'}
        ],
        'Flexibility': [
            {'name': 'Shoulder Rolls', 'duration': '10 repetitions', 'notes': 'Rotate shoulders forward and backward'},
            {'name': 'Neck Stretches', 'duration': '5 each direction', 'notes': 'Gentle movements only'},
            {'name': 'Ankle Circles', 'duration': '10 each foot', 'notes': 'Rotate in both directions'}
        ],
        'Strength': [
            {'name': 'Wall Push-ups', 'duration': '10 repetitions', 'notes': 'Keep body straight'},
            {'name': 'Chair Squats', 'duration': '10 repetitions', 'notes': 'Use chair for support'},
            {'name': 'Toe Raises', 'duration': '15 repetitions', 'notes': 'Hold onto counter for balance'}
        ]
    }
    
    progress = {
        'dates': [(datetime.now() - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(7)][::-1],
        'minutes': [random.randint(15, 45) for _ in range(7)],
        'completed': [random.randint(3, 8) for _ in range(7)]
    }
    
    return render_template('exercise.html', exercises=exercises, progress=progress)

@app.route('/api/exercise/start', methods=['POST'])
@login_required
def start_exercise():
    mobility_level = request.form.get('mobility_level', 'moderate')
    energy_level = int(request.form.get('energy_level', 5))
    
    # Generate exercise plan based on mobility and energy levels
    exercise_plan = []
    
    if mobility_level == 'high':
        exercise_plan = [
            {'activity_type': 'Warm Up', 'duration': 5, 'notes': 'Light stretching and mobility exercises'},
            {'activity_type': 'Balance Training', 'duration': 10, 'notes': 'Single-leg stands and heel-toe walks'},
            {'activity_type': 'Strength Training', 'duration': 15, 'notes': 'Wall push-ups and chair squats'},
            {'activity_type': 'Cool Down', 'duration': 5, 'notes': 'Gentle stretching'}
        ]
    elif mobility_level == 'moderate':
        exercise_plan = [
            {'activity_type': 'Gentle Warm Up', 'duration': 5, 'notes': 'Seated stretching exercises'},
            {'activity_type': 'Chair Exercises', 'duration': 10, 'notes': 'Seated marching and arm circles'},
            {'activity_type': 'Standing Exercises', 'duration': 10, 'notes': 'Wall push-ups and toe raises'},
            {'activity_type': 'Cool Down', 'duration': 5, 'notes': 'Breathing exercises'}
        ]
    else:  # limited
        exercise_plan = [
            {'activity_type': 'Seated Warm Up', 'duration': 5, 'notes': 'Gentle arm and leg movements'},
            {'activity_type': 'Chair Strength', 'duration': 10, 'notes': 'Seated leg lifts and arm exercises'},
            {'activity_type': 'Flexibility', 'duration': 5, 'notes': 'Gentle stretching'},
            {'activity_type': 'Cool Down', 'duration': 5, 'notes': 'Deep breathing and relaxation'}
        ]
    
    # Adjust duration based on energy level (1-10)
    if energy_level <= 3:
        for exercise in exercise_plan:
            exercise['duration'] = max(3, exercise['duration'] - 2)
    elif energy_level >= 8:
        for exercise in exercise_plan:
            exercise['duration'] += 2
    
    return jsonify({'status': 'success', 'plan': exercise_plan})

@app.route('/nutrition')
@login_required
def nutrition():
    meal_suggestions = {
        'Breakfast': [
            {'name': 'Oatmeal with Berries', 'benefits': ['High in fiber', 'Antioxidants']},
            {'name': 'Greek Yogurt Parfait', 'benefits': ['Protein-rich', 'Probiotics']},
            {'name': 'Whole Grain Toast with Avocado', 'benefits': ['Healthy fats', 'B vitamins']}
        ],
        'Lunch': [
            {'name': 'Quinoa Buddha Bowl', 'benefits': ['Complete protein', 'Anti-inflammatory']},
            {'name': 'Mediterranean Salad', 'benefits': ['Heart-healthy', 'Omega-3s']},
            {'name': 'Lentil Soup', 'benefits': ['Iron-rich', 'Fiber']}
        ],
        'Dinner': [
            {'name': 'Grilled Fish with Vegetables', 'benefits': ['Lean protein', 'Omega-3s']},
            {'name': 'Turkey and Sweet Potato', 'benefits': ['Lean protein', 'Complex carbs']},
            {'name': 'Stir-Fried Tofu with Brown Rice', 'benefits': ['Plant protein', 'Fiber']}
        ]
    }
    
    nutrition_log = {
        'dates': [(datetime.now() - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(7)][::-1],
        'water_intake': [random.randint(6, 10) for _ in range(7)],
        'meal_quality': [random.randint(70, 95) for _ in range(7)]
    }
    
    return render_template('nutrition.html', meal_suggestions=meal_suggestions, nutrition_log=nutrition_log)

@app.route('/api/nutrition/log', methods=['POST'])
@login_required
def log_nutrition():
    meal_type = request.form.get('meal_type')
    food_items = request.form.getlist('food_items[]')
    portions = request.form.getlist('portions[]')
    difficulties = request.form.getlist('difficulties[]')
    
    # In a real app, save this to a database
    return jsonify({
        'status': 'success',
        'message': 'Meal logged successfully',
        'summary': {
            'calories': {'value': 1200, 'target': 2000, 'percentage': 60},
            'protein': {'value': 45, 'target': 70, 'percentage': 64},
            'hydration': {'value': 6, 'target': 8, 'percentage': 75}
        }
    })

@app.route('/sleep')
@login_required
def sleep():
    sleep_tips = [
        'Maintain a consistent sleep schedule',
        'Create a relaxing bedtime routine',
        'Keep your bedroom cool and dark',
        'Avoid screens before bedtime',
        'Practice relaxation techniques',
        'Exercise regularly, but not close to bedtime'
    ]
    
    sleep_data = {
        'dates': [(datetime.now() - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(7)][::-1],
        'hours': [random.randint(6, 9) for _ in range(7)],
        'quality': [random.randint(60, 95) for _ in range(7)],
        'disruptions': [random.randint(0, 3) for _ in range(7)]
    }
    
    return render_template('sleep.html', sleep_tips=sleep_tips, sleep_data=sleep_data)

@app.route('/api/sleep/log', methods=['POST'])
@login_required
def log_sleep():
    duration = float(request.form.get('duration', 0))
    quality = int(request.form.get('quality', 5))
    bedtime = request.form.get('bedtime')
    wake_time = request.form.get('wake_time')
    disturbances = request.form.getlist('disturbances')
    
    # In a real app, save this to a database
    return jsonify({
        'status': 'success',
        'message': 'Sleep logged successfully',
        'summary': {
            'duration': duration,
            'quality': quality,
            'disturbances': len(disturbances)
        }
    })

@app.route('/speech')
@login_required
def speech():
    exercises = {
        'Breathing': [
            {'name': 'Diaphragmatic Breathing', 'duration': '5 minutes'},
            {'name': 'Pursed Lip Breathing', 'duration': '3 minutes'},
            {'name': 'Lion\'s Breath', 'duration': '2 minutes'}
        ],
        'Voice': [
            {'name': 'Sustained Vowel Sounds', 'duration': '5 repetitions'},
            {'name': 'Pitch Glides', 'duration': '3 minutes'},
            {'name': 'Volume Control', 'duration': '5 minutes'}
        ],
        'Articulation': [
            {'name': 'Tongue Twisters', 'duration': '5 minutes'},
            {'name': 'Word Lists', 'duration': '3 minutes'},
            {'name': 'Reading Aloud', 'duration': '5 minutes'}
        ]
    }
    
    progress = {
        'dates': [(datetime.now() - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(7)][::-1],
        'clarity': [random.randint(60, 95) for _ in range(7)],
        'volume': [random.randint(65, 90) for _ in range(7)],
        'fluency': [random.randint(70, 95) for _ in range(7)]
    }
    
    return render_template('speech.html', exercises=exercises, progress=progress)

@app.route('/api/speech/analyze', methods=['POST'])
@login_required
def analyze_speech():
    # In a real app, this would process audio data
    # For demo, return mock analysis
    return jsonify({
        'status': 'success',
        'analysis': {
            'risk_score': random.randint(10, 40),
            'patterns': [
                {'type': 'Volume', 'score': random.randint(70, 95), 'note': 'Good vocal projection'},
                {'type': 'Clarity', 'score': random.randint(65, 90), 'note': 'Clear pronunciation'},
                {'type': 'Fluency', 'score': random.randint(75, 95), 'note': 'Smooth speech flow'}
            ],
            'recommendations': [
                'Practice deep breathing exercises',
                'Continue regular speech exercises',
                'Focus on pacing during conversations'
            ]
        }
    })

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5003)
