#!/usr/bin/python3
try:
    from requests.exceptions import RequestException
    from rich.console import Console
    import requests, time, os, json
    from rich.panel import Panel
    from rich import print
except (Exception) as e:
    exit(f"[Error]{str(e).capitalize()}!")

COOKIES, SUKSES, GAGAL, XRP = {
    "KEY": None
}, [], [], {
    "KEY": 0.000000
}

def BANNER():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Panel("""[bold red]●[bold yellow] ●[bold green] ●[/]
[bold red]    ______                      __                 
   / ____/___ ___  __________  / /____  ____ ______
  / /_  / __ `/ / / / ___/ _ \/ __/ _ \/ __ `/ ___/
 / __/ / /_/ / /_/ / /__/  __/ /_/  __/ /_/ / /    
[bold white]/_/    \__,_/\__,_/\___/\___/\__/\___/\__,_/_/     
        [italic white on red]Free XRP Tokens - Coded by Rozhak""", style="bold bright_black", width=56))

class CLAIM:

    def __init__(self) -> None:
        pass

    def EXECUTION(self):
        with requests.Session() as r:
            r.headers.update({
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Encoding': 'gzip, deflate',
                'Cache-Control': 'max-age=0',
                'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-Mode': 'navigate',
                'dnt': '1',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 14; RMX3706 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.144 Mobile Safari/537.36',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-User': '?1',
                'Referer': 'https://faucetearner.org/dashboard.php',
                'Host': 'faucetearner.org',
            })
            response = r.get('https://faucetearner.org/faucet.php', cookies = {
                'Cookie': COOKIES['KEY']
            })
            r.headers.update({
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Content-Type': 'application/json',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Host': 'faucetearner.org',
                'Origin': 'https://faucetearner.org',
            })
            response2 = r.post('https://faucetearner.org/api.php?act=faucet', data = {}, cookies = {
                'Cookie': COOKIES['KEY']
            })
            if 'congratulations' in str(response2.text).lower():
                try: # Congratulations on receiving 0.000000 It has been deposited into your account balance and can be viewed on the dashboard!
                    self.XRP_earn = (str(response2.text).split(' XRP')[0].split('0.')[1])
                except (IndexError):
                    self.XRP_earn = ("0.000000")
                XRP.update({
                    "KEY": f"0.{self.XRP_earn}"
                })
                print(Panel(f"[italic green]Congratulations on receiving {XRP['KEY']} XRP, It has been deposited into your account balance and can be viewed on the dashboard!!", style="bold bright_black", width=56, title=">>> Sukses <<<"))
                for sleep in range(60, 0, -1):
                    print(f"[bold bright_black]   ╰─>[bold green] {sleep}[bold white]/[bold green]{XRP['KEY']}[bold white] Sukses:-[bold green]{len(SUKSES)}[bold white] Gagal:-[bold red]{len(GAGAL)}     ", end='\r')
                    time.sleep(1.0)
                SUKSES.append(f'{response2.text}')
                return ("0_0")
            elif 'you have already' in str(response2.text).lower():
                print(Panel(f"[italic red]You have already claimed, please wait for the next wave!", style="bold bright_black", width=56, title=">>> Gagal <<<"))
                time.sleep(30)
                GAGAL.append(f'{response2.text}')
                return ("0_-") # You have already claimed, please wait for the next wave!
            else:
                print(Panel(f"[italic red]{str(response2.text).capitalize()}!", style="bold bright_black", width=56, title=">>> Error <<<"))
                return ("-_-")

    def CHECK_LOGIN(self):
        BANNER()
        if COOKIES["KEY"] == None:
            print(Panel(f"[italic white]Masukkan cookies akun faucetearner anda dan pastikan akun faucetearner anda sudah dalam keadaan login!", style="bold bright_black", width=56, title=">>> Cookies Faucetearner <<<", subtitle="╭──────", subtitle_align="left"))
            self.cookies = Console().input("[bold bright_black]   ╰─> ")
            if len(self.cookies) != 0:
                COOKIES.update({
                    "KEY": f"{self.cookies}"
                })
                return ("0_0")
            else:
                print(Panel(f"[italic red]Pengisian cookies harus dilakukan dengan benar dan valid. Data yang kosong atau tidak sesuai dapat menyebabkan proses selanjutnya terhambat!", style="bold bright_black", width=56, title=">>> Tidak Boleh Kosong <<<"))
                exit()
        else:
            return ("0_0")

    def XRP(self):
        try:
            self.CHECK_LOGIN()
            print(Panel(f"[italic white]Penambangan token XRP sedang dilakukan. Anda dapat menghentikan prosesnya kapan saja dengan menekan tombol CTRL + Z.", style="bold bright_black", width=56, title=">>> Catatan <<<"))
            while True:
                try:
                    self.EXECUTION()
                except (RequestException):
                    print("[bold bright_black]   ╰─>[bold red] KONEKSI BERMASALAH!", end='\r')
                    time.sleep(10.5)
                    continue
                except (KeyboardInterrupt):
                    print("                                                       ", end='\r')
                    time.sleep(2.5)
                    continue
        except (Exception) as e:
            print(Panel(f"[italic red]{str(e).capitalize()}!", style="bold bright_black", width=56, title=">>> Error <<<"))
            exit()

if __name__ == '__main__':
    try:
        if os.path.exists("Data/Subscribe.json") == False:
            youtube_url = json.loads(requests.get('https://raw.githubusercontent.com/RozhakXD/Faucetearner/main/Data/Youtube.json').text)['Link']
            os.system(f'xdg-open {youtube_url}')
            with open('Data/Subscribe.json', 'w') as w:
                w.write(json.dumps({
                    "Status": True
                }))
            w.close()
            time.sleep(3.5)
        os.system('git pull')
        CLAIM().XRP()
    except (KeyboardInterrupt, KeyboardInterrupt):
        exit()