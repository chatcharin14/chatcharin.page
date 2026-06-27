import json
import random
from datetime import date
from pathlib import Path


ZODIAC_SIGNS = [
    "ราศีเมษ", "ราศีพฤษภ", "ราศีเมถุน", "ราศีกรกฎ", "ราศีสิงห์", "ราศีกันย์",
    "ราศีตุลย์", "ราศีพิจิก", "ราศีธนู", "ราศีมังกร", "ราศีกุมภ์", "ราศีมีน",
]

TEMPLATES = {
    "positive": [
        "วันนี้เป็นวันที่ดี — โอกาสใหม่ ๆ จะเข้ามา", 
        "พลังงานของคุณสูง — ทำสิ่งที่สำคัญได้สำเร็จ", 
        "คนรอบตัวให้การสนับสนุน — เปิดใจรับคำแนะนำ",
    ],
    "caution": [
        "ระวังเรื่องเอกสารหรือการสื่อสารที่จะผิดพลาดได้", 
        "อย่าตัดสินใจเร่งรีบ — รอสักนิดก่อนลงมือ", 
        "งบประมาณต้องคุมให้ดี — หลีกเลี่ยงการใช้จ่ายฟุ่มเฟือย",
    ],
    "advice": [
        "เดินออกไปข้างนอกสักพัก — ผ่อนคลายความคิด", 
        "คุยกับคนที่ไว้ใจได้เรื่องแผนงาน", 
        "จดสิ่งที่ต้องทำเป็นรายการให้ชัดเจน",
    ],
}


def generate_for_sign(sign: str) -> dict:
    """Generate a horoscope entry for one zodiac sign."""
    mood_roll = random.random()
    if mood_roll > 0.7:
        mood = "positive"
    elif mood_roll > 0.35:
        mood = "caution"
    else:
        mood = "advice"

    message = random.choice(TEMPLATES[mood])
    lucky_number = random.randint(1, 99)
    lucky_color = random.choice(["Red", "Blue", "Green", "Gold", "Purple", "Silver"])

    return {
        "sign": sign,
        "mood": mood,
        "message": message,
        "lucky_number": lucky_number,
        "lucky_color": lucky_color,
    }


def generate_daily_horoscopes(output_dir: str = "horoscopes") -> Path:
    """Generate horoscopes for all signs and save as JSON file.

    Returns the path to the written JSON file.
    """
    today = date.today().isoformat()
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    data = {
        "date": today,
        "horoscopes": [generate_for_sign(s) for s in ZODIAC_SIGNS],
    }

    out_path = out_dir / f"horoscopes-{today}.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return out_path


def cli():
    import argparse

    parser = argparse.ArgumentParser(description="Generate daily horoscopes and save to JSON.")
    parser.add_argument("--out", "-o", default="horoscopes", help="Output directory for JSON files")
    args = parser.parse_args()

    path = generate_daily_horoscopes(args.out)
    print(f"Wrote horoscopes to: {path}")


if __name__ == "__main__":
    cli()
