# InstructLab CLIのインストール

公式文書: [InstructLab 🐶 (ilab)](https://github.com/instructlab/instructlab/blob/main/README.md)

1. Ubuntuあるいはターミナルを開き、次のコマンドを実行して、Python 仮想環境 ilab を作成します。
これまでのwatsonx.ai Dojoで使っていた仮想環境vlabと別の環境であることに注意してください。

```
cd ~/wxai
python -m venv --upgrade-deps ienv
source ienv/bin/activate
```
2. 続けて、次のコマンドを実行します。
```
pip cache remove llama_cpp_python

```

3. 次のコマンドを入力して、InstructLab CLIをインストールします。 
```
pip install instructlab
```

