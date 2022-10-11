"""Subclass of MyFrame1, which is generated by wxFormBuilder."""

import os
import subprocess
import tempfile

import cv2
import moviepy.editor as mp
import numpy as np
import wx
import App

from pydub import AudioSegment


WIDTH = 800
HEIGHT = 600
FPS = 60
SAMPLE_RATE = 44100
FRAME_SIZE = 2048  
SAMPLING_SIZE = FRAME_SIZE * 4
INT16_MAX = 32767

preview_data = [23.97877689, 6.85166079, 0.0, 0.0, 7.74882264, 0.0, 0.0, 9.77712341, 0.0, 20.93901343, 0.0, 33.45155314, 29.2166891, 0.0, 9.52927197, 11.16447276, 19.95186728, 0.0, 14.15247974, 18.98400545, 19.80741083, 49.46484202, 6.85965645, 12.70949027, 4.00079555, 12.15805654, 20.20038415, 13.70362379, 32.43606186, 30.16001426, 58.84907029, 45.15902352, 28.94616422, 50.62166162, 103.4423617, 200.58170151, 209.43992705, 267.33022312, 76.84569139, 60.68818881, 74.12634801, 128.76411455, 42.16144102, 35.71657766, 52.19179011, 23.2780897, 26.23851274, 29.75537854, 38.60292573, 28.12012731, 42.14545554, 36.32095902, 53.45524617, 36.86722298, 31.47895737, 72.50372511, 100.38679199, 40.98758931, 74.43735078, 65.5357791, 58.66018862, 106.40858241, 113.95347814, 103.46142682, 89.91234329, 150.69379353, 136.26565617, 170.44672991, 189.39906453, 249.12484728, 276.01626992, 242.96915763, 324.41724943, 285.57455461, 379.27829873, 416.02735037, 526.86589897, 648.80578632, 730.0380328, 846.29444645, 842.31018416, 889.29242904, 1335.26024003, 1405.62453582, 1460.25159463, 1524.69427391, 1731.44561156, 1927.27107693, 2226.31246776, 2137.92277822, 2040.65799756, 2143.53545926, 2090.95210328, 2251.60565529, 1852.38596794, 1929.41548201, 1802.70399699, 1607.27375332, 1437.16933874, 1169.71338282]
spectram_range = [int(22050 / 2 ** (i/10)) for i in range(100, -1,-1)]
freq = np.abs(np.fft.fftfreq(SAMPLING_SIZE, d=(1/SAMPLE_RATE)))
spectram_array = (freq <= spectram_range[0]).reshape(1,-1)
for index in range(1, len(spectram_range)):
    tmp_freq = ((freq > spectram_range[index - 1]) & (freq <= spectram_range[index])).reshape(1,-1)
    spectram_array = np.append(spectram_array, tmp_freq, axis=0)
part_w = WIDTH / len(spectram_range)
part_h = HEIGHT / 100


