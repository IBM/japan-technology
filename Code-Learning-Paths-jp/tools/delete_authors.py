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

learning_path = "../docs"

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
    #  return frontmatter.parse(f.read())
    # return frontmatter.load(md_file_path)
    with open(md_file_path) as f:
        file_contents = f.read()
        file_contents = re.sub('\t', '  ', file_contents)
        return frontmatter.loads(file_contents)


for md_path in glob.glob(f"{learning_path}/**/*.md", recursive=True):
    logger.info(md_path)

    md_path = os.path.abspath(md_path)
    post = load_header_and_body(md_path)
    if "authors" in post.metadata:
        post.metadata["authors"] = ""
    frontmatter.dump(post, md_path)
