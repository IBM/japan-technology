# InstructLab CLI体験その2 (モデルのサーブとチャット)

このハンズオンでは、InstructLabの主な機能を体験していきます。公式文書は[こちら](https://github.com/instructlab/instructlab?tab=readme-ov-file#-serving-the-model)。

* コマンドは、InstructLab CLIをインストール済みのUbuntuまたはターミナル上で操作してください。

## 全体像
![ilab](https://github.com/user-attachments/assets/3edcea99-7b89-4225-a1a0-fcfceb456d07)

### モデルのサーブ
* 公式文書は[こちら](https://github.com/instructlab/instructlab/tree/main?tab=readme-ov-file#-serving-the-model)
1. 次のコマンドを実行します。
```
ilab model serve
```

出力例:
```
INFO 2024-12-16 22:04:21,714 instructlab.model.serve_backend:56: Using model '/home/ilab/.cache/instructlab/models/granite-7b-lab-Q4_K_M.gguf' with -1 gpu-layers and 4096 max context size.
WARNING 2024-12-16 22:04:29,340 instructlab.model.backends.common:169: Unable to read tokenizer config for model: /home/ilab/.cache/instructlab/models/granite-7b-lab-Q4_K_M.gguf: Unable to load file tokenizer_config.json from /home/ilab/.cache/instructlab/models/granite-7b-lab-Q4_K_M.gguf: [Errno 20] Not a directory: '/home/ilab/.cache/instructlab/models/granite-7b-lab-Q4_K_M.gguf/tokenizer_config.json'. Falling back to in-memory chat template mapping
INFO 2024-12-16 22:04:29,340 instructlab.model.backends.llama_cpp:305: Replacing chat template:
 {% set eos_token = "<|endoftext|>" %}
{% set bos_token = "<|begginingoftext|>" %}
{% for message in messages %}{% if message['role'] == 'pretraining' %}{{'<|pretrain|>' + message['content'] + '<|endoftext|>' + '<|/pretrain|>' }}{% elif message['role'] == 'system' %}{{'<|system|>'+ '
' + message['content'] + '
'}}{% elif message['role'] == 'user' %}{{'<|user|>' + '
' + message['content'] + '
'}}{% elif message['role'] == 'assistant' %}{{'<|assistant|>' + '
' + message['content'] + '<|endoftext|>' + ('' if loop.last else '
')}}{% endif %}{% if loop.last and add_generation_prompt %}{{ '<|assistant|>' + '
' }}{% endif %}{% endfor %}
INFO 2024-12-16 22:04:29,343 instructlab.model.backends.llama_cpp:232: Starting server process, press CTRL+C to shutdown server...
INFO 2024-12-16 22:04:29,343 instructlab.model.backends.llama_cpp:233: After application startup complete see http://127.0.0.1:8000/docs for API.
```
* 注意: Webサービスが起動して、Ubuntuまたはターミナルから入力ができなくなります。

### InstructLabのチャット機能
* 公式文書は[こちら](https://github.com/instructlab/instructlab/tree/main?tab=readme-ov-file#-chat-with-the-model-optional)
1. Ubuntuまたはターミナルの新しいウィンドウを開いてください。コマンドが入力できるようになったら、Python ienv 仮想環境へ切り替えます。
```
cd ~/wxai
source ienv/bin/activate
```


2. チャット機能を起動します。
```
ilab model chat
```

出力例:
```
╭─────────────────────────────────── system ───────────────────────────────────╮
│ Welcome to InstructLab Chat w/ GRANITE-7B-LAB-Q4_K_M.GGUF (type /h for help) │
╰──────────────────────────────────────────────────────────────────────────────╯
>>>
```

3. ヘルプ画面を表示します。
```
/h
```
出力例:
```
╭──────────────────────────────────── system ─────────────────────────────────────╮
│ Help / TL;DR                                                                    │
│                                                                                 │
│  • /q: quit                                                                     │
│  • /h: show help                                                                │
│  • /a assistant: amend assistant (i.e., model)                                  │
│  • /c context: change context (available contexts: default, cli_helper)         │
│  • /lc: list contexts                                                           │
│  • /m: toggle multiline (for the next session only)                             │
│  • /M: toggle multiline                                                         │
│  • /n: new session                                                              │
│  • /N: new session (ignoring loaded)                                            │
│  • /d <int>: display previous response based on input, if passed 1 then         │
│    previous, if 2 then second last response and so on.                          │
│  • /p <int>: previous response in plain text based on input, if passed 1 then   │
│    previous, if 2 then second last response and so on.                          │
│  • /md <int>: previous response in Markdown based on input, if passed 1 then    │
│    previous, if 2 then second last response and so on.                          │
│  • /s filepath: save current session to filepath                                │
│  • /l filepath: load filepath and start a new session                           │
│  • /L filepath: load filepath (permanently) and start a new session             │
│                                                                                 │
│ Press Alt (or Meta) and Enter or Esc Enter to end multiline input.              │
╰─────────────────────────────────────────────────────────────────────────────────╯
>>>
```
4. 何か英語で質問してみましょう。
```
what is InstructLab?
```

出力例:
```
╭────────────────────────── granite-7b-lab-Q4_K_M.gguf ───────────────────────────╮
│ InstructLab is an innovative platform developed by Red Hat, designed to         │
│ facilitate hands-on learning experiences in computer science and technology for │
│ educators and students. This lab environment empowers users to explore and      │
│ experiment with various technologies, such as artificial intelligence, machine  │
│ learning, containerization, and more, in a safe and controlled setting.         │
│ InstructLab's mission is to make cutting-edge technology accessible and         │
│ understandable, fostering the development of future tech talent.                │
│                                                                                 │
│ InstructLab offers several benefits:                                            │
│                                                                                 │
│ 1. **Hands-on Learning:** InstructLab enables users to engage in experiential   │
│ learning through interactive simulations, tutorials, and projects, promoting a  │
│ deeper understanding of complex concepts.                                       │
│ 2. **Curriculum Support:** The platform aligns with popular computer science    │
│ curricula, making it an ideal tool for educators to complement their teaching   │
│ materials.                                                                      │
│ 3. **Flexibility:** InstructLab supports multiple operating systems, including  │
│ Linux, allowing users to work with the technology of their choice and providing │
│ a diverse learning experience.                                                  │
│ 4. **Collaboration:** InstructLab facilitates collaboration among students and  │
│ educators, enabling them to share projects, learn from each other, and engage   │
│ in meaningful discussions.                                                      │
│ 5. **Resources:** The platform offers a wide range of resources, such as        │
│ tutorials, example projects, and documentation, to support users in their       │
│ learning journey.                                                               │
│                                                                                 │
│ By leveraging InstructLab, educators can create dynamic, interactive, and       │
│ engaging learning environments that cater to various learning styles and paces, │
│ ultimately preparing students for success in the technology industry.           │
╰───────────────────────────────────────────────────────── elapsed 6.019 seconds ─╯
>>>
```

5. チャット機能を終了します。
```
/q
```



