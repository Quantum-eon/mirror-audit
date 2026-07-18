#!/usr/bin/env python3
"""MIRROR 'Editorial paper' style — per founder's references:
warm paper bg, coral/blue/periwinkle, big numerals, mono-caps captions,
pill badges, subtle grain, hatched fills, generous whitespace."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

PAPER = "#F2EDE3"; INK = "#171512"; MUT = "#7A7468"; LINE = "#DDD6C8"
CORAL = "#E8503A"      # fail / blindness / the surprise
BLUE = "#5D8CA8"       # norm / determinism
PERI = "#8D95E8"       # intervention / injection
MUST = "#D9A441"       # accent (sparingly)
SANS, MONO = "Liberation Sans", "Liberation Mono"

plt.rcParams.update({"font.family": SANS, "text.color": INK,
                     "xtick.color": MUT, "ytick.color": MUT,
                     "axes.labelcolor": MUT, "svg.fonttype": "none"})

def grain(fig):
    w, h = fig.canvas.get_width_height()
    rng = np.random.default_rng(7)
    noise = rng.random((h, w))
    fig.figimage(noise, xo=0, yo=0, alpha=0.035, cmap="gray", zorder=50,
                 origin="lower")

def chrome(fig, title, sub, footer, part, pcol=CORAL):
    fig.text(0.06, 0.945, title, fontsize=20, fontweight="bold", va="top",
             color=INK, fontfamily=SANS)
    fig.text(0.06, 0.868, sub.upper(), fontsize=8.6, va="top", color=MUT,
             fontfamily=MONO)
    # footer rule + mono caps
    fig.lines.append(plt.Line2D([0.06, 0.94], [0.062, 0.062],
                     transform=fig.transFigure, color=INK, lw=0.8))
    fig.text(0.06, 0.032, footer.upper(), fontsize=7.6, va="top", color=MUT,
             fontfamily=MONO)
    fig.text(0.94, 0.032, f"MIRROR — {part}".upper(), fontsize=7.6, va="top",
             ha="right", color=INK, fontfamily=MONO,
             bbox=dict(boxstyle="round,pad=0.38", fc=pcol, ec="none", alpha=0.25))

def pill(fig, x, y, txt, fc, tc=INK, fs=8.6):
    fig.text(x, y, txt.upper(), fontsize=fs, color=tc, fontfamily=MONO,
             ha="center", va="center",
             bbox=dict(boxstyle="round,pad=0.45", fc=fc, ec="none"))

# ================================================================ FIG A: injection
absurds = ["DUAL CURRENCY PEG", "LANDLOCKED + DEEP-SEA FLEET", "ELECTED MONARCH, 47 YRS",
           "14 PARTIES × EQUAL SEATS", "340M PEOPLE / 850 KM²", "UN-SANCTIONED + UNHRC CHAIR",
           "LIFE EXPECTANCY 147", "BORDERS INCL. JAPAN"]
ctrl = np.zeros((8, 4)); ctrl[5, 1] = ctrl[5, 2] = ctrl[5, 3] = 1
inj = np.ones((8, 2)); inj[0, 0] = inj[6, 0] = 0; inj[0, 1] = inj[3, 1] = inj[6, 1] = 0
runs_c, runs_i = ["REP2", "REP3", "REP4", "B3"], ["INJ 1", "INJ 2"]

fig = plt.figure(figsize=(12.6, 7.2), dpi=160)
fig.patch.set_facecolor(PAPER)
gs = fig.add_gridspec(1, 2, width_ratios=[4, 2.05], left=0.30, right=0.72,
                      top=0.66, bottom=0.17, wspace=0.16)
axc, axi = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])
for ax, runs, M, col in [(axc, runs_c, ctrl, BLUE), (axi, runs_i, inj, PERI)]:
    ax.set_facecolor(PAPER)
    ax.set_xlim(-0.5, len(runs) - 0.5); ax.set_ylim(-0.6, 7.6); ax.invert_yaxis()
    for y in range(8):
        ax.axhline(y, color=LINE, lw=0.7, zorder=1)
        for x in range(len(runs)):
            on = M[y, x] == 1
            if on:  # soft glow
                ax.scatter(x, y, s=1500, marker="o", fc=col, ec="none",
                           alpha=0.15, zorder=2)
            ax.scatter(x, y, s=340, marker="o", fc=col if on else PAPER,
                       ec=col if on else "#B9B29F", lw=1.4, zorder=3)
    ax.set_xticks(range(len(runs)))
    ax.set_xticklabels(runs, fontsize=9, fontfamily=MONO)
    ax.set_yticks(range(8)); ax.tick_params(length=0)
    [s.set_visible(False) for s in ax.spines.values()]
    ax.grid(False)
axc.set_yticklabels(absurds, fontsize=8.6, color=INK, fontfamily=MONO)
axi.set_yticklabels([])
for x, t in zip(range(4), ["0/8", "1/8", "1/8", "1/8"]):
    axc.text(x, -1.25, t, ha="center", fontsize=9.5, color=MUT, fontfamily=MONO)
for x, t in zip(range(2), ["6/8", "5/8"]):
    axi.text(x, -1.25, t, ha="center", fontsize=11, fontweight="bold",
             color=PERI, fontfamily=MONO)
axc.text(0.5, 1.16, "CONTROL — UNTOUCHED PIPELINE", transform=axc.transAxes,
         ha="center", fontsize=8.6, color=INK, fontfamily=MONO,
         bbox=dict(boxstyle="round,pad=0.45", fc="#E3DCCB", ec="none"))
axi.text(0.5, 1.16, "INJECTED INTO GRAPH", transform=axi.transAxes,
         ha="center", fontsize=8.6, color="white", fontfamily=MONO,
         bbox=dict(boxstyle="round,pad=0.45", fc=PERI, ec="none"))
# big numeral block, WeTransfer-style
fig.text(0.745, 0.585, "0→6", fontsize=54, fontweight="bold", color=CORAL,
         ha="left", va="center", fontfamily=SANS)
fig.text(0.905, 0.615, "/8", fontsize=16, color=CORAL, ha="left",
         va="center", fontfamily=MONO, fontweight="bold")
fig.text(0.745, 0.485, "absurdities flagged once\nthey reach the graph", fontsize=11.5,
         color=INK, ha="left", va="top", fontfamily=SANS)
fig.text(0.745, 0.375, "The report layer isn't blind.\nIt's starved.", fontsize=12,
         color=INK, ha="left", va="top", fontstyle="italic", fontfamily=SANS)
chrome(fig,
       "One intervention flips the audit verdict",
       "report-level Q3 flags per seeded absurdity · valdoria seed · byte-identical input · deepseek v3 · cell layout illustrative, totals observed",
       "github.com/quantum-eon/mirror-audit · data/injection_runs.csv · pre-registered criterion ≥3: met",
       "part 3/8", PERI)
grain(fig)
fig.savefig("/home/claude/figures/ed_fig1_injection.png", facecolor=PAPER)
plt.close(fig)

# ================================================================ FIG B: horizon law
fig, ax = plt.subplots(figsize=(12.6, 7.2), dpi=160)
fig.patch.set_facecolor(PAPER); ax.set_facecolor(PAPER)
fig.subplots_adjust(left=0.09, right=0.70, top=0.70, bottom=0.15)
xs = np.linspace(0, 95, 200)
ax.fill_between(xs, 0, 24 * xs, color=BLUE, alpha=0.06, hatch="///",
                edgecolor=BLUE, linewidth=0, zorder=1)
ax.plot(xs, 24 * xs, color=BLUE, lw=2.4, zorder=3)
pts = [(7, 168, "o"), (14, 336, "o"), (90, 2160, "o"), (7, 168, "s"), (7, 168, "^")]
off = {"o": -1.8, "s": 0.0, "^": 1.8}
for x, y, mk in pts:
    ax.scatter(x + (off[mk] if x == 7 else 0), y, marker=mk, s=95, fc=PAPER,
               ec=INK, lw=1.6, zorder=4)
# glow on the 2160 point
for r, a in [(2600, 0.10), (1200, 0.16), (420, 0.9)]:
    ax.scatter(90, 2160, s=r, fc=CORAL if a > 0.5 else CORAL, ec="none",
               alpha=a, zorder=5 if a > 0.5 else 2)
for y in [72, 96, 120, 144]:
    ax.axhline(y, color=MUT, lw=0.8, ls=(0, (3, 4)), alpha=0.6, zorder=2)
ax.annotate("NO CLAUSE → MODEL DEFAULTS 72–144", xy=(43, 144), xytext=(36, 500),
            fontsize=8, color=MUT, fontfamily=MONO,
            arrowprops=dict(arrowstyle="-", color=MUT, lw=0.8))
ax.text(46, 1330, "ROUNDS = HORIZON × 24", fontsize=10.5, color=BLUE,
        fontfamily=MONO, fontweight="bold", rotation=38.5,
        rotation_mode="anchor", ha="center", va="bottom")
ax.set_xlim(0, 96); ax.set_ylim(0, 2400)
ax.set_xticks([0, 7, 14, 30, 60, 90])
ax.set_yticks([0, 500, 1000, 1500, 2000])
ax.set_xlabel("HORIZON IN THE PROMPT, DAYS", fontsize=8.6, fontfamily=MONO, labelpad=8)
ax.set_ylabel("COMMITTED ROUNDS", fontsize=8.6, fontfamily=MONO, labelpad=8)
for lab in ax.get_xticklabels() + ax.get_yticklabels():
    lab.set_fontfamily(MONO); lab.set_fontsize(8.6)
ax.grid(axis="y", color=LINE, lw=0.8); ax.set_axisbelow(True)
[s.set_visible(False) for s in ax.spines.values()]
ax.tick_params(length=0)
# right column: numeral + story
fig.text(0.735, 0.62, "2,160", fontsize=52, fontweight="bold", color=CORAL,
         ha="left", va="center", fontfamily=SANS)
fig.text(0.735, 0.525, "ROUNDS FROM THE PHRASE\n“OVER THE NEXT 90 DAYS”", fontsize=9,
         color=INK, ha="left", va="top", fontfamily=MONO)
fig.text(0.735, 0.43, "No cap. No sanity check.\nSame ×24 rule on DeepSeek,\nClaude and Gemini — the law\nlives in the pipeline, not\nin any model.", fontsize=11.5,
         color=INK, ha="left", va="top", fontfamily=SANS)
pill(fig, 0.775, 0.24, "3 model families · 5/5 exact", "#E3DCCB")
chrome(fig,
       "One phrase becomes a resource commitment",
       "rounds_inferred vs horizon clause · 5 runs with clause · defaults dashed · captured verbatim at stage 05",
       "github.com/quantum-eon/mirror-audit · data/master_runs.csv · n=5 (+4 defaults)",
       "part 6/8", CORAL)
grain(fig)
fig.savefig("/home/claude/figures/ed_fig2_horizon.png", facecolor=PAPER)
plt.close(fig)

# ================================================================ FIG C: four worlds
runs = ["B3", "REP2", "REP3", "REP4"]
nodes = [11, 10, 10, 11]; edges = [6, 9, 6, 8]
verdict = ["FLAGS SANCTIONS", "BLIND", "FLAGS SANCTIONS", "FLAGS UNHRC"]
fig, ax = plt.subplots(figsize=(12.6, 7.2), dpi=160)
fig.patch.set_facecolor(PAPER); ax.set_facecolor(PAPER)
fig.subplots_adjust(left=0.08, right=0.66, top=0.66, bottom=0.16)
x = np.arange(4)
for i in x:
    ax.plot([i, i], [edges[i], nodes[i]], color="#C9C2AF", lw=2.4, zorder=2)
ax.scatter(x, nodes, s=340, fc=INK, ec=PAPER, lw=2, zorder=3)
ax.scatter(x, edges, s=340, fc=PAPER, ec=INK, lw=1.8, zorder=3)
# glow behind the BLIND run
ax.scatter([1], [(nodes[1] + edges[1]) / 2], s=9000, fc=CORAL, ec="none",
           alpha=0.12, zorder=1)
for i in x:
    ax.text(i + 0.13, nodes[i], str(nodes[i]), fontsize=12, fontweight="bold",
            color=INK, va="center", fontfamily=SANS)
    ax.text(i + 0.13, edges[i], str(edges[i]), fontsize=12, color=MUT,
            va="center", fontfamily=SANS)
for i, v in enumerate(verdict):
    fc = CORAL if v == "BLIND" else "#E3DCCB"
    tc = "white" if v == "BLIND" else INK
    pill_x = 0.08 + (0.66 - 0.08) * (0.062 + 0.292 * i)  # approx axes->fig mapping
    ax.text(i, 13.6, v, ha="center", fontsize=8.2, color=tc, fontfamily=MONO,
            bbox=dict(boxstyle="round,pad=0.42", fc=fc, ec="none"))
ax.text(-0.45, 15.1, "REPORT-LEVEL VERDICT", fontsize=8, color=MUT, fontfamily=MONO)
ax.set_xticks(x)
ax.set_xticklabels([f"{r}" for r in runs], fontsize=9.5, fontfamily=MONO)
ax.set_ylim(0, 16); ax.set_yticks([0, 4, 8, 12, 16])
for lab in ax.get_yticklabels():
    lab.set_fontfamily(MONO); lab.set_fontsize(8.6)
ax.set_ylabel("GRAPH SIZE", fontsize=8.6, fontfamily=MONO, labelpad=8)
ax.grid(axis="y", color=LINE, lw=0.8); ax.set_axisbelow(True)
[s.set_visible(False) for s in ax.spines.values()]
ax.tick_params(length=0)
from matplotlib.lines import Line2D
ax.legend(handles=[Line2D([], [], marker="o", ls="", mfc=INK, mec=PAPER, ms=11, label="nodes"),
                   Line2D([], [], marker="o", ls="", mfc=PAPER, mec=INK, ms=11, label="edges")],
          loc="lower right", frameon=False, fontsize=9,
          prop={"family": MONO, "size": 9})
fig.text(0.70, 0.60, "Same bytes in.", fontsize=22, fontweight="bold",
         color=INK, ha="left", fontfamily=SANS)
fig.text(0.70, 0.525, "Four worlds out.", fontsize=22, fontweight="bold",
         color=CORAL, ha="left", fontfamily=SANS)
fig.text(0.70, 0.44, "Byte-identical seed and prompt,\nsame model, same settings.\nGraph extraction is stochastic —\nand the audit verdict follows\nthe graph, not the input.", fontsize=11.5,
         color=INK, ha="left", va="top", fontfamily=SANS)
pill(fig, 0.745, 0.235, "sha256-verified identical input", "#E3DCCB")
chrome(fig,
       "Same input, four different worlds",
       "valdoria seed × deepseek v3 · no-horizon · 4 byte-identical replicas · graph size, monarch in all four casts",
       "github.com/quantum-eon/mirror-audit · data/master_runs.csv · n=4 replicas (b3 + rep2–4)",
       "part 3/8", CORAL)
grain(fig)
fig.savefig("/home/claude/figures/ed_fig3_worlds.png", facecolor=PAPER)
plt.close(fig)
print("done")
