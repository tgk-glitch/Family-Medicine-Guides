"""Small HTML helpers for bilingual content modules."""

def ul(items):
    return '<ul>' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'

def ol(items):
    return '<ol>' + ''.join('<li>%s</li>' % i for i in items) + '</ol>'

def p(t):
    return '<p>%s</p>' % t

def tbl(head, rows, wide=False):
    h = '<thead><tr>' + ''.join('<th>%s</th>' % c for c in head) + '</tr></thead>'
    b = '<tbody>' + ''.join('<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>' for r in rows) + '</tbody>'
    return '<div class="cs-table-wrap%s"><table>%s%s</table></div>' % (' fmg-wide' if wide else '', h, b)

def blk(kind, bid, en_title, ar_title, en, ar):
    """kind: glance flag tool features dx ddx mx special prev comp dispo prog fu tell local trap note exam evidence"""
    return dict(kind=kind, id=bid, t_en=en_title, t_ar=ar_title, en=en, ar=ar)
