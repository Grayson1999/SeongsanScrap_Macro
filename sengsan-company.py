import urllib.request
import urllib.error
import time
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys



def move_mouse(c,d):
    a=pg.moveTo(c,d,0.2)
    pg.click(a)

#클릭 위치
locationY=[]
x=320
y=469
for i in range(17):
    locationY.append(y)
    y+=21.9

#이미지 위치
locationImg="C:\\my python file\\virtual_environment\\SeongsanScrap\\img\\05.png"

myTime = pg.prompt(text="시간 입력",title="시간 입력 창",default="13:00")
myTimeList = myTime.split(":")


# 드라이버 설정
caps = webdriver.DesiredCapabilities.INTERNETEXPLORER
caps [ 'ignoreProtectedModeSettings'] = True
caps [ 'nativeEvents'] = True
caps [ 'ignoreZoomSetting'] = True
caps [ 'InternetExplorerDriver.INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
caps [ 'requireWindowsFocus'] = True
driver = webdriver.Ie (capabilities = caps)
# 드라이버를 사용하여 웹 사이트
driver.get("http://hpro.hyundai-steel.com/login_scr.jsp")
a = pg.alert(text='준비과정', title='준비', button='OK')
print(a)
pg.hotkey('winleft', 'left') 


#예약 시간 선택창
reservationTime = pg.confirm('Enter option', buttons=['07:00~59', '08:00~59', '09:00~59', '10:00~59', '11:00~59', '12:00~59','13:00~59', '14:00~59', '15:00~59','16:00~59', '17:00~59', '18:00~59','19:00~59', '20:00~59', '21:00~59'])

if reservationTime == '07:00~59':
    ry=locationY[2]
elif reservationTime == '08:00~59':
    ry=locationY[3]
elif reservationTime == '09:00~59':
    ry=locationY[4]
elif reservationTime == '10:00~59':
    ry=locationY[5]
elif reservationTime == '11:00~59':
    ry=locationY[6]
elif reservationTime == '12:00~59':
    ry=locationY[7]
elif reservationTime == '13:00~59':
    ry=locationY[8]
elif reservationTime == '14:00~59':
    ry=locationY[9]
elif reservationTime == '15:00~59':
    ry=locationY[10]
elif reservationTime == '16:00~59':
    ry=locationY[11]
elif reservationTime == '17:00~59':
    ry=locationY[12]
elif reservationTime == '18:00~59':
    ry=locationY[13]
elif reservationTime == '19:00~59':
    ry=locationY[14]
elif reservationTime == '20:00~59':
    ry=locationY[15]
elif reservationTime == '21:00~59':
    ry=locationY[16]
else:
    print(pg.alert(text='잘못 눌렀습니다.', title='error', button='OK'))
#취소시 다시 하기 버튼 예약어로 만들기



while True:
    #서버 시간 받아오기
    date = urllib.request.urlopen("https://hpro.hyundai-steel.com/spmainpage.do").headers['Date']
    dateList = date.split(" ")
    dateListTime = dateList[4].split(":")#['00','00','00']
    #dateListTime int로 변환
    for i in range(len(dateListTime)):
        dateListTime[i]=int(dateListTime[i])
    #GMT+9
    dateListTime[0] +=9
    if dateListTime[0]>=24:
        dateListTime[0]-=9
    #dateListTime str로 변환
    for i in range(len(dateListTime)):
        dateListTime[i]=str(dateListTime[i])
    #dateListTime중 분 파트 "00" 형식으로 변경
    if len(dateListTime[1])==1:
        dateListTime[1]="0"+dateListTime[1]
    #myTimeList중 분 파트 "00" 형식으로 변경
    if len(myTimeList[1])==1:
        myTimeList[1]="0"+myTimeList[1]
    
    print(dateListTime)
    print(myTimeList)
    print("-----------")

    if int(dateListTime[0]) == int(myTimeList[0]) and int(dateListTime[1]) == int(myTimeList[1]):
        move_mouse(674,357)
        while True:
            if pg.locateOnScreen(locationImg) != None:
                break
        move_mouse(x,ry)
        time.sleep(0.2)
        pg.press('enter')
        print('완료')
        break
