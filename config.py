import os

API_ID = int(os.getenv("API_ID", "17896688"))
API_HASH = os.getenv("API_HASH", "947327cf5ff0053a66bf7951f9db5658")
SESSION_STRING = os.getenv("BQAP-GEAJeLaW5zShFphAkcsPn1yau3TXAXGhGCqp2zzm_lu2Pi-GmfiGN7G-7YM3KSRLFoS-YHNEGX9F13-rJm9zJr9LUuoICsbzxe7bUvfsXxSnoUaF5bIxHP3SilzWBJ3-vLgW0AANsUNGSgJbR6vyG1iyT5_Racc3CosPz8SznpLTaKq6x6w4s08-xO03btFljAhnDxjPSiXfgaodwNLzOfu42I2AiiFdwU_GwnOCmaitlrM6fqoxYL--8-2ppmmOzWU2IF1ZAgAAjLOwepxwFVCZTkW3lkbR24D8Aj3rdT0w26ch7WZ86Dr7UDPFV3khlm6337h_m99uKbHUttX-2CHIwAAAAByE1_bAA"
)
TIME_ZONE = os.getenv("Asia/Jakarta")
BOT_LIST = [i.strip() for i in os.getenv("ArabUltraUbot ArabV2Ubot supernovaxubot DayforuMusic_bot ArabxRobot AfterGankUbot SASProtectV1_Bot SonixUbot OnedayXUbot RoyalUbot MydamnUbot fsubprem_1bot DomiUbot").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.getenv("-1001837260549"))
MESSAGE_ID = int(os.getenv("43"))
BOT_ADMIN_IDS = [int(i.strip()) for i in os.getenv.get("BOT_ADMIN_IDS").split(' ')]
