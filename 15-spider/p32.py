from lxml import etree

# 只能读取 xml 文件，HTML 报错
html = etree.parse('./p31.html')
rst = etree.tostring(html, pretty_print=True)
print(rst)