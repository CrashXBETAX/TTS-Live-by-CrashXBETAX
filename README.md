<h1 align="center">🔊<br>
⌨️</h1>
<h3 align="center">TTS-Live Simple by CrashXBETAX</h3>
<br>
<p align="center">
  <a href="https://github.com/CrashXBETAX/TTS-Live-by-CrashXBETAX/issues"><strong>Report Bug »</strong></a>
</p>
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o projeto</a>
    </li>
    <li><a href="#instalação">Instalação</a></li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#licença">Licença</a></li>
    <li><a href="#contato">Contato</a></li>
  </ol>
</details>

## Sobre o projeto
### Objetivo:

Esse projeto é a conversão de texto em voz e reproduzir instantânea por emulador de terminal. A saída de áudio pode redirecionar para microfone usando algum programa como VB-Cable Virtual. Será útil para pessoa com deficiência auditiva em reunião com ouvintes.

#### Online
TTS-Live Simple Online usa uma biblioteca [gTTS](https://github.com/pndurette/gTTS) que usa a API de conversão de texto em voz do Google Tradutor. 

##### Pré-requisitos
<list>
  <li><a href="https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5"> A versão 3.10 do Python do Microsoft Store</li>
  <li><a href="https://github.com/pndurette/gTTS"> gTTS</li>
  <li><a href="https://pyglet.org"> pyglet</li>
  <li><a href="https://vb-audio.com/Cable"> [Opcional] VB-Audio CABLE</li>
</list>

#### Offline
TTS-Live Simple Offline usa uma biblioteca [pyttsx3](https://github.com/nateshmbhat/pyttsx3) que usa um motor do sistema operacional para converter de texto em fala.

##### pyttsx3 suporta três motores de sistema operacional:
<list>
  <li>Windows - SAPI5 (Testado)</li> 
  <li>Mac OS - NSSpeechSynthesizer (Não testado)</li>
  <li>Linux - espeak (Não testado)</li>
</list>

##### Pré-requisitos
<list>
  <li><a href="https://www.python.org/downloads"> A versão mais recente do Python 3</li>
  <li><a href="https://github.com/nateshmbhat/pyttsx3"> pyttsx3</li>
  <li>Sistema operacional com motor de TTS que pyttsx3 suporta</li>
  <li><a href="https://vb-audio.com/Cable"> [Opcional] VB-Audio CABLE</li>
</list>

## Instalação
### Online:
Instale [a versão 3.10 do Python do Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5)

Instale a biblioteca [gTTS](https://github.com/pndurette/gTTS) com comando `pip install gTTS` pelo emulador de terminal

Instale a biblioteca [pyglet](https://pyglet.org) com comando `pip install pyglet` pelo emulador de terminal

Baixe o arquivo TTS-Live Simple Online na [release](https://github.com/CrashXBETAX/TTS-Live-by-CrashXBETAX/releases)

[Opcional] Para Windows: Instale a driver [VB-Audio Virtual](https://vb-audio.com/Cable/) ou cross-platform: conecte o cabo AUX da saída de audio na entrada de microfone.

### Offline:
Instale [a versão mais recente do Python](https://www.python.org/downloads)

Instale a biblioteca [pyttsx3](https://github.com/pndurette/gTTS) com comando `pip install pyttsx3` pelo emulador de terminal

Baixe o arquivo TTS-Live Simple Offline na [release](https://github.com/CrashXBETAX/TTS-Live-by-CrashXBETAX/releases)

[Opcional] Para Windows: Instale a driver [VB-Audio Virtual](https://vb-audio.com/Cable/) ou para cross-platform: conecte o cabo AUX da saída de audio na entrada de microfone.

## Uso
Para usar VB-Audio Virtual, configure o áudio para redirecionar ao microfone.

Execute o emulador de terminal com pasta onde o arquivo TTS-Live Simple está.

Abre o arquivo TTS-Live Simple com comando `python "TTS-Live Simple Online"` ou `python "TTS-Live Simple Offline"`

Para usar umas frases prontas, digite número no terminal. Clique em Enter para converter e reproduzir o áudio (Podem personalizar frases prontas)

Para digitar frase, digite no terminal. Clique em Enter para converter e reproduzir o áudio

## Licença
Esse projeto está sob licença MIT. Veja o arquivo [LICENÇA](LICENSE) para mais detalhes.<br>

## Contato
Gabriel Hagui

<a href="mailto:gabrielhagui@live.com" target="_blank"><img src="https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white" target="_blank"></a>
