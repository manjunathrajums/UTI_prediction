UTI Prediction Flask Web App
This project is a Flask-based Web Application designed to predict Urinary Tract Infections (UTI) based on user-provided medical details. 
The app features a simple and intuitive web interface where users can enter relevant health data, and the system will generate a prediction using a Random Forest Classifier (RFC) model trained on medical records. 
The application ensures ease of use by allowing users to select categorical values such as Male/Female and Yes/No through dropdown menus, rather than manually entering 1 or 0.

Features
The application provides a modern and user-friendly interface with dropdown selections for categorical values.
It includes automatic data preprocessing, where numerical values like Serum Creatinine and WBC Count are standardized using StandardScaler before being passed to the model.
The system is built to be responsive, meaning it works well on both desktop and mobile devices. The backend logic is structured to ensure smooth communication between the frontend, the Flask API, and the machine learning model.

Technologies Used
The app is developed using Python 3.11 and Flask for backend operations, while Scikit-learn is used for machine learning. 
NumPy and Pandas handle data preprocessing, and Bootstrap & CSS ensure a visually appealing frontend. 
The web pages use Jinja2 templating, making them dynamic and interactive.

Installation & Setup
To run this project locally, first, ensure that you have Python 3.11+ installed on your system. Clone the repository and navigate to the project directory:

Copy
Edit
git clone https://github.com/yourusername/uti-prediction.git  
cd uti-prediction

Next, install the required dependencies using the following command:

Copy
Edit
pip install -r requirements.txt
Once the dependencies are installed, start the Flask application by running:

Copy
Edit
python app.py
The app will be available at http://127.0.0.1:5000/.

How to Use
To use the application, open the web app in your browser and fill in the required details.
