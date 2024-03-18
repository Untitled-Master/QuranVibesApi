import json

# Load the filtered JSON data from the file
with open('reciters_m.json', 'r') as file:
  filtered_data = json.load(file)

# Find reciters whose names contain "Minshawi"
minshawi_reciters = [
    reciter for reciter in filtered_data['reciters']
    if 'Minshawi' in reciter.get('name', '')
]

# Save the filtered data to a new JSON file
filtered_minshawi_data = {'reciters': minshawi_reciters}
with open('muhammad_reciters.json', 'w') as file:
  json.dump(filtered_minshawi_data, file, indent=4)
print("Filtered data saved to 'minshawi_reciters.json'")
