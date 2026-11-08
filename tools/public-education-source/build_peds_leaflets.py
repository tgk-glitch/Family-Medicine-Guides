"""Build only the Peds ER parent leaflets.  usage: python3 build_peds_leaflets.py SITE_SRC   (e.g. ../../src)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leaflet_content
from peds_leaflets import PEDS_LEAFLETS
leaflet_content.LEAFLETS[:] = PEDS_LEAFLETS      # build only the two new leaflets
import build_leaflets
for r in build_leaflets.build(sys.argv[1]):
    print('%-22s %s  page overflow(px)=%s  card overflow(px)=%s' % r)
