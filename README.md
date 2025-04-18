# Contrary LLM Chat

A Streamlit app that lets you chat with a locally running LLM that does the opposite of what you ask.

## Overview

This application runs small language models locally on your MacBook Pro M3, instructing them to behave in a contrary manner - doing the opposite of whatever is requested. It's a fun experiment in AI behavior and prompt engineering.

## Requirements

- Python 3.8+
- MacBook with M1/M2/M3 chip (for MPS acceleration) or other computer with sufficient RAM
- ~8-16GB of RAM (depending on model size)

## Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/contrary-llm.git
cd contrary-llm
```

2. Create a virtual environment and install requirements:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. The app will open in your browser. If not, navigate to `http://localhost:8501`.

3. Choose a model from the sidebar and adjust the "Contrary Level" as desired.

4. Chat with the AI and watch it do the opposite of what you ask!

## Models

The app includes several pre-configured models:

- **Phi-2 (2.7B)**: A compact but powerful model from Microsoft (recommended)
- **TinyLlama (1.1B)**: An even smaller model that requires less memory
- **Mistral-7B-Instruct-v0.2**: A larger model for better quality responses (requires more RAM)

The first time you use a model, it will be downloaded from Hugging Face.

## How It Works

The application uses prompt engineering to instruct the language model to be contrary. When you send a message, the system prepends special instructions telling the model to do the opposite of what you ask. You can control how contrary the model is using the "Contrary Level" slider.

## Troubleshooting

- **Out of Memory**: If you encounter memory issues, try a smaller model or restart your computer
- **Slow Responses**: The first generation might be slow as the model loads; subsequent responses should be faster
- **Model Loading Errors**: Ensure you have an internet connection for the initial model download

## Extending the Project

Some ideas for extending this project:
- Add more models of different sizes
- Implement different "contrary personalities"
- Add a feature to toggle between contrary and helpful modes
- Implement a scoring system for how contrary the responses are