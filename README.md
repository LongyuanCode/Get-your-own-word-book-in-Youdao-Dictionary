# Get-your-own-word-book-in-Youdao-Dictionary
最近想把有道单词本中自己收藏的单词都导出来输入给GPT，让它帮我写若干篇英文文章帮助记忆我自己收藏的单词。但是突然发现有道词典把导出单词的按钮下线了🙂。

希望这个小项目可以帮助那些想导出自己在某个应用中的东西的人。毕竟我们花了那么长时间积累的东西不应该被限定使用。

# Main steps
主要的思路其实就是用python脚本模拟浏览器获取数据的行为。所以需要知道两个东西就行：去哪里获取数据（接口）；个人身份信息。
## 1. 找接口
登陆并打开有道词典单词本网页；Chrome浏览器按F12进入开发者模式，点击Network选项卡，刷新网页；找到单词列表所在的字段：
![youdao_network](https://github.com/user-attachments/assets/e2a5d50d-d8f3-43d0-97df-a1539289d2de)

右键，复制字段URL。
## 2. 个人身份信息
个人身份信息在上述字段的Headers选项里面找，填入到get_youdao_word.py文件的对应位置即可。

# 获得结果
在docker中运行get_youdao_word.py脚本就可以在执行目录获得一个youdao_word.txt文件，里面含有你的所有收藏的单词，用`,`分隔。
