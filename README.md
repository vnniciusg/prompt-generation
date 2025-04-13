# Prompt Generation

Generate prompts dynamically based on user input using the LangChain framework. This repository provides a simple and effective way to create prompts that can be used in various applications, such as chatbots, virtual assistants, and more.

## Features

- Generate prompts dynamically based on user input.
- Utilize state-of-the-art NLP models for accurate and context-aware results.
- Easily customizable for various use cases.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/vnniciusg/prompt-generation.git
   cd prompt-generation
   ```
2. Install the required dependencies:

   ```bash
   uv sync
   ```

3. Set up your environment variables. Create a `.env` file in the root directory and add your OpenAI API key:

   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Run the application:
   ```bash
    uv run main.py
   ```

## References

- [Prompt Generation from User Requirements](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
