#!/usr/bin/env python3
"""
build_layouts.py - regenerate data/odyssey_layouts.json from Odyssey Site Maps.

Reads the map JSON files of a local clone of Voz DeCarabas' Odyssey Site
Maps (https://github.com/voz-decarabas/Odyssey-Site-Maps) and writes, per
settlement layout: its economy, size class, buildings (OMG labels mapped to
Inara's building codes) and data ports, each port attributed to a building.

Port attribution: by the port's own description when it names a building
("hab data port", "Lab data port 1", "Security Data Port"), else to the
nearest building label on the map. Labels sit roughly in the middle of a
building, so the nearest-label guess can be wrong between two close
buildings - the per-layout total is exact (as exact as the map, see
On-Foot.md §5: Extraction 2 misses one port).

The "pads" field is NOT on the OMG data: it is read from the map images by
hand (see PADS below) and kept as it is in the existing JSON when the file
is regenerated, so corrections made from play survive a rebuild.

Usage:
  git clone --depth 1 https://github.com/voz-decarabas/Odyssey-Site-Maps.git
  python tools/build_layouts.py Odyssey-Site-Maps
"""

import glob
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "odyssey_layouts.json")

# OMG folder -> Spansh settlement economy
ECONOMY = {"agriculture": "Agriculture", "extraction": "Extraction",
           "high_tech": "High Tech", "industrial": "Industrial",
           "military": "Military", "tourist": "Tourism"}
# OMG building label -> Inara location code. LAB = research (Inara "RES"),
# SEC/OPR = security / operations, counted with command (Inara "CMD"),
# PROC = processing, counted with industrial (Inara "IND").
BUILDING = {"LAB": "RES", "SEC": "CMD", "OPR": "CMD", "PROC": "IND"}
# Port description keyword -> building code
PORT_WORDS = (("hab", "HAB"), ("lab", "RES"), ("sec", "CMD"),
              ("pwr", "PWR"), ("power", "PWR"), ("ind", "IND"),
              ("cmd", "CMD"))

# Ports the nearest-label rule gets wrong, checked on the map images (24 Nov
# 2026): (layout, n-th data port of the map file, from 1) -> building. The
# labels sit at a building's edge, not its middle, so a port in a big
# building can be nearer the label of a small one next door.
PORT_FIX = {
    ("high_tech_01", 3): "CMD",    # east wing of CMD, upper floor (not PWR)
    ("military_02", 5): "CMD",     # CMD building, under the dish (not PWR)
    ("agriculture_04", 3): "AGRI",  # central AGRI building (not STO)
}

# Landing pads, 24 Nov 2026: pad count read from the map images, sizes from
# a Spansh census of 20,000 settlements (150 ly around Cubeo and Sol): each
# economy has only a few pad signatures, about one per layout, and the
# settlements visited in play confirm them (Agri 1 and 3, Ext 2, Mil 3,
# Tour 4). "?" = still to check in game: Ext 4 / Ext 5 share S1 and M1, and
# Industrial has both S1 and M1 for Ind 1 alone (a 6th, unmapped layout?).
# Same signature, different layouts: tell them apart by the in-game size
# marker (tiny "-", small "+", medium "++").
PADS = {
    "agriculture_01": "L1 S1",
    "agriculture_02": "S1",
    "agriculture_03": "L1 S1",
    "agriculture_04": "L1 S2",
    "agriculture_05": "S1",
    "extraction_01": "L1 S1",
    "extraction_02": "L1 S1",
    "extraction_03": "L1",
    "extraction_04": "S1?",
    "extraction_05": "M1?",
    "high_tech_01": "L1 S1",
    "high_tech_02": "S1",
    "high_tech_03": "L1 S1",
    "high_tech_04": "S3",
    "industrial_01": "M1?",
    "industrial_02": "L1",
    "industrial_03": "L1",
    "industrial_04": "L1 S1",
    "industrial_05": "L1",
    "military_01": "L1 S2",
    "military_02": "L1 S2",
    "military_03": "M1 S1",
    "military_04": "M1",
    "military_05": "S1",
    "tourist_01": "L2 S2",
    "tourist_02": "M1",
    "tourist_03": "L1 S2",
    "tourist_04": "L1 S1",
}


def norm_id(raw):
    m = re.match(r"([a-z_]+?)_?0?(\d+)$", raw.lower())
    return "%s_%02d" % (m.group(1).rstrip("_"), int(m.group(2)))


def port_building(port, labels):
    desc = (port.get("description") or "").lower()
    for word, code in PORT_WORDS:
        if re.search(r"\b" + word, desc):
            return code
    best = min(labels, key=lambda l: math.hypot(
        float(l["x"]) - float(port["x"]),
        float(l["y"]) - float(port["y"])))
    return best["code"]


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    root = sys.argv[1]
    index = json.load(open(os.path.join(root, "maps", "index.json")))
    titles = {norm_id(m["id"]): m["name"] for v in index.values() for m in v}
    try:
        old = json.load(open(OUT))["layouts"]
    except (OSError, ValueError, KeyError):
        old = {}

    layouts = {}
    for folder, economy in ECONOMY.items():
        for path in sorted(glob.glob(os.path.join(root, "maps", folder,
                                                  folder + "_*.json"))):
            raw = json.load(open(path))
            lid = norm_id(raw["id"])
            labels = [dict(l, code=BUILDING.get(l["text"], l["text"]))
                      for l in raw.get("labels", [])]
            buildings = {}
            for l in labels:
                buildings[l["code"]] = buildings.get(l["code"], 0) + 1
            ports, n = {}, 0
            for m in raw.get("markers", []):
                if m.get("type") == "dataPort":
                    n += 1
                    code = PORT_FIX.get((lid, n)) or port_building(m, labels)
                    ports[code] = ports.get(code, 0) + 1
            title = titles.get(lid, raw.get("name", lid))
            size = re.search(r"(tiny|small|medium|large)", title.lower())
            layouts[lid] = {
                "name": re.sub(r"\s+", " ", title.split(" - ")[0]).strip(),
                "economy": economy,
                "size": size.group(1) if size else "?",
                "buildings": dict(sorted(buildings.items())),
                "data_ports": dict(sorted(ports.items())),
                "pads": old.get(lid, {}).get("pads") or PADS.get(lid, "?"),
                "alarm_panels": sum(1 for m in raw.get("markers", [])
                                    if m.get("type") == "alarmPanel"),
                "map_updated": (raw.get("metadata") or {}).get("updated"),
            }
            if old.get(lid, {}).get("notes"):
                layouts[lid]["notes"] = old[lid]["notes"]

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({"source": "Odyssey Site Maps (Voz DeCarabas), "
                             "github.com/voz-decarabas/Odyssey-Site-Maps",
                   "building_codes": BUILDING, "layouts": layouts},
                  fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print("%d layouts written to %s" % (len(layouts), OUT))


if __name__ == "__main__":
    main()
