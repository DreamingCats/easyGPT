import openai
openai.api_key = ""  #fill in your api_key

question=input("Input your question:")
print("chatGPT says:")

answer = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": question}
    ]
)

print(answer['choices'][0]['message']['content'])
input('\nPress Enter to exit...')
