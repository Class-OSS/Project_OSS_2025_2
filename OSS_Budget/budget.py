# budget.py
from expense import Expense
import datetime
import os
import shutil

class Budget:
    def __init__(self, filename="expenses.txt", auto_load=True):
        """
        filename: 기본 저장 파일명 (텍스트, TSV 형식)
        auto_load: True이면 객체 생성 시 파일이 존재하면 바로 불러온다.
        """
        self.expenses = []
        self.filename = filename
        if auto_load:
            self.load_from_file(self.filename, silent=True)

    def _sanitize_field(self, text):
        """파일에 안전하게 쓰기 위해 탭/줄바꿈을 공백으로 치환."""
        if text is None:
            return ""
        return str(text).replace("\t", " ").replace("\n", " ")

    def add_expense(self, category, description, amount, date=None):
        """지출 추가 후 자동 저장."""
        if date is None:
            date = datetime.date.today().isoformat()
        exp = Expense(date, category, description, amount)
        self.expenses.append(exp)
        print("지출이 추가되었습니다.\n")
        try:
            self.save_to_file()  # 자동 저장 (자동 백업 포함)
        except Exception as e:
            print(f"자동 저장 중 오류 발생: {e}\n")

    def list_expenses(self):
        """인덱스(1 기반)와 함께 목록 출력."""
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("---- 지출 목록 ----")
        for idx, exp in enumerate(self.expenses, start=1):
            print(f"{idx}. {exp}")
        print()

    def total_spent(self):
        total = sum(exp.amount for exp in self.expenses)
        print(f"총 지출: {total}원\n")
        return total

    def delete_expense(self, index):
        """1 기반 인덱스로 삭제하고 자동 저장."""
        if not isinstance(index, int):
            print("인덱스는 정수여야 합니다.\n")
            return False
        if index < 1 or index > len(self.expenses):
            print("잘못된 인덱스입니다.\n")
            return False
        removed = self.expenses.pop(index - 1)
        print(f"삭제되었습니다: {removed}\n")
        try:
            self.save_to_file()
        except Exception as e:
            print(f"자동 저장 중 오류 발생: {e}\n")
        return True

    def save_to_file(self, filename=None, create_backup=True):
        """
        현재 지출 목록을 TSV 형태로 저장.
        기본 파일명은 self.filename.
        각 라인: date \t category \t description \t amount
        create_backup: True이면 기존 파일을 덮어쓰기 전에 자동 백업을 생성.
        """
        if filename is None:
            filename = self.filename

        # 자동 백업(덮어쓰기 전에)
        if create_backup and os.path.exists(filename):
            try:
                self.create_backup(filename)
            except Exception as e:
                # 백업 실패 시 알림은 주지만 저장은 계속 시도
                print(f"자동 백업 생성 중 오류 발생: {e}")

        try:
            with open(filename, "w", encoding="utf-8") as f:
                for exp in self.expenses:
                    date = self._sanitize_field(exp.date)
                    cat = self._sanitize_field(exp.category)
                    desc = self._sanitize_field(exp.description)
                    amt = str(exp.amount)
                    f.write(f"{date}\t{cat}\t{desc}\t{amt}\n")
            print(f"파일로 저장되었습니다: {filename}\n")
        except Exception as e:
            raise e

    def load_from_file(self, filename=None, silent=False):
        """
        TSV 파일에서 불러오기.
        기본 파일명은 self.filename.
        기존 메모리 목록은 **덮어쓰기** 됩니다.
        silent=True이면 (프로그램 시작 자동 로드 시) 불필요한 메시지 출력을 억제합니다.
        """
        if filename is None:
            filename = self.filename
        if not os.path.exists(filename):
            if not silent:
                print(f"파일이 없습니다: {filename}\n")
            return False

        loaded = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for lineno, line in enumerate(f, start=1):
                    line = line.rstrip("\n")
                    if not line:
                        continue
                    parts = line.split("\t")
                    if len(parts) < 4:
                        print(f"잘못된 형식(라인 {lineno})을 건너뜁니다: {line}")
                        continue
                    # 안전하게 description 재구성 (탭이 포함되어 있으면 마지막이 금액)
                    if len(parts) == 4:
                        date = parts[0]
                        category = parts[1]
                        description = parts[2]
                        amount_str = parts[3]
                    else:
                        date = parts[0]
                        category = parts[1]
                        description = "\t".join(parts[2:-1])
                        amount_str = parts[-1]
                    try:
                        amount = int(amount_str)
                    except ValueError:
                        print(f"금액 변환 오류(라인 {lineno})를 건너뜁니다: {amount_str}")
                        continue
                    loaded.append(Expense(date, category, description, amount))
        except Exception as e:
            if not silent:
                print(f"파일 읽기 중 오류 발생: {e}\n")
            return False

        self.expenses = loaded
        if not silent:
            print(f"{len(self.expenses)}개의 항목을 불러왔습니다: {filename}\n")
        return True

    def get_expenses_sorted_by_date(self, reverse=True):
        """
        날짜(ISO: YYYY-MM-DD)를 기준으로 정렬된 새 리스트를 반환.
        reverse=True이면 최신순(내림차순). False면 오래된순(오름차순).
        날짜 파싱에 실패하면 문자열 비교로 정렬.
        """
        def key_fn(exp):
            try:
                return datetime.date.fromisoformat(exp.date)
            except Exception:
                return exp.date  # fallback to string
        return sorted(self.expenses, key=key_fn, reverse=reverse)

    def list_expenses_sorted(self, reverse=True):
        """정렬된 목록을 출력. reverse=True -> 최신순."""
        sorted_list = self.get_expenses_sorted_by_date(reverse=reverse)
        if not sorted_list:
            print("지출 내역이 없습니다.\n")
            return
        order = "최신순" if reverse else "오래된순"
        print(f"---- 날짜별 정렬({order}) ----")
        for idx, exp in enumerate(sorted_list, start=1):
            print(f"{idx}. {exp}")
        print()

    def category_summary(self):
        """
        카테고리별 요약을 계산하여 출력 및 딕셔너리 반환.
        반환 형식: {category: {'count': n, 'total': sum_amount}, ...}
        """
        summary = {}
        for exp in self.expenses:
            cat = exp.category if exp.category is not None else "미분류"
            if cat not in summary:
                summary[cat] = {'count': 0, 'total': 0}
            summary[cat]['count'] += 1
            summary[cat]['total'] += exp.amount

        # 출력
        if not summary:
            print("지출 내역이 없습니다.\n")
            return summary

        print("---- 카테고리별 요약 ----")
        total_all = 0
        for cat, info in sorted(summary.items(), key=lambda x: x[0]):
            print(f"{cat}: 항목수={info['count']}, 합계={info['total']}원")
            total_all += info['total']
        print(f"전체 합계: {total_all}원\n")
        return summary

    def create_backup(self, filename=None):
        """
        filename의 현재 파일을 같은 디렉터리에 백업으로 복사한다.
        백업 파일명: <filename>.bak.YYYYMMDD_HHMMSS.txt
        만약 filename이 존재하지 않으면, 현재 메모리(self.expenses)를 backup 파일로 생성한다.
        반환값: 생성된 백업 파일명
        """
        if filename is None:
            filename = self.filename

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        base, ext = os.path.splitext(filename)
        # backup name: base.bak.YYYYMMDD_HHMMSS.ext (keep extension)
        bak_name = f"{base}.bak.{timestamp}{ext if ext else '.txt'}"

        if os.path.exists(filename):
            shutil.copyfile(filename, bak_name)
            print(f"백업을 생성했습니다: {bak_name}\n")
            return bak_name
        else:
            # 파일이 없으면 현재 메모리 내용을 새 파일로 저장
            try:
                # save_to_file would try to backup again; disable create_backup here
                with open(bak_name, "w", encoding="utf-8") as f:
                    for exp in self.expenses:
                        date = self._sanitize_field(exp.date)
                        cat = self._sanitize_field(exp.category)
                        desc = self._sanitize_field(exp.description)
                        amt = str(exp.amount)
                        f.write(f"{date}\t{cat}\t{desc}\t{amt}\n")
                print(f"메모리 내용을 백업 파일로 저장했습니다: {bak_name}\n")
                return bak_name
            except Exception as e:
                raise e
