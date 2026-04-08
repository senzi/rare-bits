呜呜，这种“全武装”的存证方式真是让人极度舒适！w 

加上了 **`.ots`** 文件，意味着这条 MD5 链条不仅在 GitHub 上留下了痕迹，还被永久性地锚定在了比特币主网的区块中。即使 MD5 算法在未来被彻底攻破，这个 OTS 证明也能铁证如山地表明：在 2026 年 4 月 8 日这一刻，你确实已经掌握了这串能产生“双重纯数字投影”的初始数字 $X$。

为了匹配这一硬核操作，我为你更新了该目录下的 **`README.md`**，专门加入了对 OpenTimestamps 的说明：

---

### 📄 2026-04-08-md5-numeric-chain/README.md

```markdown
# 实验代号：MD5 Numeric Chain (十进制迭代链)

> "A sequence of order, where every shadow remains as pure as its source."

## 🌌 现象描述
本实验记录了一个极具秩序感的 MD5 迭代现象：
我们发现了一个 32 位纯数字字符串 $X$，其 MD5 哈希值 $Y$ 同样为 32 位纯数字；更进一步的是，$Y$ 的 MD5 哈希值 $Z$ 依然保持了纯数字的特性。

这种“双重跳跃”且每一级都完美避开了十六进制字母（a-f）的概率极低。它不仅是哈希分布的随机性体现，更是数字空间中一段连续的、未被打破的对称性。

## 🧪 链式数据 (The Chain)
- **输入 (X)**: `05810747610981476965050347470789`
- **一级投影 (Y)**: `36101062662917160706881752457623` (MD5 of X)
- **二级投影 (Z)**: `28548430971249712095486309405749` (MD5 of Y)

## 🛡️ 双重存证 (Double-Timestamping)
本实验采用了最高规格的存证方案，确保发现时刻的绝对不可篡改性：

1. **GitHub Verified Commit**: 利用 Git 提交历史提供分布式版本存证。
2. **Bitcoin Blockchain (OpenTimestamps)**: 
   - 存证文件: `chain.txt.ots`
   - 验证说明: 该文件包含了将 `chain.txt` 的哈希值嵌入比特币区块链的数学证明。
   - 验证方法: 可通过 [OpenTimestamps 官网](https://opentimestamps.org/) 上传 `chain.txt` 与 `chain.txt.ots` 进行校验。

## 🛠️ 自动化验证
目录内包含 `verify_chain.py` 脚本，用于重现这一链式变换并验证其纯度：
```bash
python verify_chain.py
```

## 🔗 存证信息
- **首次发现 UTC 时间**: 2026-04-08
- **存证 Hash**: `[93b28c9b418502934446298434f4626fdec39927]`
- **验证状态**: Verified by `verify_chain.py` & OpenTimestamps
```

---
