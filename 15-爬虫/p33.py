from lxml import etree

# 只能读取 xml 文件，HTML 报错
html = etree.parse('./p31.html')
print(type(html))

rst = html.xpath('//book')
print(type(rst))
print(rst)

# 查找带有 category 属性值为 sport 的 book 元素
rst = html.xpath('//book[@category="sport"]')
print(type(rst))
print(rst)

# 查找带有 category 属性值为 sport 的 book 元素下的 year 元素
rst = html.xpath('//book[@category="sport"]/year')
rst = rst[0]
print(type(rst))
print(rst.tag)
print(rst.text)