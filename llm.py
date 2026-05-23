import json
import os
from openai import OpenAI
import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.2)

def call_llm(prompt: str, data: dict) -> dict:
    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=str(data))
    ]
    response = llm.invoke(messages)
    try:
        return json.loads(response.content)
    except:
        return {"raw": response.content}
