import tkinter as tk
import winsound

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x500")

        self.expression = ""

        # 버튼 소리 설정
        self.sound_on = True
        self.sound_index = 0  # 0~2, 3가지 효과음
        self.volume_level = 1  # 1~3
        # 예시로 간단한 winsound.Beep 사용, 실제 파일도 가능
        self.sounds = [
            (440, 100),  # 효과음1: 440Hz, 0.1초
            (550, 100),  # 효과음2
            (660, 100),  # 효과음3
        ]

        self.buttons_widgets = []

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 설정 버튼 프레임
        settings_frame = tk.Frame(root)
        settings_frame.pack(fill="x", padx=10, pady=5)

        # 1. 소리 ON/OFF 버튼
        self.sound_btn = tk.Button(settings_frame, text="🔊 ON", command=self.toggle_sound)
        self.sound_btn.pack(side="left", expand=True, fill="both")
        self.buttons_widgets.append(self.sound_btn)

        # 2. 효과음 변경 버튼
        self.effect_btn = tk.Button(settings_frame, text="효과음 1", command=self.change_effect)
        self.effect_btn.pack(side="left", expand=True, fill="both")
        self.buttons_widgets.append(self.effect_btn)

        # 3. 볼륨 버튼
        self.volume_btn = tk.Button(settings_frame, text="볼륨 1", command=self.change_volume)
        self.volume_btn.pack(side="left", expand=True, fill="both")
        self.buttons_widgets.append(self.volume_btn)

        # 계산기 버튼
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(frame, text=char, font=("Arial", 18),
                                command=lambda ch=char: self.on_click(ch))
                btn.pack(side="left", expand=True, fill="both")
                self.buttons_widgets.append(btn)

    # 버튼 소리 함수
    def play_sound(self):
        if self.sound_on:
            freq, dur = self.sounds[self.sound_index]
            # 볼륨은 단순히 길이로 표현
            winsound.Beep(freq, dur * self.volume_level)

    def toggle_sound(self):
        self.sound_on = not self.sound_on
        self.sound_btn.config(text="🔊 ON" if self.sound_on else "🔇")
        self.play_sound()

    def change_effect(self):
        self.sound_index = (self.sound_index + 1) % len(self.sounds)
        self.effect_btn.config(text=f"효과음 {self.sound_index + 1}")
        self.play_sound()

    def change_volume(self):
        self.volume_level = self.volume_level % 3 + 1  # 1→2→3→1
        self.volume_btn.config(text=f"볼륨 {self.volume_level}")
        self.play_sound()

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
        self.play_sound()


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
