import xml.etree.cElementTree as et
import pandas as pd

xml_tree = et.ElementTree(file='test.xml')
dfcols = ['sentence', 'opinionated', 'polarity']
df_xml = pd.DataFrame(columns=dfcols)
root = xml_tree.getroot();

for sub_node in root:
    for node in sub_node:
        #print(node, node.tag, node.attrib, node.text)
        sentence = node.text
        opinionated = node.attrib.get('opinionated')
        polarity = node.attrib.get('polarity')

        df_xml = df_xml.append(
            pd.Series([sentence, opinionated, polarity], index=dfcols),
            ignore_index=True)


