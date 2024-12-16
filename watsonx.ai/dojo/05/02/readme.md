# InstructLab CLIのインストール

公式文書: [InstructLab 🐶 (ilab)](https://github.com/instructlab/instructlab/blob/main/README.md)

1. Ubuntuあるいはターミナルを開き、次のコマンドを実行して、Python 仮想環境 ienv を作成します。
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

ここまでの手順で、Apple M1/M2/M3プロセッサーを搭載したmacであれば、AI推論にMetalを利用します。それ以外の環境の場合、CPUで推論処理を実行します。

以下、ハンズオンとしては、必須ではありませんが、Ubuntu(Windows)でNVIDIA GPUが使える場合のオプションとして書いておきます。一部モジュールに[問題](https://github.com/instructlab/instructlab/issues/1864)があり、InstructLab CLIの公式文書通りだとうまくセットアップができないようです。加えて、NVIDIA GPUのサポートについては、データセンター用のプロファイルを想定しており、コンシューマー向けGPUの利用は十分に考慮されていません。
4. UbuntuにPytorchをインストールします。
```
pip install torch torchvision torchaudio
```
5. UbuntuからCUDA 12.4をインストールします。公式手順は[こちら](https://developer.nvidia.com/cuda-12-4-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_network)

 
```
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb
```

```
sudo dpkg -i cuda-keyring_1.1-1_all.deb
```

```
sudo apt-get update
```

```
sudo apt-get -y install cuda-toolkit-12-4
```

5. gitコマンドを使い、Ubuntu環境へInstructLab CLIのソースをダウンロードします。
```
git clone https://github.com/instructlab/instructlab.git
```

6. Ubuntu環境で、次のコマンドを実行します。 

```
sudo apt install cmake
```

```
cd instructlab
```
```
CMAKE_ARGS="-DLLAMA_CUDA=on" pip install .
```
```
pip install packaging wheel setuptools-scm
```
```
pip install .[cuda]
```
```
pip install vllm@git+https://github.com/opendatahub-io/vllm@v0.6.2
```


