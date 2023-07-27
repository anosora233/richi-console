from os import system, mkdir
from os.path import exists
from _thread import start_new_thread
from mitmproxy.tools.main import mitmdump
from json import load, dump

if not exists("settings.json"):
    SETTINGS = {
        {
            "enable_helper": False,
            "enable_skins": False,
            "upstream_proxy": "",
            "api_url": "https://localhost:12121/",
        }
    }
    dump(SETTINGS, open("settings.json", "w"))

ARGS = ["-p", "23410", "-s", "src/addons.py"]
SETTINGS = load(open("settings.json", "r"))
UPSTREAM_PROXY = SETTINGS["upstream_proxy"]

if len(UPSTREAM_PROXY):
    ARGS.extend(["-m", f"upstream:{UPSTREAM_PROXY}"])

WindowsTitle = "Console · 🀄"

# REGISTRY = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
# KEY = winreg.OpenKey(
#     REGISTRY,
#     r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",
#     0,
#     winreg.KEY_ALL_ACCESS,
# )

# try:
#     PROXY, __ = winreg.QueryValueEx(KEY, "ProxyServer")
#     ENABLE, __ = winreg.QueryValueEx(KEY, "ProxyEnable")
# except Exception:
#     PROXY = ""
#     ENABLE = 0

# winreg.SetValueEx(KEY, "ProxyServer", 0, winreg.REG_SZ, "127.0.0.1:23410")
# winreg.SetValueEx(KEY, "ProxyEnable", 0, winreg.REG_DWORD, 1)


# def reset_proxy() -> None:
#     winreg.SetValueEx(KEY, "ProxyServer", 0, winreg.REG_SZ, PROXY)
#     winreg.SetValueEx(KEY, "ProxyEnable", 0, winreg.REG_DWORD, ENABLE)

#     print("=======================")
#     print("RESET SYSTEM PROXY DONE")
#     print("=======================")


# def run(id: str) -> None:
# # start_new_thread(run, (WindowsTitle,))


def main() -> None:
    if SETTINGS["enable_helper"]:
        system('start cmd /c "title Console · 🀄 && bin\\console.exe -majsoul"')

    mitmdump(args=ARGS)


if __name__ == "__main__":
    main()