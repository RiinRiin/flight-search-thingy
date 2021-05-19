import csv, json

# Function to convert a CSV to JSON
def make_json(csvFilePath, jsonFilePath):
    data = []
    with open(csvFilePath) as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            data.append(rows)
            # key = rows['id']
            # data[key] = rows
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
         