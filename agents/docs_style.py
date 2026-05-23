from llm import call_llm

DOCS_PROMPT = """
You are a code reviewer focused on documentation and style.

Check:
- missing comments
- poor naming
- inconsistent formatting
- missing docs for functions/APIs

Return JSON:
{
  "issues": [
    {
      "type": "docs_style",
      "severity": "low|medium",
      "message": "",
      "location": "",
      "suggestion": "",
      "confidence": 0-1
    }
  ]
}
"""


def docs_agent(chunk: dict):
    return call_llm(DOCS_PROMPT, chunk)