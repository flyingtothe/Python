# 结构化文件存储
- xml, json
- 为了解决不同设备之间信息交换
- xml
- json

# XML文件
- 参考资料
    - https://docs.python.org/3/library/xml.etree.elementtree.html
    - http://www.runoob.com/python/python-xml.html
    - https://blog.csdn.net/seetheworld518/article/details/49535285
- XML(eXtensibleMarkupLanguage)：可扩展标记语言
    - 标记语言：语言中使用艰苦哦靠括起来的文本字符串标记
    - 可扩展：用户可以自定义需要的标记
        
            <Teacher>
                自定义标记Teacher
                在两个标记之间任何内容都英语Teacher
            </Teacher>
    - XML 描述的是数据本身，技术局的结构与语义
    - HTML 侧重于如何显示 web 页面中的数据
- XML文档的构成
    - 处理指令
        - 只有一行，且必须在第一行
        - 以 xml 关键字开头
        - 一般用于声明xml的版本和采用的编码
            - version 属性必须
            - encoding 用来支出解释器使用的编码
    - 根元素
        - 一个文件只有一个根元素，树状结构
    - 子元素
    - 属性
    - 内容
    - 注释
        - <!---  -->    三短横线必须放在开头  
- 保留字处理
    - 使用符号与实际符号冲突时，使用实体引用表示保留字
    - CDATA 段内
- 命名空间
    - 为避免冲突，为元素添加命名空间
    - xmlns：xml name space
        <schooler xmlns:student='http://my_student' xmlns:room='my_room'>
            <student:Name>liu</student:Name>
            <room:Name>2014</room:Name>
        </schooler>

# XML访问
- 读取
    - xml 读取技术： SAX， DOM
    - SAX
        - 事件驱动型解释器
        - 利用 SAX 解析文档设计到解析器和时间处理两部分
        - 特点
            - 处理速度快
            - 流式读取
    - DOM
        - W3C规定的接口
        - xml 文件在缓存中以树状结构储存，读取
        - 用途
            - 定义 xml 文件仁义节点的信息
            - 添加删除相应内容
        - minidom
            -  minidom.parse(filename):加载读取的xml文件, filename也可以是xml代码
            - doc.documentElement:获取xml文档对象，一个xml文件只有一个对于的文档对象
            - node.getAttribute(attr_name):获取xml节点的属性值
            - node.getElementByTagName(tage_name)：得到一个节点对象集合
            - node.childNodes:得到所有孩子节点
            - node.childNodes[index].nodeValue:获取单个节点值
            - node.firstNode:得到第一个节点，等价于node.childNodes[0]
            - node.attributes[tage_name]
            - 案例 01
        - etree 
            - 以树形结构来表示xml
            - root.getiterator:得到相应的可迭代的node集合
            - root.iter
            - find(node_name):查找指定node_name的节点,返回一个node
            - root.findall(node_name):返回多个node_name的节点
            - node.tag: node对应的tagename
            - node.text:node的文本值
            - node.attrib： 是node的属性的字典类型的内容
            - 案例 02
        
    - xml文件写入
        - 更改
            - ele.set:修改属性
            - ele.append: 添加子元素
            - ele.remove:删除元素
            - 案例 03
        - 生成创建
            - SubElement, 案例 04
            - minidom 写入， 案例 05
            - etree创建， 案例 06