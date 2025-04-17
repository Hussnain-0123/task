from google import genai

client = genai.Client(api_key="zz")

while True:
    user_input = input("Ask me anything: ")

    if "which model" in user_input.lower() or "what model" in user_input.lower():
        print("I am Einstein.")
        continue  # Skip AI processing and go to the next question

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"""
        You are Albert Einstein. Answer the following question with wisdom, wit, and scientific insight:
        Question: {user_input}
        """,
    )

    print(response.text)
