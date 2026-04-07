# 实验代号：Janus Files (雅努斯之面)

> "Two distinct realities, one identical digital fingerprint."

## 🌌 现象描述
本实验记录了一组基于 **MD5 前缀选择攻击 (Chosen-prefix Collision)** 构造的数字奇迹。

“Janus” 取自罗马神话中的双面神。在本目录中，`anya_coll.png` 与 `tombkeeper_coll.png` 虽然在视觉内容上完全不同（分别是 Anya 与 Tombkeeper 的图像），但在 MD5 算法的度量下，它们产生了完全一致的哈希值。

## 🧪 实验数据
- **文件组 A**: `anya_coll.png` / `anya_coll2.png`
- **文件组 B**: `tombkeeper_coll.png` / `tombkeeper_coll2.png`
- **碰撞特性**: 
  - 宏观：MD5 哈希值完全相等。
  - 微观：在偏移量 `0x40` 处存在本质的二进制差异。

## 🛠️ 自动化验证
本目录包含一个专用验证脚本，运行后可实时比对 MD5 值并提取二进制差异样本：
```bash
python verify_collisions.py
```

## 🔗 存证信息
- **首次发现 UTC 时间**: 2026-04-06
- **存证 Hash**: `[8c070d67609a47e1cbbe47c735222a4a62d737db]`
- **稀有度说明**: MD5 碰撞攻击的经典展示，证明了算法的结构性弱点。

-----