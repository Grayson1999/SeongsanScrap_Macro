import urllib.request
import urllib.error
import time
import pyautogui as pg

def move_mouse(x,y):
    a=pg.moveTo(x,y,0.15)
    pg.click(a)

def checkNone(msgReturnValue):
    if msgReturnValue == None:
        pg.alert(text='오류', title='창을 종료합니다.', button='종료')
        exit()
    return msgReturnValue
def coordinateCalculation(x1,x2):
    x2 = x2 -x1
    return x2

def changeInt(list):
    for i in range(len(list)):
        list[i]=int(list[i])
    return list


inputdata = pg.prompt(text="시간 좌표 입력",title="시간 인식 데이터",default="x1 y1 x2 y2")
inquiryInput =pg.prompt(text="조회 좌표 입력",title="조회 인식 데이터",default="x1 y1 x2 y2")

inquirySplit = inquiryInput.split(" ")
inquirySplit = changeInt(inquirySplit)
#x2-x1 and y2-y1
inquirySplit[2] = coordinateCalculation(inquirySplit[0],inquirySplit[2])
inquirySplit[3] = coordinateCalculation(inquirySplit[1],inquirySplit[3])

inputSplit = inputdata.split(" ")
inputSplit = changeInt(inputSplit)
inputSplit[2] = coordinateCalculation(inputSplit[0],inputSplit[2])
inputSplit[3] = coordinateCalculation(inputSplit[1],inputSplit[3])
for i in range(len(inputSplit)):
    inputSplit[i] = float(inputSplit[i])


for i in range(5,21):
    pg.screenshot('./img/'+str(i)+'.png', region=(inputSplit[0], inputSplit[1], inputSplit[2], inputSplit[3]))
    inputSplit[1]+=inputSplit[3]

pg.screenshot('./img/inquiry.png', region=(inquirySplit[0], inquirySplit[1], inquirySplit[2], inquirySplit[3]))

# while True:
#     try:
#         x,y = pg.locateCenterOnScreen('./img/20.png')#이미지 위치
#         break
#     except:
#         recognition=pg.confirm('인식할 수 없습니다.','인식 오류', buttons=['다시 인식'])
#         checkNone(recognition)
# move_mouse(x,y)

# errorInput =pg.prompt(text="오류 좌표 입력",title="오류 인식 데이터",default="x1 y1 x2 y2)")
# errorSplit = errorInput.split(" ")
# errorSplit[2] = coordinateCalculation(errorSplit[0],errorSplit[2])
# errorSplit[3] = coordinateCalculation(errorSplit[1],errorSplit[3])
# pg.screenshot('./img/error.png', region=(errorSplit[0], errorSplit[1], errorSplit[2], errorSplit[3]))

# confirmInput = pg.prompt(text="확인 좌표 입력",title="확인 인식 데이터",default="x1 y1 x2 y2)")
# confirmSplit = confirmInput.split(" ")
# confirmSplit[2] = coordinateCalculation(confirmSplit[0],confirmSplit[2])
# confirmSplit[3] = coordinateCalculation(confirmSplit[1],confirmSplit[3])
# pg.screenshot('./img/confirm.png', region=(confirmSplit[0], confirmSplit[1], confirmSplit[2], confirmSplit[3]))




