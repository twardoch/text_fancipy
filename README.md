# Text FanciPy

Text FanciPy is a Python tool designed to transform standard English alphabet characters (A-Z, a-z) into a variety of "fancy" Unicode styles. It can also reverse this process, converting styled text back into regular characters.

It's important to note that while these "fancy" styles use Unicode characters, the resulting text is not standard, searchable, or guaranteed to display correctly across all devices and platforms. Therefore, Text FanciPy is best suited for decorative purposes where universal compatibility and accessibility are not primary concerns.

## Part 1: General Audience

### What does Text FanciPy do?

Text FanciPy takes your input text and converts the English letters within it to visually distinct styles using Unicode characters. For example, it can make your text look **𝐛𝐨𝐥𝐝**, 𝘴𝘤𝘳𝘪𝘱𝘵𝘦𝘥, 𝚖𝚘𝚗𝚘𝚜𝚙𝚊𝚌𝚎𝚍, or even ⓒⓘⓡⓒⓛⓔⓓ. It also handles most accented Latin letters by decomposing them before conversion and normalizing them afterward.

### Who is it for?

This tool is for anyone looking to add a bit of visual flair to their text:
- Social media users wanting to make their posts stand out.
- Designers looking for quick decorative text effects.
- Anyone needing to generate text in a specific Unicode character style for limited, non-critical applications.

### Why is it useful?

- **Aesthetic Appeal:** It allows for the creation of visually interesting text for headings, social media bios, or nicknames.
- **Simplicity:** Provides an easy-to-use command-line and Python interface for text styling.
- **Variety:** Offers a range of Unicode styles to choose from.

**Important Considerations:**
- **Accessibility:** Styled text can be difficult or impossible for screen readers to interpret, making it inaccessible to visually impaired users.
- **Searchability:** Text converted into these fancy styles is generally not searchable by search engines or within documents.
- **Display Issues:** Not all fonts or platforms support all Unicode characters, so your fancy text might not appear as intended for everyone. Use with caution!

### How to Install Text FanciPy

You can install Text FanciPy using pip:

```bash
python3 -m pip install --upgrade text-fancipy
```

To install the current development version directly from GitHub:

```bash
python3 -m pip install --upgrade git+https://github.com/twardoch/text_fancipy
```

### How to Use Text FanciPy

Text FanciPy can be used both from the command line and as a Python library.

#### Command-Line Interface (CLI)

Once installed, the `fancipy` command becomes available in your terminal.

**1. Converting text to a fancy style:**

   Specify the style followed by your text using the `-t` option:

   ```bash
   fancipy <style_code> -t "Your text here"
   ```

   Example (using `scrb` for Script Bold):
   ```bash
   $ fancipy scrb -t "Książęcych spóźnień czułość"
   𝓚𝓼𝓲𝓪̨𝔃̇𝓮̨𝓬𝔂𝓬𝓱 𝓼𝓹𝓸́𝔃́𝓷𝓲𝓮𝓷́ 𝓬𝔃𝓾ł𝓸𝓼́𝓬́
   ```

**2. Converting fancy text back to regular text:**

   Use the `undo` command:

   ```bash
   fancipy undo -t "𝖶𝗁𝖺𝗍 ⓐ 𝖜𝖔𝖓𝖉𝖊𝖗𝖋𝖚𝖑 𝒘𝒐𝒓𝒍𝒅!"
   ```
   Output:
   ```
   What a wonderful world!
   ```

**3. Using with pipes:**

   You can pipe text into `fancipy` and chain commands:

   ```bash
   echo "Hello World" | fancipy bold | fancipy undo
   ```
   Output:
   ```
   Hello World
   ```

**4. Using with files:**

   Specify input and output files using `-f` and `-o` respectively:

   ```bash
   fancipy <style_code> -f input.txt -o output.txt
   fancipy undo -f styled_input.txt -o normal_output.txt
   ```
   If `-t` or `-f` is not provided, `fancipy` will read from standard input. If `-o` is not provided, it will print to standard output.

**5. Listing available styles:**

   Use the `show` command to see all available styles:

   ```bash
   fancipy show
   ```
   This will output a table like the following (actual output may vary slightly based on your terminal):

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

#### Python Usage (as a library)

You can import and use Text FanciPy functions in your Python scripts.

```python
from text_fancipy.fancipy import fancipy, unfancipy_all

# Text to be converted
original_text = "Hello, World! This is a test with Étienne."

# Convert to a fancy style (e.g., 'bold')
fancy_text = fancipy(original_text, "bold")
print(f"Bold: {fancy_text}")
# Expected output: 𝐇𝐞𝐥𝐥𝐨, 𝐖𝐨𝐫𝐥𝐝! 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐚 𝐭𝐞𝐬𝐭 𝐰𝐢𝐭𝐡 É𝐭𝐢𝐞𝐧𝐧𝐞.

# Convert to another style (e.g., 'snbi' for Sans Bold Italic)
sans_bold_italic_text = fancipy(original_text, "snbi")
print(f"Sans Bold Italic: {sans_bold_italic_text}")
# Expected output: 𝙃𝙚𝙡𝙡𝙤, 𝙒𝙤𝙧𝙡𝙙! 𝙏𝙝𝙞𝙨 𝙞𝙨 𝙖 𝙩𝙚𝙨𝙩 𝙬𝙞𝙩𝙝 É𝙩𝙞𝙚𝙣𝙣𝙚.

# Convert fancy text back to regular text
# This works even if multiple styles are mixed (though fancipy itself only applies one at a time)
mixed_fancy_text = "𝐓𝐡𝐢𝐬 𝘪𝘴 ⓐ 𝘮𝘪𝘹𝘦𝘥 𝓢𝓽𝔂𝓵𝓮."
regular_text = unfancipy_all(mixed_fancy_text)
print(f"Regular from mixed: {regular_text}")
# Expected output: This is a mixed Style.
```

