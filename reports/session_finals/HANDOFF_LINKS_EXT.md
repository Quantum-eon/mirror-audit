# MIRROR EXT-серия (P1–P7) — реестр артефактов / ссылки для команды
Собрано: 2026-07-18. Корень проекта: `~/Projects/MIRROR` (Mac mini, устройство mac-mini-local).
Git HEAD: `34fc61f`. Портативная история: `archive/mirror_archive_ext_20260718.bundle`.
Все пути ниже — относительно корня проекта.

---

## Входные точки (читать первыми)
- `MIRROR_SESSION_FINAL_EXT_2026-07-17.md` — главный сводный документ EXT-серии. §1–§5 DeepSeek-блок; **§6–§9 кросс-модельный блок P5–P7**; §7 находки; §8.1 сверка стоимости.
- `HANDOFF_TEAM_MIRROR_2026-07-16.md` — командный хэндофф; внизу секция «ДОПОЛНЕНИЕ 2026-07-18 — EXT-СЕРИЯ» с экшенами по ролям (Finch / Yuki / Victor / Q-Alex / Lex / Luna).
- `docs/SESSION_JOURNAL_2026-07-17.md` — хронология решений (append-only), записи P1–P7.
- `docs/PREREG_INJECTION_EXPERIMENT.md` — пре-регистрация P2 (зафиксирована до данных).
- `runs/INDEX.md` и `runs/all_runs.csv` — сводные таблицы по всем прогонам (строка на RUN_ID).

## Прогоны
Структура каждого: `input/` `outputs/` `interrogation/` `analysis/run_manifest.json` `screenshots/` `notes.md`.

### DeepSeek-блок
- `runs/MIRROR-VALDORIA-DEEPSEEK-NOHORIZON-REP2-20260717` — P1 реплика (граф 10n/9e)
- `runs/MIRROR-VALDORIA-DEEPSEEK-NOHORIZON-REP3-20260717` — P1 реплика (10n/6e, report NEG-CASE)
- `runs/MIRROR-VALDORIA-DEEPSEEK-NOHORIZON-REP4-20260717` — P1 реплика (11n/8e, уникальная Япония в графе)
- `runs/MIRROR-VALDORIA-DEEPSEEK-INJECT1-20260717` — P2 граф-инъекция (switching MET: Q3 6/8)
- `runs/MIRROR-VALDORIA-DEEPSEEK-INJECT2-20260717` — P2 реплика (switching REPLICATED: Q3 ≥5/8)
- `runs/MIRROR-REINT-Q1B-20260717` — P4 пере-интеррогация 5 родителей (гейт G6)

### Кросс-модельный блок
- `runs/MIRROR-VALDORIA-CLAUDE-HORIZON7-20260717` — **P5** Claude, rounds=168; отчёт `.../outputs/report/report.md`
- `runs/MIRROR-LOREM2-CLAUDE-20260717` — **P6** lorem (Finding #1); сид `scenarios/lorem/seed_document_v2.txt`
- `runs/MIRROR-VALDORIA-GEMINI-HORIZON7-20260718` — **P7** Gemini, rounds=168; отчёт `.../outputs/report/report.md`

## Портативная git-история (бандлы, на постоянном диске)
- `archive/mirror_archive_ext_20260718.bundle` — актуальный, HEAD `34fc61f` (P1–P7 + сверка стоимости)
- `archive/mirror_archive_ext_20260717.bundle` — резервный, HEAD `9f8e515` (до P5)
- `archive/mirror_archive_20260716.bundle` — история пред-EXT (A/B-серии)

Восстановить историю:
```
git clone --bare ~/Projects/MIRROR/archive/mirror_archive_ext_20260718.bundle mirror.git
```

## Git-коммиты EXT (в бандле _ext_20260718)
| hash | что |
|---|---|
| `34fc61f` | cost reconciled vs OpenRouter (balance $24.31, all-time $60.69, EXT-неделя $33.10) |
| `632dd8b` | FINAL_EXT + team-handoff: синтез кросс-модельного блока P5–P7 |
| `44fb780` | P5+P6+P7 (recovered) — Claude+Gemini блоки |
| `9f8e515` | FINAL: DeepSeek-блок P1+P2+P4 |
| `e921813` | P4 REINT-Q1b (G6 graph-gated) |
| `d35f94a` | P2 INJECT2 (switching replicated) |
| `e6fb498` | P2 INJECT1 (switching met) |
| `71aeeed` | PREREG injection experiment |
| `022eede` | P1 REP4 |
| `c47692f` | P1 REP3 |
| `b9d3922` | P1 REP2 |

## Ключевые ID прогонов (MiroFish бэкенд)
- **P5:** project `proj_43fdea658b7e` / graph `f88d1437-ebcf-49c5-88d1-ea7450f72f60` / sim `sim_86b0444d4207` / report `report_7e83b0281b90`
- **P6:** project `proj_f5ec20f8106e` / graph `6d136399-f8e9-433a-9101-973d1bbde83b` / sim `sim_61b9bf5a0aa2` (fast-fail, без отчёта)
- **P7:** project `proj_86843f7d9444` / graph `19aac222-8fab-4cda-a231-03577b9d3284` / sim `sim_e4c7a9bff1ed` / report `report_24c4affb9eb1`

## Ключевые находки (СЫРЬЁ — классификация за Finch, Rule 4)
1. Графовый гейтинг видимости абсурда: report-level слеп, если абсурд не попал в граф; инъекция в граф ПЕРЕКЛЮЧАЕТ Q3 (6/8, ≥5/8 vs контроль ≤2). Переформулирует Finding #2.
2. horizon×24 — МОДЕЛЬ-ИНВАРИАНТ: rounds=168 на DeepSeek, Claude, Gemini. Finding #3.
3. Два слоя видимости: отчёт (graph-gated, слеп) vs агенты (persona-context, зрячи).
4. Ранг сопротивления абсурду на уровне агентов: Gemini > Claude > DeepSeek.
5. Q1b/G6: DeepSeek recall+конфаб / Claude recall==граф / Gemini ОТКАЗ (новый negative-case).
6. Finding #1 (lorem) переформулирован: backend fast-fail, «тихий фриз» — артефакт UI.
7. Коллапс трекает число агентов, не модель (чистые 168 на 10–11 агентах vs stop на 18–19).

## Стоимость (сверено с дашбордом OpenRouter 2026-07-18T08:04Z; ключ редактирован)
- Баланс остаток: **$24.31**; куплено всего: **$85.00**; потрачено all-time: **$60.69**.
- Окно EXT (последняя неделя): **$33.10** — 3K запросов, 52.2M токенов, кэш 66.9%, blended $0.63/1M.
- Атрибуция P1–P7 ≈ $26–27. Детали: §8.1 в `MIRROR_SESSION_FINAL_EXT_2026-07-17.md`.

## Операционные заметки для команды
- Все данные на смонтированном диске `~/Projects/MIRROR` (персистентно); отчёты report-chat НЕ персистятся бэкендом (захвачены verbatim через API), интервью персистятся в `.../ipc_responses/`.
- Смена модели требует `docker compose up -d --force-recreate` (обычный restart НЕ перечитывает .env).
- Редакция API-ключей (префикс OpenRouter-ключа) = 0 совпадений на каждом коммите.
