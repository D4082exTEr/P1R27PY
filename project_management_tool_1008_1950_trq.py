# 代码生成时间: 2025-10-08 19:50:50
import tkinter as tk
from tkinter import messagebox, ttk

"""
项目管理工具，使用TKINTER框架创建GUI。
"""

class ProjectManagementTool:
    def __init__(self, root):
        """
        初始化项目管理工具界面。
        :param root: tkinter主窗口
        """
        self.root = root
        self.root.title('项目管理工具')

        # 设置窗口大小
        self.root.geometry('800x600')

        # 创建项目列表
        self.projects = []

        # 创建左侧框架用于显示项目列表
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # 创建项目列表的滚动条
        self.projects_scroll = tk.Scrollbar(self.left_frame)
        self.projects_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # 创建项目列表
        self.projects_list = tk.Listbox(self.left_frame, yscrollcommand=self.projects_scroll.set)
        self.projects_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.projects_scroll.config(command=self.projects_list.yview)

        # 创建右侧框架用于显示项目详情
        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 创建项目信息标签
        self.project_info_label = tk.Label(self.right_frame, text="项目信息")
        self.project_info_label.pack()

        # 创建项目名称输入框
        self.project_name_entry = tk.Entry(self.right_frame)
        self.project_name_entry.pack(pady=10)

        # 创建添加项目按钮
        self.add_project_button = tk.Button(self.right_frame, text="添加项目", command=self.add_project)
        self.add_project_button.pack(pady=10)

        # 创建删除项目按钮
        self.delete_project_button = tk.Button(self.right_frame, text="删除项目", command=self.delete_project)
        self.delete_project_button.pack(pady=10)

    def add_project(self):
        """
        添加项目到列表。
        """
        project_name = self.project_name_entry.get()
        if not project_name:
            messagebox.showwarning("警告", "项目名称不能为空")
            return

        if project_name in self.projects:
            messagebox.showwarning("警告", "项目已存在")
            return

        self.projects.append(project_name)
        self.projects_list.insert(tk.END, project_name)
        self.project_name_entry.delete(0, tk.END)

    def delete_project(self):
        """
        从列表中删除项目。
        """
        try:
            project_index = self.projects_list.curselection()[0]
            project_name = self.projects_list.get(project_index)
            self.projects.remove(project_name)
            self.projects_list.delete(project_index)
        except IndexError:
            messagebox.showwarning("警告", "请选择一个项目")

if __name__ == '__main__':
    """
    程序入口。
    """
    root = tk.Tk()
    app = ProjectManagementTool(root)
    root.mainloop()
