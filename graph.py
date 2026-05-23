from langgraph.graph import StateGraph, END
from state import PRState

from agents.architecture import architecture_agent
from agents.best_practices import best_practices_agent
from agents.security import security_agent
from agents.docs_style import docs_agent
from agents.aggregator import aggregator_agent


# -------- Nodes --------

def chunk_files(state: PRState):
    chunks = []

    for f in state["files"]:
        chunks.append({
            "file_name": f["file_name"],
            "diff": f["diff"],
            "full_file": f["full_file"]
        })

    return {"chunks": chunks}


def run_arch(state: PRState):
    return {
        "arch_results": [
            architecture_agent(c) for c in state["chunks"]
        ]
    }


def run_best(state: PRState):
    return {
        "best_practice_results": [
            best_practices_agent(c) for c in state["chunks"]
        ]
    }


def run_security(state: PRState):
    return {
        "security_results": [
            security_agent(c) for c in state["chunks"]
        ]
    }


def run_docs(state: PRState):
    return {
        "docs_results": [
            docs_agent(c) for c in state["chunks"]
        ]
    }


def aggregate(state: PRState):
    all_results = (
        state["arch_results"]
        + state["best_practice_results"]
        + state["security_results"]
        + state["docs_results"]
    )

    return {
        "aggregated": aggregator_agent(all_results)
    }


# -------- Graph --------

graph = StateGraph(PRState)

graph.add_node("chunk", chunk_files)

graph.add_node("arch", run_arch)
graph.add_node("best", run_best)
graph.add_node("security", run_security)
graph.add_node("docs", run_docs)

graph.add_node("aggregate", aggregate)

graph.set_entry_point("chunk")

graph.add_edge("chunk", "arch")
graph.add_edge("chunk", "best")
graph.add_edge("chunk", "security")
graph.add_edge("chunk", "docs")

graph.add_edge("arch", "aggregate")
graph.add_edge("best", "aggregate")
graph.add_edge("security", "aggregate")
graph.add_edge("docs", "aggregate")

graph.add_edge("aggregate", END)

app = graph.compile()