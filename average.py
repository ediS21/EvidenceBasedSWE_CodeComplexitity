import xml.etree.ElementTree as ET
import json

def calculate_average_ncss_ccn(item):
    ncss = int(item.find('value[2]').text)
    ccn = int(item.find('value[3]').text)
    num_functions = int(item.find('value[4]').text)

    average_ncss = ncss / num_functions if num_functions != 0 else 0
    average_ccn = ccn / num_functions if num_functions != 0 else 0

    return average_ncss, average_ccn

def process_xml(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    result = []

    for item in root.findall('.//item'):
        file_name = item.attrib.get('name', '')
        average_ncss, average_ccn = calculate_average_ncss_ccn(item)

        result.append({
            "file_name": file_name,
            "average_ncss": average_ncss,
            "average_ccn": average_ccn
        })

    return result

if __name__ == "__main__":
    xml_file_path = "test2.xml"
    output_json_file = "output.json"

    result = process_xml(xml_file_path)

    with open(output_json_file, 'w') as json_file:
        json.dump(result, json_file, indent=2)

    print(f"Output written to {output_json_file}")
