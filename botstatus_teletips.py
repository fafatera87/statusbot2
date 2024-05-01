#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [BotStatus Telegram bot by TeLe TiPs] (https://github.com/teletips/Powerful_BotStatus-TeLeTiPs)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/Powerful_BotStatus-TeLeTiPs/blob/main/LICENSE

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    name = "botstatus_teletips",
    api_id = int(os.environ["29737623"]),
    api_hash = os.environ["71a4bb6501593f225cdab4d4b368a830"],
    session_string = os.environ["BQAP-GEAJeLaW5zShFphAkcsPn1yau3TXAXGhGCqp2zzm_lu2Pi-GmfiGN7G-7YM3KSRLFoS-YHNEGX9F13-rJm9zJr9LUuoICsbzxe7bUvfsXxSnoUaF5bIxHP3SilzWBJ3-vLgW0AANsUNGSgJbR6vyG1iyT5_Racc3CosPz8SznpLTaKq6x6w4s08-xO03btFljAhnDxjPSiXfgaodwNLzOfu42I2AiiFdwU_GwnOCmaitlrM6fqoxYL--8-2ppmmOzWU2IF1ZAgAAjLOwepxwFVCZTkW3lkbR24D8Aj3rdT0w26ch7WZ86Dr7UDPFV3khlm6337h_m99uKbHUttX-2CHIwAAAAByE1_bAA"]
)
TIME_ZONE = os.environ["Asia/Jakarta"]
BOT_LIST = [i.strip() for i in os.environ.get("ArabUltraUbot ArabV2Ubot supernovaxubot DayforuMusic_bot ArabxRobot AfterGankUbot SASProtectV1_Bot SonixUbot OnedayXUbot RoyalUbot MydamnUbot fsubprem_1bot DomiUbot").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["-1001837260549"])
MESSAGE_ID = int(os.environ["43"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

async def main_teletips():
    async with app:
            while True:
                print("Checking...")
                xxx_teletips = f"📈 | **Real-Time Bot Status**"
                for bot in BOT_LIST:
                    try:
                        yyy_teletips = await app.send_message(bot, "/start")
                        aaa = yyy_teletips.id
                        await asyncio.sleep(10)
                        zzz_teletips = app.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_teletips:
                            bbb = ccc.id
                        if aaa == bbb:
                            xxx_teletips += f"\n\n🤖  @{bot}\n        └ **Down** ❌"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"🚨 **Beep! Beep!! @{bot} is down** ❌")
                                except Exception:
                                    pass
                            await app.read_chat_history(bot)
                        else:
                            xxx_teletips += f"\n\n🤖  @{bot}\n        └ **Alive** ✅"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_teletips += f"\n\n✔️ Last checked on: {last_update} ({TIME_ZONE})\n\n<i>♻️ Refreshes automatically</i>"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_teletips)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(6300)
                        
app.run(main_teletips())

#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
