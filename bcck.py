import random
LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "!@#$%^&*()"
def password_strength(pw):
    """Đánh giá độ mạnh của mật khẩu"""
    score = 0
    if any(c.islower() for c in pw): score += 1
    if any(c.isupper() for c in pw): score += 1
    if any(c.isdigit() for c in pw): score += 1
    if any(c in SYMBOLS for c in pw): score += 1
    if len(pw) >= 12: score += 1
    levels = {
        1: "Rất yếu",
        2: "Yếu",
        3: "Trung bình",
        4: "Mạnh",
        5: "Rất mạnh"
    }
    return levels.get(score, "Không xác định")
while True:
    print("\n=== Trình tạo mật khẩu ===")
    while True:
        try:
            count = int(input("Số lượng mật khẩu muốn tạo: "))
            if count > 0:
                break
            print("Số lượng phải là số nguyên dương!")
        except:
            print("Vui lòng nhập số!")
    print("\nChọn nhóm ký tự (y = dùng, n = bỏ qua):")
    use_lower = input("Dùng chữ thường? (y/n): ").lower() == "y"
    use_upper = input("Dùng chữ hoa? (y/n): ").lower() == "y"
    use_num   = input("Dùng chữ số? (y/n): ").lower() == "y"
    use_sym   = input("Dùng ký tự đặc biệt? (y/n): ").lower() == "y"
    if not (use_lower or use_upper or use_num or use_sym):
        print("Bạn phải chọn ít nhất 1 nhóm ký tự!")
        continue
    while True:
        try:
            length = int(input("Độ dài mật khẩu (>= 4): "))
            if length >= 4:
                break
            print("Độ dài phải >= 4!")
        except:
            print("Vui lòng nhập số!")
    pool = ""
    if use_lower: pool += LOWER
    if use_upper: pool += UPPER
    if use_num:   pool += NUMBERS
    if use_sym:   pool += SYMBOLS
    print("\nKết quả")
    for _ in range(count):
        password = ""
        mandatory = []
        if use_lower: mandatory.append(random.choice(LOWER))
        if use_upper: mandatory.append(random.choice(UPPER))
        if use_num: mandatory.append(random.choice(NUMBERS))
        if use_sym: mandatory.append(random.choice(SYMBOLS))
        while len(password) + len(mandatory) < length:
            password += random.choice(pool)
        password += "".join(mandatory)
        password = ''.join(random.sample(password, len(password)))
        print(f"→ {password}   ({password_strength(password)})")
    again = input("\nTạo tiếp? (y/n): ").lower()
    if again != "y":
        print("Thoát chương trình. Tạm biệt!")
        break
