import os
import requests
import json
from dotenv import load_dotenv
from loguru import logger
from art import text2art

# 現在の作業ディレクトリのパスを取得
current_dir = os.path.dirname(os.path.abspath(__file__))

# .envファイルのパスを作成
dotenv_path = os.path.join(current_dir, '.env')

# .envファイルを読み込む
load_dotenv(dotenv_path)

logger.add("ideogram_api.log", rotation="500 MB", encoding="utf-8")

def generate_image(api_key, prompt, model="V_2", magic_prompt_option="AUTO"):
    url = "https://api.ideogram.ai/generate"
    
    payload = {
        "image_request": {
            "model": model,
            "prompt": prompt,
            "magic_prompt_option": magic_prompt_option
        }
    }
    
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Api-Key": api_key
    }
    
    logger.info(f"Ideogram APIにリクエストを送信します。プロンプト: {prompt}")
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        logger.success("Ideogram APIからの応答を正常に受信しました")
        return json.loads(response.text)
    else:
        logger.error(f"エラー: {response.status_code}")
        logger.error(response.text)
        return None

def main():
    title = text2art("Ideogram API", font="block")
    print(title)

    # .envファイルからAPIキーを読み込む
    api_key = os.getenv("IDEOGRAM_API_KEY")
    if not api_key:
        logger.error(f"APIキーが見つかりません。{dotenv_path} の.envファイルにIDEOGRAM_API_KEYを設定してください。")
        return

    prompt = "A captivating Pixar-Disney 3D animation scene, ᎩᗩᏆᔑ(◠‿◠), Beautiful sunset over the beach. cool text 'Ideogram API' "

    logger.info("Ideogram APIリクエストプロセスを開始します")
    result = generate_image(api_key, prompt)

    if result:
        logger.info("生成された画像を処理します")
        for i, image in enumerate(result['data'], 1):
            print(f"\n--- 画像 {i} ---")
            logger.info(f"画像URL: {image['url']}")
            logger.info(f"プロンプト: {image['prompt']}")
            logger.info(f"解像度: {image['resolution']}")
            logger.info(f"画像は安全: {image['is_image_safe']}")
    else:
        logger.warning("画像が生成されませんでした")

    logger.info("Ideogram APIリクエストプロセスが完了しました")

if __name__ == "__main__":
    main()
