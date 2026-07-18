#!/usr/bin/env python3
"""MIRROR series — before/after example figures for the content style guide.
One source script -> PNG renders (light theme). Semantic palette (validated):
  BLUE  #2563EB  = system correct / determinism / norm
  ORANGE#EA580C  = system confabulates / failure / blindness
  PURPLE#7C3AED  = injection / intervention / anomaly
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np

BLUE, ORANGE, PURPLE = "#2563EB", "#EA580C", "#7C3AED"
INK, MUT, GRID, SURF = "#1A1D23", "#6B7280", "#E5E7EB", "#FCFCFB"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "text.color": INK,
    "axes.edgecolor": GRID, "axes.labelcolor": MUT,
    "xtick.color": MUT, "ytick.color": MUT,
    "figure.facecolor": SURF, "axes.facecolor": SURF,
})

def header(fig, title, subtitle, footer, part):
    fig.text(0.055, 0.955, title, fontsize=19, fontweight="bold", va="top", color=INK)
    fig.text(0.055, 0.895, subtitle, fontsize=11.5, va="top", color=MUT)
    fig.text(0.055, 0.022, footer, fontsize=9, va="bottom", color=MUT)
    # series badge (lime brand chip, dark text)
    fig.text(0.985, 0.022, f"MIRROR · {part}", fontsize=9, va="bottom", ha="right",
             color="#1A1D23", bbox=dict(boxstyle="round,pad=0.35", fc="#E9F010", ec="none"))

# ---------------------------------------------------------------- FIG 1: flagship
# Injection dot-matrix: 8 absurdities x 6 runs (2 panels)
absurds = ["Dual currency peg", "Landlocked + deep-sea fleet", "Elected monarch, 47 yrs",
           "14 parties × equal seats", "340M people / 850 km²", "UN-sanctioned + UNHRC chair",
           "Life expectancy 147", "Borders incl. Japan"]
ctrl_runs = ["REP2", "REP3", "REP4", "B3"]
inj_runs = ["INJECT1", "INJECT2"]
# totals are real (0,1,1,1 control; 6/8 & 5/8 injected); cell layout illustrative pending flag-coding
ctrl = np.zeros((8, 4)); ctrl[5, 1] = ctrl[5, 2] = ctrl[5, 3] = 1
inj = np.ones((8, 2)); inj[0, 0] = inj[6, 0] = 0; inj[0, 1] = inj[3, 1] = inj[6, 1] = 0

fig = plt.figure(figsize=(12, 6.9), dpi=160)
gs = fig.add_gridspec(1, 2, width_ratios=[4, 2.1], left=0.265, right=0.775, top=0.70, bottom=0.155, wspace=0.14)
ax1, ax2 = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])
for ax, runs, M, col, lab, tots, tcol in [
        (ax1, ctrl_runs, ctrl, BLUE, "CONTROL — untouched pipeline", ["0/8", "1/8", "1/8", "1/8"], MUT),
        (ax2, inj_runs, inj, PURPLE, "INJECTED into the graph", ["6/8", "5/8"], PURPLE)]:
    ax.set_xlim(-0.5, len(runs) - 0.5); ax.set_ylim(-0.6, 7.6); ax.invert_yaxis()
    for y in range(8):
        for x in range(len(runs)):
            flagged = M[y, x] == 1
            ax.scatter(x, y, s=430, marker="o", fc=col if flagged else "none",
                       ec=col if flagged else GRID, lw=1.6, zorder=3)
    ax.set_xticks(range(len(runs))); ax.set_xticklabels(runs, fontsize=10)
    ax.set_yticks(range(8))
    ax.set_title(lab, fontsize=10, color=INK if tcol is MUT else PURPLE, pad=52)
    for x, tot in zip(range(len(runs)), tots):
        ax.text(x, -1.15, tot, ha="center", fontsize=10.5, color=tcol,
                fontweight="normal" if tcol is MUT else "bold")
    ax.tick_params(length=0); [s.set_visible(False) for s in ax.spines.values()]
    ax.grid(False)
ax1.set_yticklabels(absurds, fontsize=10.5, color=INK); ax2.set_yticklabels([])
fig.text(0.805, 0.52, "0→6", fontsize=44, fontweight="bold", color=PURPLE, ha="left")
fig.text(0.805, 0.44, "of 8 absurdities flagged\nonce they reach the graph", fontsize=10.5, color=INK, ha="left", va="top")
fig.text(0.805, 0.30, "The report layer isn't\nblind — it's starved.", fontsize=10.5, color=MUT, ha="left", va="top", style="italic")
header(fig,
       "One intervention flips the audit verdict: 0–1 → 6 of 8",
       "Report-level Q3 flags per seeded absurdity · Valdoria seed, byte-identical input, DeepSeek V3 · filled = flagged\n"
       "Cell-level layout illustrative pending formal flag-coding; per-run totals are as observed.",
       "github.com/Quantum-eon/mirror-audit · data/injection_runs.csv · n = 8 absurdities × 6 runs · pre-registered switching criterion ≥3: MET",
       "Part 3/8")
fig.savefig("/home/claude/figures/fig1_injection_matrix.png", bbox_inches=None)
plt.close(fig)

# ---------------------------------------------------------------- FIG 2: horizon x 24
fig, ax = plt.subplots(figsize=(11, 7), dpi=160)
fig.subplots_adjust(left=0.10, right=0.93, top=0.78, bottom=0.12)
xs = np.linspace(0, 95, 100)
ax.plot(xs, 24 * xs, color=BLUE, lw=2, zorder=2)
pts = [(7, 168, "DeepSeek", "o"), (14, 336, "DeepSeek", "o"), (90, 2160, "DeepSeek", "o"),
       (7, 168, "Claude", "s"), (7, 168, "Gemini", "^")]
off = {"o": -1.6, "s": 0.0, "^": 1.6}
for x, y, m, mk in pts:
    ax.scatter(x + (off[mk] if x == 7 else 0), y, marker=mk, s=90, fc="white", ec=BLUE, lw=2, zorder=3)
for y in [72, 96, 120, 144]:
    ax.axhline(y, color=GRID, lw=1.2, ls=(0, (4, 3)), zorder=1)
ax.annotate("no clause in the prompt →\nmodel-specific defaults: 72 / 96 / 120 / 144",
            xy=(48, 144), xytext=(40, 460), fontsize=9.5, color=MUT,
            arrowprops=dict(arrowstyle="->", color=MUT, lw=1))
ax.annotate("rounds = horizon × 24\nexact on 5/5 observations,\n3 model families", xy=(55, 24 * 55),
            xytext=(30, 1750), fontsize=11, color=BLUE, fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=BLUE, lw=1))
ax.annotate('"over the next 90 days"\n→ 2,160-round commitment\n(no cap, no sanity check)', xy=(90, 2160),
            xytext=(58, 2080), fontsize=10, color=ORANGE, ha="left",
            arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.2))
ax.text(4, 320, "7d → 168\n(all 3 models)", fontsize=9, color=MUT)
ax.set_xlim(0, 96); ax.set_ylim(0, 2350)
ax.set_xlabel("Horizon in the prompt (days)", fontsize=11)
ax.set_ylabel("Rounds the system commits to", fontsize=11)
ax.grid(axis="y", color=GRID, lw=0.6); [ax.spines[s].set_visible(False) for s in ["top", "right"]]
from matplotlib.lines import Line2D
ax.legend(handles=[Line2D([], [], marker="o", ls="", mfc="white", mec=BLUE, label="DeepSeek V3"),
                   Line2D([], [], marker="s", ls="", mfc="white", mec=BLUE, label="Claude Sonnet 4"),
                   Line2D([], [], marker="^", ls="", mfc="white", mec=BLUE, label="Gemini 2.5 Flash"),
                   Line2D([], [], color=GRID, ls=(0, (4, 3)), label="No-horizon defaults")],
          loc="upper left", frameon=False, fontsize=9.5, bbox_to_anchor=(0.01, 0.99))
header(fig,
       "One phrase becomes a resource commitment: rounds = horizon × 24",
       "rounds_inferred vs horizon clause · 5 runs with a horizon clause, 3 model families · defaults without a clause shown dashed\n"
       "The law is a property of the pipeline's config-generation step, not of any model.",
       "github.com/Quantum-eon/mirror-audit · data/master_runs.csv · captured verbatim at stage “05 Preparation completed” · n=5 (+4 defaults)",
       "Part 6/8")
fig.savefig("/home/claude/figures/fig2_horizon_law.png", bbox_inches=None)
plt.close(fig)

# ---------------------------------------------------------------- FIG 3: one input, four worlds
runs = ["B3", "REP2", "REP3", "REP4"]
nodes = [11, 10, 10, 11]; edges = [6, 9, 6, 8]
monarch = [1, 1, 1, 1]; verdict = ["flags\nsanctions", "BLIND", "flags\nsanctions", "flags\nUNHRC"]
japan = [0, 0, 0, 1]
fig, ax = plt.subplots(figsize=(11, 6.2), dpi=160)
fig.subplots_adjust(left=0.09, right=0.70, top=0.76, bottom=0.13)
x = np.arange(4)
for i in x:
    ax.plot([i, i], [edges[i], nodes[i]], color=GRID, lw=2, zorder=1)
ax.scatter(x, nodes, s=150, fc=BLUE, ec="white", lw=1.5, zorder=3, label="Graph nodes")
ax.scatter(x, edges, s=150, fc="white", ec=BLUE, lw=2, zorder=3, label="Graph edges")
for i in x:
    ax.text(i + 0.09, nodes[i] + 0.12, str(nodes[i]), fontsize=11, fontweight="bold", color=BLUE)
    ax.text(i + 0.09, edges[i] - 0.34, str(edges[i]), fontsize=11, color=BLUE)
    v = verdict[i]
    col = ORANGE if v == "BLIND" else BLUE
    ax.text(i, 13.3, v, ha="center", fontsize=10, color=col,
            fontweight="bold" if v == "BLIND" else "normal")
    if japan[i]:
        ax.text(i, edges[i] - 1.25, "+ Japan node", ha="center", fontsize=8.5, color=PURPLE)
ax.text(1, 14.6, "report-level verdict:", fontsize=9, color=MUT, ha="center")
ax.annotate("richest graph — still blind:\ngating is about WHICH facts\nland in the graph, not how many",
            xy=(1, 9.6), xytext=(1.55, 4.2), fontsize=10, color=ORANGE,
            arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.2))
ax.set_xticks(x); ax.set_xticklabels([f"{r}\n(monarch: yes)" for r in runs], fontsize=10)
ax.set_ylim(0, 16); ax.set_ylabel("Count", fontsize=11)
ax.grid(axis="y", color=GRID, lw=0.6); [ax.spines[s].set_visible(False) for s in ["top", "right"]]
ax.legend(loc="lower right", frameon=False, fontsize=10)
fig.text(0.73, 0.60, "Same bytes in.\nFour different\nworlds out.", fontsize=15, fontweight="bold", color=INK)
fig.text(0.73, 0.44, "Byte-identical seed +\nprompt, same model,\nsame settings — graph\nextraction is stochastic,\nand the verdict follows\nthe graph.", fontsize=10, color=MUT, va="top")
header(fig,
       "Same input, four worlds — and the verdict follows the graph",
       "Valdoria seed × DeepSeek V3, no-horizon · identical input bytes (sha256-verified) · graph size, cast and report verdict per run",
       "github.com/Quantum-eon/mirror-audit · data/master_runs.csv · n = 4 byte-identical replicas (B3 anchor + REP2–4)",
       "Part 3/8")
fig.savefig("/home/claude/figures/fig3_four_worlds.png", bbox_inches=None)
plt.close(fig)
print("done")
