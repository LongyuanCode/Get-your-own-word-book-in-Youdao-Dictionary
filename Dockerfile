FROM python:3.9

WORKDIR /Users/longyuan/Documents/get_youdao_word_book

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  --upgrade pip

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

