import asyncio
import discord
from selenium import webdriver
from Champion import *

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36')
driver = webdriver.Chrome('./chromedriver', chrome_options=options)

client = discord.Client()

# 생성된 토큰을 입력해준다.
token = "NjA4ODg4MzkxMTAyMzY1Njk4.XV4q2w.Bbpr8cojfEk2VJHeG_dPWCvN4t4"

def Champ(name):
    if name in champName.name:
        name = champName.name[name]

        url = 'https://www.op.gg/champion/{name}/statistics/'.format(name=name)
        driver.get(url)
        driver.implicitly_wait(2)

        href = driver.find_element_by_css_selector('body > div.l-wrap.l-wrap--champion > div.l-container > div > div.l-champion-statistics-header > div > ul > li.champion-stats-header__position.champion-stats-header__position--active > a > span.champion-stats-header__position__role')
        championName = href.text

    else:
        championName = "다시 입력해주세요."

    return championName

# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.author.bot:
        return None

    if message.content.startswith(';;안녕'):
        channel = message.channel
        await channel.send('반가워!')

    if message.content.startswith(';;champ'):
        channel = message.channel
        msg = message.content.split(" ")
        name = msg[1]
        search = Champ(name)
        await channel.send(search)

client.run(token)