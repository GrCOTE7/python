import tools.gc7 as gc7, os, subprocess, time
from tools.gc7 import EC, EW, ER, EN  # En Cyan, Rouge, En Normal


def comp(a, b):
    return -1 if a > b else (1 if b > a else 0)


@gc7.chrono
def run_script(lang):
    (
        subprocess.run(["python", "apps/count/n.py"])
        if lang == "python"
        else subprocess.run(["mojo", "run", "apps/count/n.mojo"])
    )


langs = ["python", "mojo"]
for n in [2e7]:  # [:5] pour test
    with open("apps/count/n.txt", "w") as f:
        f.write(str(int(n)))
    time.sleep(1)

    tps = {}
    for lang in langs:
        run_script(lang)
        tps[lang] = run_script.duration

        line = f"\b\b... J'ai compté jusqu'à {EC}{gc7.nf(n,0):>17}{EN} en {EW}{lang[0].upper() + lang[1:].lower():^6}{EN} → ⏱️ : {ER}{gc7.nf(run_script.duration,2):>9}{EN} secondes"
        print(line)
    
    print(tps)

    print("─" * (gc7.rawStrLength(line)[0] + 4))
print("Fini:", gc7.theTime())
