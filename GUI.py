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
    # 플레이어 이름
    canvas.create_line(Player_Name_LineX, 0, Player_Name_LineX, 500, fill="black")

    # 주간미션
    canvas.create_line(Week_Score_LineX, 0, Week_Score_LineX, 500, fill="black")
    canvas.create_line(Week_Score_LineX2, 0, Week_Score_LineX2, 500, fill="black")


canvas.pack(padx=10,pady=5)
canvas.create_rectangle(0, 0, 500, 450, fill="red")

Lines()

window.attributes("-transparentcolor", "#FF0000")




window.mainloop()