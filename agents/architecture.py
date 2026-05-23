from llm import call_llm

ARCH_PROMPT = """
You are a senior software architect.

Analyze the given GitHub PR chunk and identify:
- structural issues
- design flaws
- scalability problems
- performance bottlenecks

Return JSON:
{
  "issues": [
    {
      "type": "architecture",
      "severity": "low|medium|high|critical",
      "message": "",
      "location": "",
      "suggestion": "",
      "confidence": 0-1
    }
  ]
}
"""


def architecture_agent(chunk: dict):
    return call_llm(ARCH_PROMPT, chunk)