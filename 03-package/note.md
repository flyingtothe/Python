#1.模块
- 包含python代码的文件
- 定义模块
    - 与普通代码书写要求一致
    - 需在模块砦蟹一下内容
        - 函数（单一功能）
        - 类（相似功能的组合或类似业务模块）
        - 测试代码
- 模块使用
    - 模块直接导入
        - 加入模块名称以数字开头
    - 语法：import module_name
             module_name.function_name
             module_name.class_name
         - 案例：p01,p02,01
    - import 模块 as 别名
        - 导入时给模块起别名
        - 案例：:p03
    - from module_name import func_name, class_name
        - 从模块中导入指定功能
        - 使用时可直接导入内容，不需要前缀
        - 案例 p04
    - from module_name import *
        - 导入模块所有内容
        - 案例p05
- if __name__ == '__main__'的使用
    - 可以有效避免模块代码被倒入时执行的问题
    - 建议所有代码以此为入口

# 2.模块的搜索路径和存储
- 模块搜索路径：加载模块时，系统会在哪些地方寻找此模块
- 系统默认的模块路径
        import sys
        sys.path 属性可获取路径列表
        案例:p06
- 添加搜索路径
        sys.path.append(dir)
- 模块加载顺序
    1.搜索内存中已经加载好的模块
    2.搜索python的内置模块
    3.搜索sys.path路径
    
# 包
- 是一种组织管理代码的方式，包中存放模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包结构
        |---包
        |---|---__init__.py     包的标志性文件
        |---|---模块1
        |---|---模块2
        |---|---子包（子文件夹）
        |---|---|---__init__.py
        |---|---|---子包模块1
- 包导入操作
    - import package_name
        - 直接倒入一个包，可使用__init__.py中的内容
        package_name.func_name
        package_name.class_name.func_name()
        案例：pkg01,p07
    - import package_name as 别名
        - 使用方法与上述一致
        - 注意：此方法默认导入__init__.py中的内容
    - improt package.module
        - 导入包中某一个具体模块
        - 使用方面
            package.module.func_name
            package.module.class.fun()
            package.module.class.var
            案例：p08
    - import package.module as pm
- from ... import 导入
    - from package import module1， mod2,....
    - 此种方法不执行__init__的内容

    -from package import *
        - 导入当前包__init__.py文件中所有的函数和泪
        - 使用方法
                func_name()
                class_name.func_name()
                class_name.var
        _ 案例p09 注意侧重导入的具体内容
    - from package.module import *
        - 导入包中指定的模块的所有内容
                func_name()
                class_name.func_name()
- 再开发环境中使用其他模块，可在当钱包直接导入其他模块中的内容
    - import 完整的包或模块路径
- __all__用法
    - 在使用 from package import* 时候，* 可导入的内容
    - __init__.py中如无文件，或没有__all__，那么只可以吧__init__中的内容导入
    - __init__ 如果设置了__all__的值，则按照__all__指定的子包或模块进行加载，如此则不会载入__init__中的内容

