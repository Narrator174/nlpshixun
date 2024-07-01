import json

# 从文件读取JSON数据
file_path = 'dataset/dev.json'
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 提取对话并转换格式
def extract_dialogues(data):
    results = []
    for dialog_id, dialog_data in data.items():
        results.append(f"{dialog_id}:\n")
        for dialogue in dialog_data.get('dialogue', []):
            speaker = dialogue.get('speaker')
            sentence = dialogue.get('sentence')
            results.append(f"{speaker}:{sentence}\n")
    return results

# 保存到txt文件
def save_to_txt(filename, lines):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# 使用示例数据进行提取和保存
dialogue_lines = extract_dialogues(data)
save_to_txt('dialogue_output.txt', dialogue_lines)

