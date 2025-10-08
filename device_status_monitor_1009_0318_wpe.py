# 代码生成时间: 2025-10-09 03:18:28
import tkinter as tk
from tkinter import messagebox
import threading
import time

"""
设备状态监控程序，使用TKINTER框架创建GUI界面
实现设备状态的实时监控和显示
"""

class DeviceStatusMonitor:
    def __init__(self, master):
        """初始化监控程序，设置GUI界面"""
        self.master = master
        self.master.title("设备状态监控")
        self.master.geometry("400x300")

        # 创建状态标签
        self.status_label = tk.Label(master, text="初始状态", font=("Arial", 14))
        self.status_label.pack(pady=20)

        # 创建开始按钮
        self.start_button = tk.Button(master, text="开始监控", command=self.start_monitoring)
        self.start_button.pack(pady=20)

        # 创建停止按钮
        self.stop_button = tk.Button(master, text="停止监控", command=self.stop_monitoring)
        self.stop_button.pack(pady=20)

        # 初始化监控线程和设备状态
        self.monitor_thread = None
        self.device_status = "初始状态"

    def start_monitoring(self):
        """开始监控设备状态"""
        if self.monitor_thread is None:
            self.monitor_thread = threading.Thread(target=self.monitor_device_status)
            self.monitor_thread.start()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
        else:
            messagebox.showwarning("警告", "监控已在进行中！")

    def stop_monitoring(self):
        """停止监控设备状态"""
        if self.monitor_thread is not None:
            self.monitor_thread.join()
            self.monitor_thread = None
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
        else:
            messagebox.showwarning("警告", "监控未在进行中！")

    def monitor_device_status(self):
        """监控设备状态的线程函数"""
        while True:
            try:
                # 模拟设备状态更新
                self.device_status = self.get_device_status()
                # 更新GUI界面
                self.status_label.config(text=self.device_status)
                # 每隔1秒更新一次
                time.sleep(1)
            except Exception as e:
                messagebox.showerror("错误", f"监控过程中出现错误：{str(e)}")
                break

    def get_device_status(self):
        """获取设备当前状态（模拟函数）"""
        # 模拟设备状态变化
        statuses = ["正常", "警告", "异常", "离线"]
        return statuses[(len(statuses) - 1) % time.time() % len(statuses)]

if __name__ == "__main__":
    # 创建主窗口
    root = tk.Tk()

    # 创建监控程序实例
    monitor = DeviceStatusMonitor(root)

    # 开始主循环
    root.mainloop()