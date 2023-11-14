# Text FanciPy

Text FanciPy is a Python tool for converting plain English letters (A-Za-z) in a text to their Unicode counterparts in various “fancy” styles, and vice versa. It’s perfect for adding a unique, stylistic touch to your text messages, documents, or any other content, where text styling can be applied. 

However, note that any “fancy-styled” text is not proper Unicode text, so it’s not searchable, and it’s not guaranteed to be displayed correctly on all devices. It’s best used for decorative purposes only.

## Features

- Converts the plain English letters in your text to various fancy styles (which are still plain Unicode text).
- Converts fancy-styled text back to correct text.
- Can be used via a command line interface (CLI) or imported as a Python package.

Text FanciPy supports several “fancy styles” for text conversion: 

| style  | name                   |
|--------|------------------------|
| `bdit` | 𝑩𝒐𝒍𝒅 𝑰𝒕𝒂𝒍𝒊𝒄            |
| `bold` | 𝐁𝐨𝐥𝐝                   |
| `bscr` | 𝓑𝓸𝓵𝓭 𝓢𝓬𝓻𝓲𝓹𝓽            |
| `dbst` | 𝔻𝕠𝕦𝕓𝕝𝕖-𝕤𝕥𝕣𝕦𝕔𝕜          |
| `dflt` | Default                |
| `ital` | 𝐼𝑡𝑎𝑙𝑖𝑐                 |
| `mono` | 𝙼𝚘𝚗𝚘𝚜𝚙𝚊𝚌𝚎              |
| `sans` | 𝖲𝖺𝗇𝗌-𝗌𝖾𝗋𝗂𝖿             |
| `snbd` | 𝗦𝗮𝗻𝘀-𝘀𝗲𝗿𝗶𝗳 𝗕𝗼𝗹𝗱        |
| `snbi` | 𝙎𝙖𝙣𝙨-𝙨𝙚𝙧𝙞𝙛 𝘽𝙤𝙡𝙙 𝙄𝙩𝙖𝙡𝙞𝙘 |
| `snit` | 𝘚𝘢𝘯𝘴-𝘴𝘦𝘳𝘪𝘧 𝘐𝘵𝘢𝘭𝘪𝘤      |

## Installation

To install Text FanciPy, run:

```bash
python3 -m pip install --upgrade text_fancipy
```

For the current development version: 

```
python3 -m pip install --upgrade git+https://github.com/twardoch/text_fancipy
```

## Command-line usage

After installation, `fancipy` can be used directly from the command line.

### With text specified as an argument

Convert text to a fancy style:

```bash
fancipy <style> -t "Your text"
```

For example, to convert to Bold style:

```bash
$ fancipy bold -t "Hello World"
𝐇𝐞𝐥𝐥𝐨 𝐖𝐨𝐫𝐥𝐝
```

Convert text back from a fancy style to plain text:

```bash
fancipy undo -t "𝐇𝐞𝐥𝐥𝐨 𝐖𝐨𝐫𝐥𝐝"
```

### With piping

```bash
$ echo "Hello World" | fancipy bold | fancipy undo
Hello World
```

### With files

You can also specify input and output files:

```bash
fancipy <style> -f input.txt -o output.txt
```

## Python usage

You can use Text FanciPy as a library in your Python scripts.

```python
from text_fancipy.fancipy import fancipy, unfancipy_all

# Convert to fancy text
fancy_text = fancipy("Your Text", "bold")

# Convert back to plain text
plain_text = unfancipy_all(fancy_text)
```


## Development

To contribute to FanciPy, clone the repository from GitHub and install the required development dependencies:

```bash
git clone https://github.com/twardoch/text_fancipy
cd text_fancipy
pip install -e .[testing]
```

## Testing

Run tests using pytest:

```bash
pytest
```


## License

- Text FanciPy (c) 2023 Adam Twardoch, 
- Licensed under the [Apache-2.0 license](./LICENSE.txt)

## Contact

Open an [issue](https://github.com/twardoch/text_fancipy/issues) and describe your problem or suggestion.
