import os
import re
from datetime import datetime

# Source and Output Paths
TARGET_DIR = os.path.expanduser("~/Court_Affairs")
OUTPUT_HTML = os.path.expanduser("~/timeline_view.html")

# Verify base infrastructure exists
if not os.path.exists(TARGET_DIR):
    os.makedirs(TARGET_DIR)

def compile_timeline_data():
    events = []
    # Strict master regex signature validation
    pattern = re.compile(r"^(\d{4}-\d{2}-\d{2})_([^_]+)_([^_]+)_(.+)\.(png|jpg|jpeg|pdf|json)$", re.IGNORECASE)
    
    all_files = os.listdir(TARGET_DIR)
    if not all_files:
        print(f"[-] Operational Alert: {TARGET_DIR} is currently empty.")
        print("[*] Action Required: Populate this directory with formatted screenshots.")
        return events, set()

    tags_found = set()
    skipped_count = 0

    print("[*] Parsing ledger files and checking signature structures...")
    for filename in all_files:
        # Ignore system metadata hidden files
        if filename.startswith('.'):
            continue
            
        # Ignore internal storage folders dynamically
        if os.path.isdir(os.path.join(TARGET_DIR, filename)):
            continue
            
        match = pattern.match(filename)
        if match:
            date_str, tag, confidence, desc, ext = match.groups()
            normalized_tag = tag.upper().strip()
            normalized_conf = confidence.upper().strip()
            
            tags_found.add(normalized_tag)
            events.append({
                "date": date_str,
                "tag": normalized_tag,
                "confidence": normalized_conf,
                "desc": desc.replace("_", " "),
                "filename": filename
            })
        else:
            print(f" [WARNING] Invalid File Signature: '{filename}'")
            print("           -> Required Format: YYYY-MM-DD_TAG_CONFIDENCE_Description.ext")
            skipped_count += 1
            
    # Sort dataset chronologically by date
    events.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"))
    
    print(f"[+] Successfully indexed {len(events)} files. (Skipped/Flagged: {skipped_count})")
    return events, sorted(list(tags_found))

