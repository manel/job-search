"""Merge duplicate Basecamp project names into one Markdown table, sorted by first year."""
import collections
import re
import sys

alias = {
    "10a1.com - Wed redesign": "10a1.com - Web redesign",
    "Campanyes Stan James To-Do List: Upcoming": "Campanyes Stan James",
    "Projects To-Do List: On going": "Campanyes Stan James",
    "Projects": "Campanyes Stan James",
    "Campanyes 10a1.com": "Campanyes Stan James",
    "Bifrutas Geocaching KoM + Strabinarius": "Bifrutas Geocaching",
    "Bifrutas Geocaching KoM + Strabinarius To-Do List: To-Dos Bifrutas previ llançament": "Bifrutas Geocaching",
    "SNTalent Imagen corporativa y website": "Imagen corporativa y website",
    "SNTalent: SNTalent maquetación": "SNTalent maquetación",
    "Codifel: TPBarcelona": "TPBarcelona", "TPB": "TPBarcelona",
    "TPBarcelona website": "TPBarcelona", "TP Barcelona website": "TPBarcelona",
    "Kings of Mambo: Proyectos varios con Jim": "Proyectos varios con Jim",
    "Québueno.es": "QUEBUENO.ES", "Pares i Nens - KoM + Gyo": "Pares i nens",
    "Àlex Rovira": "Alexrovira.com", "Álex Rovira": "Alexrovira.com",
    "8TV website": "8TV: 8TV website", "8 al dia website": "8TV: 8 al dia website",
    "Parc Sanitari Sant Joan de Déu": "Parc Sanitari Sant Joan de Dèu",
    "Redisseny web Intercom": "Redisseny web corporatiu", "Hair by Vueling": "Hairbyvueling.com",
    "enracha Digital": "enracha", "Revista enracha2": "enracha", "EnRacha campanyes online": "enracha",
    "EnRacha app": "enracha app equip Barcelona", "Els Vilars Rurals SEHRS": "Els Vilars Rurals SERHS",
    "vLex App + Mortensen": "vLex App", "KYMCO - eBikes": "Kymco eBikes", "KYMCO": "Kymco",
    "Liquens": "Líquens", "SCW 2020 Watchity": "Smart City Week 2020", "FUNK3D": "Funk3D",
    "Joinenergy": "JoinEnergy", "FFWi - Manteniments": "FFWi", "Opertek Marketing y SEO": "Opertek",
    "Mind Analytics RRSS": "Mind Analytics", "Ciutat Proactiva 2021": "Ciutat Proactiva",
    "COS Creix": "COS Cooperativa", "COS landing": "COS Cooperativa", "Mailings juntspelsi": "juntspelsi.cat",
    "Josep Manel Ventosa": "Josep Maria Ventosa website", "The Coffee Experience": "The Coffee Market",
    "Viral candidatos Navidad 2009": "Viral candidatos",
}
internal = {"Información común", "Tareas semanales", "CAMON", "Kings of Mambo website 2009",
            "2009-Corporativo-Andrea-Nuevo logo", "Projectes amb la Carla", "Kings of Mambo - Mandril Beer",
            "KoM", "Creativitats KoM", "Invoice", "Proyectos varios con Jim", "Mailing",
            "Comunicació i campanya aire", "WEB (Tecnologia", "WEB i XARXES"}

merged = collections.OrderedDict()
for line in open(sys.argv[1], encoding="utf-8"):
    name, co, yr, n = line.rstrip("\n").split("\t")
    key = alias.get(name, name)
    e = merged.setdefault(key, {"co": "", "y": [], "n": 0})
    e["co"] = e["co"] or co
    e["y"] += [int(x) for x in re.findall(r"\d{4}", yr)]
    e["n"] += int(n)

print("| Project (Basecamp name) | Client | Years | Messages |\n|---|---|---|---|")
for k, v in sorted(merged.items(), key=lambda x: (min(x[1]["y"]), x[0].lower())):
    if k in internal:
        continue
    a, b = min(v["y"]), max(v["y"])
    print(f"| {k} | {v['co']} | {a if a == b else f'{a} to {b}'} | {v['n']} |")
print("\nInternal KoM projects: " + ", ".join(sorted(k for k in merged if k in internal)) + ".")
