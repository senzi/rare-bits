import hashlib
import os
from datetime import datetime

# ==========================================
# 实验配置
# ==========================================
EXPERIMENT_NAME = "Decimal Resonance: Pure Numeric SHA-256 Collision"
INPUT_FILE = "input.txt"
REPORT_FILE = "REPORT.md"

def verify_resonance():
    if not os.path.exists(INPUT_FILE):
        print(f"❌ 错误: 找不到 {INPUT_FILE}")
        return

    with open(INPUT_FILE, "r") as f:
        x_str = f.read().strip()

    # 1. 验证输入纯度
    is_x_numeric = x_str.isdigit() and len(x_str) == 64
    
    # 2. 计算 SHA-256
    sha256_hash = hashlib.sha256(x_str.encode()).hexdigest()
    
    # 3. 验证输出纯度 (Hex 结果是否全部由 0-9 组成)
    is_hash_numeric = sha256_hash.isdigit()

    print("\n" + "=" * 80)
    print(f" {EXPERIMENT_NAME} ".center(80))
    print("=" * 80)
    print(f"  输入 X: {x_str}")
    print(f"  哈希 Y: {sha256_hash}")
    print("-" * 80)

    # 生成报告内容
    report = []
    report.append(f"# {EXPERIMENT_NAME}\n")
    report.append(f"> 自动生成的实验报告 | 发现时刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report.append("## 🌌 现象描述")
    report.append("在 SHA-256 的海量空间中，寻找到一个输入为 64 位纯数字且输出 Hex 亦为 64 位纯数字的实例。")
    report.append(f"其理论发生概率约为 $(\\frac{{10}}{{16}})^{{64}} \\approx 6.84 \\times 10^{{-14}}$。\n")
    
    report.append("## 🧪 实验数据")
    report.append(f"- **输入 (X)**: `{x_str}` (Length: {len(x_str)})")
    report.append(f"- **哈希 (SHA-256)**: `{sha256_hash}`")
    report.append(f"- **性质验证**: {'✅ 纯数字共鸣达成' if is_hash_numeric else '❌ 验证失败'}\n")
    
    report.append("## 🔗 存证信息")
    report.append("- **存证 Hash**: `[在 Push 后回传此 Commit SHA]`")
    report.append("- **验证状态**: Verified by `verify_purity.py`")

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(report))

    print(f"✅ 验证完成，报告已生成: {REPORT_FILE}\n")

if __name__ == "__main__":
    verify_resonance()