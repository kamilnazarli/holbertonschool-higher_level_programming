#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element(filename)

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)

        if isinstance(value, list):
            for item in value:
                item_el = ET.SubElement(child, "item")
                item_el.text = str(item)
        else:
            child.text = str(value)
    with open(filename, "w") as f:
        f.write(ET.tostring(root, encoding='unicode'))

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}

    for child in root:
        if len(child) > 0:
            result[child.tag] = [item.text for item in child]
        else:
            result[child.tag] = child.text
    return result
