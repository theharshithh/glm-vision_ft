import json

# Read the original JSONL file and modify the 'image' keys
modified_lines = []
with open('val.jsonl', 'r') as file:
    for line in file:
        data = json.loads(line)
        if 'image' in data:
            data['image'] = f"./data/imgs/{data['image']}"
        modified_lines.append(json.dumps(data))

# Write the modified content back to the original JSONL file
with open('val.jsonl', 'w') as file:
    for line in modified_lines:
        file.write(line + '\n')
