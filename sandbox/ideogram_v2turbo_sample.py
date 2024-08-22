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

def generate_image(api_key, prompt, model="V_2_TURBO", magic_prompt_option="ON", aspect_ratio="ASPECT_16_9", style_type="RENDER_3D"):
    url = "https://api.ideogram.ai/generate"
    
    payload = {
        "image_request": {
            "model": model,
            "prompt": prompt,
            "magic_prompt_option": magic_prompt_option,
            "aspect_ratio": aspect_ratio,
            "style_type": style_type
        }
    }
    
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Api-Key": api_key
    }
    
    logger.info(f"Ideogram APIにリクエストを送信します。プロンプト: {prompt}")
    logger.info(f"パラメータ: モデル={model}, マジックプロンプト={magic_prompt_option}, アスペクト比={aspect_ratio}, スタイル={style_type}")
    
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

    prompt = """
A captivating Pixar-Disney 3D animation scene, ᎩᗩᏆᔑ(◠‿◠), A stunning, hyper-realistic 3D render of a miniature tropical paradise encapsulated within a wine glass.

The interior of the wine glass is transformed into a serene beach scene, complete with pristine white sand, tiny sparkling shells, and an exquisitely detailed palm tree swaying gently under the warm sunlight filtering through the glass.

A quaint, miniature thatched-roof hut stands at one side, and the shimmering blue of the glass itself reflects the azure sky and tranquil ocean waves that seem to lap against the invisible boundaries of this small, enclosed world.

The large name "Ideogram API Sandbox" is delicately inscribed in the sand, evoking a sense of joy and tranquility within this tiny, self-contained paradise.

The cinematic and illustrative style of the rendering transports the viewer to this breathtaking escape, all within the confines of the wine glass, highlighting the juxtaposition of the grand and the small.

bringing a conceptual and imaginative world to life within a simple wine glass.
    """

    logger.info("Ideogram APIリクエストプロセスを開始します")
    result = generate_image(api_key, prompt)

    if result:
        logger.info("生成された画像の情報:")
        logger.info(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        logger.warning("画像が生成されませんでした")

    logger.info("Ideogram APIリクエストプロセスが完了しました")

if __name__ == "__main__":
    main()
