"""
Zakładamy, że klucze 1A-1F mają zazwyczaj ustaloną (z góry narzuconą) wartość
i nie zwracamy ich przez model LLM z uwagi na koszt tokenów.

#     "1a", "1b", "1c", "1d", "1e", "1f",

"""

opisy = {
    "1g": "częsta zmiana opatrunków",
    "1h": "pielęgnacja drenaży",
    "2a": "wentylacja mechaniczna",
    "2b": "leczenie tlenem",
    "2c": "sztuczne drogi oddechowe",
    "3a": "leki wazoaktywne",
    "3b": "więcej, niż jeden lek wazoaktywny",
    "3c": "masywna płynoterapia",
    "3d": "cewnik tętniczy",
    "3e": "cewnik Swana-Ganza",
    "3f": "cewnik w żyle centralnej",
    "3g": "RKO w OIT",
    "3h": "monitorowanie hemodynamiczne (termodylucja, dylucja litu, ODM)",
    "3i": "monitorowanie hemodynamiczne (kardiogrfia imped, bioreaktancja)",
    "3j": "monitorowanie hemodynamiczne (met. niekalibr)",
    "4a": "crrt",
    "4b": "monitorowanie diurezy",
    "4c": "diureza wymuszona",
    "5a": "leczenie kwasicy bikarbonatem",
    "5b": "żywienie IV",
    "5c": "żywienie do PP",
    "6a": "procedura w OIT",
    "6b": "procedury w OIT",
    "6c": "procedury poza OIT",
    "6d": "hipotermia ogólnoustr.",
    "6e": "hipotermia miejsc.",
    "7a": "ICP",
}


klucze = opisy.keys()
#
# klucze = [
#     "1g",
#     "1h",
#     "2a",
#     "2b",
#     "2c",
#     "3a",
#     "3b",
#     "3c",
#     "3d",
#     "3e",
#     "3f",
#     "3g",
#     "3h",
#     "3i",
#     "3j",
#     "4a",
#     "4b",
#     "4c",
#     "5a",
#     "5b",
#     "5c",
#     "6a",
#     "6b",
#     "6c",
#     "6d",
#     "6e",
#     "7a",
# ]
