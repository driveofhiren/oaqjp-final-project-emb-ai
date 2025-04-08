import requests

def emotion_detector(text):

    if not text or not text.strip():
        return {
            'emotions': [
                {'label': 'anger', 'score': None},
                {'label': 'disgust', 'score': None},
                {'label': 'fear', 'score': None},
                {'label': 'joy', 'score': None},
                {'label': 'sadness', 'score': None}
            ],
            'dominant_emotion': None
        }
  
    url = "https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions"
    headers = {"Authorization": "Bearer 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"}  
    
    data = {"inputs": text}
    
    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 400:
            return {
                'emotions': [
                    {'label': 'anger', 'score': None},
                    {'label': 'disgust', 'score': None},
                    {'label': 'fear', 'score': None},
                    {'label': 'joy', 'score': None},
                    {'label': 'sadness', 'score': None}
                ],
                'dominant_emotion': None
            }
        
        if response.status_code == 200:
   
            emotions = response.json()
            
        
            if isinstance(emotions, list) and len(emotions) > 0:
                emotion_list = emotions[0] 
                dominant_emotion = max(emotion_list, key=lambda x: x['score'])
                
                modified_response = {
                    'emotions': emotion_list,
                    'dominant_emotion': dominant_emotion['label']
                }
                return modified_response
            return emotions
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    test_text = "I am feeling very happy and excited today!"
    result = emotion_detector(test_text)
    print(result)

















