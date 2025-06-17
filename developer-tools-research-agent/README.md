# Developer Tools Research Agent
## Overview
The Developer Tools Research Agent is an AI-powered tool that helps developers discover, compare, and analyze software development tools and technologies. It automates the research process by searching for relevant tools, extracting key information, and providing structured comparisons and recommendations.

## Features
- Search for development tools based on natural language queries
- Extract and compare key features of different tools
- Analyze pricing models, open-source status, and technical specifications
- Provide developer-focused recommendations
- Evaluate API availability and integration capabilities
## Requirements
- Python 3.8+
- langchain
- langchain_openai
- langgraph
- fastapi
- uvicorn
- pydantic
- python-dotenv
- Node.js and npm (for Firecrawl MCP)
- OpenAI API key
- Firecrawl API key

## Installation
  ```bash
# Clone the repository
git clone https://github.com/yourusername/developer-tools-research-agent.git
cd developer-tools-research-agent

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
python main.py
You'll be prompted to enter your query about developer tools. For example:

- "What are the best CI/CD tools for Python projects?"
- "Compare GraphQL client libraries for React"
- "Find open-source alternatives to Postman"

### API Server
Start the FastAPI server:
```bash
uvicorn main:app --reload
Access the API at http://localhost:8000
 ```

## Docker Support
```bash
# Build the Docker image
docker build -t dev-tools-research-agent .

# Run the container
docker run -p 8000:8000 -e OPENAI_API_KEY=your_openai_api_key -e FIRECRAWL_API_KEY=your_firecrawl_api_key dev-tools-research-agent
 ```
<img width="493" alt="Developer_tools_research_agent_1" src="https://github.com/user-attachments/assets/52910cd8-a0aa-42f7-8cd4-3eb266dcb565" />

<img width="506" alt="Developer_tools_research_agent_2" src="https://github.com/user-attachments/assets/0f673df9-18ea-4b3a-a7a4-7d71fd7d0d59" />

<img width="506" alt="Developer_tools_research_agent_3" src="https://github.com/user-attachments/assets/1b60d0f2-ce94-496b-901a-7d3b13707276" />


## License
This project is licensed under the MIT License - see the LICENSE file for details.


