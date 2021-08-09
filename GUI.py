from tkinter import *

window= Tk()
window.title("캡처도구")
window.geometry("600x500")
window.resizable(0, 0)

canvas = Canvas(window,width=450,height=400,relief="solid", bd=1)

def Lines():
    Player_Name_LineX = 80
    Week_Score_LineX =270
    Week_Score_LineX2 = 300
    Sharenian_Score_LineX = 325
    Sharenian_Score_LineX2 = 375
    Flag_Score_LineX = 400
    # 플레이어 이름
    canvas.create_line(Player_Name_LineX, 0, Player_Name_LineX, 500, fill="#8A7FFF")

    # 주간미션
    canvas.create_line(Week_Score_LineX, 0, Week_Score_LineX, 500, fill="#FFFF7F")
    canvas.create_line(Week_Score_LineX2, 0, Week_Score_LineX2, 500, fill="#FFFF7F")

    #지하수로
    canvas.create_line(Sharenian_Score_LineX, 0, Sharenian_Score_LineX, 500, fill="#FF7FBF")
    canvas.create_line(Sharenian_Score_LineX2, 0, Sharenian_Score_LineX2, 500, fill="#FF7FBF")

    #플래그
    canvas.create_line(Flag_Score_LineX, 0, Flag_Score_LineX, 500, fill="#9F7FFF")

canvas.pack(padx=10,pady=5)
canvas.create_rectangle(0, 0, 500, 450, fill="#590000")

Lines()

window.attributes("-transparentcolor", "#590000")




window.mainloop()