from tkinter import*
from tkinter import filedialog

root=Tk()
root.geometry("200x200")

def encrypt_image():
    file1st=filedialog.askopenfile(mode='r',filetypes=[('jpg file','*.jpg')])
    if file1st is not None:
        file_name=file1st.name
        key=entry1st.get(1.0,END)
        print(file_name,key)
        fi=open(file_name,'rb')
        image=fi.read()
        fi.close()
        image=bytearray(image)
        for index,values in enumerate(image):
            image[index]=values^int(key)
        fi1=open(file_name,'wb')
        fi1.write(image)
        fi1.close()

button=Button(root,text="encrypt/decrypt",command=encrypt_image)
button.place(x=50,y=10)
entry1st=Text(root,height=1,width=10)
entry1st.place(x=55,y=55)

root.mainloop()
