# encoding:utf-8

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

# rootfileName="./xmltest.xml"
rootfileName="./test.xml"


def readXML():
	tree = ET.ElementTree(file='test.xml')
	map = tree.getroot();
	print(map.tag, map.attrib)
	for datasource in map:
		print(datasource.tag, datasource.attrib)
		print(datasource.attrib['name'], datasource.attrib['type'])
		key = datasource.attrib;
		print(list(key.keys()))
		for style in datasource:
			print(style.attrib['name'])
			for rule in style:
				scale = rule.find('test1')
				print(scale.tag, scale.text)

				catalog = rule.find('test2');
				print(catalog.tag, catalog.text)

				code = rule.find('test3');
				print(code.tag, code.text)

				priority = rule.find('test4')
				print(priority.tag, priority.text)


		if 'href' in datasource.attrib:
			print(datasource.attrib['href'])
			subtree = ET.ElementTree(file=datasource.attrib['href'])
			subMap = subtree.getroot();
			print(subMap.tag, subMap.attrib['name'])
			for rule in subMap:
				scale = rule.find('test1')
				print(scale.tag, scale.text)

				catalog = rule.find('test2');
				print(catalog.tag, catalog.text)

				code = rule.find('test2');
				print(code.tag, code.text)

				priority = rule.find('test3')
				print(priority.tag, priority.text)
	tree.write('person.xml', 'utf-8','<?xml version="1.0" encoding="utf-8"?>')

def writeXML():
	print("writeXML")
	root = ET.Element('QuoteWerksXML')
	tree = ET.ElementTree(root)
	ver = ET.SubElement(root, "AppVersionMajor")
	ver.text = '5.1'
	tree.write('person.xml')

if __name__ == '__main__':
	readXML()

