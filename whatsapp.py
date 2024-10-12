from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import keyboard

def init_driver():
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com")
    input("Scan the QR code and press Enter to continue...\n")
    return driver

def search_contact(driver, contact_name):
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.send_keys(contact_name)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

def send_message(driver, message):
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    message_box.click()
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)

def send_message_loop(driver, message, interval, number_of_messages):
    for i in range(number_of_messages):
        try:
            send_message(driver, message)
            print(f"{i + 1} messages are being sent. Press Esc to stop.")
            if interval:
                time.sleep(interval)

            if keyboard.is_pressed('esc'):
                print("Loop stopped.")
                time.sleep(2)
                break

        except Exception as e:
            print(f"Failed, error: {e}")
            time.sleep(2)
            break
    else:
        print("Operation successful.")
        time.sleep(2)

def display_menu():
    os.system("cls")
    print("""    ░██╗░░░░░░░██╗██╗░░██╗░█████╗░████████╗░██████╗░█████╗░██████╗░██████╗░        ██████╗░░█████╗░████████╗
    ░██║░░██╗░░██║██║░░██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗        ██╔══██╗██╔══██╗╚══██╔══╝
    ░╚██╗████╗██╔╝███████║███████║░░░██║░░░╚█████╗░███████║██████╔╝██████╔╝        ██████╦╝██║░░██║░░░██║░░░
    ░░████╔═████║░██╔══██║██╔══██║░░░██║░░░░╚═══██╗██╔══██║██╔═══╝░██╔═══╝░        ██╔══██╗██║░░██║░░░██║░░░
    ░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║░░░██║░░░██████╔╝██║░░██║██║░░░░░██║░░░░░        ██████╦╝╚█████╔╝░░░██║░░░
    ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░        ╚═════╝░░╚════╝░░░░╚═╝░░░\n""")
    print("\n=== WhatsApp Bot Menu ===")
    print("Type 'menu' at any time to return to the menu")
    print("1. Send a message")
    print("2. Send multiple messages")
    print("3. Change contact")
    print("4. Quit")
    choice = input("Choose an option: ")
    return choice

def get_contact_name():
    contact_name = input("Contact or group name: ")
    if contact_name.lower() == "menu":
        return None
    return contact_name

if __name__ == "__main__":
    driver = init_driver()

    contact_name = get_contact_name()
    if contact_name is None:
        exit()

    search_contact(driver, contact_name)

    while True:
        choice = display_menu()

        if choice == '1':
            message = input("What message do you want to send? ")
            if message.lower() == "menu":
                continue
            send_message(driver, message)
            print("Message sent! Press any key to continue.")
            os.system("pause")

        elif choice == '2':
            message = input("What message do you want to send? ")
            if message.lower() == "menu":
                continue
            interval_input = input("Delay between messages? Type 'no' for spam: ")
            if interval_input.lower() == "menu":
                continue
            number_of_messages = int(input("How many messages do you want to send? "))
            if number_of_messages == "menu":
                continue

            if interval_input.lower() == "no":
                interval = None
            else:
                interval = int(interval_input)

            send_message_loop(driver, message, interval, number_of_messages)

        elif choice == '3':
            contact_name = input("New contact or group name: ")
            if contact_name.lower() == "menu":
                continue
            search_contact(driver, contact_name)

        elif choice == '4':
            print("Closing bot...")
            time.sleep(2)
            os.system("cls")
            for _ in range(15):
                os.system("echo.")
            driver.quit()
            break

        else:
            print("Invalid choice")
