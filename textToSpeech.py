import wx
import pyttsx3

class TextToSpeechConverter(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Text To Speech Converter", size=(1000, 580))
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('#F7AC40')

        upper_panel = wx.Panel(self.panel, size=(1000, 130))
        upper_panel.SetBackgroundColour('#14A7DD')

        text_label = wx.StaticText(self.panel, label="Text to speech converter", pos=(250, 35), size=(500, -1))
        text_label.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        text_label.SetForegroundColour(wx.WHITE)

        self.text_box = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE, pos=(30, 150), size=(940, 180), value='')
        self.text_box.SetFocus()

        gender_label = wx.StaticText(self.panel, label="Select Voice", pos=(340, 370))
        gender_label.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        gender_label.SetForegroundColour(wx.WHITE)

        self.gender_box = wx.ComboBox(self.panel, pos=(340, 400), choices=['Voice 1', 'Voice 2'], style=wx.CB_READONLY)
        self.gender_box.SetValue('Voice 1')

        speed_label = wx.StaticText(self.panel, label="Select Speed", pos=(540, 370))
        speed_label.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        speed_label.SetForegroundColour(wx.WHITE)

        self.speed_box = wx.ComboBox(self.panel, pos=(540, 400), choices=['Fast', 'Medium', 'Slow'], style=wx.CB_READONLY)
        self.speed_box.SetValue('Medium')

        play_btn = wx.Button(self.panel, label="Play (Alt+P)", pos=(400, 450))
        play_btn.Bind(wx.EVT_BUTTON, self.on_play)
        play_btn.SetToolTip("Press Alt+P to play")

        self.tts = pyttsx3.init()

        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Bind(wx.EVT_MENU, self.on_open_edit, id=wx.ID_EDIT)
        self.Bind(wx.EVT_MENU, self.on_play_shortcut, id=wx.ID_EXECUTE)

        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_ALT, ord('E'), wx.ID_EDIT),
                                          (wx.ACCEL_ALT, ord('P'), wx.ID_EXECUTE)])
        self.SetAcceleratorTable(accel_tbl)

    def on_play(self, event):
        text = self.text_box.GetValue()
        gender = self.gender_box.GetValue()
        speed = self.speed_box.GetValue()

        voices = self.tts.getProperty('voices')

        def set_voice():
            if gender == 'Voice 1':
                self.tts.setProperty('voice', voices[0].id)
                self.tts.say(text)
                self.tts.runAndWait()
            else:
                self.tts.setProperty('voice', voices[1].id)
                self.tts.say(text)
                self.tts.runAndWait()

        if text:
            if speed == 'Fast':
                self.tts.setProperty('rate', 250)
                set_voice()
            elif speed == 'Medium':
                self.tts.setProperty('rate', 150)
                set_voice()
            else:
                self.tts.setProperty('rate', 60)
                set_voice()

    def on_close(self, event):
        self.tts.stop()
        self.Destroy()

    def on_open_edit(self, event):
        self.text_box.SetFocus()

    def on_play_shortcut(self, event):
        self.on_play(event)

if __name__ == "__main__":
    app = wx.App(False)
    frame = TextToSpeechConverter()
    frame.Show()
    app.MainLoop()
