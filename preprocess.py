import re

def clean_text(text):
    """
    Cleans input text by:
    - Converting to lowercase
    - Removing special characters and numbers
    - Removing extra whitespace
    """
    if not isinstance(text, str):
        return ""

    text = text.lower()  
    text = re.sub(r'[^a-z\s]', '', text) 
    text = re.sub(r'\s+', ' ', text).strip()  
    return text
