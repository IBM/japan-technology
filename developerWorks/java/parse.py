from bs4 import BeautifulSoup
import sys
import glob
import os

def parse(indexhtml):
  soup = BeautifulSoup(open(indexhtml), "html.parser")

  for meta in soup.find_all("meta"):
    if(meta.get("name") == "keywords"):
      keyword = meta.get("content")
    if(meta.get("name") == "description"):
      description = meta.get("content")

  title = soup.find("title").text
  authordate = soup.find(class_="dw-article-authordate")
  if authordate:
    pubdate = soup.find(class_="dw-article-pubdate").text
    authordate.find(class_="dw-article-pubdate").decompose()
    author = authordate.text
  else:
    author = soup.find("dw-article-archive-author")
    pubdate = soup.find("dw-article-archive-date")

  return [title, description, keyword, author, pubdate]

target_pdf = 'library/*/*.pdf'

print("# 旧developerWorks 日本語版 転載文章一覧")
print('')
print("旧developerWorks 日本語版に掲載されていたJava関連の日本語資料を，このgithubリポジトリで再掲載しています。掲載されている情報は，原則として公開された当時のものであり，現在の情報とは異なっている場合がありますのでご注意ください。")
print('')
print("同じく WebSphere Application Server 関連の日本語資料は [Japan WebSphere User Group (日本WebSphereユーザーグループ)](https://ibm.biz/JapanWebSphereUG) にある [旧developerWorks 日本語版 転載文章一覧リンク](https://community.ibm.com/community/user/wasdevops/blogs/takakiyo-tanaka1/2021/05/14/developerworks?CommunityKey=d6c93aa2-6e10-48da-96dc-3831da8ee185) より参照することができます。")
print('')
print("| タイトル | 概要 | PDF | キーワード | 著者 | 公開日 |")
print("----|----|----|----|----|----")
sp = "|"

metas = []
for pdf_path in glob.glob(target_pdf):
  index_html_path = f"{os.path.dirname(pdf_path)}/index.html"
  if os.path.isfile(index_html_path):
    meta = parse(index_html_path)
    meta.insert(2, f"[{pdf_path}](./{pdf_path})")
    metas.append(meta)

#metas.sort(key=lambda x: x[0])
metas.sort()
for meta in metas:
  print(sp + sp.join([f" {x} " for x in meta]) + sp)
