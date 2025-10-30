import json
import sys

def load_schema(file_path):
    """Load GraphQL schema JSON (introspection output)."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_queries_with_args(schema_data, arg_names=None):
    """
    Extract queries from the GraphQL schema that take specific argument names.
    Default arg_names = ['id', 'name']
    """
    if arg_names is None:
        arg_names = ['id', 'name']

    queries = []
    # Traverse types to find the Query type
    types = schema_data.get('data', {}).get('__schema', {}).get('types', [])
    for t in types:
        if t.get('name') == 'Query' and 'fields' in t:
            for field in t['fields']:
                args = field.get('args', [])
                arg_names_in_query = [a['name'] for a in args]
                # Check if any of our target argument names are in this query
                if any(arg in arg_names_in_query for arg in arg_names):
                    queries.append({
                        "query": field['name'],
                        "args": arg_names_in_query
                    })
    return queries

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <schema.json> [arg1 arg2 ...]")
        sys.exit(1)

    schema_file = sys.argv[1]
    arg_names = sys.argv[2:] if len(sys.argv) > 2 else ['id', 'name']

    schema = load_schema(schema_file)
    queries = extract_queries_with_args(schema, arg_names)

    print("\n🧩 Queries that accept any of:", ', '.join(arg_names))
    print("-" * 60)
    if not queries:
        print("No matching queries found.")
    else:
        for q in queries:
            print(f"• {q['query']} (args: {', '.join(q['args'])})")

if __name__ == "__main__":
    main()
