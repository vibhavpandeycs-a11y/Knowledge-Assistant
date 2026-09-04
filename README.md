# Knowledge Assistant

An AI-powered local knowledge assistant built with Python. It allows users to have normal conversations with a local LLM and ask questions about PDF documents.

## Features

- Normal chat with a local LLM
- Chat with PDF documents
- Extract and process PDF content
- Retrieve relevant information from PDFs
- Simple graphical interface built with Tkinter

## Requirements

- Python 3
- Ollama
- Required Python packages listed in `requirements.txt`

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## How to Run

Make sure Ollama is installed and the required local LLM model is available.

Run the application:

```bash
python main.py
```

The application provides two options:

- **Normal Chat** — chat with the local LLM.
- **PDF Chat** — select a PDF and ask questions about its content.

## Technologies

- Python
- Tkinter
- Ollama
- PDF processing
- Embeddings
- Information retrieval
