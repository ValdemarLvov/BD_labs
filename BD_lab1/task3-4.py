import lxml.etree as etree
import requests
#task3
url = "http://www.moyo.ua/search.html?posted=1&s%5Btext%5D=Apple&x=0&y=0"
root = etree.Element("root")

tree = etree.HTML(requests.get(url).text)
doc = etree.SubElement(root, "data")
name = tree.xpath('//a[@class="goods_title ddd"]/text()')
image = tree.xpath('//a[@class="goods_image"]/img/@src')
price = tree.xpath('//div[@class="goods_price"]/text()' )
#description = tree.xpath('//*[@class="row"]//text()' )


k=1
for i in range(21):
    node = etree.SubElement(doc, 'product', id=str(i + 1))
    etree.SubElement(node, 'name').text = name[i]
    etree.SubElement(node, 'price').text = price[i+k]
    etree.SubElement(node, 'image').text = image[i]
    k += 2
    tree = etree.tostring(root, pretty_print=True, encoding='utf-8', xml_declaration=True)
    f = open("task3.xml", "w")
    f.writelines(tree)
    f.close()

#task4

tree = etree.parse("task3.xml")
xslt_root = etree.XML('''\
<?xml version="1.0" encoding="WINDOWS-1251"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html xmlns="http://www.w3.org/1999/xhtml">
<style>
   h1 {
    font-family: 'Times New Roman', Times, serif;
    font-size: 250%;
    font-align: center;
   }
   p {
    font-family: Verdana, Arial, Helvetica, sans-serif;
    font-size: 25pt;
   }
</style>

<h1> MOYO.UA </h1>
<table>

<xsl:for-each select="root/data">
<xsl:for-each select="product">

<product>
<tr>
<th width="200">
<img align = "center" >
<xsl:attribute name="src">
<xsl:value-of select="image"/>
</xsl:attribute>
</img>
</th>

<td  width="200" align = "center">
<p>
<xsl:value-of select="name"/>
</p>
</td>

<th width="200" align = "center">
<h1>
<xsl:value-of select="price"/>
</h1>
</th>
</tr>
</product>

</xsl:for-each>
</xsl:for-each>
</table>
</html>
</xsl:template>
</xsl:stylesheet>''')

transform = etree.XSLT(xslt_root)

my_file = open("task4.xhtml", 'w')
my_file.write(etree.tostring(transform(tree)))
my_file.close()










