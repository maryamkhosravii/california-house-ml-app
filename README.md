**California Housing Price Prediction App**

 
**Overview**
This project provides a web application for predicting California housing prices using machine learning.
It leverages XGBoost for model training and FastAPI as the backend API with authentication, while the frontend UI is built using Streamlit.
 
**Features**
•	Train and use an XGBoost model for housing price prediction
•	FastAPI backend with token-based authentication
•	SQLite database integration for user management and data persistence
•	Interactive and user-friendly Streamlit frontend for input and prediction
•	Dockerized setup for easy deployment
 
**Getting Started**
Prerequisites
•	Python 3.9 or higher
•	Docker and Docker Compose (optional but recommended for deployment)
Installation
1.	Clone the repository:
git clone https://github.com/maryamkhosravii/california-housing-ml-app.git
cd california-housing-ml-app
2.	Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
3.	Install dependencies:
pip install -r requirements.txt
4.	Run the FastAPI backend:
uvicorn main:app --reload
5.	Run the Streamlit frontend:
streamlit run streamlit_app.py
 
**Usage**
1.	Register and log in to get your authentication token
2.	Use the Streamlit UI to input housing features like longitude, latitude, median age, bedrooms, population, median income, and ocean proximity
3.	Submit your inputs to receive a price prediction
 
**Docker Deployment**
To build and run the application using Docker:
docker-compose up --build
Access the Streamlit app at http://localhost:8501 and the FastAPI backend at http://localhost:8000.
 
**Contributing**
Contributions are welcome! Please open an issue or submit a pull request.
 
**Contact**
Your Name – mrm.khosravi@yahoo.com
Project Link: https://github.com/maryamkhosravii/california-housing-ml-app 

Made with ❤️ by Maryam Khosravi
