# pairwise-editor-undo-redo

## 领域

游戏、图形与多媒体

## 主题

编辑器撤销重做

## 说明

远端插入、批量合并与栈裁剪。

初始状态下 `gameplay/editor_undo_redo.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
