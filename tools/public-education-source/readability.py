"""Flesch-Kincaid grade with a heuristic syllable counter (no network corpus)."""
import re
def syl(w):
    w=w.lower(); w=re.sub(r'[^a-z]','',w)
    if not w: return 0
    if len(w)<=3: return 1
    w=re.sub(r'(?:[^laeiouy]es|ed|[^laeiouy]e)$','',w); w=re.sub(r'^y','',w)
    return max(1,len(re.findall(r'[aeiouy]{1,2}',w)))
def fk(text):
    sents=[s for s in re.split(r'[.!?:;—]+\s|\n',text) if s.strip()]
    words=re.findall(r"[A-Za-z][A-Za-z'\-]*|\d+",text)
    s=sum(syl(w) for w in words)
    return 0.39*len(words)/len(sents)+11.8*s/len(words)-15.59, len(words)/len(sents)
def blocks_text(blocks):
    out=[]
    for b in blocks:
        if b[0] in('p','h'): out.append(b[1])
        elif b[0] in('ul','ul2'): out+=b[1]
        elif b[0] in('key','help','tip'): out+=b[2]
        elif b[0]=='tiers': out+=[i for _,_,its in b[1] for i in its]
        elif b[0]=='break' and len(b)>1: break
        elif b[0]=='table': out+=[c for r in b[2] for c in r if c]
    return '\n'.join(re.sub('<[^>]+>','',x) for x in out)
if __name__=='__main__':
    from leaflet_content import LEAFLETS
    for L in LEAFLETS:
        g,wps=fk(blocks_text(L['en']))
        ar=blocks_text(L['ar']); n=len(ar.split()); ns=len([s for s in re.split(r'[.؟!:\n]',ar) if s.strip()])
        print(f"{L['slug']:22} EN grade {g:.1f} ({wps:.1f} words/sentence) · AR {n/ns:.1f} words/sentence")
