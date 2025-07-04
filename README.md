





notebook_agent
===




<!--


导入知识库约定

特定领域知识文档集中在一个文档中:
```
data/
└── cormacksigir09-rrf.md

// cormacksigir09-rrf.md
# Reciprocal Rank Fusion outperforms Condorcet and individual Rank Learning Methods
...
```

特定领域知识文档分散在一个目录中,需要包含 `SUMMARY.md` 或 `README.md` 中包含 Content Index,如以下目录结构:
```
data/
├── README.md
├── Overview.md
└── doc_xxx.md

// README.md
## Content Index
- [Overview](Overview.md)
- ...
```
文档检索会根据文件名称与 Content Index 查询

SUMMARY 结构
```
data/
├── SUMMARY.md
├── README.md
├── my-first-chapter.md
└── nested/
    ├── README.md
    └── sub-chapter.md

// SUMMARY.md
[Introduction](README.md)
- [My First Chapter](my-first-chapter.md)
- [Nested example](nested/README.md)
    - [Sub-chapter](nested/sub-chapter.md)
```
文档检索会优先根据 `SUMMARY.md` 查询




### 参考资源
- [llms](https://github.com/drawmoon/llms)



-->





