import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
from dotenv import load_dotenv

load_dotenv()

set_tracing_disabled(True)

api_key = os.getenv("GEMINI_API_KEY")

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
    instructions="You are a helpful AI chatbot.",
    model=model
)

async def ask_agent(user_input: str):
    result = await Runner.run(agent, input=user_input)
    return result.final_output