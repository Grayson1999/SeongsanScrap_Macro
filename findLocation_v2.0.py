import pyautogui as pg
import mouse
import time

def findLocation():
    while(True):
        x,y = pg.position()
        if mouse.is_pressed('left'):
            print("{}, {}".format(x,y))
            time.sleep(1)
        if mouse.is_pressed('right'):
            break

'''********************시간 블록 인식*******************************'''
def timeblock():
    pg.alert(text='시간 인식 데이터 좌표 인식', title='준비', button='OK')
    x1,y1 = pg.position()
    tempy1 = y1

    #시간 좌표 ->노트북 기준 (x= +300, y= +22)
    xp = 300
    yp = 22
    for i in range(5,17):
        pg.screenshot('./img/'+str(i)+'.png', region=(x1, y1, xp, yp))
        y1+= yp
    return totalCoordinate(x1,tempy1,xp,yp)


'''********************조회 블록 인식********************************'''
def lookupblock():
    pg.alert(text='조회 인식 데이터 x1, y1좌표 인식', title='준비', button='OK')
    x1,y1 = pg.position()

    #조회 좌표 ->노트북 기준(x= +60 y= +15)
    xp = 60
    yp = 15

    pg.screenshot('./img/inquiry.png', region=(x1, y1, xp, yp))

'''********************인식해야 할 좌표*******************************'''
def totalCoordinate(x,y,xp,yp):
    #5시~16시까지의 화면만 인식
    total = [x-4,y-4,xp+4,yp*12+4]
    print(total)


'''*********************main******************'''
inputData = int(input("[1] 좌표 찾기 [2] 시간 블록 캡쳐 & 인식해야 할 좌표 출력 [3] 조회 블록 캡쳐: \n"))
if inputData == 1:
    findLocation()
elif inputData == 2:
    timeblock()
elif inputData == 3:
    lookupblock()
else:
    print("잘못 입력되었습니다.")
    
