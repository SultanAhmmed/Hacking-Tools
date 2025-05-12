from requests import post
from requests.utils import quote as urlEncode
from json import loads
import os

def clear_screen():
    """Clear the terminal screen cross-platform"""
    os.system('cls' if os.name == 'nt' else 'clear')



def show_banner():
    clear_screen()
    banner = f"""
\033[1;33m
░░▒▒▓▓██ GHOSTGATE ██▓▓▒▒░░  
   _______________  
  /  _|  _  |_   _|  
 / / | | | | | |  
/ /__| |_| | | |  
\\____/\\___/  |_| \n  
\033[1;33m👻 Your links vanish into the shadows... 👻  
───────────────────────────────  
\033[1;37m[+] Created By: \033[1;36mSultan Ahmmed
\033[1;37m[+] Github: \033[1;36mgithub.com/SultanAhmmed
\033[1;37m[+] Version: \033[1;36m1.0.0\033[1;33m
───────────────────────────────
"""
    
    print(banner)

class GhostGate:
    def __init__(self, url, masking_domain="google.com", keywords=["login"],alias=None):
        self.url = url
        self.masking_domain = masking_domain
        self.keywords = keywords if isinstance(keywords, list) else [keywords]
        self.shorturl = None
        self.alias = alias    
    def shorten(self):
        
        encoded_url = urlEncode(self.url)
        # api_url = (f"https://is.gd/create.php?format=json&url={encoded_url}")
        
        if self.alias:
            payload = {
                "url": self.url,
                "alias": self.alias
            }
        else:
            payload = {
                "url": self.url,
            }

        headers = {
            "Accept": "application/json"
        }
        
        shorter_main_url = "https://spoo.me"
        response = post(shorter_main_url, data=payload, headers=headers)
        json_data = loads(response.text)
            
        try:
            self.shorturl = json_data["short_url"]
        except:
            self.shorturl = self.url
        return self.shorturl

    def mask_url(self):
        # Combine multiple keywords with hyphens
        keyword_str = '-'.join(self.keywords)
        return self.shorturl.replace("https://", f"https://{self.masking_domain}-{keyword_str}@")

def get_multiple_keywords():
    print("\n\033[32m[+]\033[36m Enter keywords (login,auth)\033[34m (default: login)\033[0m")
    user_input = input("\033[95m[➤ ] \033[37m").strip()
    
    if not user_input:
        return ["login"]
    
    # Split by commas and clean up whitespace
    keywords = [kw.strip() for kw in user_input.split(',') if kw.strip()]
    return keywords if keywords else ["login"]

def main():
    show_banner()
    try:
        # Get user input with color formatting
        print("\033[32m[+]\033[36m Enter URL to mask\033[34m(https://your-long-url.com)\033[0m")
        url = input("\033[95m[➤ ] \033[37m").strip()
        if not url.startswith(('http://', 'https://')):
            url = f'https://{url}'

        print("\n\033[32m[+]\033[36m Enter masking domain \033[34m(default: google.com)\033[0m")
        masking_domain = input("\033[95m[➤ ] \033[37m").strip() or "google.com"

        print("\n\033[32m[+]\033[36m Enter custom Alias \033[34m(*spoo.me/your-custom-alias)\033[0m")
        alias = input("\033[95m[➤ ] \033[37m").strip()

        keywords = get_multiple_keywords()

        # Process request
        ghost = GhostGate(url, masking_domain, keywords, alias)
        print("\n\033[33m[~] Generating masked link...\033[0m")
        
        if ghost.shorten():
            masked_url = ghost.mask_url()
            if masked_url:
                print(f"\n\033[1;33m[✓] Masked URL:\033[0m \033[1;36m{masked_url}\033[0m\n")
                print("\n\033[32m[>] Thank you for using GhostGate!\033[0m")
                return

        print("\n\033[31m[✗] Failed to create masked URL\033[0m")

    except KeyboardInterrupt:
        print("\n\033[31m[!] Operation cancelled by user\033[0m")
    finally:
        print("\n\033[31m[>] Exiting the applicaiton...\n\n\033[0m")

if __name__ == "__main__":
    main()