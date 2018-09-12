from lxml import etree

'''
用 lxml 来解析 HTML 代码
'''

text = '''
<div>
    <ul>
        <li class="item-0"><a herf="0.html">frist item</a></li>
        <li class="item-1"><a herf="1.html">frist item</a></li>
        <li class="item-2"><a herf="2.html">frist item</a></li>
        <li class="item-3"><a herf="3.html">frist item</a></li>
        <li class="item-5"><a herf="4.html">frist item</a></li>
        <li class="item-5"><a herf="5.html">frist item</a>
    </ul>
</div>
'''
# 利用 etree.HTML 将字符串解析成 HTML 文档
html = etree.HTML(text)
s = etree.tostring(html)
print(s)