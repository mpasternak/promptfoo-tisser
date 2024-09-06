"""
Skrypt do testowania wartości zwracanych z modeli LLM pod kątem oceny ich
zgodności z oczekiwanymi wartościami dla pól skali TISS-28.
"""

from typing import Union, Any, Dict
import json
import tiss28


def get_assert(output: str, context) -> Union[bool, float, Dict[str, Any]]:
    output = output.strip()

    if output.startswith("```json"):
        # Model może zwrócić kod json zaczynający się od ciągu typowego dla
        # dokumentów w formacie RST czyli "```json", na końcu tak samo "```"
        output = output[7:-3].strip()

    # Model może zwrócić wartości kluczy wielkimi literami lub wartości
    # false jako "False" czyli niezgodnie z formatem json
    output = output.lower()

    output = json.loads(output)

    slownik = None

    if "1g" in output and "1h" in output:
        try:
            slownik = dict(
                [(x["numer_punktu"], x["odpowiedz"]) for x in output.values()]
            )
        except TypeError:
            pass

    if not slownik:
        try:
            slownik = dict([(x["numer_punktu"], x["odpowiedz"]) for x in output])
        except TypeError:
            try:
                # Claude 3.5 Sonnet ma tu klucz 'odpowiedzi'
                toplevel = "odpowiedzi"
                if "support_messages" in output:
                    # OpenAI GPT-4o ma klucz `supported_messages`
                    toplevel = "support_messages"

                slownik = dict(
                    [(x["numer_punktu"], x["odpowiedz"]) for x in output[toplevel]]
                )
            except KeyError:
                # ... zaś OpenAI GPT 4o-mini zwraca po prostu klucze i wartości
                slownik = dict([(x, y) for x, y in output.items()])

    score = 0.0
    total = float(len(slownik.keys()))
    if total == 0:
        # Jeżeli jest zero kluczy w odpowiedzi z LLMa, zwróć błąd.
        return {
            "pass": False,
            "score": 0,
            "reason": "brak kluczy w slowniki zwroconego JSON",
        }

    errors = []

    for elem in tiss28.klucze:
        if slownik.get(elem) is None:
            # Jeżeli jakiegoś z kluczy, które weryfikujemy nie ma w odpowiedzi
            # LLMa, raportuj błąd
            errors.append(
                "brak klucza %s (%s) w zwroconym JSON" % (elem, tiss28.opisy[elem])
            )
            continue

        zwrocono = slownik[elem]
        poszukiwano = context["vars"].get(elem)
        if poszukiwano is None:
            # tego klucza nie ma w kontekscie, czyli w liście zmiennych zadeklarowanych
            # w słowniku 'vars', czyli ten klucz nas nie interesuje:
            total -= 1
            continue

        if zwrocono != poszukiwano:
            # jeżeli wartości z modelu i z klucza się różnią
            errors.append(
                "Różnica punktu %s (%s) (oczekiwano: %s, model obliczył: %s)"
                % (elem, tiss28.opisy[elem], poszukiwano, zwrocono)
            )
            continue

        score += 1

    if total == 0:
        return {
            "pass": False,
            "score": 0,
            "reason": "nie podano zadnych punktow skali do weryfikacji",
        }

    if errors:
        return {"pass": False, "score": score / total, "reason": ". ".join(errors)}

    return {"pass": True, "score": score / total, "reason": "OK"}
