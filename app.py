import os

from flask import Flask, render_template, request

app = Flask(__name__)

# Simple graph for demo purposes
GRAPH = {
    "Non": {"Pupa": 99, "I here zax": 2},
    "Pupa": {"Non": 3},
    "I here zax": {"Non": 5},
    "Jack": {"Non": 29},
    "Fiw": {"Jack": 100},
    "Chatcharin": {"G": 2},
    "G": {"Pupa": 3}
}


def shortest_path(graph, start, end):
    if start == end:
        return [start]

    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0
    visited = set()

    while True:
        current = None
        for node in graph:
            if node in visited:
                continue
            if current is None or distances[node] < distances[current]:
                current = node

        if current is None or distances[current] == float("inf"):
            break

        visited.add(current)
        if current == end:
            break

        for neighbor, weight in graph[current].items():
            candidate = distances[current] + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                previous[neighbor] = current

    if distances[end] == float("inf"):
        return []

    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous[node]
    path.reverse()
    return path


@app.route("/health")
def health():
    return "ok", 200


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        start = request.form.get("start", "start")
        end = request.form.get("end", "end")
        path = shortest_path(GRAPH, start, end)
        if path:
            result = {
                "start": start,
                "end": end,
                "path": path,
                "distance": sum(GRAPH[path[i]][path[i + 1]] for i in range(len(path) - 1) if path[i + 1] in GRAPH[path[i]]),
            }
        else:
            result = {"start": start, "end": end, "path": [], "distance": None}

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
