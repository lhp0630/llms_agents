from pydantic_ai import Agent
from pydantic_ai.capabilities import MCP, WebFetch, WebSearch

agent = Agent(
    "openai:gpt-5.2",
    capabilities=[
        # MCP("https://"),

        # Searches the web for information and returns the results.
        WebSearch(),

        # Fetches the content of a web page at the given URL and returns it as markdown or binary content.
        WebFetch(),
    ],
)
