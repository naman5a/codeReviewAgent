from typing import TypedDict, List, Dict, Any


class PRState(TypedDict):
    files: List[Dict]

    chunks: List[Dict]

    arch_results: List[Dict]
    best_practice_results: List[Dict]
    security_results: List[Dict]
    docs_results: List[Dict]

    aggregated: Dict[str, Any]