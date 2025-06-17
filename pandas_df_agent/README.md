# Pandas DataFrame Agent
## Overview
The Pandas DataFrame Agent is an intelligent assistant that helps you analyze and manipulate pandas DataFrames using natural language queries. This project leverages the power of LangChain and OpenAI's language models to interpret your questions about data and execute the appropriate pandas operations.

## Features
- Query DataFrames using natural language
- Perform complex data analysis without writing pandas code
- Get instant answers to questions about your data
- Support for data visualization and statistical analysis

## Requirements
- Python 3.8+
- pandas
- langchain
- langchain_experimental
- langchain_openai
- python-dotenv
- OpenAI API key

## Installation

```bash
# Clone the repository
git clone https://github.com/elifkeskin/pandas-df-agent.git
cd pandas-df-agent

# Install dependencies
pip install -r requirements.txt

# Create a .env file with your OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

## Usage
The project is implemented as a Jupyter notebook. To use it:

1. Start Jupyter notebook:
jupyter notebook
2. Open the pandas_dataframe_agents.ipynb notebook
3. Run the cells to initialize the agent with your DataFrame
4. Query your data using natural language

Example queries:

- "What is the price total for all products?"
- "Which salesperson sold the most units?"
- "Calculate the average price of products"
- "Create a bar chart of units sold by product"

## Docker Support
 ```bash
You can also run the project using Docker:
# Build the Docker image
docker build -t pandas-df-agent .

# Run the container
docker run -p 8888:8888 -e OPENAI_API_KEY=your_api_key_here pandas-df-agent
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
