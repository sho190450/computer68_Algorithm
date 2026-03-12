import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

# ตัวแปรเก็บข้อมูลรายรับ-จ่าย
balance = 0
total_income = 0
total_expense = 0

# ฟังก์ชันเพิ่มข้อมูล
def add_data():
    global balance, total_income, total_expense

    date = entry_date.get()
    item = entry_item.get()
    income = entry_income.get()
    expense = entry_expense.get()

    if income == "":
        income = 0
    else:
        income = float(income)

    if expense == "":
        expense = 0
    else:
        expense = float(expense)

    total_income += income
    total_expense += expense
    balance = total_income - total_expense

    table.insert("", "end", values=(date, item, income, expense, balance))

    income_label.config(text="รวมรายรับ: " + str(total_income))
    expense_label.config(text="รวมรายจ่าย: " + str(total_expense))
    balance_label.config(text="คงเหลือ: " + str(balance))

    entry_item.delete(0, tk.END)
    entry_income.delete(0, tk.END)
    entry_expense.delete(0, tk.END)


# สร้างหน้าต่าง
window = tk.Tk()
window.title("บัญชีรายรับรายจ่าย")
window.geometry("950x550")
window.configure(bg="#1e1e1e")

# หัวข้อ
title = tk.Label(window,
                 text="บัญชีรายรับรายจ่าย",
                 font=("Segoe UI",22,"bold"),
                 bg="#1e1e1e",
                 fg="#c084fc")
title.pack(pady=10)

# กรอบกรอกข้อมูล
frame_input = tk.Frame(window, bg="#1e1e1e")
frame_input.pack(pady=10)

font_main = ("Segoe UI",11)

# วันที่ (Calendar)
tk.Label(frame_input,text="วันที่",font=font_main,bg="#1e1e1e",fg="white").grid(row=0,column=0,padx=5)

entry_date = DateEntry(frame_input,
                       width=12,
                       background='purple',
                       foreground='white',
                       borderwidth=2,
                       date_pattern='dd/mm/yyyy')

entry_date.grid(row=1,column=0)

# รายการ
tk.Label(frame_input,text="รายการ",font=font_main,bg="#1e1e1e",fg="white").grid(row=0,column=1,padx=5)
entry_item = tk.Entry(frame_input,width=25,font=font_main)
entry_item.grid(row=1,column=1)

# รายรับ
tk.Label(frame_input,text="รายรับ",font=font_main,bg="#1e1e1e",fg="white").grid(row=0,column=2,padx=5)
entry_income = tk.Entry(frame_input,width=12,font=font_main)
entry_income.grid(row=1,column=2)

# รายจ่าย
tk.Label(frame_input,text="รายจ่าย",font=font_main,bg="#1e1e1e",fg="white").grid(row=0,column=3,padx=5)
entry_expense = tk.Entry(frame_input,width=12,font=font_main)
entry_expense.grid(row=1,column=3)

# ปุ่มเพิ่มข้อมูล
tk.Button(window,
          text="เพิ่มข้อมูล",
          command=add_data,
          font=("Segoe UI",11,"bold"),
          bg="#9333ea",
          fg="white").pack(pady=10)

# ตาราง
style = ttk.Style()
style.theme_use("default")

style.configure("Treeview",
                font=("Segoe UI",11),
                rowheight=28,
                background="#ffffff",
                fieldbackground="#ffffff")

style.configure("Treeview.Heading",
                font=("Segoe UI",11,"bold"),
                background="#9333ea",
                foreground="white")

columns = ("date","item","income","expense","balance")

table = ttk.Treeview(window,
                     columns=columns,
                     show="headings",
                     height=15)

table.heading("date",text="วันที่")
table.heading("item",text="รายการ")
table.heading("income",text="รายรับ")
table.heading("expense",text="รายจ่าย")
table.heading("balance",text="คงเหลือ")

table.column("date",width=120,anchor="center")
table.column("item",width=350)
table.column("income",width=120,anchor="center")
table.column("expense",width=120,anchor="center")
table.column("balance",width=120,anchor="center")

table.pack(pady=10)

# สรุปยอด
summary = tk.Frame(window,bg="#1e1e1e")
summary.pack(pady=10)

income_label = tk.Label(summary,text="รวมรายรับ: 0",
                        font=("Segoe UI",12,"bold"),
                        fg="#c084fc",
                        bg="#1e1e1e")
income_label.grid(row=0,column=0,padx=20)

expense_label = tk.Label(summary,text="รวมรายจ่าย: 0",
                         font=("Segoe UI",12,"bold"),
                         fg="#c084fc",
                         bg="#1e1e1e")
expense_label.grid(row=0,column=1,padx=20)

balance_label = tk.Label(summary,text="คงเหลือ: 0",
                         font=("Segoe UI",12,"bold"),
                         fg="#c084fc",
                         bg="#1e1e1e")
balance_label.grid(row=0,column=2,padx=20)

# เครดิตผู้พัฒนา
credit = tk.Label(window,
                  text="พัฒนาโดย ศรัณย์ มาใหญ่ 684245014",
                  font=("Segoe UI",10),
                  bg="#1e1e1e",
                  fg="gray")
credit.pack(side="bottom", pady=5)

window.mainloop()