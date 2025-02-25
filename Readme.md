# askanywhere
# 一个划词ai助手，以及个人生活记录助手，支持横向深入提问，在结果之上可再次选取，并在新窗口提问新问题，不影响原本问答流程。通过记录你的行为，成为最理解你的私人助手。
初次使用：运行会产生一个config txt文件，按照说明配置deepseek api即可使用

## 使用说明：

### 划词
- 在能选中的文字上划词即可弹出悬浮条，点击ALt直接提问，或者在文本框中输入相关内容后提问。
- 回复在新的悬浮窗口中展示，可以进一步沟通，也可以对于新的疑问点划词打开新窗口沟通，不影响之前的问答。
- AI自动识别意图，翻译，解释代码还是修正文本?你只要划词一下，剩下交给AI

### 笔记
-在任何输入框中输入#标签1 #标签2 可以记录笔记

### AI记录
- 日常每一个问答全部由AI记录总结，包括活动总结，日总结月总结等。全面掌握日常活动信息。
- 主界面结合RAG,每次提问会通过查询历史信息进行匹配回答。

### 复习
- 每日自动根据前一天记录，形成总结，以及需要复习回顾的知识点
- 根据艾宾浩斯遗忘曲线设置，按照不同间隔进行复习，强化记忆。

### 存储调用
-根据标签，时间，模糊词，调用已经存储的记录
### 暂停划词
-系统托盘，右键，可以暂停、恢复、退出功能
### 命令行功能
-主界面聊天输入框，输入~开启命令行功能，准确查询笔记，删除笔记等内容

## 关于主窗口
主窗口默认提供记忆调取，所以回复相对较慢，日常提问建议使用划词提问。
在主窗口可以沟通询问，总结近期活动，询问日程安排等等。
默认每次打开会总结上一天内容，此时询问可能得不到准确答复。

### 主窗口界面
![示例图片](图片展示picture/主界面.png)
### 划词查询
![示例图片](图片展示picture/划词查询.png)
### 查询结果
![示例图片](图片展示picture/划词查询-展示.png)
### 嵌套查询
![示例图片](图片展示picture/嵌套询问.png)
### 模块框架
![示例图片](图片展示picture/模块框架.png)
### 逻辑框架
![示例图片](图片展示picture/逻辑框架.png)
### 复习模块
![示例图片](图片展示picture/review.png)
