# MIRROR — Командный хэндофф (2026-07-16)

Для: Finch (классификация находок), Yuki (Phase 4 кодинг), Lex (юр-ревью), Victor (репозиторий/инфра), Q-Alex (протокол), Luna (нарративы — ПОЗЖЕ, после кодинга).
От: фаундер (Stepanov) / Cowork-оператор. Статус проекта: **полевая часть run_matrix (Variant 1b) ЗАВЕРШЕНА** — 9 прогонов в архиве, дальше ваша аналитическая фаза.

**Папка проекта (всё лежит здесь): `~/Projects/MIRROR`** (Mac mini). Портативная копия git-истории: `archive/mirror_archive_20260716.bundle` (см. §5).

---

## 1. Что такое MIRROR в одном абзаце (для новых)

Исследование того, как мультиагентная LLM-симуляция (MiroFish-Offline: Neo4j + GraphRAG + агенты на OpenRouter-моделях) обращается с «отравленными» входными документами — сидами с внедрёнными абсурдами и противоречиями (вымышленная страна Valdoria, банк Halcourt, lorem-ipsum). Меряем три вещи: замечают ли агенты абсурд (Finding #2 Ignored Absurdity), падает ли пайплайн на пустом сигнале (Finding #1 Silent Freeze), и какие ресурсные обязательства система берёт на себя сама (Finding #3 Autonomous Horizon Commitment).

## 2. Состояние прогонов (9 в архиве)

| Run | RUN_ID | Модель | Статус |
|---|---|---|---|
| A1 Control | MIRROR-CONTROL-DEEPSEEK-BASE-20260420 | DeepSeek | done (pre-v1.2) |
| A4 | MIRROR-VALDORIA-DEEPSEEK-NOHORIZON-20260421 | DeepSeek | done (pre-Cowork) |
| A5 | MIRROR-VALDORIA-CLAUDE-BASE-20260623 | Claude Sonnet 4 | done — якорь, NEG-CASE |
| A6 | MIRROR-VALDORIA-GEMINI-BASE-20260623 | Gemini 2.5 Flash | done — MIXED, no-monarch |
| A7 | MIRROR-CASHBACK-DEEPSEEK-BASE-20260716 | DeepSeek | done, все 5 фаз |
| B1 | MIRROR-VALDORIA-DEEPSEEK-HORIZON7-20260716 | DeepSeek | done (Part B partial) |
| B3 | MIRROR-VALDORIA-DEEPSEEK-NOHORIZON-20260716 | DeepSeek | done, Part B полный |
| B2 | MIRROR-VALDORIA-DEEPSEEK-HORIZON90-20260716 | DeepSeek | controlled stop R592/2160 (наблюдаемая захвачена) |
| C1 | MIRROR-LOREM-CLAUDE-BASE-20260716 | Claude Sonnet 4 | Silent Freeze воспроизведён (ожидаемо) |
| B4/B5 | — | — | skip-and-document (UI-контролов нет) |

Главный сводный документ по свежей серии: **`MIRROR_SESSION_FINAL_2026-07-16.md`** (кросс-таблицы Finding #2/#3, состав ролей, аномалии, рекомендации к v1.3). Хронология решений: `docs/SESSION_JOURNAL_2026-07-16.md`.

## 3. Карта папки — где что лежит

```
~/Projects/MIRROR/
├── MIRROR_SESSION_FINAL_2026-07-16.md   ← НАЧИНАТЬ ЧТЕНИЕ ОТСЮДА
├── HANDOFF_TEAM_MIRROR_2026-07-16.md    ← этот документ
├── TIME_ESTIMATE_REMAINING_RUNS.md      ← оценка vs факт (для планирования v1.3-серий)
├── A7_SEED_DRAFT.md                     ← драфт Halcourt-сида + обоснования (NOT Lex-cleared!)
├── seed_*.txt                           ← канон-сиды (корень, исторические)
├── scenarios/{valdoria,cashback,lorem}/ ← канонические seed_document + prediction_request (после этой сессии считать locked)
├── runs/<RUN_ID>/                       ← ПОЛНЫЕ архивы прогонов:
│   ├── input/        seed, prediction_request, env_snapshot (секреты заредактированы)
│   ├── outputs/      report/*, simulation/* (run_state, actions_*.jsonl, логи), neo4j_export.json
│   ├── interrogation/ part_a_general.md, part_b_probes.md (ВЕРБАТИМ Q&A) + raw_ipc/*.json
│   ├── analysis/     run_manifest.json (валидный JSON, тайминги/аномалии/кост-ноты)
│   ├── screenshots/  *.txt — text-snapshot standard (PNG нет — env-gap, это норма)
│   └── notes.md      хронологический журнал прогона (UTC)
├── runs/INDEX.md + runs/all_runs.csv    ← сводные реестры (append-only)
├── docs/                                 ← журналы сессий, DECISION, спека агента
├── cowork/skills/mirror-operator/       ← операционный скилл: hard_rules, run_matrix, чеклисты фаз, скрипт допроса
├── archive/mirror_archive_20260716.bundle ← git-история всех коммитов сессии (см. §5)
└── MiroFish-Offline/                    ← стек (docker compose; в git-архив не входит)
```

## 4. Что от кого нужно (next actions по ролям)

**Finch — классификация.** Материал для вердиктов Finding #2 по A7/B1/B3 разложен в `runs/*/phase4_handoff.md` + interrogation/*. Ключевой вопрос сессии, требующий твоего решения: report-level слепота к абсурду коррелирует с наполнением графа, а не с моделью (B3 vs A7/B1 на одной модели) — см. FINAL §2.2 и предложение эксперимента с инъекцией фактов в граф (§3.2). Плюс кандидаты в новые находки: unbounded memory collapse (2 реплики), дегенеративные циклы допроса, мета-утечки («[CEO Name]», fiction-note B3), UK-якорение монарха кросс-модельно.

**Yuki — Phase 4 кодинг (batch).** Все прогоны застейджены: verbatim Q&A в interrogation/, сырые actions_*.jsonl и профили в outputs/simulation/, отчёты в outputs/report/. confidence_coding.csv и contradiction_flags.md — пустые слоты под тебя в analysis/. Тайминги и стоимости — в манифестах (сессия $6.67 факт, аппроксимации per-run в cost-нотах). Внимание на B1: Part B partial (valdoria-пробы blocked) — кодируй что есть, каверза задокументирована.

**Lex.** `A7_SEED_DRAFT.md` — сид Halcourt составлен оператором в сессии БЕЗ твоего клиренса (санкция фаундера, диспетч §2.3); прогон A7 уже выполнен на нём. Нужен ретроспективный ревью + D-MIRROR entry. Спорные места перечислены в драфте §4 (реальные регуляторы поимённо, BTC-пег).

**Victor — инфра.** (1) Родной git в папке так и не работает (FUSE-монт) — история сессии спасена в `archive/mirror_archive_20260716.bundle`: `git clone mirror_archive_20260716.bundle` или `git bundle verify`. Прошлые сессии теряли историю с очисткой /tmp — почини это (native repo или постоянный GIT_DIR). (2) `docs/handoff/` с Protocol v1.0–1.2, Seed Canonical, cashback_seed_document_v1_0, L4 Ground Truth в репо ОТСУТСТВУЕТ — восстанови из project knowledge, сессия работала по чеклистам-производным. (3) MiroFish-фиксы по приоритету: подрезка памяти агентов (блокирует все длинные прогоны), кнопка Stop в UI (сейчас только недокументированный `POST /api/simulation/stop`), interview 120s-таймаут.

**Q-Alex — Protocol v1.3.** Входные предложения — FINAL §3: per-seed replicates (≥3), лимит ≤200 раундов до фикса памяти, kill-критерии + стоп-процедура, Q1b про «original seed document» в Part A, двойной Q4 (константа 7/10), патч слага в phase1_setup §1.4 (`deepseek/deepseek-chat-v3-0324`), формализация text-snapshot стандарта и D-MIRROR entries на сессионные решения (Start Engine override, A7-сид, B2 controlled stop).

## 5. Операционная шпаргалка (чтобы прогнать самим)

- Стек: `cd ~/Projects/MIRROR/MiroFish-Offline && docker compose up -d` (сервис называется `mirofish`, контейнер — `mirofish-offline`; для смены модели в `.env` нужен `up -d --force-recreate mirofish` — простой restart .env НЕ перечитывает).
- Рабочие model-слаги: `deepseek/deepseek-chat-v3-0324`, `anthropic/claude-sonnet-4`, `google/gemini-2.5-flash`. `.env` сейчас на DeepSeek.
- Эмбеддинги DISABLED = стандарт проекта (не включать; GraphRAG degraded — константа, не баг).
- Сырцы прогонов тянуть из `MiroFish-Offline/backend/uploads/{projects,simulations,reports}/<id>/` — не скрапить UI.
- Допрос: Report Chat рендер-баг → API `POST :5001/api/report/chat`; интервью агентов `POST :5001/api/simulation/interview/batch` (agent_id = индекс в списке агентов прогона!); при 120s-таймауте ответы забирать из `simulations/<sim>/ipc_responses/*.json`.
- Остановка симуляции: `POST :5001/api/simulation/stop {simulation_id}`.
- rounds не конфигурируется — только наблюдается на стадии «05 Preparation completed» (D-MIRROR-38).
- Бюджет: OpenRouter all-time $34.26 / хард-кап $50 (headroom ~$15.7 на 2026-07-16). Ключ `MIRROR-experiment`.

## 6. Открытые вопросы (кратко)

1. Вердикты Finding #2 по трём новым прогонам — Finch.
2. Гипотеза граф-гейтинга — дизайн эксперимента с инъекцией (дёшево, ~$1).
3. B2 полный (90 дней) — только после фикса памяти MiroFish.
4. A7-сид — Lex-ревью задним числом.
5. Protocol v1.3 — пакет предложений в FINAL §3.
6. Публичный repo (mirror-audit) — Victor init; до этого никаких push (данные локальные).

— Собрано Cowork-оператором 2026-07-16 по запросу фаундера. Вся первичка вербатим, интерпретации помечены как агентские наблюдения.
