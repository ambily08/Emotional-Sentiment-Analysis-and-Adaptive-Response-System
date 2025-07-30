# Emotional-Sentiment-Analysis-and-Adaptive-Response-System

Project Overview

The Emotional Sentiment Analysis and Adaptive Response System is a Streamlit-based chatbot prototype that identifies a user's emotional state through natural language processing (NLP) and responds with culturally sensitive, empathetic messages. The project demonstrates the integration of a pre-trained transformer model with adaptive response logic tailored to emotional and cultural contexts.

Objective

To build an intelligent chatbot capable of:

* Understanding emotional intent in user text.

* Classifying emotions such as joy, sadness, anger, fear, love, and surprise.

* Responding in a culturally relevant and empathetic manner (e.g., Indian or Western style).

* Demonstrating the application of NLP for emotional wellbeing and mental health support.

Project Structure:

Emotional-Sentiment-Analysis-and-Adaptive-Response-System/

├── app.py
├── requirements.txt
│ ├── model/ │ ├── init.py │ ├── emotion_model.py
│ └── response_generator.py
│ ├── utils/ │ ├── init.py │ └── preprocess.py
│ ├── data/  │  └── emotions_dataset.csv
│ └── README.md

Setup Instructions

 1. Clone the repository:

 git clone git clone https://github.com/ambily08/Emotional-Sentiment-Analysis-and-Adaptive-Response-System.git cd Emotional-Sentiment-Analysis-and-Adaptive-Response-System
  
 3. Create a virtual environment:

 python -m venv env source env/bin/activate # On Windows: env\Scripts\activate

 3. Install dependencies:

 pip install -r requirements.txt

 4. Run the Streamlit app:

 streamlit run app.py
