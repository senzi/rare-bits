# MD5 Collision: Anya vs Tombkeeper

> 自动生成的实验报告 | 生成时间: 2026-04-06 16:37:26

## 🌌 实验背景
本实验展示了基于 **MD5 前缀选择攻击 (Chosen-prefix Collision)** 构造的数字奇迹。两张视觉内容完全不同的图像文件，在 MD5 算法下的哈希值完全一致。

---

### 🧪 验证组: Group 1
| 文件名 | 文件大小 (Bytes) | MD5 哈希值 |
| :--- | :--- | :--- |
| `anya_coll.png` | 81920 | `adf65d6d5181b4164e2c0940858c4546` |
| `tombkeeper_coll.png` | 81920 | `adf65d6d5181b4164e2c0940858c4546` |

#### 二进制差异证明
在偏移量 `0x40` 处发现数据分叉点：

```text
anya_coll.png        | bc bc e7 77 5c e7 99 e5 cb ff eb 7e 9c e9 9e 3b
tombkeeper_coll.png  | c4 dd 67 d4 55 55 96 3e fa 43 14 90 24 2a a2 22
```
**结论**: 验证通过。宏观哈希一致，微观数据存在本质差异。

---

### 🧪 验证组: Group 2
| 文件名 | 文件大小 (Bytes) | MD5 哈希值 |
| :--- | :--- | :--- |
| `anya_coll2.png` | 81920 | `76c2680a1d1b199a00e6dea9807f9455` |
| `tombkeeper_coll2.png` | 81920 | `76c2680a1d1b199a00e6dea9807f9455` |

#### 二进制差异证明
在偏移量 `0x40` 处发现数据分叉点：

```text
anya_coll2.png       | bc bc e7 77 5c e7 99 e5 cb ff eb 7e 9c e9 9e 3b
tombkeeper_coll2.png | c4 dd 67 d4 55 55 96 3e fa 43 14 90 24 2a a2 22
```
**结论**: 验证通过。宏观哈希一致，微观数据存在本质差异。

---

## 🔗 存证信息
- **存证 Hash**: `[在 Push 后回填此 Commit SHA]`
- **验证状态**: Verified by `verify_collisions.py`