import tkinter as tk
from tkinter import ttk
import math

THEME = {
    "bg": "#0B0F17",
    "panel": "#141C2B",
    "panel_border": "#233148",
    "fg": "#F1F5F9",
    "sub_fg": "#94A3B8",
    "accent_cyan": "#00F2FE",
    "accent_blue": "#4FACFE",
    "accent_green": "#10B981",
    "accent_purple": "#8B5CF6",
    "entry_bg": "#1C273C",
    "entry_border": "#2E3F5E",
    "card_kpi": "#182236"
}

class UltraDrywallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drywall Master Pro 4.0 — Ultimate UI/UX")
        self.root.geometry("1180x800")
        self.root.minsize(1050, 720)
        self.root.configure(bg=THEME["bg"])

        self.room_length = tk.StringVar(value="5.0")
        self.room_width = tk.StringVar(value="4.0")
        self.room_height = tk.StringVar(value="2.7")
        self.exclude_doors = tk.StringVar(value="3.5")

        self.sheet_L = tk.StringVar(value="1.5")
        self.sheet_W = tk.StringVar(value="0.6")
        self.waste_pct = tk.StringVar(value="10")
        self.price_per_sheet = tk.StringVar(value="9.50")

        self.build_ui()
        self.calculate()

    def build_ui(self):
        header = tk.Frame(self.root, bg=THEME["panel"], padx=30, pady=18, highlightbackground=THEME["panel_border"], highlightthickness=1)
        header.pack(fill="x")

        title_box = tk.Frame(header, bg=THEME["panel"])
        title_box.pack(side="left")

        logo_lbl = tk.Label(title_box, text="🚀 DRYWALL MASTER", font=("Segoe UI", 18, "bold"), fg=THEME["fg"], bg=THEME["panel"])
        logo_lbl.pack(side="left")

        badge = tk.Label(title_box, text=" PRO 4.0 ", font=("Segoe UI", 9, "bold"), fg=THEME["bg"], bg=THEME["accent_cyan"], padx=6, pady=2)
        badge.pack(side="left", padx=(10, 0))

        sub_title = tk.Label(header, text="Экспресс-расчет малоформатного ГКЛ & Смета", font=("Segoe UI", 10), fg=THEME["sub_fg"], bg=THEME["panel"])
        sub_title.pack(side="right")

        workspace = tk.Frame(self.root, bg=THEME["bg"], padx=25, pady=25)
        workspace.pack(fill="both", expand=True)

        left_panel = tk.Frame(workspace, bg=THEME["panel"], padx=22, pady=22, highlightbackground=THEME["panel_border"], highlightthickness=1)
        left_panel.pack(side="left", fill="y", padx=(0, 22))

        sec1 = tk.Label(left_panel, text="📐 ГЕОМЕТРИЯ ПОМЕЩЕНИЯ", font=("Segoe UI", 11, "bold"), fg=THEME["accent_cyan"], bg=THEME["panel"])
        sec1.pack(anchor="w", pady=(0, 12))

        self._create_input_field(left_panel, "Длина комнаты", self.room_length, "м")
        self._create_input_field(left_panel, "Ширина комнаты", self.room_width, "м")
        self._create_input_field(left_panel, "Высота потолков", self.room_height, "м")
        self._create_input_field(left_panel, "Вычесть проемы (окна/двери)", self.exclude_doors, "м²")

        divider = tk.Frame(left_panel, height=1, bg=THEME["panel_border"])
        divider.pack(fill="x", pady=18)

        sec2 = tk.Label(left_panel, text="📦 ПАРАМЕТРЫ ПЛИТЫ И ЦЕНА", font=("Segoe UI", 11, "bold"), fg=THEME["accent_cyan"], bg=THEME["panel"])
        sec2.pack(anchor="w", pady=(0, 12))

        self._create_input_field(left_panel, "Длина листа ГКЛ", self.sheet_L, "м")
        self._create_input_field(left_panel, "Ширина листа ГКЛ", self.sheet_W, "м")
        self._create_input_field(left_panel, "Запас на обрезку", self.waste_pct, "%")
        self._create_input_field(left_panel, "Стоимость 1 листа", self.price_per_sheet, "BYN")

        right_panel = tk.Frame(workspace, bg=THEME["bg"])
        right_panel.pack(side="right", fill="both", expand=True)

        kpi_grid = tk.Frame(right_panel, bg=THEME["bg"])
        kpi_grid.pack(fill="x", pady=(0, 20))

        self.kpi_area = self._build_kpi_card(kpi_grid, "ПЛОЩАДЬ СТЕН", "0 м²", "Чистая оклейка", THEME["accent_cyan"], 0)
        self.kpi_sheets = self._build_kpi_card(kpi_grid, "ЛИСТОВ К ЗАКУПКЕ", "0 шт.", "С учетом запаса", THEME["accent_purple"], 1)
        self.kpi_cost = self._build_kpi_card(kpi_grid, "СУММА (ТОЛЬКО ГКЛ)", "0 BYN", "Ориентировочно", THEME["accent_green"], 2)

        detail_card = tk.Frame(right_panel, bg=THEME["panel"], padx=25, pady=25, highlightbackground=THEME["panel_border"], highlightthickness=1)
        detail_card.pack(fill="both", expand=True)

        tk.Label(detail_card, text="⚡ ПОЛНАЯ ВЕДОМОСТЬ МАТЕРИАЛОВ И КРЕПЕЖА", font=("Segoe UI", 12, "bold"), fg=THEME["fg"], bg=THEME["panel"]).pack(anchor="w", pady=(0, 15))

        self.summary_box = tk.Text(
            detail_card, font=("Consolas", 11), bg=THEME["entry_bg"], fg=THEME["fg"],
            relief="flat", highlightbackground=THEME["entry_border"], highlightthickness=1, padx=15, pady=15
        )
        self.summary_box.pack(fill="both", expand=True)

    def _create_input_field(self, parent, label_text, var, unit):
        box = tk.Frame(parent, bg=THEME["panel"])
        box.pack(fill="x", pady=6)

        tk.Label(box, text=label_text, font=("Segoe UI", 9), fg=THEME["sub_fg"], bg=THEME["panel"]).pack(anchor="w", pady=(0, 3))

        field = tk.Frame(box, bg=THEME["entry_bg"], highlightbackground=THEME["entry_border"], highlightthickness=1)
        field.pack(fill="x")

        entry = tk.Entry(field, textvariable=var, font=("Segoe UI", 11, "bold"), bg=THEME["entry_bg"], fg=THEME["fg"], insertbackground=THEME["accent_cyan"], relief="flat")
        entry.pack(side="left", fill="x", expand=True, padx=10, pady=7)
        entry.bind("<KeyRelease>", lambda e: self.calculate())

        tk.Label(field, text=unit, font=("Segoe UI", 9, "bold"), fg=THEME["accent_cyan"], bg=THEME["entry_bg"]).pack(side="right", padx=10)

    def _build_kpi_card(self, parent, title, val, sub, accent_color, col):
        card = tk.Frame(parent, bg=THEME["card_kpi"], padx=20, pady=18, highlightbackground=accent_color, highlightthickness=1)
        card.grid(row=0, column=col, sticky="ew", padx=(0 if col==0 else 12, 0))
        parent.columnconfigure(col, weight=1)

        tk.Label(card, text=title, font=("Segoe UI", 8, "bold"), fg=THEME["sub_fg"], bg=THEME["card_kpi"]).pack(anchor="w")
        val_lbl = tk.Label(card, text=val, font=("Segoe UI", 18, "bold"), fg=accent_color, bg=THEME["card_kpi"])
        val_lbl.pack(anchor="w", pady=(6, 2))
        tk.Label(card, text=sub, font=("Segoe UI", 8), fg=THEME["sub_fg"], bg=THEME["card_kpi"]).pack(anchor="w")

        return val_lbl

    def _safe_float(self, var, default=0.0):
        try:
            val = str(var.get()).strip().replace(",", ".")
            return float(val) if val else default
        except ValueError:
            return default

    def calculate(self):
        L = self._safe_float(self.room_length, 0)
        W = self._safe_float(self.room_width, 0)
        H = self._safe_float(self.room_height, 0)
        doors = self._safe_float(self.exclude_doors, 0)

        s_L = self._safe_float(self.sheet_L, 1.5)
        s_W = self._safe_float(self.sheet_W, 0.6)
        waste = self._safe_float(self.waste_pct, 10) / 100.0
        price = self._safe_float(self.price_per_sheet, 0)

        perimeter = 2 * (L + W)
        gross_area = perimeter * H
        net_area = max(0, gross_area - doors)

        sheet_area = s_L * s_W
        if sheet_area <= 0: sheet_area = 0.9

        sheets_needed = math.ceil((net_area / sheet_area) * (1.0 + waste))
        total_cost = sheets_needed * price

        screws = sheets_needed * 22
        dowels = math.ceil(perimeter * 2.5)

        self.kpi_area.config(text=f"{net_area:.2f} м²")
        self.kpi_sheets.config(text=f"{sheets_needed} шт.")
        self.kpi_cost.config(text=f"{total_cost:,.2f} BYN".replace(",", " "))

        report = f"""========================================================================
📌 1. ОБЩИЕ ПАРАМЕТРЫ ОБЪЕКТА
------------------------------------------------------------------------
• Периметр стен помещения:       {perimeter:.2f} м
• Общая площадь (без проемов):   {gross_area:.2f} м²
• Вычтенная площадь проемов:     {doors:.2f} м²
• ИТОГОВАЯ ПЛОЩАДЬ ОБЛИЦОВКИ:     {net_area:.2f} м²

📦 2. РАСЧЕТ МАЛОФОРМАТНОГО ГКЛ ({s_L}m x {s_W}m)
------------------------------------------------------------------------
• Площадь 1 листа:               {sheet_area:.2f} м²
• Учтенный запас на подрезку:     {int(waste*100)}%
• НЕОБХОДИМОЕ КОЛИЧЕСТВО:         {sheets_needed} шт. (листов)
• СТОИМОСТЬ МАТЕРИАЛА:           {total_cost:,.2f} BYN

🛠️ 3. РАСХОДНЫЕ МАТЕРИАЛЫ И КРЕПЕЖ (РАСЧЕТНЫЙ)
------------------------------------------------------------------------
• Саморезы по ГКЛ (3.5х25 мм):   ~{int(screws)} шт.
• Дюбель-гвозди (6х40 мм):        ~{int(dowels)} шт.
========================================================================
💡 ПРЕИМУЩЕСТВА ИСПОЛЬЗОВАНИЯ МАЛОФОРМАТНОГО ГКЛ:
  - Легко перевозится в багажнике обычного легкового авто
  - Монтируется в одиночку без использования подъемников
"""
        self.summary_box.delete("1.0", tk.END)
        self.summary_box.insert(tk.END, report)

if __name__ == "__main__":
    root = tk.Tk()
    app = UltraDrywallApp(root)
    root.mainloop()
