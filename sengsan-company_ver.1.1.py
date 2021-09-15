import urllib.request
import urllib.error
import time
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys



def move_mouse(c,d):
    a=pg.moveTo(c,d,0.15)
    pg.click(a)





myTime = pg.prompt(text="시간 입력",title="시간 입력 창",default="13:00")
myTimeList = myTime.split(":")
#myTimeList 변수 int로 변환
for i in range(len(myTimeList)):
    myTimeList[i]=int(myTimeList[i])


# # 드라이버 설정
# caps = webdriver.DesiredCapabilities.INTERNETEXPLORER
# caps [ 'ignoreProtectedModeSettings'] = True
# caps [ 'nativeEvents'] = True
# caps [ 'ignoreZoomSetting'] = True
# caps [ 'InternetExplorerDriver.INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
# caps [ 'requireWindowsFocus'] = True
# driver = webdriver.Ie (capabilities = caps)
# # 드라이버를 사용하여 웹 사이트
# driver.get("http://hpro.hyundai-steel.com/login_scr.jsp")


#예약 시간 선택창
reservationTime = pg.confirm('조회를 누른 뒤 시간 좌표 인식', buttons=['07:00~59', '08:00~59', '09:00~59', '10:00~59', '11:00~59', '12:00~59','13:00~59', '14:00~59', '15:00~59','16:00~59', '17:00~59', '18:00~59','19:00~59', '20:00~59'])
pg.alert(text='안정적인 인식을 위해 확인 버튼을 누른 뒤 창의 위치를 변경하지 마세요', title='준비', button='OK')
#처음 조회 누르기
while True:
    try:
        inqX,inqY= pg.locateCenterOnScreen('./img/inquiry.png')
        move_mouse(inqX,inqY)
        break
    except:
        pg.alert(text='인식할 수 없습니다.', title='인식 오류', button='다시 인식')

#좌표 인식 변수
global x
global y
global locationImg
for i in range(7,21):
    if i <10:
        i="0"+str(i)
    if reservationTime==str(i)+":00~59"  :
        while True:
            try:
                x,y = pg.locateCenterOnScreen('./img/'+str(i)+'.png')#이미지 위치
                locationImg='./img/'+str(i)+'.png'
                print("여기")
                inqX,inqY= pg.locateCenterOnScreen('./img/inquiry.png')
                break
            except:
                pg.alert(text='인식할 수 없습니다.', title='인식 오류', button='다시 인식')
#취소시 다시 하기 버튼 예약어로 만들기



while True:
    #서버 시간 받아오기
    date = urllib.request.urlopen("https://hpro.hyundai-steel.com/spmainpage.do").headers['Date']
    dateList = date.split(" ")
    dateListTime = dateList[4].split(":")#['00','00','00']
    #dateListTime의 시간데이터 int로 변환
    for i in range(len(dateListTime)):
        dateListTime[i]=int(dateListTime[i])
    #GMT+9
    dateListTime[0] +=9
    if dateListTime[0]>=24:
        dateListTime[0]-=9

    print(dateListTime)
    print(myTimeList)
    print("-----------")

    if dateListTime[0] == myTimeList[0] and dateListTime[1] == myTimeList[1]:
        #조회 버튼 인식
        move_mouse(inqX,inqY)
        while True:
            if pg.locateOnScreen(locationImg) != None:
                break
        move_mouse(x,y)
        # pg.press('enter')
        time.sleep(5)
        pg.alert(text='동작 수행 완료', title='완료 메세지', button='OK')
        break
