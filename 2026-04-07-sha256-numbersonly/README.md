# 实验代号：Decimal Resonance (十进制共鸣)

> "In the desert of $2^{256}$, a pure sequence echoes itself."

## 🌌 现象描述
本实验记录了一个极罕见的密码学现象：寻找到了一个长度为 64 位的纯数字字符串 $X$，其 SHA-256 的十六进制（Hex）输出同样为 64 位纯数字。

在统计学上，这种“纯净”转换的发生概率约为：
$$(\frac{10}{16})^{64} \approx 6.842 \times 10^{-14}$$
这相当于在数以万亿计的随机尝试中，捕捉到了一个完美的秩序瞬间。

## 🧪 实验数据
- **原始数据**: `input.txt` (包含 64 位纯数字 $X$)
- **目标哈希**: 通过 `verify_purity.py` 验证其 SHA-256 结果是否全由 `0-9` 组成。

## 🛡️ 双重时间戳存证 (Double-Timestamping)
为了确保发现时刻的绝对真实性与不可篡改性，本项目采用了双重存证方案：

1. **GitHub Verified Commit**: 利用 Git 提交历史提供分布式存证。
2. **Bitcoin Blockchain (OpenTimestamps)**: 
   - 存证文件: `input.txt.ots`
   - 验证说明: 该文件包含了将 `input.txt` 的哈希值嵌入比特币区块链的证明。
   - 验证方法: 可使用 [OpenTimestamps 官网](https://opentimestamps.org/) 或是本地 `ots` 工具进行校验。

## 🛠️ 自动化验证
运行以下脚本即可复现验证过程并生成详细报告：
```bash
python verify_purity.py
```

## 🔗 存证信息
- **首次发现 UTC 时间**: 2026-04-07
- **存证 Hash**: `[439dd69228a4124ca9fa5f3bb3c222c27715224e]`
- **OTS 证明**: 已关联 `input.txt.ots`