# GraphIDOR
This Python tool takes a GraphQL introspection schema and automatically extracts all query operations that accept `id` or `name` as arguments.  
You can also specify additional arguments.
---
## Installation
```bash
git clone https://github.com/Joex0x/GraphIDOR.git
cd GraphIDOR
chmod +x GraphIDOR.py
```
---
## Usage

```bash
python GraphIDOR.py schema.json
```
You can also specify any argument you want:
```bash
python GraphIDOR.py schema.json username
```
--- 
## Example output
```
Queries that accept any of: id, name
------------------------------------------------------------
• getUser(args: id)
• getProduct(args: name)
