## 文件清单

- `text_clean.py`：文本清洗脚本，用于原始长文本预处理（去除换行冗余、多余空格、过滤无效标记，用于会议转写稿、业务文档前置处理）
- `score_calc.py`：简易打分辅助脚本，读取评估记录，自动计算五维评估总分，辅助评估报告生成

## 环境依赖

仅需 Python3，无额外重型第三方库，开箱即可运行。

```
# 安装（无额外依赖，原生python即可）
python3 text_clean.py
python3 score_calc.py
```

# scripts/text_clean.py

commit：`feat: 增加文本预处理清洗脚本`

```
#!/usr/bin/env python3
# 文本清洗工具：用于原始业务长文本预处理
# 适用场景：会议转写稿、业务文档，去除多余空行、重复空格，简化文本，便于后续AI抽取
def clean_text(raw_text: str) -> str:
    # 去除多余换行
    lines = [line.strip() for line in raw_text.splitlines()]
    # 过滤空行
    lines = [line for line in lines if line]
    # 合并为干净文本
    clean_result = "\n".join(lines)
    return clean_result

if __name__ == "__main__":
    # 示例输入
    raw = """
    2026年9月20日 项目A同步会

    项目进度80%。     剩余预算12万。
    """
    res = clean_text(raw)
    print("清洗后的文本：")
    print(res)
```

---

# scripts/score_calc.py

commit：`feat: 评估打分辅助计算脚本`

```
#!/usr/bin/env python3
# 五维评估量表自动计分工具
# 输入5个维度分数，输出总分与评价等级
def calculate_score(acc, completeness, logic, compliance, style):
    total = acc + completeness + logic + compliance + style
    if total >=90:
        level = "优秀，可直接使用"
    elif total >=70:
        level = "良好，少量修改可用"
    elif total >=50:
        level = "一般，需要大幅调整"
    else:
        level = "较差，存在严重问题，不可使用"
    return total, level

if __name__ == "__main__":
    # 示例，填入5个维度得分，每项0-20
    score_acc = 20
    score_completeness = 18
    score_logic = 20
    score_compliance = 20
    score_style =14
    total_score, level_result = calculate_score(score_acc,score_completeness,score_logic,score_compliance,score_style)
    print(f"总分：{total_score}/100")
    print(f"综合评价：{level_result}")
```
