import tkinter as tk
from tkinter import messagebox
import turtle
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("600x650") 

        self.expression = ""

        
        top_frame = tk.Frame(root)
        top_frame.pack(side="top", fill="x", padx=10, pady=10)

        
        self.entry = tk.Entry(top_frame, font=("Arial", 20), justify="right")
        self.entry.pack(fill="x", ipadx=8, ipady=10, pady=(0, 10))

        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['x', '(', ')', '**', '='] 
        ]

        btn_frame = tk.Frame(top_frame)
        btn_frame.pack(fill="x")

        for row in buttons:
            row_f = tk.Frame(btn_frame)
            row_f.pack(expand=True, fill="both")
            for char in row:
                
                bg_color = "SystemButtonFace"
                if char == 'x':
                    bg_color = "#FFD700"
                elif char == '=':
                    bg_color = "#90EE90"

                btn = tk.Button(
                    row_f, text=char, font=("Arial", 12), bg=bg_color,
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both", padx=1, pady=1)

        
        draw_btn = tk.Button(top_frame, text="계산 / 그래프 (Enter)", bg="lightblue", 
                             command=self.process_input)
        draw_btn.pack(fill="x", pady=5)
        
        
        self.root.bind('<Return>', lambda event: self.process_input())

        
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)

        self.screen_t = turtle.TurtleScreen(self.canvas)
        self.screen_t.bgcolor("white")
        self.t = turtle.RawTurtle(self.screen_t)
        self.t.speed(0)
        self.t.hideturtle()
        
        self.draw_axes()

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.draw_axes()
        elif char == '=':
            self.process_input()
            return
        else:
            self.expression += str(char)
        
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def process_input(self):
        """입력값을 분석해서 계산을 할지 그래프를 그릴지 결정"""
        expr = self.entry.get()
        if not expr: return

        
        if 'x' in expr:
            self.draw_graph(expr)
        else:
            self.calculate_number(expr)

    def calculate_number(self, expr):
        """일반 숫자 계산 함수"""
        try:
            
            context = {"sin":math.sin, "cos":math.cos, "tan":math.tan, "log":math.log, "e":math.e, "pi":math.pi}
            
            
            result = eval(expr, {}, context)
            
            
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            
            
            self.expression = str(result)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
            
            
            self.draw_axes()
            
        except Exception as e:
            self.expression = ""
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def draw_axes(self):
        self.t.clear()
        self.t.width(1)
        self.t.color("black")
        
        # X축
        self.t.penup(); self.t.goto(-300, 0); self.t.pendown(); self.t.goto(300, 0)
        # Y축
        self.t.penup(); self.t.goto(0, -300); self.t.pendown(); self.t.goto(0, 300)
        
        self.t.penup(); self.t.home()

    def draw_graph(self, expr):
        """그래프 그리기 함수"""
        
        
        context = {"x":0, "sin":math.sin, "cos":math.cos, "tan":math.tan, "log":math.log, "e":math.e, "pi":math.pi}
        try:
            eval(expr, {}, context)
        except Exception as e:
            messagebox.showerror("수식 오류", f"수식이 올바르지 않습니다.\n({e})\n\n[팁] 2x 대신 2*x를 사용하세요.")
            return

        self.draw_axes()
        self.t.color("red")
        self.t.width(2)
        
        scale = 20
        step = 0.1
        
        x = -15
        first = True
        
        while x <= 15:
            context["x"] = x
            try:
                y = eval(expr, {}, context)
                sx, sy = x * scale, y * scale
                
                if abs(sy) > 300:
                    self.t.penup()
                    first = True
                else:
                    if first:
                        self.t.penup()
                        self.t.goto(sx, sy)
                        self.t.pendown()
                        first = False
                    else:
                        self.t.goto(sx, sy)
            except:
                self.t.penup()
                first = True
            
            x += step
