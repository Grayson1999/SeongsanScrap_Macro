import urllib.request
import urllib.error
import time
import pyautogui as pg


#마우스 움직임 후 클릭
def move_mouse(x,y):
    a=pg.moveTo(x,y,0.15)
    pg.click(a)

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

#분 입력
while True:
    try:
        myTime = pg.prompt(text="시간 입력",title="시간 입력 창",default="00")
        break
    except(TypeError):
        pg.alert(text='다시 실행 필요', title='입력 받은 값이 없습니다.', button='종료')
        exit()

#입력한 분 int형 변환
myTime = int(myTime)


#버튼 리스트 생성
buttonList = []
for i in range(6,17):
    buttonList.append(str(i))
    

#예약 시간 선택창
reservationTime = pg.confirm('조회를 누른 뒤 시간 좌표 인식', buttons=buttonList)
checkNone(reservationTime)
pg.alert(text='안정적인 인식을 위해 확인 버튼을 누른 뒤 창의 위치를 변경하지 마세요', title='준비', button='OK')

#이미지를 인식할 창의 좌표 입력
browserLocation = pg.prompt(text="창 좌표 입력",title="좌표 입력 창",default="x,y,w,h")
blList = browserLocation.split(",")
blList = changeInt(blList)

#처음 조회 누르기
while True:
    try:
        inqX,inqY= pg.locateCenterOnScreen('./img/inquiry.png')
        move_mouse(inqX,inqY)
        break
    except:
        recognition=pg.confirm('인식할 수 없습니다.','인식 오류', buttons=['다시 인식'])
        checkNone(recognition)


#좌표 인식 변수
# for i in range(7,21):
#     if reservationTime==str(i)+":00~59"  :
#         try:
#             timeX,timeY = pg.locateCenterOnScreen('./img/'+str(i)+'.png', region=(blList[0],blList[1],blList[2],blList[3]))#이미지 위치
#             break
#         except:
#             recognition=pg.confirm('인식할 수 없습니다.','인식 오류', buttons=['다시 인식'])
#             checkNone(recognition)      
while True:
    try:
        timeX,timeY = pg.locateCenterOnScreen('./img/'+reservationTime+'.png')
        break 
    except:
        recognition=pg.confirm('인식할 수 없습니다.','인식 오류', buttons=['다시 인식'])
        checkNone(recognition)
#취소시 다시 하기 버튼 예약어로 만들기
check = False
print("running..."+str(timeX) + str(timeY))
while True:
    #서버 시간 받아오기
    date = urllib.request.urlopen("http://hpro.hyundai-steel.com/indexWebkit.jsp?rpage=/spIndex.do").headers['Date']
    dateList = date.split(" ")
    dateListTime = dateList[4].split(":")#['00','00','00']
    dateTime = int(dateListTime[1])
    time.sleep(5)
    if dateTime == myTime :
        print("-------Start--------")
        while True: 
            move_mouse(inqX,inqY)
            while True:
                if pg.locateOnScreen('./img/16.png', region=(blList[0],blList[1],blList[2],blList[3])) != None or pg.locateOnScreen('./img/9.png',region=(blList[0],blList[1],blList[2],blList[3])) != None:
                    break
            for i in range(6,17):
                if pg.locateOnScreen("./img/"+ str(i) +".png",region=(blList[0],blList[1],blList[2],blList[3])) == None:
                    check = True
                    break
            if check == True:
                break
        move_mouse(timeX,timeY)
        pg.press('enter')
        time.sleep(6)
        pg.alert(text='동작 수행 완료', title='완료 메세지', button='OK')
        break

       
        
