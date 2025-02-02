# ParkinScan - Parkinson's Disease Monitoring App

ParkinScan is a comprehensive web application designed to help individuals with Parkinson's Disease monitor their symptoms, track their daily activities, and maintain their health and wellness routines. The app provides personalized recommendations and alerts users when medical attention may be needed.

## Features

### 1. Daily Health Check-in
- Quick symptom assessment
- Automatic recommendations based on symptom severity
- Tracks changes in:
  - Movement speed
  - Handwriting
  - Speech
  - Mobility
  - Tremors
  - Muscle stiffness

### 2. Exercise Tracking
- Customized exercise plans
- Real-time workout guidance
- Progress tracking
- Difficulty adjustment based on mobility level
- Timer-based exercise sessions

### 3. Nutrition Monitoring
- Meal logging
- Dietary recommendations
- Hydration tracking
- Difficulty tracking for eating and drinking
- Nutritional progress visualization

### 4. Sleep Analysis
- Sleep quality tracking
- Sleep pattern monitoring
- Disturbance logging
- Sleep hygiene recommendations
- Historical sleep data visualization

### 5. Speech Exercises
- Voice recording and analysis
- Speech pattern monitoring
- Volume and clarity assessment
- Personalized speech exercise recommendations
- Progress tracking over time

## Getting Started

### Prerequisites
- Python 3.x
- Flask
- SQLite (for development)
- Modern web browser

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ParkinScan.git
cd ParkinScan
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
python init_db.py
```

5. Start the application:
```bash
python web_app.py
```

6. Access the application at: `http://localhost:5003`

## Usage

1. **First Time Setup**
   - Create an account or log in
   - Complete the initial health assessment
   - Set your preferences for notifications

2. **Daily Routine**
   - Complete the daily check-in
   - Follow exercise recommendations
   - Log meals and medications
   - Record speech exercises
   - Track sleep patterns

3. **Monitoring Health**
   - Review daily summaries
   - Track progress over time
   - Share reports with healthcare providers
   - Receive alerts for concerning changes

## Technical Details

### Built With
- Frontend: HTML5, CSS3, JavaScript, Bootstrap 5
- Backend: Python, Flask
- Database: SQLite (development), PostgreSQL (production)
- Authentication: Flask-Login
- Charts: Plotly.js

### Project Structure
```
ParkinScan/
├── static/
│   ├── css/
│   ├── js/
│   └── img/
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── exercise.html
│   ├── nutrition.html
│   ├── sleep.html
│   └── speech.html
├── web_app.py
├── models.py
├── init_db.py
└── requirements.txt
```

## Security

- All data is encrypted at rest
- HTTPS required for all connections
- Regular security audits
- HIPAA compliance measures
- Secure password hashing

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Developers: Srimathi Vadivel and Anushka Kondur
- Healthcare professionals and students who provided guidance
- Parkinson's Disease research community
- Open source contributors
- Beta testers and early users

## Support

For support, open an issue in the GitHub repository.

## Roadmap

- Mobile app development
- Integration with wearable devices
- Machine learning-based predictions
- Telemedicine integration
- Community features
