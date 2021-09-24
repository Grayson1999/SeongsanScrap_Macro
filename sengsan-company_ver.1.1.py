import urllib.request
import urllib.error
import time
import pyautogui as pg



#마우스 움직임 후 클릭
def move_mouse(x,y):
    a=pg.moveTo(x,y,0.15)
    pg.click(a)

#"변수"가 포함되어 있는 지 확인
def inputNCheckString(delimiter):
    while True:
        try:
            myTime = pg.prompt(text="시간 입력",title="시간 입력 창",default="13:00")
            j=0
            for i in myTime:
                if i == delimiter:
                    j+=1
            if j == 1:
                break
            else:
                pg.alert(text=':(콜론) 비 포함 오류', title='":"(콜론)을 포함해 입력하세요', button='다시 입력 ')
        except(TypeError):
            pg.alert(text='다시 실행 필요', title='입력 받은 값이 없습니다.', button='종료')
            exit()
    return myTime

#myTimeList 변수 int로 변환
def changeInt(list):
    for i in range(len(list)):
        list[i]=int(list[i])
    return list

def checkNone(msgReturnValue):
    if msgReturnValue == None:
        pg.alert(text='오류', title='창을 종료합니다.', button='종료')
        exit()
    return msgReturnValue


myTimeList = inputNCheckString(':').split(":")
myTimeList = changeInt(myTimeList)


#버튼 리스트
buttonList = []
for i in range(7,21):
    if i <10:
        i="0"+str(i)
    buttonList.append(str(i)+":00~59")
    

#예약 시간 선택창
reservationTime = pg.confirm('조회를 누른 뒤 시간 좌표 인식', buttons=buttonList)
checkNone(reservationTime)
pg.alert(text='안정적인 인식을 위해 확인 버튼을 누른 뒤 창의 위치를 변경하지 마세요', title='준비', button='OK')

#처음 조회 누르기
while True:
    try:
        inqX,inqY= pg.locateCenterOnScreen('./img/inquiry.png')
        move_mouse(inqX,inqY)
        break
    except:
        recognition=pg.confirm('인식할 수 없습니다.','인식 오류', buttons=['다시 인식'])
        checkNone(recognition)

timeX = 0
timeY = 0
#좌표 인식 변수
for i in range(7,21):
    if reservationTime==str(i)+":00~59"  :
        while True:
            try:
                timeX,timeY = pg.locateCenterOnScreen('./img/'+str(i)+'.png')#이미지 위치
                break
            except:
                recognition=pg.confirm('인식할 수 없습니다.','인식 오류', buttons=['다시 인식'])
                checkNone(recognition)           

#취소시 다시 하기 버튼 예약어로 만들기


myTimeList[1]-=1
if myTimeList[1]<0:
    myTimeList[0]-=1
    myTimeList[1]+=60
    
while True:
    #서버 시간 받아오기
    date = urllib.request.urlopen("https://hpro.hyundai-steel.com/spmainpage.do").headers['Date']
    dateList = date.split(" ")
    dateListTime = dateList[4].split(":")#['00','00','00']
    dateListTime = changeInt(dateListTime)

    #GMT+9
    dateListTime[0] +=9
    if dateListTime[0]>=24:
        dateListTime[0]-=9

    
    print("running...\n")

    if dateListTime[0] >= myTimeList[0] and dateListTime[1] >= myTimeList[1]:
        while True: 
            move_mouse(inqX,inqY)
            while True:
                if pg.locateOnScreen('./img/19.png') != None:
                    break
            if pg.locateOnScreen("./img/13.png") == None:
                break
        move_mouse(timeX,timeY)
        pg.press('enter')
        time.sleep(5)
        pg.alert(text='동작 수행 완료', title='완료 메세지', button='OK')
        break

       
        
