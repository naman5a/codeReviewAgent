from llm import call_llm

DEDUP_PROMPT = """
You are a senior engineering reviewer.

You will receive multiple code review findings from different agents.

Your job:
- merge duplicates
- remove redundant issues
- normalize severity
- group by file
- keep only actionable issues

Return final structured JSON:
{
  "issues": [
    {
      "file": "",
      "type": "",
      "severity": "",
      "message": "",
      "suggestion": "",
      "confidence": 0-1
    }
  ]
}
"""


def aggregator_agent(all_results: list):
    return call_llm(DEDUP_PROMPT, {"issues": all_results})