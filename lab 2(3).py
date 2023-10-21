import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
n_dict = {}
d = []
for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Nominal':
                if child.firstChild.nodeType == 3:

                    name = child.firstChild.data
            if child.tagName == 'Name':
                if child.firstChild.nodeType == 3:

                    nominal = child.firstChild.data

    n_dict[nominal] = name
for i in n_dict:
    if n_dict[i] == '1':
        d.append(i)

print(d)






