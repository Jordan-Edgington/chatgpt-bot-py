from openai import OpenAI
print("Hello and welcome to your own CLI ChatGPT Bot.")
client = OpenAI()
exit = False
request = None
counter = 1


def first_or_not():
    if counter == 1:
        return "What would you like to know? "
    else:
        return "\nType exit to exit the ChatGPT Bot.\nIs there anything else? "


while exit == False:
    if request == "exit":
        break
    request = input(first_or_not())
    counter += 1
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            # {"role": "system", "content": input()},
            {"role": "user", "content": request}
        ]
    )

    print(completion.choices[0].message.content)
