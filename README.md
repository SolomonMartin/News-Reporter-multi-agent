# News Reporter Multi-Agent

This project is a multi-agent news reporting system using Crew AI. It consists of two agents: a senior research agent and a writer agent. The system is designed to uncover the latest updates and advancements in various topics, particularly focusing on the impact of AI on the tech sector and jobs.

## Features

- **Senior Research Agent**: Uncovers the latest updates and advancements in a given topic using custom tools and large language models (LLMs).
- **Writer Agent**: Crafts engaging narratives based on the research findings.
- **Comprehensive Reports**: Generates comprehensive 3-paragraph long reports on the latest trends in a given topic.
- **Insightful Articles**: Composes 4-paragraph long articles on the topic's advancements, formatted as markdown.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/news-reporter-multi-agent.git
    cd news-reporter-multi-agent
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    Create a `.env` file in the root directory of the project and add your API keys:

    ```plaintext
    GOOGLE_API_KEY=your_google_api_key
    SERPER_API_KEY=your_serper_api_key
    ```

## Usage

1. Run the main script:

    ```sh
    python crew.py
    ```

2. The script will output the result of the multi-agent system, including the comprehensive report and the insightful article.

## Code Overview

### agents.py

Defines the agents used in the project:

- `news_researcher`: Senior research agent uncovering the latest updates and advancements in a given topic.
- `news_writer`: Writer agent crafting engaging narratives based on the research findings.

### tasks.py

Defines the tasks assigned to the agents:

- `research_task`: Task for the `news_researcher` to identify the next big trend in a given topic.
- `write_task`: Task for the `news_writer` to compose an insightful article based on the research findings.

### tools.py

Defines the custom tools used by the agents:

- `SerperDevTool`: Tool for searching and retrieving relevant information from the web.

### crew.py

Main script that sets up the crew, assigns tasks to the agents, and kicks off the process.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Crew AI](https://crew.ai) for the multi-agent framework.
- [Google Generative AI](https://cloud.google.com/ai-platform/generative-ai) for the large language models.
- [Serper Dev Tool](https://serper.dev) for the custom search tool.

