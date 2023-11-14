# Text FanciPy

Text FanciPy is a Python tool for converting regular English letters (A-Za-z) in a text to their Unicode counterparts in various “fancy” styles, and vice versa. However, note that any “fancy-styled” text is not proper Unicode text, so it’s not searchable, and it’s not guaranteed to be displayed correctly on all devices. It’s best used for decorative purposes only.

## Features

- Converts the regular English letters in your text to various fancy styles (which are still plain Unicode text).
- Performs Unicode decomposition before the conversion, and Unicode normalization after the conversion. This way, most accented Latin letters also get processed. 
- Converts fancy-styled text back to correct text.
- Can be used via a command line interface (CLI) or imported as a Python package.

Text FanciPy supports several “fancy styles” for text conversion. Only styles with full A-Za-z coverage in The Unicode Standard version 15.0 are included: 

| style  | name              | letters
|--------|-------------------| ---------
| `dflt` | Default           | ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
| `mono` | 𝙼𝚘𝚗𝚘𝚜𝚙𝚊𝚌𝚎         | 𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣
| `bold` | 𝐒𝐞𝐫𝐢𝐟 𝐁𝐨𝐥𝐝        | 𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳
| `bdit` | 𝑺𝒆𝒓𝒊𝒇 𝑩𝒐𝒍𝒅 𝑰𝒕𝒂𝒍𝒊𝒄 | 𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛
| `sans` | 𝖲𝖺𝗇𝗌              | 𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓
| `snbd` | 𝗦𝗮𝗻𝘀 𝗕𝗼𝗹𝗱         | 𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇
| `snit` | 𝘚𝘢𝘯𝘴 𝘐𝘵𝘢𝘭𝘪𝘤       | 𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻
| `snbi` | 𝙎𝙖𝙣𝙨 𝘽𝙤𝙡𝙙 𝙄𝙩𝙖𝙡𝙞𝙘  | 𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯
| `scrb` | 𝓢𝓬𝓻𝓲𝓹𝓽 𝓑𝓸𝓵𝓭       | 𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃
| `frak` | 𝕱𝖗𝖆𝖐𝖙𝖚𝖗 𝕭𝖔𝖑𝖉      | 𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟
| `parn` | 🄟⒜⒭⒠⒩⒮            | 🄐🄑🄒🄓🄔🄕🄖🄗🄘🄙🄚🄛🄜🄝🄞🄟🄠🄡🄢🄣🄤🄥🄦🄧🄨🄩⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵
| `circ` | Ⓒⓘⓡⓒⓛⓔⓓ           | ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ
| `wide` | Ｗｉｄｅ              | ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ

## Installation

To install Text FanciPy, run:

```bash
python3 -m pip install --upgrade text-fancipy
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

For example, convert to _Script Bold_ style some text containing accented Latin letters:

```bash
$ fancipy scrb -t "Książęcych spóźnień czułość"
𝓚𝓼𝓲𝓪̨𝔃̇𝓮̨𝓬𝔂𝓬𝓱 𝓼𝓹𝓸́𝔃́𝓷𝓲𝓮𝓷́ 𝓬𝔃𝓾ł𝓸𝓼́𝓬́
```

Convert text back from all fancy styles back to regular text:

```bash
$ fancipy undo -t "𝖶𝗁𝖺𝗍 ⓐ 𝖜𝖔𝖓𝖉𝖊𝖗𝖋𝖚𝖑 𝒘𝒐𝒓𝒍𝒅!"
What a wonderful world!
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

# Convert back to regular text
regular_text = unfancipy_all(fancy_text)
```


## Changes

- **v1.4.0**: Unicode decomposition and normalization
- **v1.3.0**: Renamed some styles
- **v1.1.0**: Change the available styles 
- **v1.0.3**: Minor fixes
- **v1.0.0**: Initial release

## License

- **Text FanciPy** written by Adam Twardoch, with assistance from GPT-4
- Copyright (c) 2023 Adam Twardoch
- Licensed under the [Apache-2.0 license](./LICENSE.txt)

## Contact

Open an [issue](https://github.com/twardoch/text_fancipy/issues) and describe your problem or suggestion.
