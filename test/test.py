import re
def extract_sql_from_text(text):
    """
    从文本中提取 ```sql ... ``` 块内的 SQL 内容，即使前后有其他内容也能正确提取
    """
    # 正则解释：
    # \s*：匹配开头可能的空格或换行
    # (.*?)：非贪婪匹配 SQL 内容
    # 取消了 ^ 和 $ 锚点，允许前后有其他文本，只捕获有效代码块
    pattern = r'```sql\s*(.*?)\s*```'
    matches = re.findall(pattern, text, flags=re.DOTALL)  # 使用 findall 捕获所有匹配项
    
    # 根据需求返回第一个匹配或所有匹配
    if matches:
        return [sql.strip() for sql in matches]# 去除 SQL 内容的首尾空白符
    return None

# 测试用例
if __name__ == "__main__":
    test_cases = [
        "xxxxxx ```sql SELECT * FROM users``` xxxxxxx",
        "```sql\nINSERT INTO logs (message) VALUES ('Hello')\n```",
        "其他文本 ```sql UPDATE users SET name = 'John' WHERE id = 1``` 其他文本",
        "多个块 ```sql DELETE FROM temp ``` 和 ```sql TRUNCATE temp_table ```"
    ]
    for i, text in enumerate(test_cases):
        print(f"用例 {i+1}:")
        result = extract_sql_from_text(text)
        print(f"输入：{text}")
        print(f"提取结果：{result}\n{'='*40}")