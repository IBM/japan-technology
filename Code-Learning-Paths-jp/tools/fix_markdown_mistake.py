import re
import frontmatter
import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s'))
logger.addHandler(stream_handler)


def load_header_and_body(md_file_path):
    """convert markdown to object
    :return markdown yaml header text and body text
    """
    # with open(md_file_path) as f:
    #    return frontmatter.parse(f.read())
    # return frontmatter.load(md_file_path)
    with open(md_file_path) as f:
        file_contents = f.read()
        file_contents = re.sub('\t', '    ', file_contents)
        return frontmatter.loads(file_contents)


# debug-
# conv_path = "japan-technology/Code-Learning-Paths-jp/docs/Code-Tutorials/protect-your-data-using-data-privacy-features/index.md"
#conv_path = "japan-technology/Code-Learning-Paths-jp/docs/Code-Tutorials/learn-to-discover-data-that-resides-in-your-data-sources/index.md"
conv_path = sys.argv[1]
print(conv_path)
md = frontmatter.load(conv_path)

# 本来"## "であるものが"# #"になっている場合がある。
# 見出しは"#"、"##"、"###"と階層化できるが、現状は２階層目の”##”での問題だけが見つかっている。他の階層の情報求む！
heading = re.compile(r'^(# #+)(.*)$')
numlist = re.compile(r'^(\s*1.\s*|\s*-\s*)(\S.*)$')
asterlist = re.compile(r'^(\s*\*)(.*)$')
siteurl = re.compile(r"www\.ibm\.com/")
backquote = re.compile(r'`')
bad_backquote = re.compile(r'^(\s*)(``)(?!`)(.*)$')
italic = re.compile(r'(?<!\*)\*(?!\*)')
asterisk = re.compile(r'\*')
italic = re.compile(r'(?<!\*)\*(?!\*)')
bold = re.compile(r'(?<!\*)\*\*(?!\*)')
bolditalic = re.compile(r'(?<!\*)\*\*\*(?!\*)')
blacket_jp_open = re.compile(r'「')
blacket_jp_close = re.compile(r'」')
blacket_open = re.compile(r'\[')
blacket_close = re.compile(r'\]')
imageurl = re.compile(r'(画像|イメージ)/')


def print_matched(header, result):
    print(f"line {i}/{header}/{result}")


fix_md_lines = []
is_in_codeblock = False
for i, md_line in enumerate(md.content.splitlines()):
    # codeblockの中は処理しない
    if md_line.strip().startswith('```'):
        is_in_codeblock = not is_in_codeblock
        continue
    result = bad_backquote.search(md_line)
    if result:
        parts = result.groups()
        print_matched("codeblock", md_line)
        md_line = f"{parts[0]}{parts[1]}`{parts[2]}"
        is_in_codeblock = not is_in_codeblock

    if is_in_codeblock:
        continue

    # 見出し、他の要素と共に使われない
    result = heading.search(md_line)
    if result:
        print_matched("heading", result.string)
        hitted = result.groups()
        fix_md_lines.append(f"{hitted[0].replace(' ', '')} {hitted[1]}")
        continue

    fix_md_line = ""
    result = numlist.search(md_line)
    if result:
        fix_md_line += result.groups()[0].rstrip() + " "
        md_line = result.groups()[1].strip()

        if fix_md_line != result.groups()[0]:
            print_matched("num-hyphen list", result.string)

    result = re.findall(asterisk, md_line)
    if result:
        if len(result) % 2 != 0:
            # *が奇数ある場合は不整合の可能性がある
            if md_line.strip().startswith('*'):
                # 先頭に * があるリスト表記パターン(正しい)
                result2 = asterlist.search(md_line)
                fix_md_line += result2.groups()[0].rstrip() + " "
                md_line = result2.groups()[1].strip()

    sentences = []
    for md_sentence in md_line.split("。"):
        if not md_sentence.strip().startswith('```') and len(re.findall(backquote, md_sentence)) % 2 != 0:
            print_matched("backquote", md_sentence)
            md_sentence = "`" + md_sentence
        if len(re.findall(blacket_close, md_sentence)) - len(re.findall(blacket_open, md_sentence)) == 1:
            print_matched("blacket", md_sentence)
            md_sentence = "[" + md_sentence

        if len(re.findall(italic, md_sentence)) % 2 != 0:
            print_matched("italic", md_sentence)
            md_sentence = "*" + md_sentence
        if len(re.findall(bold, md_sentence)) % 2 != 0:
            print_matched("bold", md_sentence)
            md_sentence = "**" + md_sentence
        if len(re.findall(bolditalic, md_sentence)) % 2 != 0:
            print_matched("bolditalic", md_sentence)
            md_sentence = "***" + md_sentence

        if len(re.findall(blacket_jp_close, md_sentence)) - len(re.findall(blacket_jp_open, md_sentence)) == 1:
            print_matched("blacket_jp", md_sentence)
            md_sentence = "「" + md_sentence
        sentences.append(md_sentence)
    md_line = '。'.join(sentences)

    result = siteurl.search(md_line)
    if result:
        base = md_line
        for s in ['cloud', 'watson', 'products']:
            md_line = md_line.replace(f"www.ibm.com/{s}", f"www.ibm.com/jp-ja/{s}")
        if md_line != base:
            print_matched("siteurl", result.string)

    result = imageurl.search(md_line)
    if result:
        print_matched("imageurl", result.string)
        md_line = md_line.replace('画像/', 'images/').replace('イメージ/', 'images/')

    fix_md_line += md_line
    fix_md_lines.append(fix_md_line)

md.content = '\n'.join(fix_md_lines)
frontmatter.dump(md, conv_path)
