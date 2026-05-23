from llm import call_llm

SECURITY_PROMPT = """
You are a security engineer reviewing code changes.

Find:
- injection vulnerabilities
- auth/authz issues
- secrets leakage
- unsafe deserialization
- insecure patterns

Return JSON:
{
  "issues": [
    {
      "type": "security",
      "severity": "medium|high|critical",
      "message": "",
      "location": "",
      "suggestion": "",
      "confidence": 0-1
    }
  ]
}
"""


def security_agent(chunk: dict):
    return call_llm(SECURITY_PROMPT, chunk)