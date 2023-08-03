from tkinter import *
from cryptography.fernet import Fernet
from functools import partial
import base64
from PIL import Image, ImageTk

# -- Encrypt and Decrypt your keys by Privacy Data App --#

# Main Elements
key = b'uvdQ21DzRo-YzyMj6bqtJ0322sAnRSCt6HZbELJUvRPzNE='  # to decrypt keys you have to use the same "key signature". Change here later
f = Fernet(key)
privacy_data = {}
MasterKey = "aa"  # its your main key to see all keys


# Functions
def Error_Message():
    global error_img
    top = Toplevel()
    top.title("Oops")
    error_img = ImageTk.PhotoImage(Image.open(r'error.png'))
    Label(top, image=error_img).pack()

try:
    def Encrypt(text_f: Entry):
        if master_key_entry.get() == MasterKey:
            encrypted = f.encrypt(bytes(text_f.get(), 'utf-8'))
            file_name = user_key_title.get()
            privacy_data.setdefault(f"{file_name}", encrypted)
            with open(f'{file_name}.txt','w') as data_file:  # While encrypting keys, creating a new txt folder to keep that. It's easy to find and read again.
                data_file.write(''.join("\n"))
                data_file.write(''.join(f"{privacy_data}"))
                data_file.close()
            screen.config(text="Encrypted successfully")
        else:
            Error_Message()
except:
        Error_Message()


try:
    def Decrypt(user_key_title: Entry):
        if master_key_entry.get() == MasterKey:
            file_name = user_key_title.get()
            with open(f'{file_name}.txt', 'r') as data_file:
                data = data_file.read()
            privacy_data.update(eval(data))
            data_file.close()
            k = privacy_data[file_name]
            decrypted = f.decrypt(k)
            decrypted = str(decrypted)
            decrypted_message = decrypted[2:-1]
            screen.config(text=f"{decrypted_message}")
        else:
            Error_Message()
except:
        Error_Message()



# Set Screen and Images

root = Tk()
root.geometry("495x700")
root.title("Privacy Data")

background_image = PhotoImage(file="dataprivacybg.png")
background_image_label = Label(root, image=background_image)
background_image_label.place(x=0, y=0)

enc_button_image = PhotoImage(file="encryptButton.png")
dec_button_image = PhotoImage(file="decryptButton.png")

screen = Label(width=18, height=4, bg="white", text="")
screen.place(x=180, y=405)


# Entry

text_user = ""
user_key = Entry(root, textvariable=text_user)
user_key.place(x=62, y=172, width=370, height=33)

user_key_title = Entry(root, textvariable=text_user)
user_key_title.place(x=62, y=240, width=370, height=33)

master_key_entry = Entry(root)
master_key_entry.place(x=62, y=572, width=370, height=33)


# Buttons


# for Encrypting
encrypt_button = Button(root, image=enc_button_image, bd=2, text="Encrypt", command=partial(Encrypt, user_key))
encrypt_button.place(x=122, y=619, width=120, height=33)

# Decrypting from key title -- You just need to know "Key title" and "Masterkey" to decrypt the "Key".
decrypt_button = Button(root, image=dec_button_image, bd=2, text="Decrypt", command=partial(Decrypt, user_key_title))
decrypt_button.place(x=242, y=619, width=120, height=33)

root.mainloop()
