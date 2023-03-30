import openai


openai.api_key = "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"
prompt = "The following is a conversation with a friendly chatbot that helps to make a budget trip'"
def generate_response(user_input):
    input_prompt = f"{user_input}\nBot:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt + "\n" + input_prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    bot_response = response.choices[0].text.strip()
    return bot_response
def main():
    print("Bot: Hi, how can I help you today?")
    while True:
        user_input = input("You: ")
        bot_response = generate_response(user_input)
        print("Bot:", bot_response)
if __name__ == "__main__":
    main()
