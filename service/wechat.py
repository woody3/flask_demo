import logging
import subprocess
from time import sleep
import win32api
import win32con
import win32gui
from PIL import ImageGrab
from pytesseract import pytesseract
from pyzbar import pyzbar
from win32com import client
from utils.configUtils import Config
from utils.convertors import Convertors


class Wechat(object):
    @staticmethod
    def get_login_qrcode():
        window: int
        wx_path = Config.get_wx_path()
        boot_waiting_time = Config.boot_waiting_sec()
        qrcode_refresh_waiting_time = Config.qrcode_refresh_waiting_sec()
        if Wechat.wechat_login_status():
            return "处理中，请勿重复获取二维码"
        subprocess.Popen(wx_path)
        while win32gui.FindWindow(None, "微信") == 0:
            sleep(boot_waiting_time)
            print("等待微信启动")

        window = win32gui.FindWindow(None, "微信")
        a, b, _, _ = win32gui.GetWindowRect(window)
        a += 64
        b += 90
        c = a + 152
        d = b + 152
        Wechat.refresh_qrcode(a, d, window, qrcode_refresh_waiting_time)
        win32gui.SetForegroundWindow(window)
        img = ImageGrab.grab(bbox=(a, b, c, d))
        while not pyzbar.decode(img):
            sleep(qrcode_refresh_waiting_time)
            logging.info("等待微信二维码刷新")
            Wechat.refresh_qrcode(a, d, window, qrcode_refresh_waiting_time)
            img = ImageGrab.grab(bbox=(a, b, c, d))
        img = img.resize((int(img.width * 1.2), int(img.height * 1.2)))
        return Convertors.pil2base64(img)

    @staticmethod
    def close_wechat():
        # handler = win32gui.FindWindow(None, "微信")
        # win32gui.SendMessage(handler, win32con.WM_CLOSE)
        processes = Wechat.get_wechat_process()
        for proc in processes:
            if proc.name == "WeChat.exe":
                try:
                    proc.Terminate()
                except:
                    pass
                logging.info("weixin zhongzhile")
        sleep(1)

    @staticmethod
    def refresh_qrcode(start_x, end_y, window, interval):
        win32gui.SetForegroundWindow(window)
        img = ImageGrab.grab(bbox=(start_x-10, end_y+80, start_x+200, end_y+110))
        text = pytesseract.image_to_string(img, lang='chi_sim')
        if "切换" in text or "重新扫码" in text:
            win32gui.SetForegroundWindow(window)
            win32api.SetCursorPos((start_x+20, end_y+98))
            win32gui.SetForegroundWindow(window)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            sleep(interval)

    @staticmethod
    def wechat_login_status():
        procs = Wechat.get_wechat_process()
        for proc in procs:
            if "WeChatPlayer" in proc.name:
                return True
        return False

    @staticmethod
    def get_wechat_process():
        process = []
        WMI = client.GetObject("winmgmts:")
        processes = WMI.InstancesOf("Win32_Process")
        for proc in processes:
            if "WeChat" in proc.name:
                process.append(proc)
        return process
