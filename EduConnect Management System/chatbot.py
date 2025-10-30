
from openai import OpenAI


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

def ai_generate_questions():
    topic = input("Enter topic keyword: ")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are an AI assistant that generates quiz questions."},
            {"role": "user", "content": f"Generate 5 quiz questions about {topic}."}
        ],
        temperature=0.7
    )

    print("\n--- Generated Quiz Questions ---\n")
    print(response.choices[0].message.content)
