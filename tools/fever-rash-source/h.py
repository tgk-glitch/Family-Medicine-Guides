"""Small HTML helpers for bilingual content modules (fever-with-rash page, prefix fr-)."""

def ul(items):
    return '<ul>' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'

def ol(items):
    return '<ol>' + ''.join('<li>%s</li>' % i for i in items) + '</ol>'

def p(t):
    return '<p>%s</p>' % t

def tbl(head, rows, wide=False):
    h = '<thead><tr>' + ''.join('<th>%s</th>' % c for c in head) + '</tr></thead>'
    import re as _re, html as _h
    lab = [_h.escape(_re.sub(r'<[^>]+>', '', c)) for c in head]
    b = '<tbody>' + ''.join('<tr>' + ''.join('<td data-label="%s">%s</td>' % (lab[i], c) for i, c in enumerate(r)) + '</tr>' for r in rows) + '</tbody>'
    return '<div class="fr-table-wrap%s"><table>%s%s</table></div>' % (' fmg-wide' if wide else '', h, b)

def blk(kind, bid, en_title, ar_title, en, ar, figs=None):
    """kind: glance flag tool features dx ddx mx special prev comp dispo fu tell local trap note exam evidence ipc"""
    return dict(kind=kind, id=bid, t_en=en_title, t_ar=ar_title, en=en, ar=ar, figs=figs or [])
