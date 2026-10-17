import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv

try:
    import matplotlib
    matplotlib.use("TkAgg")
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

THEMES = {
    "dark_fintech": {
        "name": "⚡ Тёмный Fintech",
        "bg": "#090d16", "panel_bg": "#111827", "panel_fg": "#f3f4f6",
        "accent": "#00f2fe", "accent_btn": "#2563eb", "entry_bg": "#1f2937",
        "entry_fg": "#ffffff", "card_bg": "#111827", "card_fg": "#f3f4f6",
        "card_title": "#9ca3af", "tree_bg": "#111827", "tree_fg": "#f3f4f6",
        "tree_head": "#1f2937", "select": "#2563eb"
    },
    "clean_saas": {
        "name": "🍏 Чистый Minimal",
        "bg": "#f8fafc", "panel_bg": "#ffffff", "panel_fg": "#0f172a",
        "accent": "#2563eb", "accent_btn": "#2563eb", "entry_bg": "#f1f5f9",
        "entry_fg": "#0f172a", "card_bg": "#ffffff", "card_fg": "#0f172a",
        "card_title": "#64748b", "tree_bg": "#ffffff", "tree_fg": "#0f172a",
        "tree_head": "#e2e8f0", "select": "#3b82f6"
    },
    "corporate": {
        "name": "🏛️ Банковский",
        "bg": "#0f172a", "panel_bg": "#1e3a8a", "panel_fg": "#ffffff",
        "accent": "#fbbf24", "accent_btn": "#d97706", "entry_bg": "#1e40af",
        "entry_fg": "#ffffff", "card_bg": "#1e3a8a", "card_fg": "#ffffff",
        "card_title": "#93c5fd", "tree_bg": "#ffffff", "tree_fg": "#1e293b",
        "tree_head": "#1e3a8a", "select": "#d97706"
    }
}

class BelgeeLoanCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BELGEE X80 — Финансовая экосистема (Ultimate Pro 4.0)")
        self.root.geometry("1450x900")

        self.current_theme_key = "dark_fintech"
        self.t = THEMES[self.current_theme_key]

        self.car_price = tk.StringVar(value="86900")
        self.down_payment_pct = tk.StringVar(value="40")
        self.custom_loan_amount = tk.StringVar(value="")
        self.term_months = tk.StringVar(value="120")
        self.promo_rate = tk.StringVar(value="5.0")
        self.promo_months = tk.StringVar(value="36")
        self.base_rate = tk.StringVar(value="15.75")
        
        self.calc_mode = tk.StringVar(value="differentiated")
        self.custom_payment = tk.StringVar(value="960")
        
        self.extra_payment = tk.StringVar(value="0")
        self.extra_month = tk.StringVar(value="12")

        self.build_ui()
        self.calculate()

    def apply_theme(self, theme_key):
        self.current_theme_key = theme_key
        self.t = THEMES[theme_key]
        for widget in self.root.winfo_children():
            widget.destroy()
        self.build_ui()
        self.calculate()

    def build_ui(self):
        self.root.configure(bg=self.t["bg"])
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background=self.t["tree_bg"], foreground=self.t["tree_fg"], rowheight=26, fieldbackground=self.t["tree_bg"], font=("Segoe UI", 9))
        style.configure("Treeview.Heading", background=self.t["tree_head"], foreground=self.t["panel_fg"] if self.current_theme_key != "corporate" else "#ffffff", font=("Segoe UI", 9, "bold"))
        style.map("Treeview", background=[("selected", self.t["select"])])

        header_frame = tk.Frame(self.root, bg=self.t["panel_bg"], padx=20, pady=15)
        header_frame.pack(fill="x")
        
        tk.Label(header_frame, text="🚗 BELGEE X80 — Ultimate Financial Planner", font=("Segoe UI", 16, "bold"), fg=self.t["panel_fg"], bg=self.t["panel_bg"]).pack(side="left")

        theme_switcher = tk.Frame(header_frame, bg=self.t["panel_bg"])
        theme_switcher.pack(side="right")
        tk.Label(theme_switcher, text="Стиль:", font=("Segoe UI", 9, "bold"), fg=self.t["accent"], bg=self.t["panel_bg"]).pack(side="left", padx=(0, 6))

        for key, val in THEMES.items():
            tk.Button(
                theme_switcher, text=val["name"], font=("Segoe UI", 9, "bold"),
                bg=self.t["accent_btn"] if key == self.current_theme_key else self.t["entry_bg"],
                fg="white", relief="flat", padx=8, pady=3,
                command=lambda k=key: self.apply_theme(k), cursor="hand2"
            ).pack(side="left", padx=2)

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=15, pady=15)

        self.tab_calc = tk.Frame(notebook, bg=self.t["bg"])
        self.tab_chart = tk.Frame(notebook, bg=self.t["bg"])
        self.tab_compare = tk.Frame(notebook, bg=self.t["bg"])

        notebook.add(self.tab_calc, text=" 📊 Калькулятор и График ")
        notebook.add(self.tab_chart, text=" 📈 Аналитика и Тренд долга ")
        notebook.add(self.tab_compare, text=" ⚖️ Сравнение сценариев ")

        self.build_calc_tab()
        self.build_chart_tab()
        self.build_compare_tab()

    def build_calc_tab(self):
        main_container = tk.Frame(self.tab_calc, bg=self.t["bg"])
        main_container.pack(fill="both", expand=True, padx=10, pady=10)

        left_panel = tk.Frame(main_container, bg=self.t["panel_bg"], padx=15, pady=15)
        left_panel.pack(side="left", fill="y", padx=(0, 10))

        tk.Label(left_panel, text="Параметры кредита", font=("Segoe UI", 11, "bold"), fg=self.t["accent"], bg=self.t["panel_bg"]).pack(anchor="w", pady=(0, 10))

        def add_input(parent, label_text, var):
            f = tk.Frame(parent, bg=self.t["panel_bg"])
            f.pack(fill="x", pady=4)
            tk.Label(f, text=label_text, font=("Segoe UI", 9), fg=self.t["panel_fg"], bg=self.t["panel_bg"]).pack(side="left")
            entry = tk.Entry(f, textvariable=var, font=("Segoe UI", 10, "bold"), width=10, justify="right", bg=self.t["entry_bg"], fg=self.t["entry_fg"], insertbackground="white", relief="flat")
            entry.pack(side="right")
            entry.bind("<KeyRelease>", lambda e: self.calculate())

        add_input(left_panel, "Стоимость авто (BYN):", self.car_price)
        add_input(left_panel, "Первоначальный взнос (%):", self.down_payment_pct)
        add_input(left_panel, "Сумма кредита (любая):", self.custom_loan_amount)
        add_input(left_panel, "Срок по плану (мес.):", self.term_months)
        add_input(left_panel, "Льготная ставка (%):", self.promo_rate)
        add_input(left_panel, "Период льготы (мес.):", self.promo_months)
        add_input(left_panel, "Базовая ставка (%):", self.base_rate)

        sep = tk.Frame(left_panel, height=1, bg=self.t["accent"])
        sep.pack(fill="x", pady=10)

        tk.Label(left_panel, text="Досрочный платеж (разовый)", font=("Segoe UI", 10, "bold"), fg=self.t["accent"], bg=self.t["panel_bg"]).pack(anchor="w", pady=(0, 4))
        add_input(left_panel, "Сумма досрочки (BYN):", self.extra_payment)
        add_input(left_panel, "Внести в месяц №:", self.extra_month)

        sep2 = tk.Frame(left_panel, height=1, bg=self.t["accent"])
        sep2.pack(fill="x", pady=10)

        tk.Label(left_panel, text="Режим погашения долга", font=("Segoe UI", 10, "bold"), fg=self.t["accent"], bg=self.t["panel_bg"]).pack(anchor="w", pady=(0, 4))

        rb_style = {"bg": self.t["panel_bg"], "fg": self.t["panel_fg"], "selectcolor": self.t["entry_bg"], "activebackground": self.t["panel_bg"], "activeforeground": self.t["panel_fg"], "font": ("Segoe UI", 9)}
        tk.Radiobutton(left_panel, text="Стандартный (уменьшающийся)", value="differentiated", variable=self.calc_mode, command=self.calculate, **rb_style).pack(anchor="w", pady=2)
        tk.Radiobutton(left_panel, text="Фиксированный платеж", value="fixed_payment", variable=self.calc_mode, command=self.calculate, **rb_style).pack(anchor="w", pady=2)

        f_pay = tk.Frame(left_panel, bg=self.t["panel_bg"])
        f_pay.pack(fill="x", pady=8)
        tk.Label(f_pay, text="Платеж (BYN):", font=("Segoe UI", 9), fg=self.t["panel_fg"], bg=self.t["panel_bg"]).pack(side="left")
        self.entry_fix = tk.Entry(f_pay, textvariable=self.custom_payment, font=("Segoe UI", 10, "bold"), width=10, justify="right", bg=self.t["entry_bg"], fg=self.t["entry_fg"], insertbackground="white", relief="flat")
        self.entry_fix.pack(side="right")
        self.entry_fix.bind("<KeyRelease>", lambda e: self.calculate())

        btn_export = tk.Button(
            left_panel, text="💾 Экспорт отчета в CSV", font=("Segoe UI", 10, "bold"), 
            bg=self.t["accent_btn"], fg="#ffffff", activebackground=self.t["accent"], activeforeground="#ffffff",
            relief="flat", pady=8, command=self.export_csv, cursor="hand2"
        )
        btn_export.pack(fill="x", pady=(15, 0))

        right_panel = tk.Frame(main_container, bg=self.t["bg"])
        right_panel.pack(side="right", fill="both", expand=True)

        cards_frame = tk.Frame(right_panel, bg=self.t["bg"])
        cards_frame.pack(fill="x", pady=(0, 10))

        self.lbl_loan_amount = self._create_card(cards_frame, "Сумма кредита", "0 BYN", 0)
        self.lbl_total_interest = self._create_card(cards_frame, "Переплата по процентам", "0 BYN", 1)
        self.lbl_total_paid = self._create_card(cards_frame, "Общая сумма выплат", "0 BYN", 2)
        self.lbl_actual_term = self._create_card(cards_frame, "Реальный срок", "0 мес.", 3)

        table_container = tk.Frame(right_panel, bg=self.t["panel_bg"], padx=2, pady=2)
        table_container.pack(fill="both", expand=True)

        columns = ("period", "principal", "interest", "total", "balance", "rate")
        self.tree = ttk.Treeview(table_container, columns=columns, show="headings", selectmode="browse")

        headers = {
            "period": "Месяц", "principal": "Основной долг", "interest": "Проценты",
            "total": "Итого платеж", "balance": "Остаток долга", "rate": "Ставка"
        }

        for col, text in headers.items():
            self.tree.heading(col, text=text)
            self.tree.column(col, anchor="center", width=110)

        scrollbar = ttk.Scrollbar(table_container, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def build_chart_tab(self):
        self.chart_frame = tk.Frame(self.tab_chart, bg=self.t["bg"])
        self.chart_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def build_compare_tab(self):
        self.compare_frame = tk.Frame(self.tab_compare, bg=self.t["panel_bg"], padx=20, pady=20)
        self.compare_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.lbl_compare_content = tk.Label(
            self.compare_frame, text="Расчет сравнения сценариев...", 
            font=("Segoe UI", 11), fg=self.t["panel_fg"], bg=self.t["panel_bg"], justify="left"
        )
        self.lbl_compare_content.pack(anchor="nw")

    def _create_card(self, parent, title, value, col):
        card = tk.Frame(parent, bg=self.t["card_bg"], padx=12, pady=10, relief="flat")
        card.grid(row=0, column=col, sticky="ew", padx=5)
        parent.columnconfigure(col, weight=1)

        tk.Label(card, text=title, font=("Segoe UI", 8), fg=self.t["card_title"], bg=self.t["card_bg"]).pack(anchor="w")
        val_lbl = tk.Label(card, text=value, font=("Segoe UI", 12, "bold"), fg=self.t["card_fg"], bg=self.t["card_bg"])
        val_lbl.pack(anchor="w", pady=(2, 0))
        return val_lbl

    def _safe_float(self, val_str, default=0.0):
        try:
            cleaned = str(val_str).strip().replace(",", ".")
            if not cleaned: return default
            return float(cleaned)
        except ValueError:
            return default

    def _safe_int(self, val_str, default=0):
        try:
            cleaned = str(val_str).strip()
            if not cleaned: return default
            return int(cleaned)
        except ValueError:
            return default

    def calculate(self):
        price = self._safe_float(self.car_price.get(), 0)
        pct = self._safe_float(self.down_payment_pct.get(), 0)
        custom_loan = self._safe_float(self.custom_loan_amount.get(), 0)
        term = self._safe_int(self.term_months.get(), 120)
        p_rate = self._safe_float(self.promo_rate.get(), 5.0) / 100.0
        p_months = self._safe_int(self.promo_months.get(), 36)
        b_rate = self._safe_float(self.base_rate.get(), 15.75) / 100.0
        mode = self.calc_mode.get()
        fix_pay = self._safe_float(self.custom_payment.get(), 960)
        
        extra_amt = self._safe_float(self.extra_payment.get(), 0)
        extra_m = self._safe_int(self.extra_month.get(), 12)

        if custom_loan > 0:
            loan_amount = custom_loan
        else:
            loan_amount = price * (1.0 - pct / 100.0)

        self.lbl_loan_amount.config(text=f"{loan_amount:,.2f} BYN".replace(",", " "))

        for row in self.tree.get_children():
            self.tree.delete(row)

        balance = loan_amount
        total_interest = 0
        total_paid = 0
        month = 0
        self.schedule_data = []
        months_list = []
        balance_list = []

        if mode == "differentiated":
            fixed_principal = loan_amount / term if term > 0 else 0
            while balance > 0.01 and month < 360:
                month += 1
                rate = p_rate if month <= p_months else b_rate
                interest = balance * (rate / 12.0)
                principal = min(balance, fixed_principal)
                
                if month == extra_m and extra_amt > 0:
                    extra_actual = min(balance - principal, extra_amt)
                    principal += extra_actual

                total = principal + interest
                balance -= principal
                total_interest += interest
                total_paid += total

                row_tuple = (month, f"{principal:.2f}", f"{interest:.2f}", f"{total:.2f}", f"{max(0, balance):.2f}", f"{rate*100:.2f}%")
                self.tree.insert("", "end", values=row_tuple)
                self.schedule_data.append(row_tuple)
                months_list.append(month)
                balance_list.append(balance)
        else:
            while balance > 0.01 and month < 600:
                month += 1
                rate = p_rate if month <= p_months else b_rate
                interest = balance * (rate / 12.0)
                
                if fix_pay <= interest:
                    break
                
                principal = min(balance, fix_pay - interest)
                if month == extra_m and extra_amt > 0:
                    extra_actual = min(balance - principal, extra_amt)
                    principal += extra_actual

                total = principal + interest
                balance -= principal
                total_interest += interest
                total_paid += total

                row_tuple = (month, f"{principal:.2f}", f"{interest:.2f}", f"{total:.2f}", f"{max(0, balance):.2f}", f"{rate*100:.2f}%")
                self.tree.insert("", "end", values=row_tuple)
                self.schedule_data.append(row_tuple)
                months_list.append(month)
                balance_list.append(balance)

        self.lbl_total_interest.config(text=f"{total_interest:,.2f} BYN".replace(",", " "))
        self.lbl_total_paid.config(text=f"{total_paid:,.2f} BYN".replace(",", " "))
        self.lbl_actual_term.config(text=f"{month} мес.")

        if HAS_MATPLOTLIB:
            for widget in self.chart_frame.winfo_children():
                widget.destroy()

            fig, ax = plt.subplots(figsize=(8, 4.5), dpi=100)
            fig.patch.set_facecolor(self.t["bg"])
            ax.set_facecolor(self.t["panel_bg"])

            ax.plot(months_list, balance_list, color=self.t["accent"], linewidth=2.5, label="Остаток долга (BYN)")
            ax.set_title("Динамика уменьшения долга по кредиту", color=self.t["panel_fg"], fontsize=12, fontweight="bold")
            ax.set_xlabel("Месяцы", color=self.t["panel_fg"])
            ax.set_ylabel("Остаток (BYN)", color=self.t["panel_fg"])
            ax.tick_params(colors=self.t["panel_fg"])
            ax.grid(True, linestyle="--", alpha=0.3)
            ax.legend(facecolor=self.t["panel_bg"], edgecolor="none", labelcolor=self.t["panel_fg"])

            for spine in ax.spines.values():
                spine.set_color("#374155")

            canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)

        compare_text = f"""📊 АНАЛИЗ И СРАВНЕНИЕ СЦЕНАРИЕВ ДЛЯ BELGEE X80:

• Исходная сумма кредита: {loan_amount:,.2f} BYN
• Итоговая переплата по процентам: {total_interest:,.2f} BYN
• Общая сумма всех выплат банку: {total_paid:,.2f} BYN
• Итоговый реальный срок выплаты: {month} месяцев ({(month/12):.1f} лет)

💡 СОВЕТ ПО ФИНАНСАМ:
Использование льготного периода под {p_rate*100}% годовых на первые {p_months} месяцев позволяет существенно сэкономить на старте. 
Регулярное внесение досрочных платежей способно сократить переплату и ускорить погашение кредита!
"""
        self.lbl_compare_content.config(text=compare_text)

    def export_csv(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV файлы", "*.csv")], title="Сохранить отчет")
        if filepath:
            with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
                writer = csv.writer(f)
                writer.writerow(["Месяц", "Основной долг", "Проценты", "Итого платеж", "Остаток долга", "Ставка"])
                writer.writerows(self.schedule_data)
            messagebox.showinfo("Успех", "Отчет успешно сохранен!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BelgeeLoanCalculator(root)
    root.mainloop()
