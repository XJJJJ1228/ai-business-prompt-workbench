#!/usr/bin/env python3
# text_clean.py 原始文本预处理脚本
# 作用：清洗会议、客服对话原始文本，去除多余换行、空白、无效乱码，用于prompt前置输入准备

import os

def clean_raw_text(raw_text: str) -> str:
    # 按行分割，去除首尾空白
    lines = [line.strip() for line in raw_text.splitlines()]
    # 过滤空行
    valid_lines = [line for line in lines if line]
    return "\n".join(valid_lines)

def load_all_test_files(data_dir="../data"):
    file_collection = {}
    if not os.path.exists(data_dir):
        print(f"警告：目录 {data_dir} 不存在，请确认data文件夹已创建")
        return file_collection

    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(data_dir, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                raw_content = f.read()
                cleaned_content = clean_raw_text(raw_content)
                file_collection[filename] = cleaned_content
    return file_collection

if __name__ == "__main__":
    result = load_all_test_files()
    print("✅ 文本预处理完成，已加载清洗后的测试文本：")
    for name, text in result.items():
        print(f"\n==== {name} ====")
        print(text[:150])
