# Gemini API Chatbot

A command-line chatbot built with Python, Google's Gemini 3.5 Flash-Lite model, and the Gemini Interactions API. Uses the Google Gen AI SDK.

## Setup

**1. Install dependencies**

```bash
pip install -r requirements.txt
```

**2. Configure API key**

Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).

Create a `.env` file in the project root and add:

```env
GEMINI_API_KEY=your_api_key_here
```

>Run main.py to start chatting. Type 'exit' to end the conversation.

## Configuration

The following settings can be changed in `main.py`:

- `MODEL` - Select the Gemini model to use.
- `USE_HISTORY` - Set to `True` to enable conversation history or `False` (default) to disable conversation history.
- `generation_config` - Adjust the model's thinking level between minimal, low, medium and high. Can be passed as an optional parameter to `client.interactions.create()` in `main.py`.
(Gemini 3.5 Flash-Lite uses minimal thinking by default.)