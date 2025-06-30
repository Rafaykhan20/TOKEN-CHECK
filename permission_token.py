import requests
import time
import os
import sys
from colorama import Fore, Style, init
from platform import system

# Initialize colorama
init(autoreset=True)

# Clear the terminal based on OS
def cls():
    if system() == 'Linux' or system() == 'Darwin':
        os.system('clear')
    elif system() == 'Windows':
        os.system('cls')

# Constants for colors and formatting
CLEAR_SCREEN = '\033[2J'
RED = '\033[1;31m'
RESET = '\033[0m'
BLUE = "\033[1;34m"
WHITE = "\033[1;37m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"
GREEN = "\033[1;32m"
BOLD = '\033[1;1m'

cls()
time.sleep(1)
os.system('clear')
logo = ("""
          
 \033[1;31m_______  _______  _______  _______  _______          
\033[1;32m(  ____ )(  ___  )(  ____ \(  ____ \(  ___  )|\     /|
\033[1;33m| (    )|| (   ) || (    \/| (    \/| (   ) |( \   / )
\033[1;36m| (____)|| (___) || (__    | (__    | (___) | \ (_) / 
\033[1;31m|     __)|  ___  ||  __)   |  __)   |  ___  |  \   /  
\033[1;36m| (\ (   | (   ) || (      | (      | (   ) |   ) (   
\033[1;33m| ) \ \__| )   ( || )      | )      | )   ( |   | |   
\033[1;31m|/   \__/|/     \||/       |/       |/     \|   \_/   

\033[1;32m<<═══════════════════════════════════════════════>>
\033[1;36m[*] \033[1;37m𝐎𝐖𝐍𝐄𝐑             \033[1;32m━▷ \033[1;37m𝙍𝘼𝙁𝙁𝘼𝙔 𝙆𝙃𝘼𝙉            \033[1;36m[*]
\033[1;36m[*] \033[1;37m𝐆𝐈𝐓𝐇𝐔𝐁            \033[1;32m━▷ \033[1;37m𝘙𝘢𝘧𝘢𝘺𝘬𝘩𝘢𝘯20            \033[1;36m[*]
\033[1;36m[*] \033[1;37m𝐑𝐔𝐋𝐄𝐗             \033[1;32m━▷ \033[1;37m𝐀𝐋𝐎𝐍𝐄 𝐒𝐓𝐀𝐍𝐃            \033[1;36m[*]
\033[1;36m[*] \033[1;37m𝐓𝐎𝐎𝐋              \033[1;32m━▷ \033[1;37m𝐓𝐎𝐊𝐄𝐍 𝐂𝐇𝐄𝐂𝐊𝐄𝐑          \033[1;36m[*]
\033[1;36m[*] \033[1;37m𝐅𝐀𝐂𝐄𝐁𝐎𝐊           \033[1;32m━▷ \033[1;37m𝐑𝐚𝐟𝐚𝐲 𝐤𝐡𝐚𝐧             \033[1;36m[*]
\033[1;32m<<═══════════════════════════════════════════════>>

""" )
# Print the logo
print(Fore.CYAN + logo + Style.RESET_ALL)

# Start time
print('\u001b[37m' + '\x1b[1;37m======================================================>>')
print("\033[92mStart Time:", time.strftime("%Y-%m-%d %H:%M:%S"))
print('\u001b[37m' + '\x1b[1;37m======================================================>>')

# Function to check a single token
def check_single_token(token):
    url = f'https://graph.facebook.com/me?access_token={token}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            user_id = data.get('id')
            name = data.get('name')
            email = data.get('email', 'Email not available')

            result = (
                f"{CYAN}[+] User ID: {user_id}\n"
                f"{CYAN}[+] Name: {name}\n"
                f"{CYAN}[+] Email: {email}\n"
                f"{CYAN}[+] Token Valid: Yes{RESET}\n"
            )
            print(result)
            save_result(result)
            save_valid_token(token, user_id, name, email)
            return True
        else:
            result = f"{RED}[+] Error: {response.status_code}\n[+] Token Expired or Invalid{RESET}"
            print(result)
            save_result(result)
            return False
    except requests.exceptions.RequestException as e:
        result = f"{RED}[+] Network Error: {e}{RESET}"
        print(result)
        save_result(result)
        return False

# Function to check tokens from a file
def check_tokens_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            tokens = file.read().splitlines()

        total_tokens = len(tokens)
        valid_tokens = 0
        print(f"{MAGENTA}[+] Total tokens to check: {total_tokens}{RESET}")

        for index, token in enumerate(tokens, start=1):
            print(f"\n{CYAN}[+] Checking Token {index}/{total_tokens}: {token[:10]}...{RESET}")
            if check_single_token(token):
                valid_tokens += 1
            time.sleep(1)

        print(f"\n{GREEN}[+] Total valid tokens: {valid_tokens}/{total_tokens}{RESET}")
    except FileNotFoundError:
        print(f"{RED}[+] Error: File not found at {file_path}{RESET}")
    except Exception as e:
        print(f"{RED}[+] Error: {e}{RESET}")

