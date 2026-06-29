# Text FanciPy

[![PyPI](https://img.shields.io/pypi/v/text-fancipy)](https://pypi.org/project/text-fancipy/)
[![Python](https://img.shields.io/pypi/pyversions/text-fancipy)](https://pypi.org/project/text-fancipy/)
[![CI](https://github.com/twardoch/text_fancipy/actions/workflows/ci.yml/badge.svg)](https://github.com/twardoch/text_fancipy/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE.txt)

**[Documentation](https://twardoch.github.io/text_fancipy)** · **[Style gallery](https://twardoch.github.io/text_fancipy/styles)** · **[PyPI](https://pypi.org/project/text-fancipy/)**

Text FanciPy converts standard English letters (A-Z, a-z) into various Unicode "fancy" styles and back. Thirteen styles are supported, drawn from Unicode Mathematical Alphanumeric Symbols, Enclosed Alphanumerics, and Fullwidth Latin blocks.

> **Accessibility warning:** These Unicode styles are decorative only. They are
> not searchable, may not display correctly on all devices, and can break
> accessibility tools. Use them only where purely visual text is acceptable.

## Part 1: General Audience

### What does Text FanciPy do?

It transforms plain English letters into stylized Unicode versions. For example:
- **𝐛𝐨𝐥𝐝**
- 𝘴𝘤𝘳𝘪𝘱𝘵𝘦𝘥
- 𝚖𝚘𝚗𝚘𝚜𝚙𝚊𝚌𝚎𝚍
- ⓒⓘⓡⓒⓛⓔⓓ

It handles accented Latin letters by breaking them down before conversion, then rebuilding them afterward.

### Who is it for?

Anyone who wants to add visual flair to text:
- Social media users making posts stand out
- Designers needing quick decorative effects
- Developers generating styled text for non-critical applications

### Why is it useful?

- **Aesthetic Appeal:** Creates eye-catching text for headings, bios, or nicknames
- **Simplicity:** Clean command-line and Python interfaces
- **Variety:** Multiple Unicode styles to choose from

### ⚠️ Important Limitations

- **Accessibility:** Screen readers may not interpret styled text correctly
- **Searchability:** Search engines and document tools won't recognize the characters
- **Display Consistency:** Not all platforms support every Unicode style—some users may see garbled text

### Installation

Install via pip:

```bash
python3 -m pip install --upgrade text-fancipy
```

Or install the development version directly from GitHub:

```bash
python3 -m pip install --upgrade git+https://github.com/twardoch/text_fancipy
```

### Usage

Text FanciPy works both as a command-line tool and a Python library.

#### Command-Line Interface (CLI)

After installation, use the `fancipy` command.

**1. Convert text to a style:**

```bash
fancipy <style_code> -t "Your text here"
```

Example using `scrb` (Script Bold):
```bash
$ fancipy scrb -t "Książęcych spóźnień czułość"
𝓚𝓼𝓲𝓪̨𝔃̇𝓮̨𝓬𝔂𝓬𝓱 𝓼𝓹𝓸́𝔃́𝓷𝓲𝓮𝓷́ 𝓬𝔃𝓾ł𝓸𝓼́𝓬́
```

**2. Convert styled text back:**

```bash
fancipy undo -t "𝖶𝗁𝖺𝗍 ⓐ 𝖜𝖔𝖓𝖉𝖊𝖗𝖋𝖚𝖑 𝒘𝒐𝒓𝒍𝒅!"
```

Output:
```
What a wonderful world!
```

**3. Use with pipes:**

```bash
echo "Hello World" | fancipy bold | fancipy undo
```

Output:
```
Hello World
```

**4. Use with files:**

```bash
fancipy <style_code> -f input.txt -o output.txt
fancipy undo -f styled_input.txt -o normal_output.txt
```

If no input (`-t` or `-f`) is provided, it reads from standard input.  
If no output (`-o`) is specified, it prints to standard output.

**5. List available styles:**

```bash
fancipy show
```

Sample output:

```
| style  | name                   | letters
|--------|------------------------| ---------
| `dflt` | Default                | ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
| `mono` | 𝙼𝚘𝚗𝚘𝚜𝚙𝚊𝚌𝚎                | 𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣
| `bold` | 𝐒𝐞𝐫𝐢𝐟 𝐁𝐨𝐥𝐝             | 𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳
| `bdit` | 𝑺𝒆𝒓𝒊𝒇 𝑩𝒐𝒍𝒅 𝑰𝒕𝒂𝒍𝒊𝒄      | 𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛
| `sans` | 𝖲𝖺𝗇𝗌                   | 𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓
| `snbd` | 𝗦𝗮𝗻𝘀 𝗕𝗼𝗹𝗱              | 𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇
| `snit` | 𝘚𝘢𝘯𝘴 𝘐𝘵𝘢𝘭𝘪𝘤            | 𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻
| `snbi` | 𝙎𝙖𝙣𝙨 𝘽𝙤𝙡𝙙 𝙄𝙩𝙖𝙡𝙞𝙘       | 𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯
| `scrb` | 𝓢𝓬𝓻𝓲𝓹𝓽 𝓑𝓸𝓵𝓭            | 𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃
| `frak` | 𝕱𝖗𝖆𝖐𝖙𝖚𝖗 𝕭𝖔𝖑𝖉           | 𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟
| `parn` | 🄟⒜⒭⒠⒩⒮                 | 🄐🄑🄒🄓🄔🄕🄖🄗🄘🄙🄚🄛🄜🄝🄞🄟🄠🄡🄢🄣🄤🄥🄦🄧🄨🄩⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵
| `circ` | Ⓒⓘⓡⓒⓛⓔⓓ                | ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ
| `wide` | Ｗｉｄｅ                   | ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ
```

#### Python Library Usage

```python
from text_fancipy.fancipy import fancipy, unfancipy_all

original_text = "Hello, World! This is a test with Étienne."

# Convert to bold
fancy_text = fancipy(original_text, "bold")
print(f"Bold: {fancy_text}")

# Convert to Sans Bold Italic
sans_bold_italic_text = fancipy(original_text, "snbi")
print(f"Sans Bold Italic: {sans_bold_italic_text}")

# Undo any known style
mixed_fancy_text = "𝐓𝐡𝐢𝐬 𝘪𝘴 ⓐ 𝘮𝘪𝘹𝘦𝘥 𝓢𝓽𝔂𝓵𝓮."
regular_text = unfancipy_all(mixed_fancy_text)
print(f"Regular from mixed: {regular_text}")
```

## Part 2: Technical Details

### Core Logic (`fancipy.py`)

**1. Unicode Normalization:**
- Input text is normalized to NFD (decomposed form) before processing
- Converted text is normalized back to NFC (composed form) after processing
- Uses `unicodedata2` if available, falls back to `unicodedata`

**2. Translation Tables:**
- `create_tables()` builds translation dictionaries for each style
- Starting Unicode points are defined for uppercase and lowercase 'A'
- All other letters are calculated relative to these starting points
- Forward and reverse tables are cached in `_precomputed_tables` for reuse

**3. Conversion Functions:**
- `fancipy(text, style)`: Normalizes input, translates, then recomposes
- `unfancipy(text, style)`: Uses reverse translation tables
- `unfancipy_all(text)`: Attempts to undo all known styles in sequence

**4. CLI (`__main__.py`):**
- Built with the `fire` library
- Dynamically creates style-specific methods at runtime
- `undo` reverses any known styling
- `show` prints supported styles in a readable table format

### Contribution Guidelines

**Code Style:**
- `ruff` for linting and formatting; `mypy` for type-checking
- Run `pip install -e ".[dev]"` then `ruff check src/ tests/` and `mypy src/text_fancipy/`

**Pull Requests:**
- Run `pytest tests/ -v` before submitting — all 11 tests must pass
- Write clear commit messages; update `CHANGELOG.md`
- Add tests for any new behaviour

**License:** Apache-2.0 (see `LICENSE.txt`)

**Authors:** Adam Twardoch (see `AUTHORS.md`)

## Support

Report bugs or suggest features by opening an [issue](https://github.com/twardoch/text_fancipy/issues) on GitHub.