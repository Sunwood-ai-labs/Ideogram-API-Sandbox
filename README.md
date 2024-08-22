<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/Ideogram-API-Sandbox.png" width="100%">
<br>
<h1 align="center">Ideogram-API-Sandbox</h1>
<h2 align="center">
  ～ Your playground for Ideogram API exploration! ～
<br>
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/Ideogram-API-Sandbox">
<img alt="PyPI - Format" src="https://img.shields.io/pypi/format/Ideogram-API-Sandbox">
<img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/Ideogram-API-Sandbox">
<img alt="PyPI - Status" src="https://img.shields.io/pypi/status/Ideogram-API-Sandbox">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/Ideogram-API-Sandbox">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/Ideogram-API-Sandbox">
<a href="https://github.com/Sunwood-ai-labs/Ideogram-API-Sandbox" title="Go to GitHub repo"><img src="https://img.shields.io/static/v1?label=Ideogram-API-Sandbox&message=Sunwood-ai-labs&color=blue&logo=github"></a>
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Sunwood-ai-labs/Ideogram-API-Sandbox">
<a href="https://github.com/Sunwood-ai-labs/Ideogram-API-Sandbox"><img alt="forks - Sunwood-ai-labs" src="https://img.shields.io/github/forks/Ideogram-API-Sandbox/Sunwood-ai-labs?style=social"></a>
<a href="https://github.com/Sunwood-ai-labs/Ideogram-API-Sandbox"><img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/Sunwood-ai-labs/Ideogram-API-Sandbox"></a>
<a href="https://github.com/Sunwood-ai-labs/Ideogram-API-Sandbox"><img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/Sunwood-ai-labs/Ideogram-API-Sandbox"></a>
<img alt="GitHub Release" src="https://img.shields.io/github/v/release/Sunwood-ai-labs/Ideogram-API-Sandbox?color=red">
<img alt="GitHub Tag" src="https://img.shields.io/github/v/tag/Sunwood-ai-labs/Ideogram-API-Sandbox?sort=semver&color=orange">
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/Ideogram-API-Sandbox/publish-to-pypi.yml">
<br>
<p align="center">
  <a href="https://hamaruki.com/"><b>[🌐 Website]</b></a> •
  <a href="https://github.com/Sunwood-ai-labs"><b>[🐱 GitHub]</b></a>
  <a href="https://x.com/hAru_mAki_ch"><b>[🐦 Twitter]</b></a> •
  <a href="https://hamaruki.com/"><b>[🍀 Official Blog]</b></a>
</p>

</h2>

</p>

>[!IMPORTANT]
>このリポジトリのリリースノートやREADME、コミットメッセージの9割近くは[claude.ai](https://claude.ai/)や[ChatGPT4](https://chatgpt.com/)を活用した[AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II)で生成しています。

## 概要

Ideogram-API-Sandboxは、Ideogram APIを活用してAI画像生成の可能性を探索するための実験的なプロジェクトです。このリポジトリには、最新のV_2_TURBOモデルを含むIdeogram APIを簡単に試せるPythonスクリプトが用意されています。

## デモ動画

https://github.com/user-attachments/assets/74daff47-9f38-42ff-81fa-80d64acb170b

## 🚀 はじめに

### 前提条件

- Python 3.7以上
- Ideogram APIキー

### インストール

1. このリポジトリをクローンします：
   ```bash
   git clone https://github.com/Sunwood-ai-labs/Ideogram-API-Sandbox.git
   ```

2. 必要なライブラリをインストールします：
   ```bash
   pip install -r requirements.txt
   ```

3. `.env.example` ファイルを `.env` にリネームし、Ideogram APIキーを設定します：
   ```bash
   IDEOGRAM_API_KEY=your_api_key_here
   ```

### 使用方法

1. `sandbox` ディレクトリに移動します。

2. サンプルスクリプトを実行します：
   ```bash
   python ideogram_api_example.py
   ```
   または
   ```bash
   python ideogram_v2turbo_sample.py
   ```

## 📁 プロジェクト構造

```bash
Ideogram-API-Sandbox/
├─ sandbox/
│  ├─ ideogram_api_example.py
│  ├─ ideogram_v2turbo_sample.py
├─ .env.example
├─ README.md
```

## 📝 更新情報

- 🎉 Ideogram API v2 Turboモデルを用いた高度な画像生成機能を追加しました。 ([![v0.1.0](https://github.com/Sunwood-ai-labs/Ideogram-API-Sandbox/releases/tag/v0.1.0)]) 🟢
- 🎉 Ideogram APIを用いた画像生成機能を追加しました。 ([![v0.1.0](https://github.com/Sunwood-ai-labs/Ideogram-API-Sandbox/releases/tag/v0.1.0)]) 🟢
- 🎉 Ideogram APIキー設定を追加しました。 ([![v0.1.0](https://github.com/Sunwood-ai-labs/Ideogram-API-Sandbox/releases/tag/v0.1.0)]) 🟢
- 🚀 READMEの構造を見直し、読みやすく改善しました。 ([![v0.1.0](https://github.com/Sunwood-ai-labs/Ideogram-API-Sandbox/releases/tag/v0.1.0)]) 🟢
- 🚀 READMEにIdeogram APIリファレンスへのリンクを追加しました。 ([![v0.1.0](https://github.com/Sunwood-ai-labs/Ideogram-API-Sandbox/releases/tag/v0.1.0)]) 🟢
- 🚀 READMEにデモ動画へのリンクを追加しました。 ([![v0.1.0](https://github.com/Sunwood-ai-labs/Ideogram-API-Sandbox/releases/tag/v0.1.0)]) 🟢
- 🚀 READMEの構造化と詳細情報の追加を行いました。 ([![v0.1.0](https://github.com/Sunwood-ai-labs/Ideogram-API-Sandbox/releases/tag/v0.1.0)]) 🟢
- 🚀 英語READMEの更新を行いました。 ([![v0.1.0](https://github.com/Sunwood-ai-labs/Ideogram-API-Sandbox/releases/tag/v0.1.0)]) 🟢

## 🤝 コントリビューション

プロジェクトへの貢献を歓迎します！詳細は[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。

## 📄 ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。

## 🙏 謝辞

- [Ideogram API](https://ideogram.ai/)チームに感謝します。
- このプロジェクトのアイデアや改善に貢献してくださったコミュニティの皆様に感謝します。
- [Ideogram API リファレンス](https://api-docs.ideogram.ai/reference/)