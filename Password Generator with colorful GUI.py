import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("660x600")
        self.root.title("Password Generator")
      
        bg_color = "#074463"
        title = tk.Label(self.root, text="Password Generator", fg="Blue", font=("time new roman", 30, "bold"), pady=2).pack(fill=tk.X)

        self.Username = tk.StringVar()
        self.password_length = tk.IntVar()
        self.generated_password = tk.StringVar()

        F1 = tk.LabelFrame(self.root,text="Password", font=("time new roman", 20, "bold"), fg="gold")
        F1.place(x=0, y=80, relwidth=1)
        
        Username_lbl = tk.Label(F1, text="Username", bg=bg_color, fg="white", font=("time new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        Username_txt = tk.Entry(F1, width=30, textvariable=self.Username, font="arial 15", bd=7, relief=tk.SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        Length_lbl = tk.Label(F1, text="Password Length", bg=bg_color, fg="white", font=("time new roman", 18, "bold")).grid(row=1, column=0, padx=20, pady=5)
        Length_txt = tk.Entry(F1, width=30, textvariable=self.password_length, font="arial 15", bd=7, relief=tk.SUNKEN).grid(row=1, column=1, pady=5, padx=10)
        
        Result_lbl = tk.Label(F1, text="Generated Password", bg=bg_color, fg="white", font=("time new roman", 18, "bold")).grid(row=3, column=0, padx=20, pady=5)
        Result_txt = tk.Entry(F1, width=30, textvariable=self.generated_password, font="arial 15", bd=7, relief=tk.SUNKEN, state='readonly').grid(row=3, column=1, pady=5, padx=10)

        generate_btn = tk.Button(F1, text="Generate Password", command=self.generate_password, bg="lightblue", fg="black", pady=15, width=20, font="arial 15 bold").grid(row=4, column=0, columnspan=2,padx=10, pady=10)
        reset_btn = tk.Button(F1, text="Reset", command=self.reset_form, bg="lightgreen", fg="black", pady=15, width=20, font="arial 15 bold").grid(row=6, column=0,columnspan=2, padx=10, pady=10)
        accept_btn = tk.Button(F1, text="Accept", command=self.accept_password, bg="lightcoral", fg="black", pady=15, width=20, font="arial 15 bold").grid(row=5, column=0, columnspan=2, padx=10, pady=10)



    def generate_password(self):
        try:
            length = self.password_length.get()
            if length < 1:
                raise ValueError("Password length must be at least 1")

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for i in range(length))
            self.generated_password.set(password)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def accept_password(self):
        username = self.Username.get()
        password = self.generated_password.get()
        if username and password:
            messagebox.showinfo("Accepted", f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showerror("Error", "Please generate a password first")

    def reset_form(self):
        self.Username.set("")
        self.password_length.set(0)
        self.generated_password.set("")

if __name__ == "__main__":
    root = tk.Tk()
    obj = PasswordGenerator(root)
    root.mainloop()
