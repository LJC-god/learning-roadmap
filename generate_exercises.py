#!/usr/bin/env python3
"""
练习题生成器 - 为 20 个主题生成练习题和答案
"""

import json
import os
import random

random.seed(42)

def generate_python_basics_environment():
    topic = "Python 环境与基础"
    questions = []
    
    # 选择题
    multiple_choice = [
        {"id": 1, "difficulty": "easy", "question": "以下哪个不是 Python 语言的特性？", "options": ["解释型语言", "面向对象", "需要编译", "跨平台"], "answer": "C"},
        {"id": 2, "difficulty": "easy", "question": "Python 源代码文件的默认扩展名是什么？", "options": [".java", ".py", ".cpp", ".c"], "answer": "B"},
        {"id": 3, "difficulty": "easy", "question": "如何启动 Python 交互式解释器？", "options": ["python", "py", "python3", "都可以"], "answer": "D"},
        {"id": 4, "difficulty": "easy", "question": "在 Python 中，单行注释使用什么符号？", "options": ["//", "#", "/*", "--"], "answer": "B"},
        {"id": 5, "difficulty": "medium", "question": "PEP 是什么的缩写？", "options": ["Python Enhancement Proposal", "Python Edition Protocol", "Program Enhancement Process", "Python Execution Path"], "answer": "A"},
        {"id": 6, "difficulty": "medium", "question": "以下哪个不是 Python 的实现版本？", "options": ["CPython", "Jython", "Pyython", "IronPython"], "answer": "C"},
        {"id": 7, "difficulty": "easy", "question": "Python 2.x 和 Python 3.x 的主要区别是什么？", "options": ["语法完全相同", "print 语句变为函数", "没有区别", "性能差异很大"], "answer": "B"},
        {"id": 8, "difficulty": "easy", "question": "如何在命令行中运行 Python 脚本？", "options": ["python script.py", "run script.py", "execute script.py", "start script.py"], "answer": "A"},
        {"id": 9, "difficulty": "medium", "question": "IDLE 是什么？", "options": ["Python 的集成开发环境", "一种数据库", "一种操作系统", "一种编程语言"], "answer": "A"},
        {"id": 10, "difficulty": "easy", "question": "Python 是一种什么类型的语言？", "options": ["编译型语言", "解释型语言", "汇编语言", "机器语言"], "answer": "B"},
        {"id": 11, "difficulty": "medium", "question": "以下哪个不是常用的 Python IDE？", "options": ["PyCharm", "VS Code", "Eclipse", "MySQL"], "answer": "D"},
        {"id": 12, "difficulty": "easy", "question": "如何查看 Python 版本？", "options": ["python --version", "python -v", "两者都可以", "都不可以"], "answer": "C"},
        {"id": 13, "difficulty": "medium", "question": "pip 是什么？", "options": ["Python 包管理工具", "Python 解释器", "Python 调试器", "Python 编译器"], "answer": "A"},
        {"id": 14, "difficulty": "medium", "question": "如何安装 Python 包？", "options": ["pip install 包名", "python install 包名", "install 包名", "get 包名"], "answer": "A"},
        {"id": 15, "difficulty": "easy", "question": "venv 或 virtualenv 是什么？", "options": ["代码编辑器", "版本控制系统", "虚拟环境管理工具", "调试工具"], "answer": "C"},
        {"id": 16, "difficulty": "medium", "question": "使用虚拟环境的主要目的是什么？", "options": ["提高运行速度", "隔离项目依赖", "增加代码安全性", "减少内存占用"], "answer": "B"},
        {"id": 17, "difficulty": "easy", "question": "Python 的创始人是？", "options": ["Guido van Rossum", "James Gosling", "Bjarne Stroustrup", "Dennis Ritchie"], "answer": "A"},
        {"id": 18, "difficulty": "medium", "question": "Python 首次发布是在哪一年？", "options": ["1989", "1991", "1995", "2000"], "answer": "B"},
        {"id": 19, "difficulty": "easy", "question": "以下哪种不是 Python 的编程范式？", "options": ["面向过程", "面向对象", "函数式", "硬件级编程"], "answer": "D"},
        {"id": 20, "difficulty": "medium", "question": "在 Jupyter Notebook 中，运行单元格使用什么快捷键？", "options": ["Ctrl+C", "Shift+Enter", "Alt+Enter", "Ctrl+Enter"], "answer": "B"},
        {"id": 21, "difficulty": "medium", "question": "Anaconda 是什么？", "options": ["Python 解释器", "Python 包发行版", "代码编辑器", "操作系统"], "answer": "B"},
        {"id": 22, "difficulty": "easy", "question": "如何在 Python 中退出交互式解释器？", "options": ["exit()", "quit()", "Ctrl+D", "以上都可以"], "answer": "D"},
        {"id": 23, "difficulty": "medium", "question": "pyc 文件是什么？", "options": ["Python 源码文件", "Python 字节码文件", "Python 配置文件", "Python 编译文件"], "answer": "B"},
        {"id": 24, "difficulty": "easy", "question": "Python 是一种动态类型语言，这意味着什么？", "options": ["不需要声明变量类型", "运行速度慢", "语法灵活", "以上都是"], "answer": "A"},
        {"id": 25, "difficulty": "medium", "question": "GIL 是什么的缩写？", "options": ["Global Interpreter Lock", "General Input Logic", "Graphics Interface Library", "Generate Intermediate Language"], "answer": "A"},
    ]
    questions.extend(multiple_choice)
    
    # 判断题
    true_false = [
        {"id": 26, "difficulty": "easy", "question": "Python 是一种编译型语言。", "answer": "False"},
        {"id": 27, "difficulty": "easy", "question": "Python 代码在执行前需要先编译。", "answer": "False"},
        {"id": 28, "difficulty": "easy", "question": "Python 支持多种编程范式。", "answer": "True"},
        {"id": 29, "difficulty": "easy", "question": "Python 是开源免费的。", "answer": "True"},
        {"id": 30, "difficulty": "medium", "question": "Python 2.x 仍然是官方推荐使用的版本。", "answer": "False"},
        {"id": 31, "difficulty": "easy", "question": "Python 代码块通过缩进来定义。", "answer": "True"},
        {"id": 32, "difficulty": "medium", "question": "所有 Python 实现都使用 GIL。", "answer": "False"},
        {"id": 33, "difficulty": "easy", "question": "Python 可以在 Windows、Linux、Mac 等操作系统上运行。", "answer": "True"},
        {"id": 34, "difficulty": "medium", "question": "Python 3.x 完全向后兼容 Python 2.x。", "answer": "False"},
        {"id": 35, "difficulty": "easy", "question": "在 Python 中，变量不需要声明类型。", "answer": "True"},
        {"id": 36, "difficulty": "medium", "question": "Jython 代码可以调用 Java 类库。", "answer": "True"},
        {"id": 37, "difficulty": "easy", "question": "Python 使用空格或制表符进行缩进。", "answer": "True"},
        {"id": 38, "difficulty": "medium", "question": "Python 的缩进必须是 4 个空格。", "answer": "False"},
        {"id": 39, "difficulty": "easy", "question": "可以在同一行写多条 Python 语句。", "answer": "True"},
        {"id": 40, "difficulty": "medium", "question": "Python 的官方文档地址是 docs.python.org。", "answer": "True"},
    ]
    questions.extend(true_false)
    
    # 填空题
    fill_blank = [
        {"id": 41, "difficulty": "easy", "question": "Python 的创始人是 _____ van Rossum。", "answer": "Guido"},
        {"id": 42, "difficulty": "easy", "question": "Python 源代码文件的标准扩展名是 _____。", "answer": ".py"},
        {"id": 43, "difficulty": "easy", "question": "单行注释以 _____ 符号开头。", "answer": "#"},
        {"id": 44, "difficulty": "medium", "question": "PEP 的全称是 _____。", "answer": "Python Enhancement Proposal"},
        {"id": 45, "difficulty": "easy", "question": "Python 是一种 _____ 型（解释型/编译型）语言。", "answer": "解释型"},
        {"id": 46, "difficulty": "medium", "question": "CPython 是 Python 的 _____ 实现。", "answer": "官方"},
        {"id": 47, "difficulty": "easy", "question": "多行注释可以使用三引号（_____）来表示。", "answer": "''' 或 \"\"\""},
        {"id": 48, "difficulty": "medium", "question": "使用 _____ 命令可以安装 Python 包。", "answer": "pip"},
        {"id": 49, "difficulty": "easy", "question": "虚拟环境可以 _____（隔离/统一）项目依赖。", "answer": "隔离"},
        {"id": 50, "difficulty": "medium", "question": "Jython 运行在 _____ 虚拟机之上。", "answer": "JVM"},
        {"id": 51, "difficulty": "easy", "question": "Python 代码块通过 _____ 来定义作用域。", "answer": "缩进"},
        {"id": 52, "difficulty": "medium", "question": "IronPython 运行在 _____ 框架之上。", "answer": ".NET"},
        {"id": 53, "difficulty": "easy", "question": "Python 2.7 于 _____ 年发布。", "answer": "2010"},
        {"id": 54, "difficulty": "medium", "question": "pyc 文件是 Python 的 _____ 码文件。", "answer": "字节"},
        {"id": 55, "difficulty": "easy", "question": "在 Jupyter Notebook 中，按 _____ + Enter 可以运行单元格。", "answer": "Shift"},
    ]
    questions.extend(fill_blank)
    
    # 编程题
    coding = [
        {"id": 56, "difficulty": "easy", "question": "编写程序：打印 Hello, World!", "requirement": "使用 print() 函数输出 Hello, World!"},
        {"id": 57, "difficulty": "easy", "question": "编写程序：计算并打印 1+2+3+...+100 的和", "requirement": "使用循环计算 1 到 100 的累加和"},
        {"id": 58, "difficulty": "medium", "question": "编写程序：打印当前 Python 版本信息", "requirement": "使用 sys 模块获取版本信息"},
        {"id": 59, "difficulty": "easy", "question": "编写程序：打印你的名字和当前日期", "requirement": "使用 datetime 模块获取当前日期"},
        {"id": 60, "difficulty": "medium", "question": "编写程序：创建一个虚拟环境", "requirement": "使用 venv 模块创建虚拟环境"},
        {"id": 61, "difficulty": "easy", "question": "编写程序：使用 pip 安装 requests 包", "requirement": "在命令行中运行 pip install requests"},
        {"id": 62, "difficulty": "medium", "question": "编写程序：查看已安装的所有包及其版本", "requirement": "使用 pip list 命令"},
        {"id": 63, "difficulty": "easy", "question": "编写程序：在 Python 交互模式下计算 2 的 10 次方", "requirement": "使用 ** 运算符"},
        {"id": 64, "difficulty": "medium", "question": "编写程序：创建一个简单的 Python 脚本并运行它", "requirement": "创建包含多行代码的 .py 文件并执行"},
        {"id": 65, "difficulty": "easy", "question": "编写程序：使用帮助功能查看 print 函数的使用方法", "requirement": "使用 help(print)"},
    ]
    questions.extend(coding)
    
    return {
        "topic": topic,
        "total_questions": len(questions),
        "questions": questions
    }