## Part 2: Technical Details

### How the Code Works

Text FanciPy's core logic resides in `src/text_fancipy/fancipy.py`.

**1. Unicode Normalization:**
   - Before any conversion, input text is normalized to NFD (Normalization Form D) using `unicodedata.normalize("NFD", text)`. This decomposes characters like "é" into "e" and a combining acute accent. This allows the base letter "e" to be identified for styling.
   - After conversion, the text is normalized back to NFC (Normalization Form C) using `unicodedata.normalize("NFC", converted_text)`. This recombines base characters with their combining diacritics where possible, which is the preferred form for general text.
   - The tool uses `unicodedata2` if available, falling back to the standard library's `unicodedata`.

**2. Translation Tables:**
   - The `create_tables()` function generates Python translation tables (dictionaries mapping character ordinals to their replacements) for each supported style.
   - For each style (e.g., "bold", "mono"), it defines the starting Unicode character for uppercase 'A' and lowercase 'a' in that style.
   - It then programmatically calculates the mapping for all English letters A-Z and a-z based on these starting points. For example, if styled 'A' is `\U0001D400` (𝐀) and plain 'A' is `\u0041`, then styled 'B' is derived by `ord('B') + ord('\U0001D400') - ord('A')`.
   - Two tables are created for each style: one for converting plain text to fancy, and a reverse table for converting fancy text back to plain.
   - These tables, along with the display name for the style, are stored in the `_precomputed_tables` dictionary for efficiency, so `create_tables()` is only called once at import time. The structure is `{'style_code': (forward_table, reverse_table, 'Fancy Name')}`.

**3. Conversion Functions:**
   - `fancipy(text: str, style: str) -> str`:
     - Normalizes the input `text` to NFD.
     - Retrieves the appropriate forward translation table for the given `style` using `get_table(style, False)`.
     - Applies the translation using `text.translate(table)`.
     - Normalizes the result to NFC.
   - `unfancipy(text: str, style: str) -> str`:
     - Similar to `fancipy`, but uses the reverse translation table `get_table(style, True)`.
   - `unfancipy_all(text: str) -> str`:
     - Iterates through all known styles in `_precomputed_tables`.
     - For each style, it calls `unfancipy(text, style)` to revert any characters from that style. This means it attempts to "undo" every style, effectively converting any recognized fancy character back to its plain equivalent.

**4. Command-Line Interface (`__main__.py`):**
   - The CLI is implemented in `src/text_fancipy/__main__.py` using the `fire` library.
   - The `FanciPyCLI` class is the main entry point for `fire`.
   - It dynamically creates methods for each style code (e.g., `fancipy.bold(...)`, `fancipy.mono(...)`) by iterating through `_precomputed_tables.keys()` in its constructor. Each dynamically created method calls the internal `convert` function with the appropriate style.
   - The `convert()` function handles reading from text arguments, files, or standard input, and writing to files or standard output. It calls either `fancipy()` or `unfancipy_all()` based on the `reverse` flag.
   - The `undo` command is a dedicated method that calls `convert()` with `reverse=True`.
   - The `show` command iterates through `_precomputed_tables` to print the list of available styles in a formatted Markdown table.
   - `fire.Fire(fancipy_cli)` exposes the public methods of the `FanciPyCLI` instance as command-line arguments.

### Coding and Contribution Rules

**Coding Style:**
- The project uses `pyproject.toml` and `setup.cfg` for configuration, which may include linters and formatters.
- `.isort.cfg` suggests that `isort` is used for import sorting.
- `.pre-commit-config.yaml` indicates the use of pre-commit hooks, likely including tools like Black, Flake8, and isort to maintain code quality and consistency. Contributors should ensure their changes pass these checks.

**Contributing:**
- **Reporting Issues:** If you find a bug or have a suggestion, please open an issue on the [GitHub repository's issue tracker](https://github.com/twardoch/text_fancipy/issues). Provide as much detail as possible, including steps to reproduce, expected behavior, and actual behavior.
- **Pull Requests:** Contributions via Pull Requests are welcome.
    - Ensure your code adheres to the project's coding style (run pre-commit hooks if configured).
    - Write clear commit messages.
    - If adding new functionality, consider adding tests (though the current project has minimal tests, new contributions could expand this).
    - Update documentation if your changes affect usage or functionality.

**License:**
- Text FanciPy is licensed under the Apache-2.0 License. See [LICENSE.txt](./LICENSE.txt) for the full license text.
- Contributions are expected to be under the same license.

**Authors:**
- Text FanciPy was primarily written by Adam Twardoch, with assistance from GPT-4. See [AUTHORS.md](./AUTHORS.md) for contributor details.

## Changes

- **v1.4.0**: Unicode decomposition and normalization
- **v1.3.0**: Renamed some styles
- **v1.1.0**: Change the available styles
- **v1.0.3**: Minor fixes
- **v1.0.0**: Initial release

## Contact

For problems or suggestions, please open an [issue](https://github.com/twardoch/text_fancipy/issues) on GitHub.
