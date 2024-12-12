import requests
import time

# 设置基础 URL 和 Headers
BASE_URL = "https://dict.youdao.com/wordbook/webapi/v2/word/list"
HEADERS = {
    "Accept": "[Your own value]",
    "Accept-Encoding": "[Your own value]",
    "Accept-Language": "[Your own value]",
    "Connection": "[Your own value]",
    "Cookie": "[Your own value]",
    "Host": "dict.youdao.com",
    "Referer": "https://dict.youdao.com/webwordbook/wordlist",
    "User-Agent": "[Your own value]",
}

# 每页单词数量
LIMIT = 48

def fetch_words():
    offset = 0
    all_words = []

    while True:
        # 构造请求参数
        params = {
            "limit": LIMIT,
            "offset": offset,
            "sort": "time",
            "lanTo": "",
            "lanFrom": "",
        }

        # 发起请求
        response = requests.get(BASE_URL, headers=HEADERS, params=params)

        # 检查响应状态码
        if response.status_code != 200:
            print(f"请求失败，状态码：{response.status_code}")
            print(response.text)
            break

        # 获取 JSON 数据
        data = response.json()
        if data["code"] != 0 or not data["data"]:
            print(f"请求返回错误，代码：{data['code']}, 信息：{data['msg']}")
            break

        # 提取单词列表
        words = [item["word"] for item in data["data"]["itemList"]]
        all_words.extend(words)

        print(f"获取到 {len(words)} 个单词，共计 {len(all_words)} 个单词")

        # 如果当前页单词少于 LIMIT，说明已到最后一页
        if len(words) < LIMIT:
            break

        # 增加偏移量，获取下一页
        offset += LIMIT
        time.sleep(1)  # 添加延时以避免频繁请求

    return all_words


def save_words_to_file(words, file_path):
    # 将单词写入文件，以逗号分隔
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(",".join(words))


if __name__ == "__main__":
    # 获取所有单词
    words = fetch_words()

    # 保存到文件
    if words:
        save_words_to_file(words, "youdao_words.txt")
        print(f"单词已保存到文件：youdao_words.txt")
    else:
        print("未能获取任何单词")

