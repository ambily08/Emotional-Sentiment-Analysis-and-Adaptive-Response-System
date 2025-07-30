import streamlit as st
from utils.preprocess import clean_text
from model.emotion_model import detect_emotion
from model.response_generator import generate_response

st.title(" Emotional Sentiment Chatbot")

st.write(" Hello! I’m here to understand how you feel and respond with empathy.")

user_input = st.text_area("How are you feeling today?")

culture = st.selectbox("Choose your culture for response style:", ["indian", "western"])

if st.button("Analyze Emotion"):
    if user_input:
        cleaned = clean_text(user_input)
        emotion, score = detect_emotion(cleaned)
        response = generate_response(emotion, culture)
        
        st.subheader("Detected Emotion:")
        st.success(f"{emotion.capitalize()} (Confidence: {score:.2f})")
        
        st.subheader("Chatbot's Response:")
        st.info(response)
    else:
        st.warning("Please enter your message.")
