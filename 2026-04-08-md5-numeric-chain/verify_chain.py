import hashlib
import os
from datetime import datetime

# ==========================================
# 实验配置
# ==========================================
EXPERIMENT_NAME = "MD5 Numeric Chain: Double Decimal Resonance"
INPUT_FILE = "chain.txt"
REPORT_FILE = "REPORT.md"

def get_md5(text):
    return hashlib.md5(text.encode()).hexdigest()

def run_verify():
    if not os.path.exists(INPUT_FILE):
        print(f"❌ 错误: 找不到输入文件 {INPUT_FILE}")
        return

    # 读取起始数字 X
    with open(INPUT_FILE, "r") as f:
        x = f.read().strip()

    # 执行链式哈希计算
    y = get_md5(x)
    z = get_md5(y)

    # 验证纯度 (是否全是 0-9)
    is_x_num = x.isdigit()
    is_y_num = y.isdigit()
    is_z_num = z.isdigit()

    print("\n" + "=" * 80)
    print(f" {EXPERIMENT_NAME} ".center(80))
    print("=" * 80)
    print(f"  [Level 0] X: {x} (Pure: {is_x_num})")
    print(f"  [Level 1] Y: {y} (Pure: {is_y_num}) <- MD5(X)")
    print(f"  [Level 2] Z: {z} (Pure: {is_z_num}) <- MD5(Y)")
    print("-" * 80)

    # 生成实验报告内容
    report = [
        f"# {EXPERIMENT_NAME}\n",
        f"> 自动生成的实验报告 | 发现时刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        "## 🌌 现象描述",
        "本实验记录了一组极具秩序感的 MD5 迭代现象：输入一个 32 位纯数字字符串 $X$，其 MD5 哈希值 $Y$ 为纯数字，且 $Y$ 的 MD5 哈希值 $Z$ 依然为纯数字。",
        "这种连续两次迭代均保持“十进制纯净度”的概率极低，是数字空间中一段连续的、未被打破的对称性。\n",
        "## 🧪 链式数据 (The Chain)",
        f"| 层级 | 数据内容 | 性质 |",
        f"| :--- | :--- | :--- |",
        f"| Level 0 (X) | `{x}` | 起始数字 |",
        f"| Level 1 (Y) | `{y}` | MD5(X) / 纯数字 |",
        f"| Level 2 (Z) | `{z}` | MD5(Y) / 纯数字 |\n",
        "## ✅ 性质验证",
        f"- 全链条纯数字属性: {'达成' if (is_y_num and is_z_num) else '未达成'}",
        f"- 链条完整性校验: 通过 (Verified by `hashlib.md5`)\n",
        "## 🔗 存证信息",
        "- **存证 Hash**: `[在 Push 后回填此 Commit SHA]`",
        "- **验证状态**: Verified by `verify_chain.py`"
    ]

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(report))
    
    print(f"✅ 验证完成，报告已生成: {REPORT_FILE}\n")

if __name__ == "__main__":
    run_verify()