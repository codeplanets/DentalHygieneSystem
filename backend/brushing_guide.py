import openai

# OpenAI API 키 설정
openai.api_key = 'YOUR_API_KEY'  # 실제 API 키로 변경

def generate_brushing_guide(image):
    # LLM을 사용하여 양치 가이드 생성
    prompt = "Provide a step-by-step guide for brushing teeth."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 사용할 모델
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    guide = response['choices'][0]['message']['content']
    return guide