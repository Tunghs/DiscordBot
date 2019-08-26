import asyncio
import discord
from selenium import webdriver
from Champion import *
from discord.ext import commands

# 창 없이 selenium 구동
options = webdriver.ChromeOptions()
options.add_argument('headless')
# 유저 정보 추가
options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36')
driver = webdriver.Chrome('./chromedriver', chrome_options=options)

client = discord.Client()

# 생성된 토큰을 입력해준다.
token = "NjA4ODg4MzkxMTAyMzY1Njk4.XV6VVg.8IbQ2DzSsi2hERyQOgnXvsiUeM4"

url = ''

# 챔피언 포지션 확인
async def ChampPositionCheck(name):
    if name in champName.name:
        name = champName.name[name]

        url = 'https://www.op.gg/champion/{name}/statistics/'.format(name=name)
        driver.get(url)
        driver.implicitly_wait(2)

        positionHref = driver.find_elements_by_css_selector('ul.champion-stats-position > li > a')

        positionList = []

        # 챔피언의 포지션 확인
        for href in positionHref:
            href = href.get_attribute("href")
            splitList = href.split('/')
            position = splitList[-1]
            positionList.append(position)

        championName = positionList

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
        name = message.content.replace(";;champ ","")
        search = ChampPositionCheck(name)
        await channel.send(search)

        if message.content.startswith(';;'):
            channel = message.channel
            position = message.content.replace(";;t")
            await channel.send("탑입니다.")

client.run(token)