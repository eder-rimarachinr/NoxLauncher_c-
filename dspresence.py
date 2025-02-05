import time
import psutil
import pypresence

from fs import get_discordrpc
from threadpool import NOXLAUNCHER_THREADPOOL
from constants import DISCORD_CLIENT_ID

RPC: pypresence.Presence = pypresence.Presence(DISCORD_CLIENT_ID)

rpc_connected, discord_opened = False, False

def _start() -> None:

    global discord_opened

    try:

        RPC.connect()
        rpc_connected = True

    except: rpc_connected = False

    if rpc_connected: 
        while True: 

            try: 
        
                RPC.update(
                    state= "Playing NoxLauncher...",
                    details= "Powerful and easy to use Minecraft Launcher.",
                    large_image= "discord_rpc",
                    large_text= "Krayson Studio"
                )

                time.sleep(10)
            
            except:

                RPC.clear()
                RPC.close()
                discord_opened = False
                rpc_connected = False
                
                return

def DiscordRPC() -> None:

    def _init() -> None: 

        global discord_opened

        while get_discordrpc():

            if not discord_opened:

                for program in psutil.process_iter():

                    if program.name().find("Discord") != -1:

                        NOXLAUNCHER_THREADPOOL.submit(_start)
                        discord_opened = True
                        break

                else: discord_opened = False

    NOXLAUNCHER_THREADPOOL.submit(_init)