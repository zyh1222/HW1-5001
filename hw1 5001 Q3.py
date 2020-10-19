import re

import xml.etree.ElementTree as ET

tree=ET.parse('blocklist.xml')
root1=tree.getroot()
#print(len(root1))
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
# for i in range(len(root1)):
#     for j in range(len(root1[i])):
#         temp=root1[i][j]
#         temp_str=root1[i][j].attrib['blockID']
#         if is_number(temp_str[len(temp_str)-1]):
#             if temp_str[0]=='i' :
#                 print("<emItem blockID=\"%s\" id=\"%s\">"%(temp.attrib['blockID'],temp.attrib['id']))
#             if temp_str[0]=='g' :
#                 print("<gfxBlacklistEntry blockID=\"%s\">"%(temp.attrib['blockID']))

for i in range(len(root1)):
    for j in range(len(root1[i])):
        temp=root1[i][j]
        if 'id' in temp.attrib:
            if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',temp.attrib['id']):
                print("<emItem blockID=\"%s\" id=\"%s\">"%(temp.attrib['blockID'],temp.attrib['id']))
            


