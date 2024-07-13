import requests
import os
import time
import webbrowser
import tkinter as tk
import threading

class ZTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ztool")
        self.create_widgets()

    def create_widgets(self):
        self.main_frame = tk.Frame(self.root, padx=20, pady=10)
        self.main_frame.pack()

        self.label = tk.Label(self.main_frame, text="Choose an option:")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.options = {
            "1": "Send Discord Webhook Message",
            "2": "Delete Discord Webhook",
            "3": "IP Address Lookup",
            "4": "What's My IP?",
            "5": "DD0s file sender",
            "6": "Send victim file. Spamming apps",
            "7": "Open Nitro Gen",
            "8": "Color Switch for GUI",
            "9": "File bomber install and send to victim!!!",
            "0": "Exit"
        }

        for key, value in self.options.items():
            option_button = tk.Button(self.main_frame, text=f"{key}. {value}", command=lambda k=key: self.handle_option(k))
            option_button.grid(row=int(key)+1, column=0, columnspan=2, pady=5)

    def handle_option(self, choice):
        if choice == "1":
            self.webhook_spammer()
        elif choice == "2":
            self.webhook_deleter()
        elif choice == "3":
            self.ip_lookup()
        elif choice == "4":
            self.what_is_my_ip()
        elif choice == "5":
            self.file_sender()
        elif choice == "6":
            self.open_link()
        elif choice == "7":
            self.open_nitro_gen()
        elif choice == "8":
            self.color_switch()
        elif choice == "9":
            self.install_file()
        elif choice == "0":
            self.root.quit()
        else:
            print("Invalid option! Please choose again.")

    def webhook_spammer(self):
        self.clear_screen()
        print("==============================")
        print("        Discord Webhook Spammer")
        print("==============================")
        webhook_url = input("Enter Discord webhook URL: ")
        message = input("Enter message to spam: ")
        message_count = int(input("Enter number of messages to send: "))

        print(f"Spamming Discord webhook {webhook_url} with {message_count} messages...")
        for i in range(message_count):
            print(f"Sending message {i + 1}...")
            requests.post(webhook_url, json={"content": message})
        
        print("Webhook spam complete.")
        input("Press Enter to continue...")

    def webhook_deleter(self):
        self.clear_screen()
        print("==============================")
        print("        Delete Discord Webhook")
        print("==============================")
        webhook_url = input("Enter Discord webhook URL to delete: ")

        print(f"Deleting Discord webhook {webhook_url}...")
        requests.delete(webhook_url)
        print("Webhook deleted.")
        input("Press Enter to continue...")

    def ip_lookup(self):
        self.clear_screen()
        print("==============================")
        print("        IP Address Lookup")
        print("==============================")
        ip_address = input("Enter IP address to lookup: ")

        print(f"Looking up information for IP address {ip_address}...")
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        print(response.json())
        input("Press Enter to continue...")

    def what_is_my_ip(self):
        self.clear_screen()
        print("==============================")
        print("        What's My IP?")
        print("==============================")
        print("Retrieving your current IP address...")
        response = requests.get("https://ipinfo.io/ip")
        print(response.text)
        input("Press Enter to continue...")

    def file_sender(self):
        self.clear_screen()
        print("==============================")
        print("        File Sender")
        print("==============================")
        ip = input("Enter IP address to send file to: ")
        num_gb = int(input("Enter number of gigabytes to send: "))

        if num_gb < 1:
            print("Input must be at least 1.")
            input("Press Enter to continue...")
            return

        for i in range(num_gb):
            print(f"Sending file: 1 GB to {ip} - Packet {i + 1}")
            time.sleep(2)
        
        print(f"File sent successfully to {ip}.")
        input("Press Enter to continue...")

    def open_link(self):
        self.clear_screen()
        print("==============================")
        print("        Open Link")
        print("==============================")
        print("Opening link: https://www.mediafire.com/file/vq2259ec6q0tkow/nitro_gens.bat.bat/file")
        webbrowser.open("https://www.mediafire.com/file/vq2259ec6q0tkow/nitro_gens.bat.bat/file")
        input("Press Enter to continue...")

    def open_nitro_gen(self):
        self.clear_screen()
        print("==============================")
        print("        Open Nitro Gen")
        print("==============================")
        print("Opening Nitro Gen: https://nitro-gen-nine.vercel.app/")
        webbrowser.open("https://nitro-gen-nine.vercel.app/")
        input("Press Enter to continue...")

    def color_switch(self):
        self.clear_screen()
        print("==============================")
        print("        Color Switch for GUI")
        print("==============================")
        print("Choose a color for the GUI:")
        print("1. Red")
        print("2. Blue")
        print("3. Green")
        print("4. Turquoise")
        print("5. Magenta")
        print("6. Yellow")
        print("7. White")
        print("8. Grey")
        print("9. Light Blue")
        print("A. Light Green")
        print("B. Light Turquoise")
        print("C. Light Red")
        print("D. Light Magenta")
        print("E. Light Yellow")
        print("F. Light White")
        print("X. Rainbow Animation")
        print("==============================")
        
        color_choice = input("Enter color choice (1-9, A-F, X): ").upper()

        if color_choice in '123456789ABCDEF':
            self.run_color_animation(color_choice)
        elif color_choice == 'X':
            self.run_rainbow_animation()
        else:
            print("Invalid color choice.")
        
        input("Press Enter to continue...")

    def run_color_animation(self, color):
        color_thread = threading.Thread(target=self.animate_single_color, args=(color,))
        color_thread.start()

    def animate_single_color(self, color):
        while True:
            self.root.configure(bg=color.lower())
            time.sleep(1)
            self.root.update()

    def run_rainbow_animation(self):
        rainbow_thread = threading.Thread(target=self.animate_rainbow)
        rainbow_thread.start()

    def animate_rainbow(self):
        colors = ['Red', 'Blue', 'Green', 'Turquoise', 'Magenta', 'Yellow', 'White', 'Grey',
                  'Light Blue', 'Light Green', 'Light Turquoise', 'Light Red', 'Light Magenta',
                  'Light Yellow', 'Light White']
        while True:
            for color in colors:
                self.root.configure(bg=color.lower())
                time.sleep(1)
                self.root.update()

    def install_file(self):
        self.clear_screen()
        print("==============================")
        print("        Install File")
        print("==============================")
        print("Installing file: C:\\Users\\Korbu\\Desktop\\surccecode.bat - Kopie800o - Kopie")
        os.system('start "" "C:\\Users\\Korbu\\Desktop\\surccecode.bat - Kopie800o - Kopie"')
        print("File installation started.")
        input("Press Enter to continue...")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    ztool = ZTool()
    ztool.start()
