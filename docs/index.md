---
layout: default
title: Home
nav_order: 1
---

# Text FanciPy

**Text FanciPy** converts standard English letters (A-Za-z) into Unicode decorative styles and back.

```bash
pip install text-fancipy
```

```bash
fancipy bold -t "Hello World"
# → 𝐇𝐞𝐥𝐥𝐨 𝐖𝐨𝐫𝐥𝐝

fancipy undo -t "𝓗𝓮𝓵𝓵𝓸 𝓦𝓸𝓻𝓵𝓭"
# → Hello World
```

> **Accessibility warning:** Unicode styled text is decorative only. Screen readers
> may read it letter-by-letter or skip it entirely. Search engines and copy-paste
> may not recognise the characters. Use only where purely visual effect is acceptable.

## Quick links

- [Style gallery](styles.md) — all 13 styles with examples
- [CLI reference](cli.md) — command-line usage
- [Python API](api.md) — library usage
- [Source on GitHub](https://github.com/twardoch/text_fancipy)
- [PyPI package](https://pypi.org/project/text-fancipy/)
