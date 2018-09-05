# GUI介绍
- GraphicalUserInterface
- GUI for Python: Tinter, wxpython, PyQt
- TKinter:
    - 绑定的是 TK GUI 工具集，用来包装 python 的 tcl 代码
- PyGTK
    - TKinter 的替代品
- wxPython
    - 跨平台的 python GUI
- PyQt
    - 跨平台的
    - 需要商业授权
- Jython
    - 程序可以和 Java 无缝集成

- 推荐资料
    - 辛星GUI, 辛星Python
    - Python GUI Proguamming cookbook
    - Tkinter reference a GUI for Python

# TKINTER
- Tkinter 是 Python 的标准 GUI 库
- 注意：Python3.x 版本使用的库名为 tkinter,即首写字母 T 为小写。
    - 创建案例 01
- 组件
    - 参数：master: 按钮的父容器     options: 可选项，即该按钮的可设置的属性。这些选项可以用键 = 值的形式设置，并以逗号分隔。
    - 按钮
        - Button            按钮组件用于在程序中添加按钮，按钮上可以放上文本或图像，按钮可用于监听用户行为，能与 Python 函数关联，当按钮被按下时，自动调用该函数
            - 语法：w = Button ( master, option=value, ... )
            - 可选项：
                - activebackground  当鼠标放上去时，按钮的背景色
                - activeforeground  当鼠标放上去时，按钮的前景色
                - bd                按钮边框的大小，默认为 2 个像素
                - bg                按钮的背景色，如bg=”red”，bg="#FF56EF"
                - command           按钮关联的函数，当按钮被点击时，执行该函数
                - fg                按钮的前景色（按钮文本的颜色），如bg=”red”，bg="#FF56EF"
                - font              字体及大小，如font=("Arial", 8)，font=("Helvetica 16 bold italic")
                - height            设置显示高度、如果未设置此项，其大小以适应内容标签
                - highlightcolor    要高亮的颜色，如highlightcolor=”red”，highlightcolor="#FF56EF"
                - image             按钮上要显示的图片，image= PhotoImage(file="../xxx/xxx.gif") ,目前仅支持gif,PGM,PPM格式的图片
                - justify           显示多行文本的时候,设置不同行之间的对齐方式，可选项包括LEFT, RIGHT, CENTER
                - padx              按钮在x轴方向上的内边距(padding)，是指按钮的内容与按钮边缘的距离
                - pady              按钮在y轴方向上的内边距(padding)
                - relief            边框样式，设置控件3D效果，可选的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT。
                - state             设置按钮组件状态,可选的有正常(normal),激活(active),禁用(disabled)。默认 NORMAL。
                - underline         下划线。默认按钮上的文本都不带下划线。取值就是带下划线的字符串索引，为 0 时，第一个字符带下划线，为 1 时，前两个字符带下划线，以此类推
                - width             按钮的宽度，如未设置此项，其大小以适应按钮的内容（文本或图片的大小）
                - wraplength        限制按钮每行显示的字符的数量，默认为0
                - text              按钮的文本内容
                - anchor            锚选项，控制文本的位置，默认为中心，可用值:n(north),s(south),w(west),e(east),和ne,nw,se,sw
                
            - 组件方法
                - deselect() 	清除单选按钮的状态
                - flash() 	    在激活状态颜色和正常颜色之间闪烁几次单选按钮，但保持它开始时的状态。
                - invoke() 	    可以调用此方法来获得与用户单击单选按钮以更改其状态时发生的操作相同的操作
                - select() 	    设置单选按钮为选中。
            - 案例 02
        
        - Checkbutton	    多选框控件；用于在程序中提供多项选择框
            - 语法：w = Checkbutton ( master, option=value, ... )
            - 可选项
                - activebackground      当鼠标放上去时，按钮的背景色
                - activeforeground      当鼠标放上去时，按钮的前景色
                - bg                    按钮的背景色
                - bitmap                指定位图，如bitmap= BitmapImage(file = filepath)
                - bd                    边框的大小，默认为 2 个像素
                - command               关联的函数，当按钮被点击时，执行该函数
                - cursor                光标的形状设定，如arrow, circle, cross, plus 等
                - disabledforeground    禁用选项的前景色
                - font                  文本字体
                - fg                    选项的前景色
                - height                复选框文本行数，默认为 1。
                - highlightcolor        聚焦的高亮颜色
                - image                 是否使用图标
                - justify               显示多行文本的时候,设置不同行之间的对齐方式，可选项包括LEFT, RIGHT, CENTER
                - offvalue              Checkbutton 的值不仅仅是 1 或 0，可以是其他类型的数值，可以通过 onvalue 和 offvalue 属性设置 Checkbutton 的状态值。
                - onvalue               Checkbutton 的值不仅仅是 1 或 0，可以是其他类型的数值，可以通过 onvalue 和 offvalue 属性设置 Checkbutton 的状态值。
                - padx                  按钮在x轴方向上的内边距(padding)，是指按钮的内容与按钮边缘的距离，默认为 1 像素。
                - pady                  按钮在y轴方向上的内边距(padding)，默认为 1 像素。
                - relief                边框样式，设置控件3D效果，可选的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT。
                - selectcolor           选中后的颜色，默认为 selectcolor="red"
                - selectimage           选中后的图片
                - state                 状   态，默认为 state=NORMAL
                - text                  显示的文本，使用 "\n" 来对文本进行换行。
                - underline             下划线。默认按钮上的文本都不带下划线。取值就是带下划线的字符串索引，为 0 时，第一个字符带下划线，为 1 时，前两个字符带下划线，以此类推
                - variable              变量，variable 的值为 1 或 0，代表着选中或不选中
                - width                 默认宽度是复选框的文本或图像决定的，你可以设置指定字符数。
                - wraplength            是否设置包裹。
            
            - 组件方法
                - deselect() 	清除复选框选中选项
                - flash() 	    在激活状态颜色和正常颜色之间闪烁几次单选按钮，但保持它开始时的状态。
                - invoke() 	    可以调用此方法来获得与用户单击单选按钮以更改其状态时发生的操作相同的操作
                - select() 	    设置单选按钮为选中
                - toflle()     选中与没有选中的选项互相切换
            
            - 案例 03
        
        - Radiobutton	单选按钮控件；显示一个单选的按钮状态
            - 案例 04
        
        - Listbox	    列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户
            - 案例 05
        
    - 文本输入
        - Entry	        输入控件；用于显示简单的文本内容
            - 语法：w = Entry( master, option, ... )
            - 可选项
                - bg                输入框背景颜色
                - bd                边框的大小，默认为 2 个像素
                - cursor            光标的形状设定，如arrow, circle, cross, plus 等
                - font              文本字体
                - exportselection   默认情况下，你如果在输入框中选中文本，默认会复制到粘贴板，如果要忽略这个功能刻工艺设置 exportselection=0。
                - fg                文字颜色。值为颜色或为颜色代码，如：'red','#ff0000'
                - highlightcolor    文本框高亮边框颜色，当文本框获取焦点时显示
                - justify           显示多行文本的时候,设置不同行之间的对齐方式，可选项包括LEFT, RIGHT, CENTER
                - relief            边框样式，设置控件3D效果，可选的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT。
                - selectbackground  选中文字的背景颜色
                - selectborderwidth 选中文字的背景边框宽度
                - selectforeground  选中文字的颜色
                - show              指定文本框内容显示为字符，值随意，满足字符即可。如密码可以将值设为 show="*"
                - state             默认为 state=NORMAL, 文框状态，分为只读和可写，值为：normal/disabled
                - textvariable      文本框的值，是一个StringVar()对象
                - width             文本框宽度
                - xscrollcommand    设置水平方向滚动条，一般在用户输入的文本框内容宽度大于文本框显示的宽度时使用。
            
            - 组件方法
                - delete ( first, last=None )   删除文本框里直接位置值
    
                        text.delete(10)      # 删除索引值为10的值
                        text.delete(10, 20)  # 删除索引值从10到20之前的值
                        text.insert(0, END)  # 删除所有值
                
                - get()                         获取文件框的值
                - icursor ( index )             将光标移动到指定索引位置，只有当文框获取焦点后成立
                - index ( index )               返回指定的索引值
                - insert ( index, s )           向文本框中插入值，index：插入位置，s：插入值
                - select_adjust ( index )       选中指定索引和光标所在位置之前的值
                - select_clear()                清空文本框
                - select_from ( index )         设置光标的位置，通过索引值 index 来设置
                - select_present()              如果有选中，返回 true，否则返回 false。
                - select_range ( start, end )   选中指定索引位置的值，start(包含) 为开始位置，end(不包含) 为结束位置start必须比end小
                - select_to ( index )           选中指定索引与光标之间的值
                - xview ( index )               该方法在文本框链接到水平滚动条上很有用。
                - xview_scroll ( number, what ) 用于水平滚动文本框。 what 参数可以是 UNITS, 按字符宽度滚动，或者可以是 PAGES, 按文本框组件块滚动。 number 参数，正数为由左到右滚动，负数为由右到左滚动。
            
            - 案例 06
        
        - Text	        文本控件；用于显示多行文本
            - 案例 07
        
    - 标签
        - Label	        标签控件；可以显示文本和位图
            - 案例 08

        - Message	    消息控件；用来显示多行文本，与label比较类似
            - 案例 09
    
    - 菜单
        - Menubutton	菜单按钮控件，由于显示菜单项。
            - 案例 10

        - Menu	        菜单控件；显示菜单栏,下拉菜单和弹出菜单
            - 案例 11
    
    - 滚动条
        - Scale	        范围控件；显示一个数值刻度，为输出限定范围的数字区间
            - 案例 12

        - Scrollbar	    滚动条控件，当内容超过可视化区域时使用，如列表框。.
            - 案例 13
    
    - 其他组件
        - Canvas	        画布控件；显示图形元素如线条或文本
            - 语法下：w = Canvas ( master, option=value, ... )
            - 可选项
                - bd                边框宽度，单位像素，默认为 2 像素。
                - bg                背景色
                - confine           如果为 true (默认), 画布不能滚动到可滑动的区域外。
                - cursor            光标的形状设定，如arrow, circle, cross, plus 等
                - height            高度
                - highlightcolor    要高亮的颜色
                - relief            边框样式,可选值为 FLAT、SUNKEN、RAISED、GROOVE、RIDGE。 默认为 FLAT。
                - scrollregion      一个元组 tuple (w, n, e, s) ，定义了画布可滚动的最大区域，w 为左边，n 为头部，e 为右边，s 为底部。
                - width             画布在 X 坐标轴上的大小。
                - xscrollincrement  用于滚动请求水平滚动的数量值。
                - xscrollcommand    水平滚动条，如果画布是可滚动的，则该属性是水平滚动条的 .set（）方法。
                - yscrollincrement  类似 xscrollincrement, 但是垂直方向。
                - yscrollcommand    垂直滚动条，如果画布是可滚动的，则该属性是垂直滚动条的 .set（）方法。
        
            - 案例 14
            
        - Frame	        框架控件；在屏幕上显示一个矩形区域，多用来作为容器
            - 案例 15
    
        - Toplevel	    容器控件；用来提供一个单独的对话框，和Frame比较类似
            - 案例 16
    
        - Spinbox	    输入控件；与Entry类似，但是可以指定输入范围值
            - 案例 17
    
        - PanedWindow	PanedWindow是一个窗口布局管理的插件，可以包含一个或者多个子控件。
            - 案例 18
    
        - LabelFrame	labelframe 是一个简单的容器控件。常用与复杂的窗口布局。
            - 案例 19
    
        - messagebox	用于显示你应用程序的消息框。
            - 案例 20

# 组建的大致使用步骤
- 1.创建总面板
- 2.创建面板上的各种组件
    - 1.利用组件的父组件，即依附关系
    - 2.利用相应的属性对组件进行设置
    - 3.给组件安排布局
- 3.类似步骤2，创建多个组件
- 4.最后，启动总面板的消息循环