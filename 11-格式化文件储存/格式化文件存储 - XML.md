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
            <student Name>liu</student:Name>
            <room:Name>2014</room:Name>
        </schooler>

# XML访问
- 读取
    - xml 读取技术： SAX， DOM
    - SAX
            