# 2do https://www.youtube.com/results?search_query=tuto+python+en+fran%C3%A7ais
import sys, os
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

tools_path = Path(__file__).parent.parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import dg, fg, lg, cls, exit, pf

cls("Pie/")

if __name__ == "__main__":

    lg = "\n" + "-" * 55
    print("{0: ^55}".format("Pie"))
    print(lg)

    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    recipe = ["375 g flour", "75 g sugar", "250 g butter", "300 g berries"]

    data = [float(x.split()[0]) for x in recipe]
    ingredients = [x.split()[-1] for x in recipe]

    def func(pct, allvals):
        absolute = int(np.round(pct / 100.0 * np.sum(allvals)))
        return f"{pct:.1f}%\n({absolute:d} g)"

    wedges, texts, autotexts = ax.pie(
        data, autopct=lambda pct: func(pct, data), textprops=dict(color="w")
    )

    ax.legend(
        wedges,
        ingredients,
        title="Ingredients",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
    )

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title("Matplotlib bakery: A pie")

    plt.show()

    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    recipe = [
        "225 g flour",
        "90 g sugar",
        "1 egg",
        "60 g butter",
        "100 ml milk",
        "1/2 package of yeast",
    ]

    data = [225, 90, 50, 60, 100, 5]

    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1) / 2.0 + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = f"angle,angleA=0,angleB={ang}"
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(
            recipe[i],
            xy=(x, y),
            xytext=(1.35 * np.sign(x), 1.4 * y),
            horizontalalignment=horizontalalignment,
            **kw,
        )

    ax.set_title("Matplotlib bakery: A donut")

    plt.show()
