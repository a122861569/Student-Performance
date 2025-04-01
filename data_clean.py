import pandas as pd

# 指定文件路径
file_path = r"C:\Users\a122861569\Desktop\新建文件夹 (2)\student-mat.csv"

# 读取 CSV 文件，指定分隔符为 ";"
df = pd.read_csv(file_path, delimiter=';')
# 保存为新的 CSV 文件，确保格式正确
cleaned_file_path = r"C:\Users\a122861569\Desktop\新建文件夹 (2)\cleaned_student-mat.csv"
df.to_csv(cleaned_file_path, index=False, encoding='utf-8')

print(f"清理完成，文件已保存至: {cleaned_file_path}")
# 创建数据
data = [
    ["school", "特征", "类别型", "", "学生的学校（'GP' - Gabriel Pereira 或 'MS' - Mousinho da Silveira）", "", "无"],
    ["sex", "特征", "二元型", "性别", "学生的性别（'F' - 女，'M' - 男）", "", "无"],
    ["age", "特征", "整数型", "年龄", "学生的年龄（数值：15 到 22）", "", "无"],
    ["address", "特征", "类别型", "", "学生的家庭住址类型（'U' - 城市，'R' - 乡村）", "", "无"],
    ["famsize", "特征", "类别型", "其他", "家庭规模（'LE3' - 小于或等于 3，'GT3' - 大于 3）", "", "无"],
    ["Pstatus", "特征", "类别型", "其他", "父母的同居状态（'T' - 住在一起，'A' - 分开）", "", "无"],
    ["Medu", "特征", "整数型", "教育水平", "母亲的受教育程度（数值：0 - 无，1 - 小学，2 - 5 到 9 年级，3 - 高中，4 - 高等教育）", "", "无"],
    ["Fedu", "特征", "整数型", "教育水平", "父亲的受教育程度（数值：0 - 无，1 - 小学，2 - 5 到 9 年级，3 - 高中，4 - 高等教育）", "", "无"],
    ["Mjob", "特征", "类别型", "职业", "母亲的职业（'教师'，'医疗' 相关，'公务员'（如行政或警察），'家庭主妇'，'其他）", "", "无"],
    ["Fjob", "特征", "类别型", "职业", "父亲的职业（'教师'，'医疗' 相关，'公务员'（如行政或警察），'家庭主夫'，'其他）", "", "无"],
    ["studytime", "特征", "整数型", "", "每周学习时间（数值：1 - 少于 2 小时，2 - 2-5 小时，3 - 5-10 小时，4 - 超过 10 小时）", "", "无"],
    ["failures", "特征", "整数型", "", "过去课程不及格次数（1<=n<3，否则为4）", "", "无"],
    ["schoolsup", "特征", "二元型", "", "额外的教育支持（是 或 否）", "", "无"],
    ["famsup", "特征", "二元型", "", "家庭教育支持（是 或 否）", "", "无"],
    ["paid", "特征", "二元型", "", "额外的付费课程（数学或葡萄牙语）（是 或 否）", "", "无"],
    ["activities", "特征", "二元型", "", "课外活动（是 或 否）", "", "无"],
    ["nursery", "特征", "二元型", "", "是否上过幼儿园（是 或 否）", "", "无"],
    ["famrel", "特征", "整数型", "", "家庭关系质量（数值：1 - 非常差，5 - 优秀）", "", "无"],
    ["freetime", "特征", "整数型", "", "课余时间（数值：1 - 很少，5 - 很多）", "", "无"],
    ["goout", "特征", "整数型", "", "与朋友外出次数（数值：1 - 很少，5 - 很多）", "", "无"],
    ["Dalc", "特征", "整数型", "", "工作日饮酒量（数值：1 - 很少，5 - 很多）", "", "无"],
    ["Walc", "特征", "整数型", "", "周末饮酒量（数值：1 - 很少，5 - 很多）", "", "无"],
    ["health", "特征", "整数型", "", "当前健康状况（数值：1 - 非常差，5 - 非常好）", "", "无"],
    ["absences", "特征", "整数型", "", "缺课次数（数值：0 到 93）", "", "无"],
]

# 创建 DataFrame
columns = ["Variable Name", "Role", "Type", "Demographic", "Description", "Units", "Missing Values"]
df = pd.DataFrame(data, columns=columns)

# 保存为 CSV
csv_filename = r"C:\Users\a122861569\Desktop\新建文件夹 (2)\variable_info.csv"
df.to_csv(csv_filename, index=False, encoding="utf-8-sig")

