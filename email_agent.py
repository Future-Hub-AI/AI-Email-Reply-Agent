from openai import OpenAI

# Add your OpenAI API key here
client = OpenAI(api_key="YOUR_API_KEY")


def generate_reply(email_text):
    prompt = f"""
You are an AI assistant that writes short professional email replies.

Email received:
{email_text}

Write a polite reply.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional email assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    email = """
Hi John,
Can we schedule a meeting tomorrow to discuss the project timeline?
Thanks
"""

    reply = generate_reply(email)

    print("\nGenerated Reply:\n")
    print(reply)
