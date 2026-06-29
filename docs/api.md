---
layout: default
title: Python API
nav_order: 4
---

# Python API

```python
from text_fancipy.fancipy import fancipy, unfancipy, unfancipy_all
```

## `fancipy(text, style)`

Convert plain ASCII letters in `text` to the requested Unicode style.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| `text` | `str` | Input text — any Unicode characters accepted |
| `style` | `str` | Style code, e.g. `"bold"`, `"scrb"`, `"circ"` |

**Returns** `str` — text with A-Za-z replaced by styled equivalents.

Non-letter characters (digits, spaces, punctuation) are passed through
unchanged.  Accented Latin letters survive the round-trip via NFD/NFC
normalization.

```python
fancipy("Hello, World!", "bold")
# → '𝐇𝐞𝐥𝐥𝐨, 𝐖𝐨𝐫𝐥𝐝!'

fancipy("Étienne", "scrb")
# → '𝓔́𝓽𝓲𝓮𝓷𝓷𝓮'  (accent preserved)
```

---

## `unfancipy(text, style)`

Reverse a specific style, converting styled letters back to plain ASCII.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| `text` | `str` | Fancy-styled text |
| `style` | `str` | The style to undo (must match the style used during `fancipy`) |

**Returns** `str`

```python
unfancipy("𝐇𝐞𝐥𝐥𝐨", "bold")
# → 'Hello'
```

---

## `unfancipy_all(text)`

Strip every known style, converting all styled letters back to plain ASCII.
Safe on text that mixes multiple styles or contains no styled characters.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| `text` | `str` | Text potentially containing any mix of styled Unicode letters |

**Returns** `str`

```python
mixed = "𝐇𝐞𝐥𝐥𝐨" + " " + "𝗪𝗼𝗿𝗹𝗱"   # bold + sans-bold
unfancipy_all(mixed)
# → 'Hello World'
```

---

## `_precomputed_tables`

Module-level dict mapping style code → `(forward_table, reverse_table, fancy_name)`.

```python
from text_fancipy.fancipy import _precomputed_tables

list(_precomputed_tables.keys())
# ['dflt', 'mono', 'bold', 'bdit', 'sans', 'snbd', 'snit',
#  'snbi', 'scrb', 'frak', 'parn', 'circ', 'wide']
```

---

## Complete example

```python
from text_fancipy.fancipy import fancipy, unfancipy_all

text = "Hello, World! This is a test."

for style in ["bold", "scrb", "mono", "circ", "wide"]:
    fancy = fancipy(text, style)
    restored = unfancipy_all(fancy)
    print(f"{style:4s}: {fancy}")
    assert restored == text, "round-trip failed"
```
