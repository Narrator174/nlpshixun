import json

# 从文件读取JSON数据
file_path = 'dataset/dev.json'
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)


# 提取对话及BIO标签并转换格式
def extract_dialogues_and_bio(data):
    results = []
    for dialog_id, dialog_data in data.items():
        results.append(f"{dialog_id}:\n")
        for dialogue in dialog_data.get('dialogue', []):
            bio_label = dialogue.get('BIO_label')
            results.append(f"{bio_label}\n")
    return results


# 保存到txt文件
def save_to_txt(filename, lines):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)


# 使用示例数据进行提取和保存
dialogue_lines = extract_dialogues_and_bio(data)
save_to_txt('bio_output.txt', dialogue_lines)

