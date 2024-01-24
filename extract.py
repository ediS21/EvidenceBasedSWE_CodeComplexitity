import xml.etree.ElementTree as ET
import json

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    results = {}

    for item in root.findall(".//item"):
        file_name = item.attrib['name'].split(" at ")[1].split(":")[0].strip()
        function_data = list(map(int, [value.text for value in item.findall("value")]))
        
        if file_name not in results:
            results[file_name] = {'ncss': [], 'ccn': []}
        
        results[file_name]['ncss'].append(function_data[1])
        results[file_name]['ccn'].append(function_data[2])

    return results

def calculate_average(data):
    average_data = {}

    for file_name, values in data.items():
        ncss_average = sum(values['ncss']) / len(values['ncss'])
        ccn_average = sum(values['ccn']) / len(values['ccn'])

        average_data[file_name] = {'ncss': ncss_average, 'ccn': ccn_average}

    return average_data

file_path = 'test.xml'

with open(file_path, 'r') as xml_file:
    xml_data = xml_file.read()

parsed_data = parse_xml(xml_data)
averages = calculate_average(parsed_data)

output_file_path = 'output.json'

with open(output_file_path, 'w') as json_file:
    json.dump(averages, json_file, indent=2)

print(f"Results saved to {output_file_path}")