def generate_python_variables():
    topic = "变量与数据类型"
    questions = []
    
    # 选择题
    multiple_choice = [
        {"id": 1, "difficulty": "easy", "question": "以下哪个不是 Python 的基本数据类型？", "options": ["int", "float", "array", "str"], "answer": "C"},
        {"id": 2, "difficulty": "easy", "question": "在 Python 中，变量必须先声明类型才能使用。", "options": ["正确", "错误", "有时需要", "视情况而定"], "answer": "B"},
        {"id": 3, "difficulty": "easy", "question": "下列哪个是 Python 的整数类型？", "options": ["int", "float", "str", "bool"], "answer": "A"},
        {"id": 4, "difficulty": "easy", "question": "Python 中，布尔类型的值包括哪些？", "options": ["0 和 1", "True 和 False", "yes 和 no", "on 和 off"], "answer": "B"},
        {"id": 5, "difficulty": "medium", "question": "type(3.14) 返回的结果是什么类型？", "options": ["int", "float", "str", "decimal"], "answer": "B"},
        {"id": 6, "difficulty": "easy", "question": "如何将字符串转换为整数？", "options": ["int('123')", "str(123)", "float('123')", "bool('123')"], "answer": "A"},
        {"id": 7, "difficulty": "medium", "question": "以下哪个函数可以获取变量的数据类型？", "options": ["type()", "typeof()", "datatype()", "gettype()"], "answer": "A"},
        {"id": 8, "difficulty": "easy", "question": "下列哪个不是字符串的表示方式？", "options": ["'hello'", '"hello"', '"hello"', "/hello/"], "answer": "D"},
        {"id": 9, "difficulty": "medium", "question": "在 Python 中，isinstance() 函数的作用是什么？", "options": ["判断变量是否存在", "判断变量是否为某种类型", "获取变量值", "修改变量类型"], "answer": "B"},
        {"id": 10, "difficulty": "easy", "question": "0b1010 表示什么？", "options": ["二进制数 10", "八进制数 10", "十六进制数 10", "十进制数 10"], "answer": "A"},
        {"id": 11, "difficulty": "medium", "question": "0xFF 表示什么？", "options": ["二进制数 255", "八进制数 255", "十六进制数 255", "十进制数 255"], "answer": "D"},
        {"id": 12, "difficulty": "easy", "question": "以下哪个是合法的变量名？", "options": ["2variable", "variable-2", "_variable", "class"], "answer": "C"},
        {"id": 13, "difficulty": "medium", "question": "以下哪个是 Python 的关键字？", "options": ["myvar", "variable", "class", "my_class"], "answer": "C"},
        {"id": 14, "difficulty": "easy", "question": "Python 中，单引号和双引号创建字符串有区别吗？", "options": ["有", "没有", "有时有", "取决于内容"], "answer": "B"},
        {"id": 15, "difficulty": "medium", "question": "str(123.45) 的结果是什么？", "options": ["123", "123.45", "123.0", "错误"], "answer": "B"},
        {"id": 16, "difficulty": "easy", "question": "len('hello') 返回什么？", "options": ["4", "5", "6", "hello"], "answer": "B"},
        {"id": 17, "difficulty": "medium", "question": "hex(255) 返回什么？", "options": ["0xff", "0xFF", "0xff", "0xFf"], "answer": "B"},
        {"id": 18, "difficulty": "easy", "question": "以下哪个不是不可变数据类型？", "options": ["int", "str", "list", "tuple"], "answer": "C"},
        {"id": 19, "difficulty": "medium", "question": "complex(1, 2) 创建的复数是什么？", "options": ["1+2i", "1+2j", "1.0+2.0j", "3j"], "answer": "B"},
        {"id": 20, "difficulty": "easy", "question": "type(None) 返回什么？", "options": ["NoneType", "Null", "Void", "None"], "answer": "A"},
        {"id": 21, "difficulty": "medium", "question": "round(3.14159, 2) 的结果是什么？", "options": ["3.14", "3.142", "3.1", "3.0"], "answer": "A"},
        {"id": 22, "difficulty": "easy", "question": "在 Python 中，变量赋值使用什么运算符？", "options": ["==", "=", "<-", ":="], "answer": "B"},
        {"id": 23, "difficulty": "medium", "question": "a = a + 1 可以简写为什么？", "options": ["a += 1", "a++", "++a", "a =+ 1"], "answer": "A"},
        {"id": 24, "difficulty": "easy", "question": "如何创建多行字符串？", "options": ["使用三引号", "使用换行符", "两者都可以", "无法创建"], "answer": "C"},
        {"id": 25, "difficulty": "medium", "question": "bool(0) 和 bool(1) 分别返回什么？", "options": ["True, True", "True, False", "False, True", "False, False"], "answer": "C"},
    ]
    questions.extend(multiple_choice)
    
    # 判断题
    true_false = [
        {"id": 26, "difficulty": "easy", "question": "Python 变量在赋值时不需要声明类型。", "answer": "True"},
        {"id": 27, "difficulty": "easy", "question": "Python 中的字符串是不可变的。", "answer": "True"},
        {"id": 28, "difficulty": "easy", "question": "Python 的整数类型有大小限制。", "answer": "False"},
        {"id": 29, "difficulty": "medium", "question": "在 Python 中，1 == '1' 返回 True。", "answer": "False"},
        {"id": 30, "difficulty": "easy", "question": "True 在数值运算中等价于 1。", "answer": "True"},
        {"id": 31, "difficulty": "easy", "question": "False 在数值运算中等价于 0。", "answer": "True"},
        {"id": 32, "difficulty": "medium", "question": "is 和 == 运算符完全等价。", "answer": "False"},
        {"id": 33, "difficulty": "easy", "question": "Python 支持链式赋值。", "answer": "True"},
        {"id": 34, "difficulty": "medium", "question": "Python 支持多变量同时赋值。", "answer": "True"},
        {"id": 35, "difficulty": "easy", "question": "del 可以删除变量。", "answer": "True"},
        {"id": 36, "difficulty": "medium", "question": "变量的类型一旦确定就不能改变。", "answer": "False"},
        {"id": 37, "difficulty": "easy", "question": "None 表示空值或无值。", "answer": "True"},
        {"id": 38, "difficulty": "medium", "question": "空字符串 '' 的布尔值为 True。", "answer": "False"},
        {"id": 39, "difficulty": "easy", "question": "空列表 [] 的布尔值为 False。", "answer": "False"},
        {"id": 40, "difficulty": "medium", "question": "Python 的复数类型使用 j 而不是 i 表示虚部。", "answer": "True"},
    ]
    questions.extend(true_false)
    
    # 填空题
    fill_blank = [
        {"id": 41, "difficulty": "easy", "question": "Python 的基本数据类型包括 int、float、str 和 _____。", "answer": "bool"},
        {"id": 42, "difficulty": "easy", "question": "使用 _____ 函数可以获取变量的类型。", "answer": "type"},
        {"id": 43, "difficulty": "easy", "question": "将字符串转换为整数使用 _____ 函数。", "answer": "int"},
        {"id": 44, "difficulty": "medium", "question": "将其他类型转换为字符串使用 _____ 函数。", "answer": "str"},
        {"id": 45, "difficulty": "easy", "question": "将十进制数转换为十六进制使用 _____ 函数。", "answer": "hex"},
        {"id": 46, "difficulty": "medium", "question": "判断变量是否为指定类型使用 _____ 函数。", "answer": "isinstance"},
        {"id": 47, "difficulty": "easy", "question": "0xFF 的十进制值是 _____。", "answer": "255"},
        {"id": 48, "difficulty": "medium", "question": "round(3.5) 的结果是 _____。", "answer": "4"},
        {"id": 49, "difficulty": "easy", "question": "空值的表示是 _____。", "answer": "None"},
        {"id": 50, "difficulty": "medium", "question": "0b1010 的十进制值是 _____。", "answer": "10"},
        {"id": 51, "difficulty": "easy", "question": "变量名不能以 _____ 开头。", "answer": "数字"},
        {"id": 52, "difficulty": "medium", "question": "使用 _____ 进行多变量交换：a, b = b, a", "answer": "解包"},
        {"id": 53, "difficulty": "easy", "question": "Python 的布尔类型名称是 _____。", "answer": "bool"},
        {"id": 54, "difficulty": "medium", "question": "创建一个复数使用 complex(实部, _____)。", "answer": "虚部"},
        {"id": 55, "difficulty": "easy", "question": "空列表的布尔值是 _____。", "answer": "True"},
    ]
    questions.extend(fill_blank)
    
    # 编程题
    coding = [
        {"id": 56, "difficulty": "easy", "question": "编写程序：创建变量 a、b、c，分别赋值 10、20、30", "requirement": "使用多个赋值语句"},
        {"id": 57, "difficulty": "easy", "question": "编写程序：交换两个变量的值", "requirement": "不使用临时变量"},
        {"id": 58, "difficulty": "medium", "question": "编写程序：判断一个变量的类型是否为字符串", "requirement": "使用 isinstance() 函数"},
        {"id": 59, "difficulty": "easy", "question": "编写程序：将字符串 '123' 转换为整数并相加", "requirement": "将 '10' 和 '20' 转换为整数后相加"},
        {"id": 60, "difficulty": "medium", "question": "编写程序：打印一个浮点数的整数部分和小数部分", "requirement": "使用 int() 和 % 运算符"},
        {"id": 61, "difficulty": "easy", "question": "编写程序：创建一个复数并分别提取实部和虚部", "requirement": "使用 complex() 函数"},
        {"id": 62, "difficulty": "medium", "question": "编写程序：比较 '==' 和 'is' 的区别", "requirement": "对 small integers 进行比较"},
        {"id": 63, "difficulty": "easy", "question": "编写程序：将十进制数转换为二进制、八进制、十六进制", "requirement": "使用 bin()、oct()、hex() 函数"},
        {"id": 64, "difficulty": "medium", "question": "编写程序：演示 Python 的动态类型特性", "requirement": "同一个变量先后赋值不同类型"},
        {"id": 65, "difficulty": "easy", "question": "编写程序：计算并打印 2 的 31 次方", "requirement": "使用 ** 运算符"},
    ]
    questions.extend(coding)
    
    return {
        "topic": topic,
        "total_questions": len(questions),
        "questions": questions
    }

