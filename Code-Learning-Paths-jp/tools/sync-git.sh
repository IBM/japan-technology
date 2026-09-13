base_url="git@github.ibm.com:Tetsuya-Kawano/"
repo_pre="Code-"
command=pull

for t in Tutorials Articles Patterns Learning-Paths
do
  if [ ${command} = clone ]; then
    git ${command} ${base_url}${repo_pre}${t}.git
  else
    cd ${repo_pre}${t}
    echo "sync github repo ${repo_pre}${t}"
    git ${command}
    cd ..
  fi
done

