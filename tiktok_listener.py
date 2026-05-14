from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Mode sans tête (pas de fenêtre)
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def listen_to_chat(driver):
    driver.get("https://www.tiktok.com/@TON_PSEUDO/live")  # Remplace par ton pseudo

    print("🔍 Connexion au live TikTok...")
    time.sleep(5)  # Attend que la page charge

    try:
        while True:
            # Cherche le chat (à adapter selon la structure de TikTok)
            chat_messages = driver.find_elements(By.CSS_SELECTOR, "div[data-e2e='chat-message']")
            for message in chat_messages:
                if "rose" in message.text.lower():  # Détecte le mot "rose"
                    print("🌹 Message 'rose' détecté !")
                    with open("results.txt", "w", encoding="utf-8") as f:
                        f.write("trigger")
                    time.sleep(6)  # Évite les déclenchements multiples
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Arrêt du script...")
        driver.quit()

if __name__ == "__main__":
    driver = setup_driver()
    try:
        listen_to_chat(driver)
    except KeyboardInterrupt:
        print("\n🛑 Arrêt du script...")
        driver.quit()