def generate_interactive_html(events, tags):
    colors = {
        "HIGH": "#2ecc71",  # Tactical Green
        "MED": "#f1c40f",   # Warning Amber
        "LOW": "#e74c3c"    # Alert Red
    }

    tag_buttons_html = "".join([f'<button class="filter-btn" onclick="filterTag(\'{t}\')">#{t}</button>' for t in tags])

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Orb Core :: Interactive Evidence Matrix</title>
    <style>
        body {{ font-family: 'Courier New', Courier, monospace; background-color: #0a0a0a; color: #dcdcdc; padding: 15px; margin: 0; }}
        .header {{ text-align: center; border-bottom: 2px solid #222; padding-bottom: 15px; margin-bottom: 20px; }}
        h1 {{ color: #00ff66; margin: 5px 0; font-size: 1.5em; text-transform: uppercase; letter-spacing: 1px; }}
        .control-panel {{ max-width: 800px; margin: 0 auto 20px auto; background: #111; padding: 10px; border: 1px solid #222; border-radius: 4px; }}
        .section-label {{ font-size: 0.8em; color: #666; font-weight: bold; margin-bottom: 5px; text-transform: uppercase; }}
        .filter-group {{ display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 10px; }}
        button {{ background: #222; color: #aaa; border: 1px solid #333; padding: 6px 12px; font-family: inherit; font-size: 0.85em; cursor: pointer; border-radius: 3px; transition: all 0.2s; }}
        button:hover {{ background: #333; color: #fff; }}
        button.active {{ background: #00ff66; color: #000; border-color: #00ff66; font-weight: bold; }}
        .timeline {{ position: relative; max-width: 800px; margin: 0 auto; padding-left: 20px; }}
        .timeline::before {{ content: ''; position: absolute; width: 2px; background-color: #222; top: 0; bottom: 0; left: 5px; }}
        .event-card {{ position: relative; background-color: #141414; border: 1px solid #222; border-left: 5px solid #555; border-radius: 4px; padding: 12px; margin-bottom: 12px; }}
        .event-card::before {{ content: ''; position: absolute; width: 8px; height: 8px; left: -21px; background-color: #0a0a0a; border: 2px solid #00ff66; top: 16px; border-radius: 50%; z-index: 1; }}
        .meta-line {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }}
        .date {{ font-weight: bold; color: #00ff66; font-size: 1.05em; }}
        .tag {{ background: #222; padding: 2px 6px; border-radius: 3px; font-size: 0.8em; font-weight: bold; color: #00bcff; }}
        .badge {{ padding: 2px 6px; border-radius: 3px; font-size: 0.75em; font-weight: bold; color: #000; }}
        .desc {{ color: #a5a5a5; font-size: 0.95em; line-height: 1.4; word-wrap: break-word; }}
        .file-link {{ display: block; margin-top: 8px; font-size: 0.75em; color: #555; text-decoration: none; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; }}
        .hidden {{ display: none !important; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Evidence Mapping Timeline</h1>
        <div style="font-size: 0.8em; color: #444;">ORB CORE WORKSTATION MATRIX</div>
    </div>

    <div class="control-panel">
        <div class="section-label">Confidence Filters</div>
        <div class="filter-group">
            <button class="filter-btn active" id="conf-all" onclick="filterConfidence('ALL')">ALL SCENARIOS</button>
            <button class="filter-btn" onclick="filterConfidence('HIGH')">HIGH CONFIDENCE</button>
            <button class="filter-btn" onclick="filterConfidence('MED')">MED CONFIDENCE</button>
            <button class="filter-btn" onclick="filterConfidence('LOW')">LOW CONFIDENCE</button>
        </div>
        <div class="section-label">Scenario Group Filters</div>
        <div class="filter-group">
            <button class="filter-btn active" id="tag-all" onclick="filterTag('ALL')">ALL TAGS</button>
            {tag_buttons_html}
        </div>
    </div>

    <div class='timeline'>
    """

    for ev in events:
        badge_color = colors.get(ev["confidence"], "#555")
        html_content += f"""
        <div class="event-card" data-confidence="{ev["confidence"]}" data-tag="{ev["tag"]}" style="border-left-color: {badge_color};">
            <div class="meta-line">
                <div>
                    <span class="date">{ev["date"]}</span>
                    <span class="tag">#{ev["tag"]}</span>
                </div>
                <span class="badge" style="background-color: {badge_color};">{ev["confidence"]}</span>
            </div>
            <div class="desc">{ev["desc"]}</div>
            <div class="file-link">File: {ev["filename"]}</div>
        </div>
        """

    html_content += """
    </div>

    <script>
        let currentConf = 'ALL';
        let currentTag = 'ALL';

        function filterConfidence(conf) {
            currentConf = conf;
            updateButtons('confidence', conf);
            applyMatrixFilters();
        }

        function filterTag(tag) {
            currentTag = tag;
            updateButtons('tag', tag);
            applyMatrixFilters();
        }

        function updateButtons(type, value) {
            const buttons = document.querySelectorAll('.filter-btn');
            buttons.forEach(btn => {
                const onClickStr = btn.getAttribute('onclick');
                if (type === 'confidence' && onClickStr.includes('filterConfidence')) {
                    btn.classList.remove('active');
                    if (onClickStr.includes(`'${value}'`) || (value === 'ALL' && onClickStr.includes('ALL'))) btn.classList.add('active');
                }
                if (type === 'tag' && onClickStr.includes('filterTag')) {
                    btn.classList.remove('active');
                    if (onClickStr.includes(`'${value}'`) || (value === 'ALL' && onClickStr.includes('ALL'))) btn.classList.add('active');
                }
            });
        }

        function applyMatrixFilters() {
            const cards = document.querySelectorAll('.event-card');
            cards.forEach(card => {
                const cMatch = (currentConf === 'ALL' || card.dataset.confidence === currentConf);
                const tMatch = (currentTag === 'ALL' || card.dataset.tag === currentTag);
                
                if (cMatch && tMatch) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
        }
    </script>
</body>
</html>
"""

    with open(OUTPUT_HTML, "w") as f:
        f.write(html_content)
    print(f"\n[+] Timeline compiled successfully.")
    print(f"[->] Interactive HTML Matrix: {OUTPUT_HTML}")

if __name__ == "__main__":
    evidence_events, unique_tags = compile_timeline_data()
    if evidence_events:
        generate_interactive_html(evidence_events, unique_tags)






