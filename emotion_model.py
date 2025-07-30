from transformers import pipeline

emotion_classifier = pipeline(
    task="text-classification",
    model="bhadresh-savani/distilbert-base-uncased-emotion",
    return_all_scores=False
)

def detect_emotion(text: str):
    """
    Detects emotion from a given text using Hugging Face Transformers pipeline.
    Returns:
        - emotion label (str)
        - confidence score (float)
    """
    if not text or not isinstance(text, str):
        return "unknown", 0.0

    result = emotion_classifier(text)[0]
    label = result.get('label', 'unknown')
    score = result.get('score', 0.0)
    return label, score
