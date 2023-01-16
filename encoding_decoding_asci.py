#here we start ..
from cgitb import text
from textwrap import wrap
from tkinter import *
from tkinter import messagebox
import base64
import time

#def forpswd(): ..no use.........................
    #var3=var.get()
    #lavel_for_pswd_scr=Label(screen_real,text=var3).pack()

screen_real=Tk()
screen_real.geometry('1085x780+00+00')
screen_real.title('Encoding and Decoding creator')
icn_pic=PhotoImage(file='C:\\Users\\neha\\Links\\project2 encrypt decryt\\spnd.png')
screen_real.iconphoto(False,icn_pic)
screen_real.resizable(False,False)
virtualpswd_database=['Anurag@123','Akashsir@123','12345678','anu12104']


bg_img=PhotoImage(file='C:\\Users\\neha\\Links\\project2 encrypt decryt\\bgmp3.png')
logo_bg_img=Label(screen_real,image=bg_img,font='300')
logo_bg_img.place(x=0,y=0)

label_fr_pswd=Label(screen_real,text='hI-tEcH eNcrYpTiOn # DeCr..',font='italic 25 bold',bg='black',fg='red',bd=2)
label_fr_pswd.place(x=300,y=100)



#text label for sentece or words.............................................................................................................
lbl_fr_txt=Text(screen_real,bg='pink',wrap=WORD,width=40,height=6,font='italic 18 bold',bd=2)
lbl_fr_txt.place(x=290,y=200)
#adding scrll br............................................................................
scrollbr1=Scrollbar(screen_real)
scrollbr1.place(x=798,y=200,height=179)
scrollbr1.config(command=lbl_fr_txt.yview)
lbl_fr_txt.config(yscrollcommand=scrollbr1.set)






def enyrption():
    
    pswd = var.get()
    
    if pswd in virtualpswd_database:
        Enyrptt_screen=Toplevel(screen_real)
        Enyrptt_screen.title('Encrpted Data')
        Enyrptt_screen.geometry('500x780+800+40')
        icn_pic=PhotoImage(file='C:\\Users\\neha\\Links\\project2 encrypt decryt\\spnd.png')
        Enyrptt_screen.iconphoto(False,icn_pic)
        Enyrptt_screen.resizable(False,False)
        Enyrptt_screen.config(bg='black')
        lb_enryw1=Label(Enyrptt_screen,text='.........Encrypted Data.........',font='italic 10 bold',bg='black',fg='yellow')
        lb_enryw1.place(x=120,y=10)

        txarea=Text(Enyrptt_screen,wrap=WORD,width=40,height=10,font='italic 13 bold',bd=2)
        txarea.place(x=70,y=45)
        scrollbr2=Scrollbar(Enyrptt_screen)
        scrollbr2.place(x=418,y=49,height=190)
        scrollbr2.config(command=txarea.yview)
        txarea.config(yscrollcommand=scrollbr2.set)


        #importing dta from main scr...........................................................................................
        txtdataencry=lbl_fr_txt.get(1.0,END)#getting data from  main txt area scrren of in main screen
        encodemsg=txtdataencry.encode('ascii')
        encrytmsg=base64.b64decode(encodemsg)
        Encrpt_dta_show=encrytmsg.decode('ascii')#we Encoding after encde bcz to see datq in scr..
        
        txarea.insert(END,Encrpt_dta_show)# inserting data in encrytpion text scr area...
    
    elif pswd=='':
        messagebox.showerror('blank password Error','Password cant be blank!') #shows error by using msg box(imp=you have to gave to aggrumts)

    else:
         messagebox.showerror('Wrong password Error','You entered wrong pswd try again!')      

         def fr():
            label_fr_pswd.set('')
            var.set('')
            txarea.set('')


def deyrption():
    
    pswd = var.get()
    
    if pswd in virtualpswd_database:
        dyrptt_screen=Toplevel(screen_real)
        dyrptt_screen.title('dycrpted Data')
        dyrptt_screen.geometry('500x780+800+40')
        icn_pic=PhotoImage(file='C:\\Users\\neha\\Links\\project2 encrypt decryt\\spnd.png')
        dyrptt_screen.iconphoto(False,icn_pic)
        dyrptt_screen.resizable(False,False)
        dyrptt_screen.config(bg='red')
        lb_enryw2=Label(dyrptt_screen,text='.........dycrypted Data.........',font='italic 10 bold',bg='black',fg='yellow')
        lb_enryw2.place(x=120,y=10)

        txarea1=Text(dyrptt_screen,wrap=WORD,width=40,height=10,font='italic 13 bold',bd=2)
        txarea1.place(x=70,y=45)
        scrollbr3=Scrollbar(dyrptt_screen)
        scrollbr3.place(x=418,y=49,height=190)
        scrollbr3.config(command=txarea1.yview)
        txarea1.config(yscrollcommand=scrollbr3.set)

        #importing dta from main scr...........................................................................................
        txtdataencry1=lbl_fr_txt.get(1.0,END)#getting data from  main txt area scrren of in main screen
        encodemsg1=txtdataencry1.encode('ascii')
        encrytmsg1=base64.b64encode(encodemsg1)
        Encrpt_dta_show1=encrytmsg1.decode('ascii')#we decode after encde bcz to see datq in scr..
        
        txarea1.insert(END,Encrpt_dta_show1)
    
    elif pswd=='':
        messagebox.showerror('blank password Error','Password cant be blank!') #shows error by using msg box(imp=you have to gave to aggrumts)

    else:
         messagebox.showerror('Wrong password Error','You entered wrong pswd try again!')        

def fr():
    lbl_fr_txt.delete(1.0,END)
    var.set('')
    
#img sec fr btns.........................................................................................................
encryptbtn=PhotoImage(file='C:\\Users\\neha\\Links\\project2 encrypt decryt\\encry.png')
dncryptbtn=PhotoImage(file='C:\\Users\\neha\\Links\\project2 encrypt decryt\\dyrpt.png')
restbtn=PhotoImage(file='C:\\Users\\neha\\Links\\project2 encrypt decryt\\rsst.png')
lblbtn=PhotoImage(file='C:\\Users\\neha\\Links\\project2 encrypt decryt\\enyrpt.png')



#adding btns..............................................................................................................
btn1=Button(screen_real,image=encryptbtn,command=enyrption,bg='orange')
btn1.place(x=742,y=440)
btn2=Button(screen_real,image=dncryptbtn,command=deyrption,bg='steel blue')
btn2.place(x=222,y=435)
btn3=Button(screen_real,image=restbtn,command=fr,bg='red')
btn3.place(x=490,y=610)







#lbls fr pswd authenthi....................................................................................................................
lpic=Label(screen_real,image=lblbtn,bg='steel blue')
lpic.place(x=500,y=380)
lbl_title=Label(screen_real,text='Enter Your Secret Key...',font='italic 10 bold',bg='purple',fg='white')
lbl_title.place(x=530,y=380)




#text input lbl.........................................................................................................................
var=StringVar()

var2=Entry(textvariable=var,bd=2,show='#').place(x=690,y=381)












screen_real.mainloop()#most imp to use this mainloop closing if not used it cause crash of your program...;)