# Function to get Facebook Page Access Token
def get_page_token(user_token):
    url = f'https://graph.facebook.com/v19.0/me/accounts?fields=access_token,name,id&access_token={user_token}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            pages = data.get('data', [])
            if not pages:
                print(f"{RED}[+] No pages found for this user.{RESET}")
                return

            print(f"{CYAN}[+] Pages managed by this user:{RESET}")
            for index, page in enumerate(pages, start=1):
                print(f"{CYAN}[{index}] Page Name: {page.get('name')}")
                print(f"{CYAN}[{index}] Page ID: {page.get('id')}")
                print(f"{CYAN}[{index}] Page Token: {page.get('access_token')}{RESET}")

            with open("page_tokens.txt", "a") as file:
                for page in pages:
                    file.write(
                        f"Page Name: {page.get('name')}\n"
                        f"Page ID: {page.get('id')}\n"
                        f"Page Access Token: {page.get('access_token')}\n"
                        f"{'-'*40}\n"
                    )
            print(f"{GREEN}[+] Page tokens saved to 'page_tokens.txt'.{RESET}")
        else:
            print(f"{RED}[+] Error: {response.status_code}\n[+] Failed to retrieve page tokens.{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}[+] Network Error: {e}{RESET}")

# Function to check token permissions
def check_token_permissions(token):
    url = f"https://graph.facebook.com/v19.0/me/permissions?access_token={token}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "data" in data:
                print(f"{CYAN}[+] Token Permissions:{RESET}")
                messaging_perms = ["pages_messaging", "pages_messaging_subscriptions"]
                for perm in data["data"]:
                    status = f"{GREEN}Granted" if perm['status'] == 'granted' else f"{RED}Not Granted"
                    if perm['permission'] in messaging_perms:
                        print(f"{YELLOW}- {perm['permission']}: {status} (Messaging Permission){RESET}")
                    else:
                        print(f"{CYAN}- {perm['permission']}: {status}{RESET}")
                return True
            else:
                print(f"{RED}[+] Error: No permissions found.{RESET}")
                return False
        else:
            print(f"{RED}[+] Error: {response.status_code} (Token may be invalid).{RESET}")
            return False
    except Exception as e:
        print(f"{RED}[+] API Error: {e}{RESET}")
        return False

# NEW: Function to fetch Messenger conversations
def get_conversations(access_token):
    url = 'https://graph.facebook.com/v19.0/me/conversations'
    params = {
        'access_token': access_token,
        'fields': 'id,name'
    }
    all_conversations = []

    print(f"{YELLOW}[+] Fetching conversations...{RESET}\n")

    while url:
        resp = requests.get(url, params=params)
        data = resp.json()

        if "error" in data:
            print(f"{RED}[+] Error: {data['error']['message']}{RESET}")
            return []

        for convo in data.get("data", []):
            convo_id = convo.get("id", "")
            convo_name = convo.get("name", "Unnamed Conversation")
            all_conversations.append((convo_name, convo_id))

        url = data.get("paging", {}).get("next", None)
        params = None

    return all_conversations

# Function to save results to a file
def save_result(result):
    with open("results.txt", "a") as file:
        file.write(result + "\n\n")

# Function to save valid tokens and their details
def save_valid_token(token, user_id, name, email):
    with open("valid_tokens.txt", "a") as file:
        file.write(
            f"Token: {token}\n"
            f"User ID: {user_id}\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"{'-'*40}\n"
        )

# Main function
def main():
    cls()
    print(logo)
    print(f"{YELLOW}\n[1] Check Single Token")
    print(f"{YELLOW}\n[2] Check Tokens from File")
    print(f"{YELLOW}\n[3] Get Facebook Page Access Token")
    print(f"{YELLOW}\n[4] Check Token Permissions")
    print(f"{YELLOW}\n[5] Fetch Messenger Conversations{RESET}")  # NEW OPTION
    choice = input(f"{CYAN}\n[+] Enter your choice (1-5): {RESET}")

    if choice == '1':
        token = input(f"{CYAN}[+] Enter the token to check: {RESET}")
        check_single_token(token)
    elif choice == '2':
        file_path = input(f"{CYAN}[+] Enter the file path (e.g., tokens.txt): {RESET}")
        check_tokens_from_file(file_path)
    elif choice == '3':
        user_token = input(f"{CYAN}[+] Enter your Facebook User Access Token: {RESET}")
        get_page_token(user_token)
    elif choice == '4':
        token = input(f"{CYAN}[+] Enter the token to check permissions: {RESET}")
        check_token_permissions(token)
    elif choice == '5':  # NEW OPTION
        token = input(f"{CYAN}[+] Enter token to fetch conversations: {RESET}")
        conversations = get_conversations(token)
        print(f"\n{MAGENTA}[+] Conversations Found:{RESET}\n")
        for idx, (name, convo_id) in enumerate(conversations, 1):
            print(f"{YELLOW}[{idx}] Name: {WHITE}{name}{RESET}")
            print(f"{CYAN}    Conversation ID: {GREEN}{convo_id}{RESET}")
            print(f"{BLUE}{'-'*40}{RESET}")
    else:
        print(f"{RED}[+] Invalid choice! Please select 1-5.{RESET}")

if __name__ == "__main__":
    main()