import pyautogui
import PIL
from tkinter import *
window= Tk()
window.title("캡처도구")
window.geometry("600x500")
window.resizable(0, 0)
ScreenShot_Count=0
canvas_line_Id=[]
canvas = Canvas(window,width=450,height=400,relief="solid", bd=1)
canvas.pack(padx=10,pady=5)
#캔버스 색상
canvas.create_rectangle(0, 0, 500, 450, fill="#590000")
#캔버스 색상을 지우기
window.attributes("-transparentcolor", "#590000")
#구분선
def Lines():
    Player_Name_LineX = 80
    Week_Score_LineX =270
    Week_Score_LineX2 = 300
    Sharenian_Score_LineX = 325
    Sharenian_Score_LineX2 = 375
    Flag_Score_LineX = 400

    # 플레이어 이름
    canvas_line_Id.append(canvas.create_line(Player_Name_LineX, 0, Player_Name_LineX, 500, fill="#8A7FFF"))
    # 주간미션
    canvas_line_Id.append(canvas.create_line(Week_Score_LineX, 0, Week_Score_LineX, 500, fill="#FFFF7F"))
    canvas_line_Id.append(canvas.create_line(Week_Score_LineX2, 0, Week_Score_LineX2, 500, fill="#FFFF7F"))

    #지하수로
    canvas_line_Id.append(canvas.create_line(Sharenian_Score_LineX, 0, Sharenian_Score_LineX, 500, fill="#FF7FBF"))
    canvas_line_Id.append(canvas.create_line(Sharenian_Score_LineX2, 0, Sharenian_Score_LineX2, 500, fill="#FF7FBF"))

    #플래그
    canvas_line_Id.append(canvas.create_line(Flag_Score_LineX, 0, Flag_Score_LineX, 500, fill="#9F7FFF"))
    print(1)

#스크린샷
def Line_Delete():
    global canvas_line_Id
    for i in range(6):
        canvas.after(1000, canvas.delete, canvas_line_Id[i])
    print(2)
def ScreenShot():
    #Line_Delete()

    global ScreenShot_Count
    ScreenShot_Count=ScreenShot_Count+1
    #canvas의 크기를 구한 값
    x,y=canvas.winfo_rootx(),canvas.winfo_rooty()
    w,h=canvas.winfo_width(),canvas.winfo_height()

    #스크린샷 이름,범위
    pyautogui.screenshot("스크린샷"+str(ScreenShot_Count)+".png",region=(x,y,w,h))

#버튼
photo = PhotoImage(file="Image/스크린샷.png")
screenshot_button=Button(window,image=photo,command=Line_Delete)
screenshot_button.pack()

line_add_button=Button(window,text="줄생성",command=Lines)
line_add_button.place(x=400,y=450)

line_delete_button=Button(window,text="줄삭제",command=Line_Delete)
line_delete_button.place(x=500,y=450)

window.mainloop()