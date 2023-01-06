import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    TG_BOT_TOKEN = "5668333055:AAHSJSStdwcnvrhhqdZaObVEg_G0Nt0kD4M"
    APP_ID = 2121142
    API_HASH = "73aea46b39f24bd55f967990926c32e9"
    TG_USER_SESSION = "BQAgXbYAGef9hSbKjfcCYcp_eQVcqjBVP1Bcz-HeQFpOu32QwVWjBJohlQwgoaEHM4g52glA09L9gwn3bka3JOqjY1SooiO9jPrCc-IarqXZO7D7x0dfCCpCmeson3ahFIrGz0UYiV9r0mQxbd-Ut4QIY15NY3XELIWHDBlkbB54cJop69Pjc7naLDkH1VCJ1N-GrClaPAnwfJBze0p8XbaH8byfI--8F-jvgGcuyrpK7YqFxtdCDbghURSlRa6mgtj1W6EVnKSefqdSxiE7GPkgnzxPVFVH4u0hvqwoIiGU6gz2qONJLJ21cMhMbvMA_SR0lIlL_srYoDV6TBJr0U3BTlB_7wAAAAA8vrrvAA"
    DB_URI = "postgres://postgres:hnrLHo36uM5yt4l@clone.internal:5432"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