# Implementing MyFrame1
class CreateMVMyFrame1( App.MyFrame1 ):
    def __init__( self, parent ):
        App.MyFrame1.__init__( self, parent )
        self.shapes = {0: draw_horizon, 1: draw_circle}
        self.colors = {0: (0, 0, 255), 1: (255, 0, 0), 2: (0, 255, 0), 3: (0, 255, 255), 4: (0, 0, 0), 5:(255, 255, 255)}
        try:
            subprocess.run("ffmpeg", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            wx.MessageBox("ffmpegがインストールされていない、またはPathが通っていないため\nmp3など一部形式に対応していません", "警告", wx.ICON_EXCLAMATION)

    # Handlers for MyFrame1 events.
    def m_button11OnButtonClick( self, event ):
        # TODO: Implement m_button11OnButtonClick
        dlg = wx.DirDialog(self, message="保存先ディレクトリ")
        if dlg.ShowModal() == wx.ID_OK:
            self.m_textCtrl16.SetValue(dlg.GetPath())

    def m_button8OnButtonClick( self, event ):
        # TODO: Implement m_button8OnButtonClick
        dlg = wx.FileDialog(self, message="音声ファイル")
        if dlg.ShowModal() == wx.ID_OK:
            self.m_textCtrl14.SetValue(dlg.GetPath())

    def m_button9OnButtonClick( self, event ):
        # TODO: Implement m_button9OnButtonClick
        dlg = wx.FileDialog(self, message="背景画像")
        if dlg.ShowModal() == wx.ID_OK:
            self.m_textCtrl15.SetValue(dlg.GetPath())

    def m_slider1OnSlider( self, event ):
        n = self.m_slider1.GetValue()
        self.m_textCtrl4.SetValue(str(n / 100))
        self.show_preview(event)

    def m_textCtrl4OnText( self, event ):
        n = self.m_textCtrl4.GetValue()
        try:
            self.m_slider1.SetValue(int(float(n) * 100))
            self.show_preview(event)
        except:
            self.m_textCtrl4.SetValue(str(self.m_slider1.GetValue() / 100))

    def m_button10OnButtonClick( self, event ):
        # TODO: Implement m_button10OnButtonClick
        dlg = wx.ProgressDialog(title="CMV", message="読み込み中...", style=wx.PD_APP_MODAL | wx.PD_ESTIMATED_TIME | wx.PD_REMAINING_TIME)
        dlg.Show()
        save_path = self.m_textCtrl16.GetValue()
        if not save_path:
            self.m_staticText13.SetLabel("保存先が指定されていません")
            dlg.Close()
            self.Refresh()
            return
        if os.path.isdir(save_path):
            save_filename = os.path.join(save_path, "video.mp4")
        elif not os.path.isdir(os.path.dirname(save_path)):
            os.makedirs(os.path.dirname(save_path))
            save_filename = save_path
        elif not save_path.rstrip(".mp4"):
            save_filename = save_path + ".mp4"
        else:
            save_filename = save_path
        audio_file = self.m_textCtrl14.GetValue()
        if not os.path.isfile(audio_file):
            self.m_staticText13.SetLabel("音声ファイルが指定されていないかファイルが\n存在しません")
            dlg.Close()
            self.Refresh()
            return
        try:
            audio = AudioSegment.from_file(audio_file)
            sample = np.array_split(np.array(audio.get_array_of_samples())[::audio.channels], int(FPS * audio.duration_seconds))
            length = len(sample)
        except:
            self.m_staticText13.SetLabel("この音声形式に対応していません。拡張子等を\n見直してください")
            dlg.Close()
            self.Refresh()
            return
        image_file = self.m_textCtrl15.GetValue()
        try:
            img = cv2.resize(cv2.imread(image_file), (WIDTH, HEIGHT))
        except:
            img = np.full((HEIGHT, WIDTH, 3), 0, dtype=np.uint8)
        beta = self.m_slider1.GetValue()
        image = cv2.convertScaleAbs(img, beta=beta)
        self.m_staticText13.SetLabel("")
        draw = self.shapes[self.m_choice2.GetSelection()]
        color = self.colors[self.m_choice3.GetSelection()]
        fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
        print(save_filename)
        with tempfile.TemporaryDirectory() as temp:
            temp_video = os.path.join(temp, ".mp4")
            video = cv2.VideoWriter(temp_video, fourcc, FPS, (WIDTH, HEIGHT))
            sampling_data = np.zeros(SAMPLING_SIZE)
            for n, s in enumerate(sample, start=1):
                draw_image = image.copy()
                sampling_data = np.concatenate([sampling_data, np.frombuffer(s.copy(order="C"), dtype="int16") / INT16_MAX])
                if sampling_data.shape[0] > SAMPLING_SIZE:
                    sampling_data = sampling_data[-SAMPLING_SIZE:]
                fft = np.abs(np.fft.fft(sampling_data))
                spectram_data = np.dot(spectram_array, fft)
                for index, value in enumerate(spectram_data):
                    draw(index, value, draw_image, spectram_data, color)
                video.write(draw_image)
                progress = round(n / length * 100)
                dlg.Update(99 if 100 <= progress else progress, newmsg=f"オーディオスペクトラムを作成中...  {n}/{length}")
            video.release()
            dlg.Update(99, newmsg=f"音声を結合中...")
            clip = mp.VideoFileClip(temp_video)
            mv = clip.set_audio(mp.AudioFileClip(audio_file))
            mv.write_videofile(save_filename)
        dlg.Update(100, newmsg=f"処理が完了しました")
            
    def show_preview( self, event ):
        path = self.m_textCtrl15.GetValue()
        if os.path.isfile(path):
            draw = self.shapes[self.m_choice2.GetSelection()]
            color = self.colors[self.m_choice3.GetSelection()]
            beta = self.m_slider1.GetValue()
            image = cv2.convertScaleAbs(cv2.imread(path), beta=beta)
            for i, v in enumerate(preview_data):
                draw(i, v, image, preview_data, color, preview=True)
            buf = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            bmp = wx.Bitmap.FromBuffer(image.shape[1], image.shape[0], buf)
            self.m_bitmap2.SetBitmap(bmp)

def draw_horizon(i, v, img, s, c, preview=False):
    h = 450 if preview else HEIGHT
    cv2.rectangle(img, (int(part_w * i + 1), h), (int(part_w * (i + 1) - 1), int(max(h - v/(1 if preview else 8), 0))), c, thickness=-1)

def draw_circle(i, v, img, s, c, preview=False):
    w = 600 if preview else WIDTH
    h = 450 if preview else HEIGHT
    rad = (2 * np.pi) * (i / len(s))
    x1 = int(w / 2 + np.sin(rad) * 80)
    y1 = int(h / 2 - np.cos(rad) * 80)
    rad = (2 * np.pi) * (i / len(s))
    x2 = int(w / 2 + np.sin(rad) * (80 + v/16))
    y2 = int(h / 2 - np.cos(rad) * (80 + v/16))
    cv2.line(img, (x1, y1), (x2, y2), c, thickness=2)
