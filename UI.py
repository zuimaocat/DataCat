import tkinter as tk  
from tkinter import PhotoImage

def start_gui():
    from main import start_spider
    def multi_spider_url():
        urls_text = text.get("1.0","end-1c")
        urls = urls_text.split('\n')

        for url in urls:
            print(url)
            start_spider(url)
    root = tk.Tk()
    root.title("独角兽团队参赛作品|货流数据挖掘工具V2.1.0")
    root.iconbitmap("logo.ico")
    root.geometry('440x330')
    logo = PhotoImage(file="logo.png")
    logo_label = tk.Label(root, image=logo)
    logo_label.place(x=1,y=1)
    text = tk.Text(root, width= 30, height= 7)
    
            

    # label1 = tk.Label(root,text='独角兽团队|货流数据挖掘工具V1.2.0')
    label2 = tk.Label(root,text='请输入需要获取数据的链接（可输入多个链接）')
    label_split = tk.Label(root,text='————————————————————————————')
    # label_split.place(x=30,y=180)

    button2 = tk.Button(root,text = '开始',command=multi_spider_url())
    label3 = tk.Label(root,text='请输入起点和终点  (终点留空可搜索全部)')
    text3 = tk.Text(root, width= 5, height= 1)
    label5 = tk.Label(root,text='省')
    text4 = tk.Text(root, width= 5, height= 1)
    label6 = tk.Label(root,text='市')
    label_TO = tk.Label(root,text='到')

    text_end_sheng = tk.Text(root, width= 5, height= 1)
    label_end_sheng = tk.Label(root,text='省')
    text_end_shi= tk.Text(root, width= 5, height= 1)
    label_end_shi = tk.Label(root,text='市')

    text_end_sheng.place(x=210, y=250)
    label_end_sheng.place(x=250, y=250)
    text_end_shi.place(x=280, y=250)
    label_end_shi.place(x=320, y=250)
    button_text = tk.Button(root,text = '开始')

    button_text.place(x=350,y=250)
    # label1.pack()
    label2.pack()
    text.pack()
    button2.pack()

    label3.place(x=10,y=220)
    text3.place(x=15, y=250)
    # label4.place(x=120, y=220)
    text4.place(x=80, y=250)
    label5.place(x=50, y=250)
    label6.place(x=120, y=250)
    label_TO.place(x=160,y=250)



    #没做完
    
    root.mainloop()