import requests
import re

# Dito kumukuha ng fresh servers (Example source)
url = "https://raw.githubusercontent.com/freefq/free/master/v2ray"

def update_portal():
    try:
        r = requests.get(url)
        # Kukuha ng unang gumaganang config
        server = r.text.splitlines()[0]
        
        with open("index.html", "r") as f:
            content = f.read()
        
        # Papalitan ang text sa HTML
        new_content = re.sub(r'id="payload">.*?</div>', f'id="payload">{server}</div>', content)
        
        with open("index.html", "w") as f:
            f.write(new_content)
        print("Success: Server Updated!")
    except:
        print("Error: Failed to fetch server.")

if __name__ == "__main__":
    update_portal()
  
