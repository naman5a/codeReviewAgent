from llm import call_llm

BEST_PRACTICES_PROMPT = """
You are a senior software engineer.

Analyze code for best practices:
- readability
- maintainability
- idiomatic usage
- unnecessary complexity
- refactoring opportunities

Return JSON:
{
  "issues": [
    {
      "type": "best_practice",
      "severity": "low|medium|high",
      "message": "",
      "location": "",
      "suggestion": "",
      "confidence": 0-1
    }
  ]
}
"""


def best_practices_agent(chunk: dict):
    return call_llm(BEST_PRACTICES_PROMPT, chunk)