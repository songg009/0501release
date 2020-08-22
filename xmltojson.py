import json
import xmltodict
xml_file = open("E:/songg/PycharmProjects/files.xml")
xml_str = xml_file.read()

jsonStr = json.dumps(xmltodict.parse(xml_str),indent=4)

#print(jsonStr)
f =open("json.txt","w")

print(jsonStr,file=f)
f.close()