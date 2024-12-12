# 读取文件，将单词以50个为一组分行
input_file = 'youdao_words.txt'
output_file = 'formatted_youdao_words.txt'

with open(input_file, 'r') as file:
    words = file.read().strip().split(',')

lines = [','.join(words[i:i+50]) for i in range(0, len(words), 50)]

with open(output_file, 'w') as file:
    file.write('\n'.join(lines))

print(f"单词已成功按50个一组写入到文件: {output_file}")
