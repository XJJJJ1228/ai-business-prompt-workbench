#!/usr/bin/env python3
# score_calc.py 五维评估打分计算器
# 维度：准确性、合规性、结构化、简洁度、无幻觉
# 自动计算总分、平均分，并导出csv评估报表

import csv

def calculate_score(accuracy, compliance, structure, conciseness, no_hallucination):
    total = accuracy + compliance + structure + conciseness + no_hallucination
    average = round(total / 5, 2)
    return total, average

def save_score_report(record_list, output_file="evaluation_result.csv"):
    header = ["样本名称","准确性","合规性","结构化","简洁度","无幻觉","总分","平均分"]
    with open(output_file, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(record_list)

if __name__ == "__main__":
    # 样例测试：会议纪要案例打分
    sample_name = "会议纪要萃取案例"
    total_score, avg_score = calculate_score(5,5,5,4,5)
    row = [sample_name,5,5,5,4,5,total_score,avg_score]
    save_score_report([row])
    print(f"✅ 打分完成，总分：{total_score}，平均分：{avg_score}")
    print("📄 评估结果已保存至 evaluation_result.csv")
