# 代码生成时间: 2025-10-01 02:10:29
import tkinter as tk
from tkinter import messagebox

# 定义一个简单的设备类
class Equipment:
    def __init__(self, name, quantity, location):
        self.name = name
        self.quantity = quantity
        self.location = location

    def display(self):
        return f"Name: {self.name}, Quantity: {self.quantity}, Location: {self.location}"

# 主应用类
class MedicalEquipmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Equipment Management")

        self.equipment_list = []
        self.create_widgets()

    def create_widgets(self):
        # 输入框
        self.name_var = tk.StringVar()
        self.quantity_var = tk.DoubleVar()
        self.location_var = tk.StringVar()

        self.name_label = tk.Label(self.root, text="Equipment Name: ")
        self.name_entry = tk.Entry(self.root, textvariable=self.name_var)

        self.quantity_label = tk.Label(self.root, text="Quantity: ")
        self.quantity_entry = tk.Entry(self.root, textvariable=self.quantity_var)

        self.location_label = tk.Label(self.root, text="Location: ")
        self.location_entry = tk.Entry(self.root, textvariable=self.location_var)

        # 按钮
        self.add_button = tk.Button(self.root, text="Add Equipment", command=self.add_equipment)
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_entries)
        self.display_button = tk.Button(self.root, text="Display Equipment", command=self.display_equipment)

        # 布局
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.quantity_label.grid(row=1, column=0)
        self.quantity_entry.grid(row=1, column=1)
        self.location_label.grid(row=2, column=0)
        self.location_entry.grid(row=2, column=1)
        self.add_button.grid(row=3, column=0)
        self.clear_button.grid(row=3, column=1)
        self.display_button.grid(row=3, column=2)

    def add_equipment(self):
        # 获取输入数据
        name = self.name_var.get()
        quantity = self.quantity_var.get()
        location = self.location_var.get()

        # 检查输入数据的有效性
        if not name or not quantity or not location:
            messagebox.showerror("Input Error", "Please fill in all fields")
            return

        try:
            quantity = float(quantity)
        except ValueError:
            messagebox.showerror("Input Error", "Invalid quantity. Please enter a number.")
            return

        # 添加设备到列表
        equipment = Equipment(name, quantity, location)
        self.equipment_list.append(equipment)
        messagebox.showinfo("Success", "Equipment added successfully")
        self.clear_entries()

    def clear_entries(self):
        self.name_var.set("")
        self.quantity_var.set(0)
        self.location_var.set("")

    def display_equipment(self):
        if not self.equipment_list:
            messagebox.showinfo("Info", "There are no equipment to display")
            return

        result = ""
        for equipment in self.equipment_list:
            result += equipment.display() + "
"
        messagebox.showinfo("Equipment List", result)

# 主函数
def main():
    root = tk.Tk()
    app = MedicalEquipmentApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()