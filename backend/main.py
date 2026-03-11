import asyncio
import os

from agents import (
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    AsyncOpenAI,
    set_tracing_disabled,
)

from dotenv import load_dotenv

load_dotenv()

async def main():
    set_tracing_disabled(True)

    api_key = os.getenv("GEMINI_API_KEY")
    print("API Key Loaded:", bool(api_key))

    provider = AsyncOpenAI(
        api_key=api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai",
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-2.5-flash",
        openai_client=provider,
    )

    agent = Agent(
        name="Testing Agent",
        instructions="You are an AI made for testing purpose only!",
        model=model
    )

    userInput = "dummy"
    while True:
        userInput = input("User: ")
        if userInput.lower() == "quit":
            break

        result = await Runner.run(agent, input=userInput)
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())