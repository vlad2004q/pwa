import os

html_code = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Drywall Master — Apple Glass Pro</title>
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
            border-color: #38bdf8;
            outline: none;
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.25);
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
            <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-sky-400/20 to-blue-600/30 border border-white/20 flex items-center justify-center shadow-inner">
                <span class="text-xl">🧱</span>
            </div>
            <div>
                <h1 class="font-bold text-base tracking-tight text-white leading-tight">Drywall Master</h1>
                <p class="text-[11px] font-medium text-sky-400/90 mt-0.5">iOS Glassmorphism Edition</p>
            </div>
        </div>
        <span class="text-[10px] font-semibold px-3 py-1 rounded-full bg-white/10 text-slate-300 border border-white/10 backdrop-blur-md">v4.0 Pro</span>
    </header>

    <main class="max-w-md mx-auto px-4 pt-5 space-y-4">

        <!-- Main Glass KPI Display -->
        <div class="apple-glass p-6 rounded-3xl relative overflow-hidden">
            <div class="absolute -right-10 -top-10 w-32 h-32 bg-sky-500/10 rounded-full blur-2xl pointer-events-none"></div>
            
            <div class="flex justify-between items-start">
                <div>
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-widest">Чистая площадь</span>
                    <div class="text-4xl font-extrabold text-white tracking-tight mt-1" id="lblNetArea">0.0 <span class="text-xl font-normal text-slate-400">м²</span></div>
                </div>
                <div class="text-right">
                    <span class="text-xs font-semibold text-sky-400 uppercase tracking-widest">Листов ГКЛ</span>
                    <div class="text-3xl font-extrabold text-sky-400 mt-1" id="lblSheets">0 шт.</div>
                </div>
            </div>

            <div class="mt-5 pt-4 border-t border-white/10 flex justify-between items-center">
                <div>
                    <div class="text-[11px] text-slate-400">Итоговая смета</div>
                    <div class="text-2xl font-black text-emerald-400 mt-0.5" id="lblTotalCost">0.00 BYN</div>
                </div>
                <div class="text-right">
                    <div class="text-[11px] text-slate-400">Цена за лист</div>
                    <div class="text-sm font-semibold text-slate-200" id="lblUnitPrice">9.50 BYN</div>
                </div>
            </div>
        </div>

        <!-- Room Geometry Section -->
        <div class="apple-glass-card p-5 rounded-3xl space-y-4">
            <h2 class="text-xs font-bold text-sky-400 uppercase tracking-widest flex items-center gap-2">
                <span>📐</span> Параметры помещения
            </h2>

            <div class="grid grid-cols-2 gap-3">
                <div>
                    <label class="text-[11px] font-medium text-slate-400">Длина комнаты (м)</label>
                    <input type="number" id="roomL" value="5.0" step="0.1" oninput="calc()" class="apple-input w-full mt-1.5 rounded-2xl px-3.5 py-2.5 text-sm font-bold text-right">
                </div>
                <div>
                    <label class="text-[11px] font-medium text-slate-400">Ширина комнаты (м)</label>
                    <input type="number" id="roomW" value="4.0" step="0.1" oninput="calc()" class="apple-input w-full mt-1.5 rounded-2xl px-3.5 py-2.5 text-sm font-bold text-right">
                </div>
            </div>

            <div class="grid grid-cols-2 gap-3">
                <div>
                    <label class="text-[11px] font-medium text-slate-400">Высота потолка (м)</label>
                    <input type="number" id="roomH" value="2.7" step="0.1" oninput="calc()" class="apple-input w-full mt-1.5 rounded-2xl px-3.5 py-2.5 text-sm font-bold text-right">
                </div>
                <div>
                    <label class="text-[11px] font-medium text-slate-400">Проемы окна/двери (м²)</label>
                    <input type="number" id="doors" value="3.5" step="0.1" oninput="calc()" class="apple-input w-full mt-1.5 rounded-2xl px-3.5 py-2.5 text-sm font-bold text-right">
                </div>
            </div>
        </div>

        <!-- Sheet Material & Price -->
        <div class="apple-glass-card p-5 rounded-3xl space-y-4">
            <h2 class="text-xs font-bold text-sky-400 uppercase tracking-widest flex items-center gap-2">
                <span>📦</span> Формат плиты и Стоимость
            </h2>

            <div class="grid grid-cols-2 gap-3">
                <div>
                    <label class="text-[11px] font-medium text-slate-400">Размер ГКЛ</label>
                    <select id="sheetPreset" onchange="calc()" class="apple-input w-full mt-1.5 rounded-2xl px-3 py-2.5 text-xs font-bold bg-slate-900">
                        <option value="1.5,0.6">1.50 x 0.60 м (0.9 м²)</option>
                        <option value="1.2,0.6">1.20 x 0.60 м (0.72 м²)</option>
                        <option value="1.5,1.0">1.50 x 1.00 м (1.50 м²)</option>
                    </select>
                </div>
                <div>
                    <label class="text-[11px] font-medium text-slate-400">Цена 1 листа (BYN)</label>
                    <input type="number" id="price" value="9.50" step="0.5" oninput="calc()" class="apple-input w-full mt-1.5 rounded-2xl px-3.5 py-2.5 text-sm font-bold text-emerald-400 text-right">
                </div>
            </div>

            <div class="pt-1">
                <div class="flex justify-between text-[11px] font-medium text-slate-400 mb-2">
                    <span>Запас на обрезку</span>
                    <span id="lblWasteVal" class="text-sky-400 font-bold">10%</span>
                </div>
                <input type="range" id="waste" min="5" max="25" value="10" step="1" oninput="calc()" class="w-full">
            </div>
        </div>

        <!-- Consumables -->
        <div class="apple-glass-card p-5 rounded-3xl space-y-3">
            <h3 class="text-xs font-bold text-slate-300 uppercase tracking-widest">🛠️ Ведомость расходников</h3>
            <div class="flex justify-between text-xs py-2 border-b border-white/5">
                <span class="text-slate-400">Саморезы по ГКЛ (3.5x25)</span>
                <span class="font-bold text-white" id="lblScrews">0 шт.</span>
            </div>
            <div class="flex justify-between text-xs py-2 border-b border-white/5">
                <span class="text-slate-400">Дюбель-гвозди (6x40)</span>
                <span class="font-bold text-white" id="lblDowels">0 шт.</span>
            </div>
            <div class="flex justify-between text-xs py-1">
                <span class="text-slate-400">Периметр каркаса</span>
                <span class="font-bold text-sky-400" id="lblPerimeter">0.0 м</span>
            </div>
        </div>

    </main>

    <script>
        function calc() {
            const L = parseFloat(document.getElementById("roomL").value) || 0;
            const W = parseFloat(document.getElementById("roomW").value) || 0;
            const H = parseFloat(document.getElementById("roomH").value) || 0;
            const doors = parseFloat(document.getElementById("doors").value) || 0;

            const preset = document.getElementById("sheetPreset").value.split(",");
            const sL = parseFloat(preset[0]);
            const sW = parseFloat(preset[1]);
            const price = parseFloat(document.getElementById("price").value) || 0;
            const waste = parseInt(document.getElementById("waste").value) || 10;

            document.getElementById("lblWasteVal").innerText = waste + "%";

            const perimeter = 2 * (L + W);
            const grossArea = perimeter * H;
            const netArea = Math.max(0, grossArea - doors);

            const sheetArea = sL * sW;
            const sheetsNeeded = Math.ceil((netArea / sheetArea) * (1 + waste / 100));
            const totalCost = sheetsNeeded * price;

            const screws = sheetsNeeded * 22;
            const dowels = Math.ceil(perimeter * 2.5);

            document.getElementById("lblNetArea").innerHTML = netArea.toFixed(1) + " <span class=\"text-xl font-normal text-slate-400\">м²</span>";
            document.getElementById("lblSheets").innerText = sheetsNeeded + " шт.";
            document.getElementById("lblTotalCost").innerText = totalCost.toFixed(2) + " BYN";
            document.getElementById("lblUnitPrice").innerText = price.toFixed(2) + " BYN";

            document.getElementById("lblScrews").innerText = "~" + screws + " шт.";
            document.getElementById("lblDowels").innerText = "~" + dowels + " шт.";
            document.getElementById("lblPerimeter").innerText = perimeter.toFixed(1) + " м";
        }

        calc();
    </script>
</body>
</html>"""

folder = os.path.expanduser("~/Desktop/Belgee_Calculator")
for name in ["index.html", "drywall_pwa.html"]:
    with open(os.path.join(folder, name), "w", encoding="utf-8") as f:
        f.write(html_code)

print("ГОТОВО: Файлы Apple Glass успешно записаны!")
