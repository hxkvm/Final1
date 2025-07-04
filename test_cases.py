from dijkstra import dijkstra

def run_tests():
    tests = [
        {
            "name": "Test Case 1",
            "graph": {
                'A': [('B', 1), ('C', 3)],
                'B': [('A', 1), ('C', 1)],
                'C': [('A', 3), ('B', 1)],
            },
            "start": 'A',
            "expected": {'A': 0, 'B': 1, 'C': 2}
        },
        {
            "name": "Test Case 2",
            "graph": {
                'A': [('B', 4), ('C', 1)],
                'B': [('A', 4), ('C', 2)],
                'C': [('A', 1), ('B', 2)],
            },
            "start": 'A',
            "expected": {'A': 0, 'B': 4, 'C': 1}
        },
        {
            "name": "Test Case 3",
            "graph": {
                'A': [('B', 10), ('C', 5)],
                'B': [('A', 10), ('C', 2)],
                'C': [('A', 5), ('B', 2)],
            },
            "start": 'A',
            "expected": {'A': 0, 'B': 10, 'C': 5}
        }
    ]

    for test in tests:
        result = dijkstra(test["graph"], test["start"])
        print(f"{test['name']}:\nExpected: {test['expected']}\nActual:   {result}\n")

if __name__ == "__main__":
    run_tests()
