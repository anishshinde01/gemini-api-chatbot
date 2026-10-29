from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL = "gemini-3.5-flash-lite" #gemini-3.8-flash
USE_HISTORY = False  # set True to enable conversation history

client = genai.Client()
previous_id = None

print("Welcome! How can I help you today?")
print(f"Conversation history: {'ON' if USE_HISTORY else 'OFF'}")
print("Type 'exit' to quit.\n")

while True:
    message = input("You: ").strip()

    if message.lower() == "exit":
        break

    if not message:
        continue

    # generation_config={"thinking_level": "minimal"} can be used
    # if getting an answer back is taking too long.
    # minimal thinking mode is the default for 3.5-flash-lite
    interaction = client.interactions.create(
        model=MODEL,
        input=message,
        previous_interaction_id=previous_id if USE_HISTORY else None,
        store=USE_HISTORY
    )

    print(f"Gemini: {interaction.output_text}\n")

    if USE_HISTORY:
        previous_id = interaction.id

print("Goodbye! It was nice talking to you.")