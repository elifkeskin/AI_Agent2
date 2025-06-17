# HR Assistant
## Overview
The HR Assistant is an AI-powered tool designed to help HR professionals and employees access and analyze employee information efficiently. It combines natural language processing with HR data retrieval to provide quick answers to HR-related queries.

## Features
- Query employee information using natural language
- Calculate total compensation including bonuses
- Answer general HR questions based on employee data
- Retrieve relevant employee records using semantic search

## Requirements
- Python 3.8+
- langchain
- langchain_openai
- langchain_community
- FAISS vector database
- HuggingFace embeddings
- python-dotenv
- OpenAI API key


## Installation
 ```bash
# Clone the repository
git clone https://github.com/elifkeskin/HR_Assistant.git
cd HR_Assistant

# Install dependencies
pip install -r requirements.txt

# Create a .env file with your OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

## Usage
The project is implemented as a Jupyter notebook. To use it:

**1.** Start Jupyter notebook:

```bash
jupyter notebook
```
**2.** Open the HR_Assistant.ipynb notebook

**3.** Run the cells to initialize the assistant

**4.** Enter an employee code when prompted

**5.** Ask HR-related questions about the employee

***Example queries:***

- "What is the total salary including bonus?"
- "How many annual leave days does this employee have?"
- "What are the work hours for this employee?"

 ```bash
## Docker Support
You can also run the project using Docker:

# Build the Docker image
docker build -t hr-assistant .

# Run the container
docker run -p 8888:8888 -e OPENAI_API_KEY=your_api_key_here hr-assistant
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
