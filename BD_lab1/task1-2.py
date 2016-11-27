import string

import lxml.etree as etree
from lxml import html
import requests

'''
root=etree.Element("DOM")
ready = etree.SubElement(root,"ready")
cmd = etree.SubElement(ready, "cmd", id = "34.26", align = "left")
message = etree.SubElement(cmd, "message").text = "GO"
tree = etree.tostring(root, pretty_print= True, encoding='utf-8',xml_declaration=True)
f=open("lab.xml","w")
f.writelines(tree)
f.close()
tree=etree.parse("lab.xml")
first_search=tree.xpath("//ready")

print first_search

search_2 = tree.xpath('//cmd[@id="34.26"]')
print  search_2
'''
#task1
url1 = 'http://isport.ua/'
root=etree.Element('root')
count =1

doc = etree.SubElement(root, 'data')
tree = etree.HTML(requests.get(url1).text)
url = tree.xpath('/html/body//a//@href')


for a in url :
        if (string.find(a, 'isport.ua') != -1 and string.find(a, 'mailto') == -1 and string.find(a,'javascript') == -1):
            if count <= 20:
                print count, a
                tree = etree.HTML(requests.get(a).text)
                img = tree.xpath('/html/body//img/@src')
                text2 = tree.xpath('/html/body//a//text()')
                url_el = etree.SubElement(doc,"page", url = a)
                for i in img:
                 etree.SubElement(url_el, "photo").text = i
                for i in text2:
                    etree.SubElement(url_el, "text").text = i
            count = count + 1

tree = etree.tostring(root, pretty_print = True, encoding = 'utf-8', xml_declaration = True)
f = open("task1.xml","w")
f.writelines(tree)
f.close()

#task2
tree = etree.parse("task1.xml")
root = tree.getroot()
text = tree.xpath("//page")
mpage = text[0].attrib
for a in text:
    count = 0
    s = a.xpath(".//photo/text()")
    for st in s:
        count = count + 1
        mpage = a.attrib
    print mpage, ":", count



