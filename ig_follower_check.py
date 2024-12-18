import json

# Load the JSON files
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Extract values from the "string_list_data" field
def extract_values(data, key="relationships_following"):
    values = set()
    if isinstance(data, dict):  # For File1
        data = data.get(key, [])
    for item in data:
        string_list_data = item.get("string_list_data", [])
        for entry in string_list_data:
            values.add(entry.get("value"))
    return values

# Compare the values between two files
def find_non_followers(following_file, followers_file):
    following_data = load_json(following_file)
    followers_data = load_json(followers_file)

    following_values = extract_values(following_data)
    followers_values = extract_values(followers_data, key=None)

    # Find values in following but not in followers
    non_followers = following_values - followers_values
    return non_followers

# Specify the file paths
following_file = "following.json"
followers_file = "followers_1.json"

# Find and print non-followers
non_followers = find_non_followers(following_file, followers_file)
print("Users you follow but who don't follow you back:")
print(non_followers)

# Optionally, save the result to a file
with open("non_followers.json", "w") as output_file:
    json.dump(list(non_followers), output_file, indent=4)
