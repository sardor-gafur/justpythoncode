while True:
    print("\n--- CALCULATOR ---")
    print("1. Qo'shish")
    print("2. Ayirish")
    print("3. Ko'paytirish")
    print("4. Bo'lish")
    print("5. Chiqish")

    choice = input("Tanlang: ")

    if choice == "5":
        print("Dastur tugadi.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Noto'g'ri tanlov!")
        continue

    try:
        a = float(input("Birinchi son: "))
        b = float(input("Ikkinchi son: "))

        if choice == "1":
            result = a + b

        elif choice == "2":
            result = a - b

        elif choice == "3":
            result = a * b

        elif choice == "4":
            if b == 0:
                print("0 ga bo'lish mumkin emas!")
                continue

            result = a / b

        print(f"Natija: {result}")

    except ValueError:
        print("Faqat son kiriting!")
