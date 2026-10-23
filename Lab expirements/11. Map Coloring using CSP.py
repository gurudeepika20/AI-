

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
result = {}
regions = list(graph.keys())

def color_map(i):
    if i == len(regions):
        return True

    region = regions[i]

    for color in colors:
        if all(result.get(n) != color
               for n in graph[region]):
            result[region] = color

            if color_map(i + 1):
                return True

            del result[region]

    return False

if color_map(0):
    print("Map Coloring:", result)
else:
    print("No solution")




