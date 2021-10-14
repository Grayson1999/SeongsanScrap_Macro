import pyautogui as pg

def move_mouse(x,y):
    a=pg.moveTo(x,y,0.15)
    pg.click(a)

def coordinateCalculation(x1,x2):
    temp = x2 -x1
    return temp


#시간 정보 칸 인식 좌표 저장
pg.alert(text='시간(1칸) 인식 데이터 x1, y1좌표 인식', title='준비', button='OK')
x1,y1 = pg.position()
pg.alert(text='시간(1칸) 인식 데이터 x2, y2좌표 인식', title='준비', button='OK')
x2,y2 = pg.position()

#x2-x1 and y2-y1
x2 = coordinateCalculation(x1,x2)
y2 = coordinateCalculation(y1,y2)

#좌표를 활용해 시간 이미지 캡쳐
for i in range(5,21):
    pg.screenshot('./img/'+str(i)+'.png', region=(x1, y1, x2, y2))
    y1+=y2


#조회 버튼 인식 좌표 저장
pg.alert(text='조회 인식 데이터 x1, y1좌표 인식', title='준비', button='OK')
x1,y1 = pg.position()
pg.alert(text='조회 인식 데이터 x2, y2좌표 인식', title='준비', button='OK')
x2,y2 = pg.position()

#x2-x1 and y2-y1
x2 = coordinateCalculation(x1,x2)
y2 = coordinateCalculation(y1,y2)

pg.screenshot('./img/inquiry.png', region=(x1, y1, x2, y2))

#창 좌표 프린트
pg.alert(text='인식이 필요한 창 x1, y1좌표 인식', title='준비', button='OK')
x1,y1 = pg.position()
pg.alert(text='인식이 필요한 창 x2, y2좌표 인식', title='준비', button='OK')
x2,y2 = pg.position()
#x2-x1 and y2-y1
x2 = coordinateCalculation(x1,x2)
y2 = coordinateCalculation(y1,y2)

print("창 좌표(x,y,w,h): {},{},{},{}".format(x1,y1,x2,y2))







