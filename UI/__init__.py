import tkintertools as tkt

root = tkt.Tk(title="登录")
root.center()

cv = tkt.Canvas(root, zoom_item=True, keep_ratio="min", free_anchor=True)
cv.place(width=1280, height=720, x=640, y=360, anchor="center")

tkt.Text(cv, (640, 200), text="账 号 登 录", fontsize=48, anchor="center")

tkt.Text(cv, (450, 300), text="账号", anchor="nw")
tkt.InputBox(cv, (450, 340), (380, 50), placeholder="点击输入账号")
tkt.Text(cv, (450, 400), text="密码", anchor="nw")
tkt.InputBox(cv, (450, 440), (380, 50), show="●", placeholder="点击输入密码")

tkt.Button(cv, (450, 540), (180, 50), text="注 册")
tkt.Button(cv, (650, 540), (180, 50), text="登 录")


root.mainloop()