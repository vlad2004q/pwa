import os

html_loan = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Belgee Finance — Apple Glass Pro</title>
    <meta name="theme-color" content="#0b1329">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: "Plus Jakarta Sans", -apple-system, sans-serif;
            background: radial-gradient(circle at 50% 0%, #1e293b 0%, #0f172a 50%, #020617 100%);
            -webkit-tap-highlight-color: transparent;
        }
        .apple-glass {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }
        .apple-glass-card {
            background: rgba(255, 255, 255, 0.04);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .apple-input {
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: #ffffff;
            transition: all 0.2s ease;
        }
        .apple-input:focus {
            background: rgba(255, 255, 255, 0.12);
            border-color: #10b981;
            outline: none;
            box-shadow: 0 0 15px rgba(16, 185, 129, 0.25);
        }
        input[type=range] {
            -webkit-appearance: none;
            background: rgba(255, 255, 255, 0.1);
            height: 6px;
            border-radius: 3px;
        }
        input[type=range]::-webkit-slider-thumb {
            -webkit-appearance: none;
            height: 22px;
            width: 22px;
            border-radius: 50%;
            background: #ffffff;
            box-shadow: 0 4px 10px rgba(0,0,0,0.4);
            cursor: pointer;
        }
    </style>
</head>
<body class="text-slate-100 min-h-screen pb-24 select-none">

    <!-- Header -->
    <header class="sticky top-0 z-50 apple-glass border-b border-white/10 px-5 py-4 flex items-center justify-between">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-emerald-400/20 to-teal-600/30 border border-white/20 flex items-center justify-center shadow-inner">
                <span class="text-xl">🚗</span>
            </div>
            <div>
                <h1 class="font-bold text-base tracking-tight text-white leading-tight">Belgee Auto Loan</h1>
                <p class="text-[11px] font-medium text-emerald-400/90 mt-0.5">iOS Glassmorphism Edition</p>
            </div>
        </div>
        <span class="text-[10px] font-semibold px-3 py-1 rounded-full bg-white/10 text-slate-300 border border-white/10 backdrop-blur-md">v4.0 Pro</span>
    </header>

    <main class="max-w-md mx-auto px-4 pt-5 space-y-4">

        <!-- Main Glass KPI Display -->
        <div class="apple-glass p-6 rounded-3xl relative overflow-hidden">
            <div class="absolute -right-10 -top-10 w-32 h-32 bg-emerald-500/10 rounded-full blur-2xl pointer-events-none"></div>
            
            <div class="flex justify-between items-start">
                <div>
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-widest">Платеж в грейс-период</span>
                    <div class="text-3xl font-extrabold text-emerald-400 tracking-tight mt-1" id="lblGracePayment">0.00 BYN</div>
                </div>
            </div>

            <div class="mt-4 pt-3 border-t border-white/10 flex justify-between items-center">
                <div>
                    <div class="text-[11px] text-slate-400">Основной платеж (после грейса)</div>
                    <div class="text-xl font-bold text-white mt-0.5" id="lblMainPayment">0.00 BYN</div>
                </div>
                <div class="text-right">
                    <div class="text-[11px] text-slate-400">Переплата</div>
                    <div class="text-sm font-semibold text-rose-400" id="lblOverpayment">0.00 BYN</div>
                </div>
            </div>
        </div>

        <!-- Loan Input Controls -->
        <div class="apple-glass-card p-5 rounded-3xl space-y-4">
            <h2 class="text-xs font-bold text-emerald-400 uppercase tracking-widest flex items-center gap-2">
                <span>💰</span> Расчет суммы кредита
            </h2>

            <div>
                <label class="text-[11px] font-medium text-slate-400">Сумма кредита (напрямую, BYN)</label>
                <input type="number" id="directLoan" value="41250" step="500" oninput="onDirectLoanInput()" class="apple-input w-full mt-1.5 rounded-2xl px-3.5 py-2.5 text-base font-bold text-emerald-400 text-right">
            </div>

            <div class="border-t border-white/5 pt-3 space-y-3">
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="text-[11px] font-medium text-slate-400">Стоимость авто (BYN)</label>
                        <input type="number" id="carPrice" value="55000" step="1000" oninput="onCarCalcInput()" class="apple-input w-full mt-1 rounded-2xl px-3 py-2 text-xs font-bold text-right">
                    </div>
                    <div>
                        <label class="text-[11px] font-medium text-slate-400">Аванс (%)</label>
                        <input type="number" id="downPctNum" value="25" min="0" max="90" step="1" oninput="onDownPctInput()" class="apple-input w-full mt-1 rounded-2xl px-3 py-2 text-xs font-bold text-right">
                    </div>
                </div>

                <div>
                    <div class="flex justify-between text-[11px] font-medium text-slate-400 mb-1">
                        <span>Ползунок аванса</span>
                        <span id="lblDownVal" class="text-emerald-400 font-bold">25% (13 750 BYN)</span>
                    </div>
                    <input type="range" id="downPct" min="10" max="80" value="25" step="5" oninput="onSliderInput()" class="w-full">
                </div>
            </div>
        </div>

        <!-- Rates & Term -->
        <div class="apple-glass-card p-5 rounded-3xl space-y-4">
            <h2 class="text-xs font-bold text-emerald-400 uppercase tracking-widest flex items-center gap-2">
                <span>⚙️</span> Ставки и Срок
            </h2>

            <div class="grid grid-cols-2 gap-3">
                <div>
                    <label class="text-[11px] font-medium text-slate-400">Льготная ставка (%)</label>
                    <input type="number" id="graceRate" value="7.25" step="0.25" oninput="calc()" class="apple-input w-full mt-1.5 rounded-2xl px-3.5 py-2.5 text-sm font-bold text-right">
                </div>
                <div>
                    <label class="text-[11px] font-medium text-slate-400">Грейс-период (мес)</label>
                    <input type="number" id="graceMonths" value="24" step="6" oninput="calc()" class="apple-input w-full mt-1.5 rounded-2xl px-3.5 py-2.5 text-sm font-bold text-right">
                </div>
            </div>

            <div class="grid grid-cols-2 gap-3">
                <div>
                    <label class="text-[11px] font-medium text-slate-400">Основная ставка (%)</label>
                    <input type="number" id="mainRate" value="16.5" step="0.25" oninput="calc()" class="apple-input w-full mt-1.5 rounded-2xl px-3.5 py-2.5 text-sm font-bold text-right">
                </div>
                <div>
                    <label class="text-[11px] font-medium text-slate-400">Срок кредита (лет)</label>
                    <select id="loanYears" onchange="calc()" class="apple-input w-full mt-1.5 rounded-2xl px-3 py-2.5 text-xs font-bold bg-slate-900">
                        <option value="3">3 года</option>
                        <option value="5">5 лет</option>
                        <option value="7" selected>7 лет</option>
                        <option value="10">10 лет</option>
                    </select>
                </div>
            </div>
        </div>

        <!-- Summary Specs -->
        <div class="apple-glass-card p-5 rounded-3xl space-y-3">
            <h3 class="text-xs font-bold text-slate-300 uppercase tracking-widest">📊 Параметры договора</h3>
            <div class="flex justify-between text-xs py-2 border-b border-white/5">
                <span class="text-slate-400">Итоговая сумма кредита</span>
                <span class="font-bold text-emerald-400" id="lblCreditSum">0 BYN</span>
            </div>
            <div class="flex justify-between text-xs py-2 border-b border-white/5">
                <span class="text-slate-400">Всего выплат за весь срок</span>
                <span class="font-bold text-white" id="lblTotalPaid">0 BYN</span>
            </div>
        </div>

    </main>

    <script>
        function onDirectLoanInput() {
            const carPrice = parseFloat(document.getElementById("carPrice").value) || 0;
            const directLoan = parseFloat(document.getElementById("directLoan").value) || 0;
            if (carPrice > 0) {
                const downBYN = Math.max(0, carPrice - directLoan);
                const pct = Math.min(100, Math.max(0, (downBYN / carPrice) * 100));
                document.getElementById("downPctNum").value = Math.round(pct);
                document.getElementById("downPct").value = Math.round(pct);
            }
            calc();
        }

        function onCarCalcInput() {
            syncFromCarAndPct();
            calc();
        }

        function onDownPctInput() {
            const pct = parseFloat(document.getElementById("downPctNum").value) || 0;
            document.getElementById("downPct").value = pct;
            syncFromCarAndPct();
            calc();
        }

        function onSliderInput() {
            const pct = parseFloat(document.getElementById("downPct").value) || 0;
            document.getElementById("downPctNum").value = pct;
            syncFromCarAndPct();
            calc();
        }

        function syncFromCarAndPct() {
            const carPrice = parseFloat(document.getElementById("carPrice").value) || 0;
            const downPct = parseFloat(document.getElementById("downPct").value) || 0;
            const downBYN = carPrice * (downPct / 100);
            const loanSum = Math.max(0, carPrice - downBYN);
            document.getElementById("directLoan").value = Math.round(loanSum);
        }

        function calc() {
            const carPrice = parseFloat(document.getElementById("carPrice").value) || 0;
            const loanSum = parseFloat(document.getElementById("directLoan").value) || 0;
            const downPct = parseFloat(document.getElementById("downPct").value) || 0;

            const graceRate = (parseFloat(document.getElementById("graceRate").value) || 0) / 100;
            const mainRate = (parseFloat(document.getElementById("mainRate").value) || 0) / 100;
            const graceMonths = parseInt(document.getElementById("graceMonths").value) || 0;
            const loanYears = parseInt(document.getElementById("loanYears").value) || 7;

            const downBYN = Math.max(0, carPrice - loanSum);

            document.getElementById("lblDownVal").innerText = Math.round(downPct) + "% (" + Math.round(downBYN).toLocaleString("ru-RU") + " BYN)";

            function getPayment(sum, rate, months) {
                if (months <= 0 || rate <= 0) return sum / (months || 1);
                const mRate = rate / 12;
                return sum * (mRate * Math.pow(1 + mRate, months)) / (Math.pow(1 + mRate, months) - 1);
            }

            const totalMonths = loanYears * 12;
            const gracePayment = getPayment(loanSum, graceRate, totalMonths);
            const mainPayment = getPayment(loanSum * 0.85, mainRate, Math.max(1, totalMonths - graceMonths));

            const totalPaid = (gracePayment * graceMonths) + (mainPayment * Math.max(0, totalMonths - graceMonths));
            const overpayment = Math.max(0, totalPaid - loanSum);

            document.getElementById("lblGracePayment").innerText = gracePayment.toFixed(2) + " BYN";
            document.getElementById("lblMainPayment").innerText = mainPayment.toFixed(2) + " BYN";
            document.getElementById("lblOverpayment").innerText = overpayment.toFixed(2) + " BYN";

            document.getElementById("lblCreditSum").innerText = Math.round(loanSum).toLocaleString("ru-RU") + " BYN";
            document.getElementById("lblTotalPaid").innerText = Math.round(totalPaid).toLocaleString("ru-RU") + " BYN";
        }

        calc();
    </script>
</body>
</html>"""

folder = os.path.expanduser("~/Desktop/Belgee_Calculator")
with open(os.path.join(folder, "belgee_pwa.html"), "w", encoding="utf-8") as f:
    f.write(html_loan)

print("Belgee Loan PWA updated with Direct Loan Amount input!")