def generate_python_control_flow():
    topic = "流程控制"
    questions = []
    
    # 选择题
    multiple_choice = [
        {"id": 1, "difficulty": "easy", "question": "以下哪个不是 Python 的流程控制语句？", "options": ["if", "for", "while", "switch"], "answer": "D"},
        {"id": 2, "difficulty": "easy", "question": "Python 中 elif 是什么的缩写？", "options": ["else if", "else elif", "elif else", "if else"], "answer": "A"},
        {"id": 3, "difficulty": "easy", "question": "for 循环通常用于什么情况？", "options": ["无限循环", "遍历序列", "条件循环", "递归"], "answer": "B"},
        {"id": 4, "difficulty": "medium", "question": "以下哪个可以正确终止循环？", "options": ["break", "stop", "end", "exit"], "answer": "A"},
        {"id": 5, "difficulty": "medium", "question": "continue 语句的作用是什么？", "options": ["终止程序", "跳过本次循环", "暂停循环", "继续下一次迭代"], "answer": "B"},
        {"id": 6, "difficulty": "easy", "question": "range(1, 10, 2) 生成什么序列？", "options": ["1,2,3,4,5,6,7,8,9", "1,3,5,7,9", "1,3,5,7,9,11", "2,4,6,8"], "answer": "B"},
        {"id": 7, "difficulty": "medium", "question": "以下哪个不是无限循环的写法？", "options": ["while True:", "while 1:", "while 0:", "for i in iter(lambda:1, 1):"], "answer": "C"},
        {"id": 8, "difficulty": "easy", "question": "Python 中 pass 语句的作用是什么？", "options": ["跳过代码", "空语句占位", "抛出异常", "终止程序"], "answer": "B"},
        {"id": 9, "difficulty": "medium", "question": "以下哪个可以创建随机数？", "options": ["random.randint(1,10)", "random.random(1,10)", "random.number(1,10)", "random.get(1,10)"], "answer": "A"},
        {"id": 10, "difficulty": "easy", "question": "if-elif-else 结构中，elif 可以出现多少次？", "options": ["0次", "1次", "任意次", "最多2次"], "answer": "C"},
        {"id": 11, "difficulty": "medium", "question": "else 子句可以与哪个循环配合使用？", "options": ["只限 for", "只限 while", "for 和 while 都可以", "都不可以"], "answer": "C"},
        {"id": 12, "difficulty": "easy", "question": "list comprehension 中 if 子句的作用是什么？", "options": ["循环控制", "条件过滤", "变量赋值", "函数调用"], "answer": "B"},
        {"id": 13, "difficulty": "medium", "question": "以下哪个不是有效的循环嵌套？", "options": ["for in for", "while in for", "for in while", "while in while"], "answer": "B"},
        {"id": 14, "difficulty": "easy", "question": "enumerate() 函数返回什么？", "options": ["索引和值的元组", "只返回值", "只返回索引", "列表"], "answer": "A"},
        {"id": 15, "difficulty": "medium", "question": "zip() 函数的作用是什么？", "options": ["压缩文件", "将多个序列打包", "解压缩", "排序"], "answer": "B"},
        {"id": 16, "difficulty": "easy", "question": "以下哪个运算符用于成员测试？", "options": ["==", "is", "in", "!="], "answer": "C"},
        {"id": 17, "difficulty": "medium", "question": "哪个函数可以将序列反转？", "options": ["reverse()", "reversed()", "flip()", "sort(reverse=True)"], "answer": "B"},
        {"id": 18, "difficulty": "easy", "question": "assert 语句的作用是什么？", "options": ["断言条件", "打印信息", "抛出异常", "注释代码"], "answer": "A"},
        {"id": 19, "difficulty": "medium", "question": "三元表达式的语法是什么？", "options": ["a if b else c", "b ? a : c", "if b a else c", "a ? b : c"], "answer": "A"},
        {"id": 20, "difficulty": "easy", "question": "match-case 是哪个 Python 版本引入的？", "options": ["Python 2", "Python 3.0", "Python 3.10", "Python 4"], "answer": "C"},
        {"id": 21, "difficulty": "medium", "question": "以下哪个不是 match-case 的模式？", "options": ["值匹配", "类型匹配", "通配符", "switch"], "answer": "D"},
        {"id": 22, "difficulty": "easy", "question": "列表推导式的基本语法是什么？", "options": ["[expr for item in iter]", "{expr for item in iter}", "(expr for item in iter)", "all of above"], "answer": "A"},
        {"id": 23, "difficulty": "medium", "question": "for-else 结构中，else 什么时候执行？", "options": ["循环正常结束时", "循环被 break 中断时", "循环出现错误时", "永不执行"], "answer": "A"},
        {"id": 24, "difficulty": "easy", "question": "input() 函数返回什么类型？", "options": ["int", "float", "str", "bool"], "answer": "C"},
        {"id": 25, "difficulty": "medium", "question": "如何从用户获取整数输入？", "options": ["int(input())", "input(int())", "input(int)", "int(input)"], "answer": "A"},
    ]
    questions.extend(multiple_choice)
    
    # 判断题
    true_false = [
        {"id": 26, "difficulty": "easy", "question": "Python 使用缩进来定义代码块。", "answer": "True"},
        {"id": 27, "difficulty": "easy", "question": "if 语句必须有 else 子句。", "answer": "False"},
        {"id": 28, "difficulty": "easy", "question": "for 循环必须指定迭代次数。", "answer": "False"},
        {"id": 29, "difficulty": "medium", "question": "break 语句只能退出当前层循环。", "answer": "True"},
        {"id": 30, "difficulty": "easy", "question": "continue 语句会跳过本次循环剩余代码。", "answer": "True"},
        {"id": 31, "difficulty": "medium", "question": "while 循环必须有终止条件。", "answer": "True"},
        {"id": 32, "difficulty": "easy", "question": "range(5) 生成 0,1,2,3,4。", "answer": "True"},
        {"id": 33, "difficulty": "medium", "question": "for 循环的 else 子句在 break 时不执行。", "answer": "True"},
        {"id": 34, "difficulty": "easy", "question": "列表推导式可以嵌套。", "answer": "True"},
        {"id": 35, "difficulty": "medium", "question": "assert 用来调试，不能用于生产环境。", "answer": "False"},
        {"id": 36, "difficulty": "easy", "question": "match-case 类似于其他语言的 switch-case。", "answer": "True"},
        {"id": 37, "difficulty": "medium", "question": "Python 没有 do-while 循环。", "answer": "True"},
        {"id": 38, "difficulty": "easy", "question": "pass 是空语句，不做任何事情。", "answer": "True"},
        {"id": 39, "difficulty": "medium", "question": "生成器表达式使用圆括号。", "answer": "True"},
        {"id": 40, "difficulty": "easy", "question": "input() 函数读取用户输入并返回字符串。", "answer": "True"},
    ]
    questions.extend(true_false)
    
    # 填空题
    fill_blank = [
        {"id": 41, "difficulty": "easy", "question": "使用 _____ 关键字定义条件语句。", "answer": "if"},
        {"id": 42, "difficulty": "easy", "question": "使用 _____ 关键字定义循环。", "answer": "for"},
        {"id": 43, "difficulty": "easy", "question": "使用 _____ 关键字跳出循环。", "answer": "break"},
        {"id": 44, "difficulty": "medium", "question": "使用 _____ 关键字跳过本次循环。", "answer": "continue"},
        {"id": 45, "difficulty": "easy", "question": "range(5) 的起始值默认是 _____。", "answer": "0"},
        {"id": 46, "difficulty": "medium", "question": "range(start, stop, step) 中 stop 是 _____（包含/不包含）的。", "answer": "不包含"},
        {"id": 47, "difficulty": "easy", "question": "使用 _____ 进行循环中的条件判断。", "answer": "if"},
