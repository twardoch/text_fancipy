---
layout: default
title: CLI reference
nav_order: 3
---

# CLI reference

After installation (`pip install text-fancipy`) the `fancipy` command is
available on your `PATH`.

## Synopsis

```
fancipy <command> [options]
```

## Commands

### `fancipy <style> -t TEXT`

Convert TEXT to the named style.

```bash
fancipy bold -t "Hello World"
# → 𝐇𝐞𝐥𝐥𝐨 𝐖𝐨𝐫𝐥𝐝

fancipy scrb -t "Hello World"
# → 𝓗𝓮𝓵𝓵𝓸 𝓦𝓸𝓻𝓵𝓭

fancipy circ -t "Hello World"
# → Ⓗⓔⓛⓛⓞ Ⓦⓞⓡⓛⓓ
```

### `fancipy <style> -f FILE [-o OUTFILE]`

Read from a file; optionally write to a file.

```bash
fancipy mono -f input.txt -o output.txt
```

### `fancipy <style>`  (stdin)

If neither `-t` nor `-f` is given, reads from standard input.

```bash
echo "Hello World" | fancipy snbd
# → 𝗛𝗲𝗹𝗹𝗼 𝗪𝗼𝗿𝗹𝗱
```

### `fancipy undo -t TEXT`

Reverse all known styles back to plain ASCII.

```bash
fancipy undo -t "𝐇𝐞𝐥𝐥𝐨 𝗪𝗼𝗿𝗹𝗱"
# → Hello World
```

### Pipe chaining

```bash
echo "Hello" | fancipy bold | fancipy undo
# → Hello
```

### `fancipy show`

Print a table of all available styles with their styled letter sets.

```bash
fancipy show
```

## Style codes

| Code | Description |
|------|-------------|
| `dflt` | Plain text (identity — no change) |
| `mono` | Monospace |
| `bold` | Serif Bold |
| `bdit` | Serif Bold Italic |
| `sans` | Sans-serif |
| `snbd` | Sans-serif Bold |
| `snit` | Sans-serif Italic |
| `snbi` | Sans-serif Bold Italic |
| `scrb` | Script Bold |
| `frak` | Fraktur Bold |
| `parn` | Parenthesised |
| `circ` | Circled |
| `wide` | Fullwidth (wide) |
