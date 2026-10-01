import random
from datetime import datetime

print("=" * 45)
print("🤖 MINI AI ASSISTANT")
print("=" * 45)

name = input("Ismingiz: ")

responses = {
    "salom": [
        f"Salom, {name}! 👋",
        f"Assalomu alaykum, {name}!",
        "Salom! Qanday yordam beray?"
    ],
    "qalaysan": [
        "Yaxshiman! 😎",
        "Ajoyib! Sizchi?",
        "Hammasi joyida!"
    ],
    "nima qila olasan": [
        "Men savollarga javob beraman, vaqtni aytaman va oddiy hisob-kitob qilaman.",
        "Men siz bilan suhbatlasha olaman 🤖"
    ]
}

def get_response(message):
    message = message.lower()

    for keyword in responses:
        if keyword in message:
            return random.choice(responses[keyword])

    if "vaqt" in message or "soat" in message:
        return "Hozirgi vaqt: " + datetime.now().strftime("%H:%M:%S")

    if "sana" in message:
        return "Bugungi sana: " + datetime.now().strftime("%d.%m.%Y")

    if message.startswith("hisobla"):
        try:
            expression = message.replace("hisobla", "").strip()
            result = eval(expression)
            return f"Natija: {result}"
        except:
            return "Hisoblashda xatolik bor."

    if "rahmat" in message:
        return "Arzimaydi! 😊"

    if "xayr" in message:
        return "Xayr! Keyin yana gaplashamiz 👋"

    return "Buni hali tushunmadim 🤔"


while True:
    user_message = input("\nSiz: ")

    answer = get_response(user_message)

    print("AI:", answer)

    if "xayr" in user_message.lower():
        break
