AI System Health Monitoring
Project Overview
AI System Health Monitoring is a real-time system health monitoring solution aimed at detecting anomalies in system metrics like CPU usage and temperature. The project includes the collection of simulated system health data, real-time monitoring through a web-based dashboard, and anomaly detection using machine learning. It provides detailed visualizations of system health metrics and flags potential anomalies using an Isolation Forest model.

Project Scope
Simulated Data Generation: Simulate CPU usage and temperature data to mimic system health monitoring.
Anomaly Detection: Use Isolation Forest, a machine learning model, to detect anomalies based on system health data.
Real-Time Data Visualization: Visualize CPU and temperature data in real-time using Chart.js on a web dashboard.
Web Interface: A Flask-based web application to serve the real-time data and predictions.
Technological Stack
Backend: Flask (Python framework)
Frontend: Chart.js (JavaScript library for visualization)
Machine Learning: Scikit-learn (for Isolation Forest model)
Data Storage: CSV files (for storing generated data)
Dependencies: Pandas, Numpy, Joblib (for saving/loading models)
Initial Setup
Prerequisites
Python 3.x
Virtual Environment (recommended)
Dependencies listed in requirements.txt
Backend Setup
Clone the Repository:

git clone https://github.com/yourusername/AI_System_Health_Monitoring.git
cd AI_System_Health_Monitoring
Set Up Virtual Environment:

python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install Dependencies:

pip install -r requirements.txt
Run the Flask Server:

python app.py
This will start the Flask development server on http://127.0.0.1:5000.

Frontend Setup
Navigate to the Frontend Directory (if applicable):

cd timezero-frontend
Install Dependencies:

npm install
Start the React Development Server:

npm start
You should be able to access the frontend at http://localhost:3000.

Data Collection and Model Training Setup
Generate Simulated Data (Optional): If the dataset (health_data.csv) is not present, you can generate it by running:

python data/generate_dataset.py
Train the Machine Learning Model: To train the Isolation Forest model and save it, run:

python train_model.py
Run the Flask Application:

python app.py
Usage
Access the Frontend
Open your browser and go to http://127.0.0.1:5000 to view the real-time system health monitoring dashboard.

Upload Log Files (Optional)
For future updates, you can add functionality to upload log files and analyze system data. This feature isn't implemented yet but could be a useful enhancement.

View Real-Time Monitoring
Ensure that the system is running and you can observe real-time updates of CPU usage and temperature in the dashboard.

View Anomalies
The system will raise alerts when anomalies are detected based on CPU usage or temperature thresholds.

Documentation
System Architecture: [Link to Architecture Diagram]
UI/UX Design: [Link to Wireframes]
API Documentation: [Link to API Docs]
Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch:
git checkout -b feature-branch
Commit your changes:
git commit -am 'Add new feature'
Push to the branch:
git push origin feature-branch
Create a new Pull Request.
License
This project is licensed under the MIT License – see the LICENSE file for details.

Acknowledgments
Special thanks to [contributors] for their valuable contributions.
Inspired by [references or inspirations].
Contact
For any questions or support, please contact [your-email@example.com] or open an issue on GitHub.

