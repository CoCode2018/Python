# -*- encoding: utf-8 -*-

"""
1.上次课内容回顾
2.作业讲解
3.本次课主要内容
    1.计算机硬件、程序和操作系统的基本理解
        学习计算机系统能更好的理解程序的指令在计算机和它的组件上所起的效果
        总线
            总线连接，CPU、内存、存储设备、输入设备、输出设备、通信设备
            数据和电信号沿着总线从计算机中的一个部分传送到另一个部分；
            个人计算机中：总线被内嵌在计算机主板上，主板是将所有部件连接在一起的电路板
        CPU：
            控制单元(协调其他组件)、算数逻辑单元(进行算术运算和逻辑运算)
            每台计算机都有一个内部时钟，该时钟会以一个稳定的速度发射电子脉冲，这些脉冲用于控制各种操作的步调。
            时钟速度越快改定时间段内执行的指令就越多，时钟速度计量单位为赫兹，1赫兹 = 每秒1个赫兹(1兆赫 = 100万赫兹)
            CUP的核心，core是处理器中完成读取指令和执行指令的部分，为了提高处理能力出现多核CPU
        内存：
            比特和字节
                二进制数字称为比特，计算机中最小的存储单元是字节，一个字节 = 8个比特
                各种数据被编码成一个字节序列，计算机系统根据编码表自动完成编码和解码
                编码表是一套规则，用于控制计算机如何将字符、数字、符合翻译成计算机真正能够使用的数据
            内存(RAM)
                内存由多个有序地字节序列组成，用来存储程序和程序使用的数据，程序和数据必须加载到内存才能执行
                内存中的每个字节都有一个唯一的地址，通过地址可以定位存储和获取数据的字节
                因为可以任意顺序方位内存中的字节，内存也被称为随机访问存储器(RAM)
            存储设备
                内存中的数据不稳定，断电后内存中的数据全都丢失，程序和数据永久的保存在存储设备上，当运行和需要他们的时候被自动载入到内存
                内存的执行速度比存储设备快得多
                存储介质：存储数据或程序指令的地方
                驱动器：从存储介质上读取和写入的工具
                    磁盘驱动器
                    光盘驱动器
                    USB闪存
            输入设备
                键盘
                鼠标
            输出设备
                显示器
                打印机
            通信设备
                无线适配去
                有限网络接口卡
                调制解调器
        程序设计语言
            机器语言
            汇编语言、汇编器(将汇编语言翻译机器代码)【低级语言：汇编语言的每条指令对应机器代码编写的指令，本质上更接近机器语言(不同机器的指令集不同)而不是独立于机器】
            高级语言：独立于机器平台，可以跨平台，每一条指令称为语句
                使用高级语言编写的程序称为源程序或源代码，计算机并不能理解这些源程序，因此需要编译器或者解释器，将源代码翻译成计算机能够理解和执行的机器代码
                解释器，从源代码中读取一条语句，将它翻译成机器代码或者虚拟机代码，然后执行
                编译器，将整个源代码翻译组成机器代码，然后执行
        操作系统
            多程序设计(多个程序之间共享CPU同步运行)
            多线程：单个程序可以同时执行多个任务
                一个程序可以边做这个边做那个
                进程是资源（CPU、内存等）分配的基本单位，它是程序执行时的一个实例。程序运行时系统就会创建一个进程，并为它分配资源，然后把该进程放入进程就绪队列，进程调度器选中它的时候就会为它分配CPU时间，程序开始真正运行。
                Linux系统函数fork()可以在父进程中创建一个子进程，这样的话，在一个进程接到来自客户端新的请求时就可以复制出一个子进程让其来处理，父进程只需负责监控请求的到来，然后创建子进程让其去处理，这样就能做到并发处理。
            多进程：并行处理，使用多个处理器一起完成同时发生的多个子任务
                为了完成一个任务需要同时做
                线程是程序执行时的最小单位，它是进程的一个执行流，是CPU调度和分派的基本单位，一个进程可以由很多个线程组成，线程间共享进程的所有资源，每个线程有自己的堆栈和局部变量。线程由CPU独立调度执行，在多CPU环境下就允许多个线程同时运行。同样多线程也可以实现并发操作，每个请求分配一个线程来处理。
    2.Python简介
        Guido van Rossum(吉多.范罗苏姆、龟叔)
        1989 阿姆斯特丹 圣诞节 作为ABC语言的继承发明的脚本语言

        应用：
            云计算
            web开发
            科学运算、人工智能
            系统运维
            数据分析
            图像处理
            金融
        简介：Python是动态的解释性弱类型语言
            解释性和编译型语言
                编译型：把源文件中的源程序交给编译器，编译器把源文件都转换为编译后得二进制文件，然后由计算机执行二进制文件
                    运行速度快
                    编译速度慢，开发效率低；
                    例子
                        C
                        C++
                        GO
                        Swift
                        OC
                解释性：源文件中的程序一条一条的执行，每读取一行程序，都交给解释器，转换成字节码文件，然后执行
                    开发效率高；跨平台兼容性好
                    运行速度慢
                    例子：
                        JavaScript
                        Python
                        Ruby
                混合型：编译成字节码，然后一行行执行
                    C#
                    Java

    3.Python安装
        Python优点：
            优雅、明确、简单
            开发效率高
            高级语言
            可移植性
            可拓展性、可嵌入性
        Python缺点：
            运行速度慢
            代码不能加密
            线程不能利用多CPU问题
        Python解释器
            Python程序一行一行的把代码交给解释器，解释器一行一行的把代码转换为字节码，交给虚拟机运行
            CPython
                将Python程序转换成C语言
            IPython
                基于CPython之上的一个交互式解释器，在交互上有所增强，执行代码的功能和CPython一样
            JyPython
                Jython是运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行。
            IronPython
                IronPython和Jython类似，只不过IronPython是运行在微软.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码。
            PyPy
                PyPy是另一个Python解释器，它的目标是执行速度。PyPy采用JIT技术，对Python代码进行动态编译（注意不是解释），所以可以显著提高Python代码的执行速度。
    4.hello world
        print("Hello World")
        # 注释
            #号,单行注释
            三引号,多行注释
    5.变量
        用来存储中间程序运行过程中的中间值,供后续使用.
        变量命名规则:
            下划线字母开头,后面跟下划线/字母/数字
            不能使用关键字
        变量名命名建议:
            小写下划线分割式
            首字母小写驼峰式
            简洁明了易懂
        变量名赋值
            在内存中创建对象(等号左边的数据); 在系统表中创建变量名; 创建从变量名到对象的指针;
            Python中变量没有声明, 在程序中对变量名第一次赋值, 就创建出了变量.
            变量没有类型, 类型是属于对象的,创建出的对象有数据/类型标志/引用计数器,        
     常量
        Python没有常量, 人为的标志一些量作为常量, 约定俗成使用全大写表示常量
        PI = 3.1415
    6.基本数据类型(Python中一切数据都是对象,类型是对象的不是变量的)
        数字类型:并不是一个对象类型,而是一个对象类型的集合
            整型
                32位机: -2**31~2**31-1(-2147483648~2147483647)
                64位机: -2**63~2**63-1(-9223372036854775808~9223372036854775807)

                <class 'int'>
            浮点型
                <class 'float'>
            复数
                <class 'complex'>
            布尔型
                <class 'bool'>
                True
                False
        字符串类型:
            单引号/双引号生成相同的字符串
                "呵呵"/'呵呵'
            三引号:按原样式输出的字符串
            转义字符:
            序列: 拼接/重复/索引/分片/迭代/成员检测
    7.用户交互
        input()
            1.程序阻塞/挂起,等待用户输入
            2.获得数据为字符串类型
    8.if
        一个if:判断条件是否成立, 是否执行
        if-else:二选一
        多个if:全选多
        if-elif-else:多选一
        嵌套的if-elif-else

"""