# 게임 안내 음성(MP3) 생성 스크립트 — edge-tts(Microsoft 신경망 음성, API 키 불필요)
# 사용: pip install edge-tts  →  python make_audio.py
import asyncio, os
import edge_tts

VOICE = "ko-KR-SunHiNeural"
RATE = "-12%"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio")

LINES = {
    "intro": "빈 페트병을 탐색해 봐요. 왼쪽 카드를 누르고, 알맞은 사진을 눌러서 연결해 보세요.",
    "act_step": "발로 밟기",
    "act_see": "눈으로 보기",
    "act_water": "물속에 넣기",
    "res_step": "페트병이 찌그러져요.",
    "res_see": "아무것도 보이지 않아요.",
    "res_water": "뽀글뽀글 거품이 나와요.",
    "ok_step": "딩동댕! 발로 밟으면 페트병이 찌그러져요.",
    "ok_see": "딩동댕! 눈으로 보면 아무것도 보이지 않아요.",
    "ok_water": "딩동댕! 물속에 넣으면 뽀글뽀글 거품이 나와요.",
    "wrong": "다시 한번 생각해 볼까요?",
    "done": "참 잘했어요! 빈 페트병 속에는 눈에 보이지 않는 공기가 들어 있어요.",
}

async def main():
    os.makedirs(OUT, exist_ok=True)
    for key, text in LINES.items():
        await edge_tts.Communicate(text, VOICE, rate=RATE).save(os.path.join(OUT, f"{key}.mp3"))
        print("saved", key)

asyncio.run(main())
