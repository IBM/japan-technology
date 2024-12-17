# InstructLab CLIのインストール

公式文書: [InstructLab 🐶 (ilab)](https://github.com/instructlab/instructlab/blob/main/README.md)

1. Ubuntuあるいはターミナルを開き、次のコマンドを実行して、Python 仮想環境 ienv を作成します。
これまでのwatsonx.ai Dojoで使っていた仮想環境vlabと別の環境であることに注意してください。

```
cd ~/wxai
python -m venv --upgrade-deps ienv
source ienv/bin/activate
pip install --upgrade pip
```
2. 続けて、次のコマンドを実行します。
```
pip cache remove llama_cpp_python

```

3. 次のコマンドを入力して、InstructLab CLIをインストールします。 
```
pip install instructlab
```

ここまでの手順で、Apple M1/M2/M3プロセッサーを搭載したmacであれば、AI推論にMetalを利用します。それ以外の環境の場合、CPUで推論処理を実行します。

2024/12/17時点で、講師のWindows PC環境において、vLLM 6.2がうまくインストールできず、InstructLabからNVIDIA GPUの動作が確認できませんでした。このため、ハンズオンにおいては、NVIDIA GPUの対応方法は、省略します。後日、コンシューマー向けのGPUでの動作確認が取れたら Connpassを通じて、お知らせします。



