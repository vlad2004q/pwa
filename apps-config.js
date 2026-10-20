// Добавьте объект в массив, чтобы приложение появилось в хабе.
// Пути относительны к index.html. Для автономности приложение хранится в своей папке.
window.ECOSYSTEM_APPS = [
  {id:'projects',title:'PRO Projects',icon:'🏗️',path:'./apps/projects/index.html',description:'Проекты, заметки и резервные копии',tags:['Проекты','Объекты']},
  {id:'cutting',title:'Cutting PRO',icon:'📐',path:'./apps/cutting/index.html',description:'Раскрой профиля, карта резов и ведомость',tags:['Раскрой','Гараж']},
  {id:'analytics',title:'PRO Analytics',icon:'📊',path:'./apps/analytics/index.html',description:'Аналитика смет и сравнение сохранённых данных',tags:['Отчёты','Смета']},
  {id:'cash-byn',title:'Касса PRO · Валюты',icon:'💵',path:'./apps/cash-byn/index.html',description:'Подсчёт купюр и монет в 8 валютах, история и экспорт',tags:['Касса','BYN','RUB','USD','EUR']},
  {id:'concrete',title:'Concrete PRO',icon:'🧱',path:'./apps/concrete/index.html',description:'Объём бетона, цемент, песок, щебень, вода, ведра и стоимость',tags:['Бетон','Фундамент','Материалы']},

  {id:'garage',title:'Garage Frame Planner',icon:'🚘',path:'./apps/garage/index.html',description:'Эскиз гаража из металлических труб, размеры, ворота и предварительная ведомость',tags:['Гараж','Металлокаркас','Стройка']},
  {id:'estimate',title:'Construction Estimate',icon:'🧾',path:'./apps/estimate/index.html',description:'Смета строительных работ, материалов, бюджета и резерва',tags:['Стройка','Смета','Бюджет']},
  {id:'car-care',title:'Car Care Planner',icon:'🛠️',path:'./apps/car-care/index.html',description:'Пробег автомобиля, следующее ТО и бюджет обслуживания',tags:['Авто','ТО','Напоминания']},
  {id:'home-budget',title:'Home Budget',icon:'💰',path:'./apps/home-budget/index.html',description:'Месячный бюджет, расходы и накопления',tags:['Быт','Финансы','Экономия']},
  {id:'converter',title:'Unit Converter',icon:'📏',path:'./apps/converter/index.html',description:'Перевод единиц для стройки, ремонта и быта',tags:['Конвертер','Единицы','Замеры']},
  {id:'checklist',title:'Lists & Checklists',icon:'✅',path:'./apps/checklist/index.html',description:'Списки покупок, материалов, инструмента и задач',tags:['Списки','Покупки','Задачи']},
  {id:'materials',title:'PRO Material Hub BY',icon:'📦',path:'./apps/materials/index.html',description:'Каталог смесей, фуг и клеёв · Litokol, Ceresit, Тайфун · BYN',tags:['Материалы','BYN','Каталог']},
  {id:'electric',title:'Инженерный Электрик PRO',icon:'⚡',path:'./apps/electric/index.html',description:'Расчёты электрика, конструктор электрощита и план помещений.',tags:['Электрика','Щит','Кабель']},
  {id:'finance',title:'Belgee Finance',icon:'🚗',path:'./apps/finance/index.html',description:'Автокредит, график платежей и досрочное погашение.',tags:['Финансы','Кредит']},
  {id:'drywall',title:'Drywall Master',icon:'🧱',path:'./apps/drywall/index.html',description:'Расчёт гипсокартона, материалов и сметы.',tags:['Стройка','ГКЛ']},
  {"id":"measure","title":"PRO Замерщик","icon":"📐","path":"./apps/measure/index.html","description":"Планы помещений, площади, объёмы и обмеры","tags":["Замеры","Площади"]},
  {"id":"tile","title":"Tile Master","icon":"▦","path":"./apps/tile/index.html","description":"Плитка, сетка укладки, клей и затирка","tags":["Плитка","Отделка"]},
  {"id":"paint","title":"Paint PRO","icon":"🎨","path":"./apps/paint/index.html","description":"Краска, грунтовка, расход и смета","tags":["Покраска","Отделка"]},
  {"id":"plumbing","title":"Plumbing PRO","icon":"🚰","path":"./apps/plumbing/index.html","description":"Каталог Varmega с артикулами, совместимостью и закупочной спецификацией","tags":["Сантехника","Varmega"]},
  {"id":"heat","title":"Heat PRO","icon":"♨️","path":"./apps/heat/index.html","description":"Предварительная оценка теплопотерь и радиаторов","tags":["Отопление","Тепло"]},
  {"id":"floor","title":"Floor Master","icon":"🪵","path":"./apps/floor/index.html","description":"Напольные покрытия, упаковки и плинтусы","tags":["Полы","Ламинат"]}
];
