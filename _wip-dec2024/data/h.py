import json, os
FIGS = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'figs', 'figs.json')))
def P(h): return {"t": "p", "h": h}
def IMG(k, alt):
    f = FIGS[k]
    return {"t": "img", "src": f['src'], "w": f['w'], "h": f['h'], "alt": alt}
def TBL(head, rows, cls=""):
    return {"t": "tbl", "cls": cls, "rowHead": False, "head": [head] if head else [], "rows": rows}
def MATCH(rows, head=("Column X", "Column Y")):
    return TBL(list(head), rows, "match")
def E(correct, wrong=None, notes=None):
    e = {"correct": correct}
    if wrong: e["wrong"] = wrong
    if notes: e["notes"] = notes
    return e
def Q(part, unit, blocks, options, expl, accept=None):
    q = {"part": part, "unit": unit, "blocks": blocks,
         "options": [{"key": str(i + 1), "text": t} for i, t in enumerate(options)],
         "explanation": expl}
    if accept: q["accept"] = accept
    return q
