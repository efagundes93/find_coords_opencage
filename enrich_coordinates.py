from opencage.geocoder import OpenCageGeocode
import json

input_file_path = 'input.json'
output_file_path = 'output.json'

try:
    with open(input_file_path, 'r', encoding='utf-8') as file:
        addresses = json.load(file)
except FileNotFoundError:
    print(f"'{input_file_path}' not found")
    exit(1)
except json.JSONDecodeError:
    print("Error in JSON.")
    exit(1)

if not addresses:
    print("The addresses file is empty")
    exit(0)

api_key = '[YOUR API KEY]' #GENERATE REGISTERING ON https://opencagedata.com/
geocoder = OpenCageGeocode(api_key)

enriched_addresses = []

for address in addresses:
    try:
        query = f"{address['street']}, {address['number']},  {address['city']}, {address['state']}, Brazil"
        print(f"Searching for: {query}")
        
        results = geocoder.geocode(query)
        
        if results and len(results) > 0:
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
            print(f"Coord found: {lat}, {lng}")
            
            address["lat"] = lat
            address["long"] = lng
            enriched_addresses.append(address)
        else:
            print(f"Coords not found for: {query}")
    
    except Exception as e:
        print(f"Failed to enrich '{query}': {e}")

try:
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(enriched_addresses, output_file, ensure_ascii=False, indent=4)
    print(f"Enriched data save in '{output_file_path}'.")

except Exception as e:
    print(f"Error to write file: {e}")
