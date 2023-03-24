# 绪论
## 一、数据结构：相互存在一种或多种特定关系的集合
- 结构：任何问题，数据元素不孤立存在，之间存在关系  
- 逻辑结构
- 存储结构（物理结构）
- 数据的运算
- 逻辑结构和存储结构密不可分
- 算法设计取决于逻辑结构，实现依赖存储结构
## 二、逻辑结构：数据元素之间的逻辑关系
- 与存储无关，独立于计算机
- 分为线性结构和非线性结构
线性结构：线性表、栈、队列、串、数组、广义表
非线性结构：树、二叉树、有向图、无向图
## 三、存储结构（物理结构）：数据结构在计算机中的映像
- 数据结构的表示
- 关系的表示
- 依赖于计算机语言
- 分为顺序存储、链式存储、索引存储、散列存储
### 1. 顺序存储：存储的物理位置相邻，逻辑上相邻的元素物理位置也相邻
- 优：实现随机存取、每个元素占用的内存少
- 缺：只能使用相邻的一块存储单元，产生较多的外部碎片
### 2.链式存储：存储的物理位置未必相邻，逻辑上的相邻的元素在物理位置上未必相邻，通过记录相邻元素的物理位置来找到相邻元素
- 优：无碎片产生、充分利用存储单元
- 缺：只能顺序存储
### 3. 索引存储：类似目录
### 4. 散列存储：通过关键字直接计算出元素的物理地址
## 四、数据运算
## 五、算法的五个特征
- 有穷性：执行有限步后结束
- 确定性：每条指令都有确定的含义，相同输入得到相同的输出
- 可行性：通过实现的基本运算执行有限次得到确定的结果
- 输入：有零或多个输入
- 输出：一个或多个程序输出结果
## 六、算法的复杂度
### 1. 时间复杂度：衡量算法随问题规模增大，算法执行时间增加的快慢
### 2. 空间复杂度：衡量算法随问题规模增大，算法占用空间增加的快慢