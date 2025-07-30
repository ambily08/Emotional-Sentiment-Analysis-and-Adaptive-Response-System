def generate_response(emotion: str, culture: str = "indian") -> str:
    """
    Returns a culturally sensitive empathetic response based on the detected emotion.

    Args:
        emotion (str): Detected emotional state (e.g., 'joy', 'sadness')
        culture (str): Culture context for response ('indian' or 'western')

    Returns:
        str: Empathetic response
    """
    responses = {
        "joy": {
            "indian": "That's wonderful to hear! Wishing you continued happiness 🌸",
            "western": "Awesome! Glad you're feeling great 😊"
        },
        "sadness": {
            "indian": "I'm here for you. It's okay to feel this way. Sending warm thoughts 🙏",
            "western": "I'm sorry you're feeling down. I'm here to talk if you need."
        },
        "anger": {
            "indian": "Let’s take a deep breath. You’re not alone in this. 🌿",
            "western": "It's understandable to feel upset. Let's find a calm way to move forward."
        },
        "fear": {
            "indian": "Fear is natural. I believe in your strength to get through this. 💪",
            "western": "That sounds scary, but you’re not alone. You’ve got this!"
        },
        "love": {
            "indian": "That’s beautiful. Cherish the love and keep spreading joy. 💖",
            "western": "That's so sweet! Love is truly special."
        },
        "surprise": {
            "indian": "Wow! That’s unexpected. Hope it’s a good surprise! 🎉",
            "western": "Whoa! That must've been unexpected. Hope it was good!"
        }
    }

    emotion = emotion.lower().strip()
    culture = culture.lower().strip()

    return responses.get(emotion, {}).get(culture, "I'm here to support you.")
