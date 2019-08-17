from selenium import webdriver
import time

# 웹 구동
url = 'http://gameinfo.leagueoflegends.co.kr/ko/game-info/champions/'
driver = webdriver.Chrome("./chromedriver.exe")
driver.get(url)
time.sleep(2)

# 챔피언의 이름을 가져올 a 태그
championName = driver.find_elements_by_css_selector('#champion-grid-content > div > ul > li > div > h3 > a')

# Dictionary 구조로 변수 새애성
championNameDic = {}

# 챔피언 개수 변수
i = 0

# 챔피언의 이름과 영어이름을 구한다.
for href in championName:
    name= href .get_attribute("href")
    # href의 영어 이름을 가져오기위한 작업
    nameRe = name.replace('http://gameinfo.leagueoflegends.co.kr/ko/game-info/champions/','')
    engName = nameRe[:nameRe.find('/')]
    # 한글 이름
    korName = href.text

    # Dictionary 에 추가해준다.
    # 추후 검색을 위해 Key를 한글이름으로 설정
    championNameDic[korName] = engName
    i = i + 1

print(championNameDic)
print(i)
