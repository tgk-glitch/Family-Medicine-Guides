# Build scripts: merged site, 15 Oct 2026

This site = public-education snapshot (13 pages) + counselling page + new
"Counselling & Communication" category. All scripts are idempotent.

Order used to produce Family-Medicine-Guides/:

1. Start from the public-education site; copy counselling.html and downloads/*.pdf from the counselling snapshot.
2. `python3 update_site.py`: wires counselling into the nav, Mental Health and Respiratory, homepage pill, directory, search (edit the SITE path at the top).
3. `python3 public-education-source/apply_updates.py SITE`: credit block, menu rows, wrap fix.
4. `python3 public-education-source/build_pages.py SITE` then `apply_updates.py SITE --entries public-education-source/_out/public_entries.json`: Patients hub now lists the quit-smoking leaflet.
5. `python3 add_counselling_category.py SITE`: new top-level category (homepage card, directory section, menu panel; 22 categories).

On the full 17-page copy from the main PC (counselling.html is already there): run steps 3–5.
