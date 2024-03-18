import json

base_url = "https://server11.mp3quran.net/sds/"
data = []

for i in range(1, 115):
    file_number = str(i).zfill(3)  # Pad with zeros to ensure 3-digit format
    url = base_url + file_number + ".mp3"
    data.append({"id": i, "url": url})  # Create a dictionary for each entry

with open("quran_data.json", "w") as f:
    json.dump(data, f, indent=4)  # Write data to JSON with indentation

print("Quran data (URL and ID) saved to quran_data.json")
