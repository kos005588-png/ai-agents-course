from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

import json
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def date_difference(start_date: str, end_date: str) -> int:
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    return (end - start).days


tools = [
    {
        "type": "function",
        "function": {
            "name": "date_difference",
            "description": "Calculate number of days between two dates.",
            "parameters": {
                "type": "object",
                "properties": {
                    "start_date": {
                        "type": "string",
                        "description": "Start date YYYY-MM-DD"
                    },
                    "end_date": {
                        "type": "string",
                        "description": "End date YYYY-MM-DD"
                    }
                },
                "required": ["start_date", "end_date"]
            }
        }
    }
]

messages = [
    {
        "role": "user",
        "content": "Kolik dní zbývá do letošních Vánoc?"
    }
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

tool_call = response.choices[0].message.tool_calls[0]

arguments = json.loads(tool_call.function.arguments)

result = date_difference(
    arguments["start_date"],
    arguments["end_date"]
)

messages.append(response.choices[0].message)

messages.append(
    {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": str(result)
    }
)

final_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

print(final_response.choices[0].message.content)