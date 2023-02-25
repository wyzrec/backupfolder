#GUI
from pathlib import Path  
import PySimpleGUI as sg 
from psgtray import SystemTray
# from PIL import Image

#backup
import shutil
import time
import os
import re

#Base64图标
backupicon=b"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"

#验证文件路径
def is_valid_path(filepath):
    if filepath and Path(filepath).exists():
        return True
    sg.popup("路径不正确",icon=backupicon, title='')
    return False

#验证输入时间
def valid_input(backuptime):
    if re.compile(r'^\d{1,5}$').match(backuptime):
        return True
    sg.popup("输入时间不正确",icon=backupicon, title='')
    return False

#主窗口
def main_window():
    #主页面
    #menu_def = [["设置",["开机自启√","开启通知√"]],["帮助", ["关于","退出"]]]

    layout = [
              #[sg.MenubarCustom(menu_def, tearoff=False)],
              #[sg.Menu(menu_def)],
              [sg.T("备份文件夹:", s=15, justification="r"), sg.I(settings["set"]["Folder1"],key="-IN-"), sg.FolderBrowse('浏览')],
              [sg.T("储存路径:", s=15, justification="r"), sg.I(settings["set"]["Folder2"],key="-OUT-"), sg.FolderBrowse('浏览')],
              [sg.T("每隔时间:", s=15, justification="r"), sg.I(settings["set"]["backuptime"],key="-TIME-",size=(6)),sg.Combo(['秒','分钟','小时'], default_value=settings["set"]["select"] if settings["set"]["select"] else "分钟",size=(5), enable_events=True, readonly=True, k='-SELECT-')],
              [sg.Column(layout=[[sg.T("00:00:00", font=('Helvetica', 20),key="countdown")]],justification='center',key='Column')],
              [sg.Column(layout=[[sg.B("自动备份", s=16),sg.B("停止",s=16, button_color="tomato",visible=False),],], justification='center')]]
    
    window_title = '文件夹备份'
    window = sg.Window(window_title, layout,enable_close_attempted_event=True,use_custom_titlebar=False,icon=backupicon,titlebar_icon=backupicon,)

    #托盘
    menu = ['', ['立即备份','---','显示窗口', '隐藏窗口', '---','关于','退出']]
    tray = SystemTray(menu, single_click_events=True, window=window, tooltip='文件夹备份', icon=backupicon)

    #计时器
    timer_running = False
    counter = 0

    #按钮交互
    while True:
        event, values = window.read(timeout=1000) #timeout实时读取
        if event == tray.key:
            #sg.cprint(f'System Tray Event = ', values[event], c='white on red')
            event = values[event]
            
        if event in (sg.WINDOW_CLOSED, "退出"):
            break
        #print(event)
        #托盘按钮
        if event in ('显示窗口', sg.EVENT_SYSTEM_TRAY_ICON_ACTIVATED):
            window.un_hide()
            window.bring_to_front()
        # if event in ('显示窗口', sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED):
        #     window.un_hide()
        #     window.bring_to_front()
        if event in ('隐藏窗口', sg.WIN_CLOSE_ATTEMPTED_EVENT):
            window.hide()
            tray.show_icon() 
        if event == "立即备份":
            if is_valid_path(values["-IN-"]) and is_valid_path(values["-OUT-"]) and valid_input(values["-TIME-"]):
                backup_folder()
                tray.show_message('提示','操作成功')
        #主页面按钮
        if event == "自动备份":
            if is_valid_path(values["-IN-"]) and is_valid_path(values["-OUT-"]) and valid_input(values["-TIME-"]):
                window[event].update(visible=False)
                window["停止"].update(visible=True)
                settings["set"]["Folder1"] = values["-IN-"]
                settings["set"]["Folder2"] = values["-OUT-"]
                settings["set"]["backuptime"] = values["-TIME-"]
                settings["set"]["select"] = values["-SELECT-"]
                timer_running = True
                if settings["set"]["select"] == '秒':countdown = int(settings["set"]["backuptime"])
                if settings["set"]["select"] == '分钟':countdown = int(settings["set"]["backuptime"])*60
                if settings["set"]["select"] == '小时':countdown = int(settings["set"]["backuptime"])*60*60
                # window["Column"].update(visible=False)
                # print(int(values["-TIME-"])*100*60)
                # print(values["-SELECT-"])
        # if event == "设置":
        #     print('ok')
        if event == "停止":
            window[event].update(visible=False)
            window["自动备份"].update(visible=True)
            window['countdown'].update("00:00:00")
            counter = 0
            timer_running = False
        if event == "关于":
            window.disappear()
            sg.popup(window_title,"Version 1.0", "BY WYZ", grab_anywhere=True,icon=backupicon, title='')
            window.reappear()
        # if values['-SELECT-'] != settings["set"]["select"]:
        #     settings["set"]["select"] = values["-SELECT-"]

        # print(counter)
        if timer_running:
            counter += 1
            countdown -= 1
            if settings["set"]["select"] == '秒':
                if counter == int(settings["set"]["backuptime"]):
                    countdown = int(settings["set"]["backuptime"])
                    counter = 0
                    backup_folder()
            if settings["set"]["select"] == '分钟':
                if counter == int(settings["set"]["backuptime"])*60: 
                    countdown = int(settings["set"]["backuptime"])*60
                    counter = 0
                    backup_folder()
            if settings["set"]["select"] == '小时':
                if counter == int(settings["set"]["backuptime"])*60*60:
                    countdown = int(settings["set"]["backuptime"])*60*60
                    counter = 0
                    backup_folder()
            
            window['countdown'].update('{:02d}:{:02d}:{:02d}'.format(countdown//60//60,(countdown // 60) % 60,countdown% 60))
    tray.close() 
    window.close()

#备份操作
def backup_folder():
    source = settings["set"]["Folder1"].replace("\\", "/")
    target = settings["set"]["Folder2"].replace("\\", "/")
    Folder1 = re.search(r'/([^/]+)$', source)
    current_time = time.strftime("%Y%m%d%H%M%S")
    target_folder = os.path.join(target, target+"/"+Folder1.group(1) +"_"+ current_time)
    shutil.copytree(source, target_folder)

#初始化
if __name__ == "__main__":
    SETTINGS_PATH = Path.cwd()
    #没有config创建文件
    config_path = os.path.join(SETTINGS_PATH, "wconfig.ini")
    if not os.path.exists(config_path):
        with open(config_path, "w") as f:
            f.write("")
    # create the settings object and use ini format
    settings = sg.UserSettings(
        path=SETTINGS_PATH, filename="wconfig.ini", use_config_file=True, convert_bools_and_none=True
    )
    font_family ='Segoe UI'
    font_size = '12'
    sg.theme('DarkGrey9')
    sg.set_options(font=(font_family, font_size))
    main_window()


