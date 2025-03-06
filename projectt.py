from tkinter import *

# ایجاد پنجره اصلی
root = Tk()
root.title("مدیریت ثبت‌نام آموزشگاه")
root.geometry("600x500")


Label(root, text="نام:").grid(row=0, column=0, padx=5, pady=5, sticky=W)
Label(root, text="نام خانوادگی:").grid(row=1, column=0, padx=5, pady=5, sticky=W)
Label(root, text="نام دوره:").grid(row=0, column=2, padx=5, pady=5, sticky=W)
Label(root, text="رمز ورود:").grid(row=1, column=2, padx=5, pady=5, sticky=W)

Entry(root).grid(row=0, column=1, padx=5, pady=5)
Entry(root).grid(row=1, column=1, padx=5, pady=5)
Entry(root).grid(row=0, column=3, padx=5, pady=5)
Entry(root, show="*").grid(row=1, column=3, padx=5, pady=5)


listbox = Listbox(root, width=70)
listbox.grid(row=2, column=0, columnspan=4, padx=5, pady=5)


Button(root, text="مشاهده همه", width=20).grid(row=3, column=3, padx=5, pady=5, sticky=E)
Button(root, text="اضافه کردن", width=20).grid(row=4, column=3, padx=5, pady=5, sticky=E)
Button(root, text="خالی کردن ورودی‌ها", width=20).grid(row=5, column=3, padx=5, pady=5, sticky=E)
Button(root, text="حذف کردن", width=20).grid(row=6, column=3, padx=5, pady=5, sticky=E)
Button(root, text="خروج", width=20).grid(row=7, column=3, padx=5, pady=5, sticky=E)


Label(root, text="رمز ورود به سامانه:").grid(row=8, column=0, padx=5, pady=5, sticky=W)
Entry(root, show="*").grid(row=8, column=1, padx=5, pady=5)
Button(root, text="ورود به سامانه").grid(row=8, column=2, padx=5, pady=5)

root.mainloop()