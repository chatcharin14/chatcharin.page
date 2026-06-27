"""Grade calculator based on score thresholds.

Flow:
- ใส่คะแนน
- ถ้าคะแนน >= 80 => เกรด A
- ถ้าคะแนน >= 70 => เกรด B
- ถ้าคะแนน >= 60 => เกรด C
- ถ้าคะแนน >= 50 => เกรด D
- หากต่ำกว่า 50 => เกรด F
"""


def calculate_grade(score: float) -> str:
    """Return the grade letter for a numeric score."""
    if score >= 80:
        return "A"
    if score >= 70:
        return "B"
    if score >= 60:
        return "C"
    if score >= 50:
        return "D"
    return "F"


def parse_score(value: str) -> float:
    """Convert input string to float and validate the range."""
    try:
        score = float(value)
    except ValueError:
        raise ValueError("กรุณาใส่ตัวเลขเท่านั้น")
    if score < 0 or score > 100:
        raise ValueError("คะแนนต้องอยู่ระหว่าง 0 ถึง 100")
    return score


def main() -> None:
    print("โปรแกรมคำนวณเกรดจากคะแนน")
    print("ตามเงื่อนไข: >=80 A, >=70 B, >=60 C, >=50 D, <50 F")

    while True:
        user_input = input("กรอกคะแนน 0-100 (หรือพิมพ์ exit เพื่อออก): ").strip()
        if user_input.lower() in {"exit", "quit", "ออก", "q"}:
            print("ออกจากโปรแกรมแล้ว")
            break

        try:
            score = parse_score(user_input)
            grade = calculate_grade(score)
            status = "ผ่าน" if grade != "F" else "ไม่ผ่าน"
            print(f"คะแนนของคุณ {score:.0f} => เกรด {grade} ({status})\n")
        except ValueError as error:
            print(f"ข้อผิดพลาด: {error}\n")


if __name__ == "__main__":
    main()
