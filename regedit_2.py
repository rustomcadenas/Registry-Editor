from tkinter import *
from tkinter import messagebox
import winreg
import ctypes, sys


class Login(Toplevel):
    def __init__(self, root):
        super().__init__(root)

        self.root = root  
        self.geometry("210x140")
        self.resizable(False, False)

        
        header_label = Label(self, text="Bawal Yaot!")
        header_label.place(x=70, y=10)

        username_var = StringVar() 
        username_label = Label(self, text="Username: ")
        username_label.place(x=5, y=40)
        username_entry = Entry(self, textvariable=username_var)
        username_entry.place(x=70, y=40)

        userpass_var = StringVar()
        userpass_label = Label(self, text="Password: ")
        userpass_label.place(x=5, y=70)
        userpass_entry = Entry(self, show="x", textvariable=userpass_var)
        userpass_entry.place(x=70, y=70)

        login_btn = Button(self, text="Login", width=10, command=lambda:self.login(username_var.get(), userpass_var.get()))
        login_btn.place(x=115, y=100)

         

    def login(self, logUsername, logPassword):
    	if logUsername == "admin" and logPassword == "h3ll0w0rld":
    		self.withdraw()
    		self.root.deiconify() 

    	else:
    		messagebox.showerror("Error", "Bawal dire ang mga yaot!, kasabot?")
    		quit()
# ===== is admin 
def is_admin():
	try: 
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False 

# ===== winreg functions 
local_machine_path = winreg.HKEY_LOCAL_MACHINE

def NoSMMyPictures(value):
	values = 1 if value==1 else 0
	key = "NoSMMyPictures"
	try:
		registry_key = winreg.OpenKeyEx(local_machine_path, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer', 0, winreg.KEY_SET_VALUE)
		winreg.SetValueEx(registry_key, key, 0, winreg.REG_DWORD, values)
	except Exception as e:
		messagebox.showerror("Error", e)
	 


# ===== Methods / Functions 
def apply(value):
	NoSMMyPictures(value)
	

def main():
	root = Tk()
	root.title("Tomas Gwapo")
	root.resizable(False, False)
	root.geometry("400x400")
	root.withdraw()

	apply_btn = Button(root, text="Apply", width=10, command=lambda: apply(NoSMMyPicture_val.get()))
	apply_btn.place(x=300, y=20)

	NoSMMyPicture_val = IntVar()
	NoSMMyPicture_check = Checkbutton(root, text="No SM My Pictures", variable=NoSMMyPicture_val, onvalue=1, offvalue=0)
	NoSMMyPicture_check.place(x=10, y=20)  

	login_window =  Login(root)
	root.mainloop()


if __name__ == "__main__":
	if is_admin(): 
		main()
	else:
		ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, 'regedit_2.py', None, 1)
 
 
