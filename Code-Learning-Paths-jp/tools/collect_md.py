#!/usr/bin/env python3

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
auth_key = "put deepl auth key here""
target_language ="ja"

search_query = "get-started-watson-discovery"
#search_query = "*cloud*pak*"

learning_path = "../../Code-Learning-Paths"
materials = {s: f"../../Code-{s.capitalize()}" for s in ["articles", "patterns", "tutorials"]}

output_path = "japan-technology/Code-Learning-Paths-jp/docs""
translate_header_keys = ["abstract", "excerpt", "meta_description", "meta_title", "title", "subtitle"]

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
  #with open(md_file_path) as f:
  #  return frontmatter.parse(f.read())
  return frontmatter.load(md_file_path)


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
    learn_content = frontmatter.load(f)

  if "embedded_slug" in learn_content:
    # is linked content
    from_learn_path = learn_content["embedded_slug"].strip("/")
    for m, p in materials.items():
      from_learn_path = from_learn_path.replace(m, p, 1)
    return from_learn_path
  else:
    # is direct content
    return learn_content_dir


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
  copy_list = []
  # get dictionary > key:learning path name, value:yaml header info
  for theme_root_child in glob.iglob(f"{theme_path}/*"):
    if os.path.isfile(theme_root_child):
      copied_filename = get_copied_filename(theme_root_child)
      copy_list.append((os.path.abspath(theme_root_child), os.path.join(output_path, theme_path, copied_filename)))
    elif os.path.isdir(theme_root_child):
      learn_content_dir_path = get_real_path(theme_root_child)
      if learn_content_dir_path is None:
        continue

      for f in glob.iglob(f"{learn_content_dir_path}/**", recursive=True):

        if os.path.isdir(f) or "/nl/" in f:
          continue

        copy_from_file_path = os.path.abspath(f)
        copied_filename = get_copied_filename(f)

        copy_to_file_path = os.path.join(output_path, os.path.dirname(f), copied_filename)
        copy_list.append((copy_from_file_path, copy_to_file_path))

  return copy_list

def is_index_markdown(from_file, to_file):
  return os.path.basename(from_file) == "index.md" and os.path.basename(to_file) == "index_en.md"


def need_translate(from_file, to_file):
  is_sames = is_same(from_file, to_file)

  if is_sames:
    logger.debug(f"{from_file} is exclude because one was already copied.")

  return not is_sames


def copy_file(f, t):
  os.makedirs(os.path.dirname(t), exist_ok=True)
  shutil.copy(f, t)


# learning path theme name(ex. get_start_with_watson_discovery)
theme_paths = [d for d in glob.iglob(f"{learning_path}/{search_query}") if not os.path.isfile(d)]

for i, theme_path in enumerate(theme_paths):
  logger.info(f"{i + 1}: {theme_path.split('/')[-1]}")

  for from_file, to_file in get_copy_list(theme_path):
    logger.debug(f"{from_file} => {to_file}")

    if is_index_markdown(from_file, to_file):
      translate_indexmd_file_path = os.path.join(os.path.dirname(to_file), os.path.basename(from_file))
      if need_translate(from_file, to_file):
        copy_file(from_file, to_file)
        translate_markdown(to_file, translate_indexmd_file_path)
    else:
      copy_file(from_file, to_file)

    #  logger.info(f"  converted: {md_file_path}")

  #for learn_theme, learn_content in sorted(learn_contents.items(), key=lambda x: x[1]["menu_order"]):
