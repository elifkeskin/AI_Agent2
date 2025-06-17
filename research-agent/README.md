
# Research Agent
## Overview
The Research Agent is an AI-powered tool that helps users scrape websites, crawl pages, and extract data using Firecrawl tools. It provides a conversational interface for web research tasks, allowing users to gather information from the web without writing complex scraping code.

## Features
- Web scraping and crawling capabilities
- Data extraction from websites
- Conversational interface for research tasks
- Integration with Firecrawl tools
- Support for both command-line and API usage

## Requirements
- Python 3.8+
- langchain
- langchain_openai
- langchain_mcp_adapters
- langgraph
- fastapi
- uvicorn
- python-dotenv
- Node.js and npm (for Firecrawl MCP)
- OpenAI API key
- Firecrawl API key

## Installation

  ```bash
# Clone the repository
git clone https://github.com/yourusername/research-agent.git
cd research-agent

# Install Python dependencies
pip install -e .

# Install Node.js dependencies
npm install -g firecrawl-mcp

# Create a .env file with your API keys
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
echo "FIRECRAWL_API_KEY=your_firecrawl_api_key_here" >> .env
   ```

## Usage
### Command Line Interface
Run the agent from the command line:
```bash
python main.py
 ```

You'll be prompted to enter your research queries. For example:

- "Find information about climate change from NASA's website"
- "Extract product prices from an e-commerce site"
- "Gather news articles about artificial intelligence from the past week"
Type "quit" to exit the program.

### API Server
Start the FastAPI server:
```bash
uvicorn main:app --reload
 ```
Access the API at http://localhost:8000

## Docker Support
```bash
# Build the Docker image
docker build -t research-agent .

# Run the container
docker run -p 8000:8000 -e OPENAI_API_KEY=your_openai_api_key -e FIRECRAWL_API_KEY=your_firecrawl_api_key research-agent
 ```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
