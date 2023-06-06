import json

# Load the data from 'combined.json'
with open('combined.json') as file:
    combined_data = json.load(file)

# Load the data from 'names.json'
with open('names.json') as file:
    names_data = json.load(file)

# Get the length of the smaller array
length = min(len(combined_data), len(names_data['api_seq']))

# Add the 'api_seq' column to each object in 'combined_data'
for i in range(length):
    combined_data[i]['api_seq'] = names_data['api_seq'][i]

# Save the modified data to 'combined.json'
with open('final_combined.json', 'w') as file: 
    json.dump(combined_data, file, indent=4) 




# print("final combined done")
