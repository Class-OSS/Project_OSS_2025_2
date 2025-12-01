import tkinter as tk
import re

# 한글 숫자(단/복합) → 정수 변환 유틸리티
# 간단한 규칙으로 '이십삼', '백이십오' 형태까지 처리 (천 단위 이하)
KOR_DIGITS = {
    '영':0,'공':0,'일':1,'이':2,'삼':3,'사':4,'오':5,'육':6,'칠':7,'팔':8,'구':9
}
KOR_UNITS = {
    '십':10,
    '백':100,
    '천':1000,
    '만':10000
}

def kor_number_to_int(s: str):
    """
    아주 복잡한 한국어 숫자 모두를 지원하지는 않지만,
    '이', '십', '이십', '이십삼', '백이십삼', '천이백삼십사' 같은 표현을 합리적으로 변환함.
    실패 시 None 리턴.
    """
    if not s:
        return None
    # 완전히 숫자로 이미 되어있다면
    if s.isdigit():
        return int(s)

    total = 0
    num = 0
    i = 0
    length = len(s)
    while i < length:
        ch = s[i]
        if ch in KOR_DIGITS:
            num = KOR_DIGITS[ch]
            i += 1
            # 다음 글자가 '십','백' 같은 단위면 처리
            if i < length and s[i] in KOR_UNITS:
                unit = KOR_UNITS[s[i]]
                total += num * unit
                num = 0
                i += 1
            else:
                # 단위 없으면 임시로 보관 (일의 자리 가능)
                # 다음 반복에서 합쳐질 수도 있음
                total += num
                num = 0
        elif ch in KOR_UNITS:
            # 예: "십" 단독으로 나오면 10
            unit = KOR_UNITS[ch]
            if total == 0:
                total = 1 * unit
            else:
                total = total * unit
            i += 1
        else:
            # 알 수 없는 문자
            return None
    return total

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("AI 계산기")
        self.root.geometry("320x460")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 구성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['AI', '=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

        # 키보드 엔터 처리 (입력창에서 엔터 = 계산)
        self.entry.bind('<Return>', lambda event: self.on_click('='))

    def natural_to_expression(self, text):
        """
        입력창의 텍스트(띄어쓰기 있어도, 없어도) -> 기계식 수식
        처리 순서:
         1) 연산자 단어를 우선 치환 (더하기/빼기/곱하기/나누기 등)
         2) 문자 스트림을 스캔하면서 한글 숫자 토큰(단/복합) -> 아라비아 숫자로 변환
         3) 그 외는 그대로 (숫자, 기호 유지)
        """
        if text is None:
            return ""

        s = text.strip()

        # 1) 연산자 단어 먼저 치환 (붙어 있어도 replace로 처리)
        # 여러 표현을 고려
        op_map = {
            '더하기': '+', '더함': '+', '플러스': '+', 'plus': '+',
            '빼기': '-', '빼다': '-', '마이너스': '-', 'minus': '-',
            '곱하기': '*', '곱함': '*', '곱': '*', 'x': '*', 'X': '*', 'times':'*',
            '나누기': '/', '나눔': '/', '나누다': '/', 'divide':'/'
        }
        # 소문자/대문자 혼합 처리
        tmp = s
        for k, v in op_map.items():
            tmp = tmp.replace(k, v)

        s = tmp

        # 2) 문자 스트림을 한 글자씩 보면서 숫자 토큰 구성
        i = 0
        out = ""
        while i < len(s):
            ch = s[i]

            # 아라비아 숫자/소수점/연산기호 그대로 통과
            if ch.isdigit() or ch in '+-*/(). ':
                out += ch
                i += 1
                continue

            # 영어 단어 숫자 (one, two 등) 간단 처리 (옵션)
            # (여기서는 건너뜀 — 필요하면 추가 가능)

            # 한글 숫자/단위 처리 시도: 최대 몇 글자 붙어있는 복합 숫자 찾기
            # 예: '이십삼' -> try longest match up to, say, 6글자
            matched = False
            max_lookahead = 6
            for L in range(max_lookahead, 0, -1):
                if i + L <= len(s):
                    chunk = s[i:i+L]
                    val = kor_number_to_int(chunk)
                    if val is not None:
                        out += str(val)
                        i += L
                        matched = True
                        break
            if matched:
                continue

            # 한글이지만 숫자 토큰으로 해석 불가하면 그냥 통과 (예: '삼겹살' -> '삼'은 숫자지만 함께 단어라면 kor_number_to_int 실패하므로 문자 그대로 추가)
            out += ch
            i += 1

        # 마지막: 연속된 한글(숫자 아닌) 남아있으면 제거하거나 남겨둠.
        # eval() 전에 안전하게 숫자/연산자/괄호/공백/점만 남기기 위해 필터링
        cleaned = []
        for ch in out:
            if ch.isdigit() or ch in '+-*/(). ':
                cleaned.append(ch)
            else:
                # 한글이나 알파벳이 남아있다면 안전하게 공백으로 대체
                cleaned.append(' ')
        final_expr = ''.join(cleaned)
        # 연속 공백을 단일 공백으로
        final_expr = re.sub(r'\s+', ' ', final_expr).strip()
        # 공백을 제거한 실제 수식(예: "1 + 2" -> "1+2")
        final_expr = final_expr.replace(' ', '')
        return final_expr

    def on_click(self, char):
        # 항상 entry의 최신 값을 읽어서 작업 (키보드 입력 지원)
        current_text = self.entry.get()

        if char == 'C':
            self.expression = ""
            self.entry.delete(0, tk.END)
            return

        elif char == 'AI':
            # entry에 있는 최신 문자열을 변환해서 다시 넣기
            converted = self.natural_to_expression(current_text)
            self.expression = converted
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)
            return

        elif char == '=':
            # 계산 시에도 entry 최신값으로 계산 (AI 변환이 필요한 경우 먼저 변환)
            expr_to_eval = current_text
            # 만약 한글이 포함되어 있으면 변환 시도
            if re.search(r'[가-힣]', expr_to_eval):
                expr_to_eval = self.natural_to_expression(expr_to_eval)

            try:
                # 안전을 위해 빈 문자열이면 에러 처리
                if expr_to_eval.strip() == "":
                    self.expression = ""
                else:
                    self.expression = str(eval(expr_to_eval))
            except Exception:
                self.expression = "에러"

            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)
            return

        else:
            # 버튼/숫자 클릭: 기존 entry에 문자 추가 (entry 기반으로 동작)
            new_text = current_text + str(char)
            self.expression = new_text
            self.entry.delete(0, tk.END)
            self.entry.insert(0, new_text)
            return

# 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
