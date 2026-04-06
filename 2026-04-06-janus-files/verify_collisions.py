import hashlib
import os
from datetime import datetime

# ==========================================
# 实验配置
# ==========================================
EXPERIMENT_NAME = "MD5 Collision: Anya vs Tombkeeper"
COLLISION_PAIRS = [
    ("Group 1", "anya_coll.png", "tombkeeper_coll.png"),
    ("Group 2", "anya_coll2.png", "tombkeeper_coll2.png")
]
REPORT_FILE = "REPORT.md"

def get_md5(file_path):
    if not os.path.exists(file_path):
        return None
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def find_first_diff(f1, f2):
    with open(f1, 'rb') as file1, open(f2, 'rb') as file2:
        offset = 0
        while True:
            b1 = file1.read(1)
            b2 = file2.read(1)
            if not b1 or not b2: break
            if b1 != b2:
                sample_size = 16
                file1.seek(offset)
                file2.seek(offset)
                return offset, file1.read(sample_size), file2.read(sample_size)
            offset += 1
    return None, None, None

def format_hex(data):
    return " ".join(f"{b:02x}" for b in data)

def run_verification():
    report_content = []
    report_content.append(f"# {EXPERIMENT_NAME}\n")
    report_content.append(f"> 自动生成的实验报告 | 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report_content.append("## 🌌 实验背景\n本实验展示了基于 **MD5 前缀选择攻击 (Chosen-prefix Collision)** 构造的数字奇迹。两张视觉内容完全不同的图像文件，在 MD5 算法下的哈希值完全一致。\n")
    report_content.append("---")

    print("\n" + "=" * 80)
    print(f" 正在运行 {EXPERIMENT_NAME} 验证脚本 ".center(80))
    print("=" * 80)

    for label, f1, f2 in COLLISION_PAIRS:
        m1, m2 = get_md5(f1), get_md5(f2)
        if not m1 or not m2:
            print(f"❌ 错误: 找不到文件 {f1} 或 {f2}")
            continue

        s1, s2 = os.path.getsize(f1), os.path.getsize(f2)
        offset, chunk1, chunk2 = find_first_diff(f1, f2)
        is_collision = (m1 == m2)

        # 终端输出
        print(f"\n[{label}]: {f1} <--> {f2}")
        print(f"  MD5: {m1} | Size: {s1}")
        print(f"  结果: {'✅ 碰撞确认' if is_collision else '❌ 未发现碰撞'}")

        # 构建报告内容
        report_content.append(f"\n### 🧪 验证组: {label}")
        report_content.append("| 文件名 | 文件大小 (Bytes) | MD5 哈希值 |")
        report_content.append("| :--- | :--- | :--- |")
        report_content.append(f"| `{f1}` | {s1} | `{m1}` |")
        report_content.append(f"| `{f2}` | {s2} | `{m2}` |")

        if is_collision and offset is not None:
            hex_table = (
                f"\n#### 二进制差异证明\n"
                f"在偏移量 `{hex(offset)}` 处发现数据分叉点：\n\n"
                f"```text\n"
                f"{f1:<20} | {format_hex(chunk1)}\n"
                f"{f2:<20} | {format_hex(chunk2)}\n"
                f"```\n"
                f"**结论**: 验证通过。宏观哈希一致，微观数据存在本质差异。\n"
            )
            report_content.append(hex_table)
            report_content.append("---")

    # 存证信息回填占位
    report_content.append("\n## 🔗 存证信息")
    report_content.append("- **存证 Hash**: `[在 Push 后回填此 Commit SHA]`")
    report_content.append("- **验证状态**: Verified by `verify_collisions.py`")

    # 写入文件
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(report_content))

    print("\n" + "=" * 80)
    print(f"✅ 报告已生成: {REPORT_FILE}".center(80))
    print("=" * 80 + "\n")

if __name__ == "__main__":
    run_verification()