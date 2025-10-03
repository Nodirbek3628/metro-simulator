import random, time


def waiting_area():
    while True:
        t  = random.randint(15,200)
        ch = random.randint(15,200)
        km = random.randint(5,10)
        x = "🚇"
        y = 0.1
      
        print(f"\n🚉 {km} ta bekatga yo‘l olindi....\n")

        for i in range(1,km+1):
            print(x)
            time.sleep(y)
            print(f"Bekat {i}/{km}")

        print(f"\n➡️ {t} yo‘lovchi tushdi")
        print(f"⬅️ {ch} yo‘lovchi chiqdi")
        print("🏃🏃‍♂🏃‍♂ Yo‘lovchilar harakatda...")
        print("⏳ Bekatda kutilyapti...\n")
        time.sleep(5)  


waiting_area()

