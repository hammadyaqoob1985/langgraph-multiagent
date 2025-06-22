from langgraph.graph import StateGraph, START
from langgraph.graph import MessagesState

from agents import research_node, chart_node


def main():
    workflow = StateGraph(MessagesState)
    workflow.add_node("researcher", research_node)
    workflow.add_node("chart_generator", chart_node)

    workflow.add_edge(START, "researcher")
    graph = workflow.compile()
    events = graph.stream(
        {
            "messages": [
                (
                    "user",
                    "Get me the share price for JP Morgan Chase for the last 10 years, then make a line chart of it with the ticker symbol and full name in the header of the chart. "
                    "Once you make the chart, finish.",
                )
            ],
        },
        # Maximum number of steps to take in the graph
        {"recursion_limit": 150},
    )
    for s in events:
        print(s)
        print("----")

if __name__ == "__main__":
    main()