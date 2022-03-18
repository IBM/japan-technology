
from posixpath import basename
import re
import frontmatter
import glob
import os
import sys
import shutil
import logging
import copy
import deepl
import hashlib

# deepl auth key
auth_key = "put deepl key here"
target_language ="ja"

search_query = sys.argv[1]

learning_path = "Code-Learning-Paths"
materials = {s: f"Code-{s.capitalize()}" for s in ["articles", "patterns", "tutorials"]}

output_path = "japan-technology/Code-Learning-Paths-jp/docs"
translate_header_keys = ["abstract", "excerpt", "meta_description", "meta_title", "title", "subtitle"]

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(stream_handler)


def load_header_and_body(md_file_path):
  """convert markdown to object
  :return markdown yaml header text and body text
  """
  #with open(md_file_path) as f:
  #  return frontmatter.parse(f.read())
  #return frontmatter.load(md_file_path)
  with open(md_file_path) as f:
    file_contents = f.read()
    file_contents = re.sub('\t', '  ', file_contents)
    return frontmatter.loads(file_contents)


def translate(original, target_lang=target_language):
  # debugcode: return original
  translator = deepl.Translator(auth_key) 

  translated_result = translator.translate_text(original, target_lang=target_lang) 
  return translated_result.text


def translate_body(org_body):
  return translate(org_body)


def translate_header(org_header):
  conv_header = copy.deepcopy(org_header)
  for t in translate_header_keys:
    if t in org_header:
      conv_header[t] = translate(org_header[t])
  return conv_header


def translate_markdown(org_path, conv_path):
  org_path = os.path.abspath(org_path)
  conv_path = os.path.abspath(conv_path)

  logger.debug(f"translate markdown: {org_path} => {conv_path}")

  post = load_header_and_body(org_path)

  post.metadata = translate_header(post.metadata)
  post.content = translate_body(post.content)

  frontmatter.dump(post, conv_path)


def get_real_path(learn_content_dir):
  indexmd_file_path = os.path.join(learn_content_dir, "index.md")

  if not os.path.isfile(indexmd_file_path):
    return None

  # load header
  with open(indexmd_file_path) as f:
    file_contents = f.read()
    file_contents = re.sub('\t', '  ', file_contents)
    learn_content = frontmatter.loads(file_contents)

  if "embedded_slug" in learn_content:
    # is linked content
    from_learn_path = learn_content["embedded_slug"].strip("/")
    for m, p in materials.items():
      from_learn_path = from_learn_path.replace(m, p, 1)
    return (from_learn_path, learn_content["menu_order"])
  else:
    # is direct content
    return (learn_content_dir, learn_content["menu_order"])


def is_same(file1, file2):
  if not os.path.exists(file2):
    return False

  with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
    return hashlib.md5(f1.read()).hexdigest() == hashlib.md5(f2.read()).hexdigest()


def get_copied_filename(from_file_path):
  copied_filename = os.path.basename(from_file_path)
  if copied_filename == "index.md":
    copied_filename = "index_en.md"
  return copied_filename


def get_copy_list(theme_path):
  copy_list = {}
  # get dictionary > key:learning path name, value:yaml header info
  for theme_root_child in glob.iglob(f"{theme_path}/*"):
    if os.path.isdir(theme_root_child):
      real = get_real_path(theme_root_child)
      if real is not None:
        learn_content_dir_path, menu_order = real
        learn_path_name = theme_root_child.split("/")[-1]
        copy_list[menu_order] = f"    - {translate(learn_path_name.replace('-', ' '))}: {learn_content_dir_path}/index.md"

  return copy_list

def is_index_markdown(from_file, to_file):
  return os.path.basename(from_file) == "index.md" and os.path.basename(to_file) == "index_en.md"



# learning path theme name(ex. get_start_with_watson_discovery)
theme_paths = [d for d in glob.iglob(f"{learning_path}/{search_query}") if not os.path.isfile(d)]

for i, theme_path in enumerate(theme_paths):
  logger.info(f"  - {translate(theme_path.split('/')[-1])}:")

  l = get_copy_list(theme_path)
  for o in sorted(l):
    logger.info(l[o])
