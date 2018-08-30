import xml.dom.minidom
# 负责解析XML文件
from xml.dom.minidom import parse
# 使用 minidom 打开 xml 文件
doctree = xml.dom.minidom.parse('student.xml')
# 得到文件对象
doc = doctree.documentElement
# 显示子元素
for ele in doc.childNodes:
    if ele.nodeName == 'Teacher':
        print('--------Node:{0}--------'.format(ele.nodeName))
        childs = ele.childNodes
        for child in childs:
            if child.nodeName == 'Name':
                # data 是文本节点的一个属性，表示他的值
                print('Name:{0}'.format(child.childNodes[0].data))
            if child.nodeName == 'Moble':
                print('Moble:{0}'.format(child.childNodes[0].data))
            if child.nodeName == 'Age':
                print('Age:{0}'.format(child.childNodes[0].data))
                if child.hasAttribute('datail'):
                    print('Age:{0}'.format(child.getAttribute('datail')))