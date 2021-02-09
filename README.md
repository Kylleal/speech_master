# speech_master

音声関係のソースコードです。

一通り、音声API関連を触った結果、SpeechRecognitionのAPIが無料でありながらとても優秀だったのでここにコードを置きます。

また、無料で動く音声からの感情分析API Empath を使っているでもも、あります。

これらのソースコードをひとまとめにしたものが、final.py　ですが、まずはデモからであれば、ほかのコードを触ってください。

また、ライブラリに pyaudio　がありますが、これは普通にcondaやpipでダウンロードできないため、下のリンクから自分に合ったpython環境でダウンロードしてください。

https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

今回のソースコードでは、リアルタイムの音声認識は行っておりません。もし、リアルタイムにやりたい場合、個人的にgoogle speech API が一番優秀でしたので、おすすめいたします。

実行環境

python 3.8

pyaudio 

SpeechRecognition 3.8.1
