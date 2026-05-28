import os
import datetime

ARCHIVE_DIR = "archive"
CATEGORIES = {
    "1": ("Legal & Case Binders (1-7)", "legal_binders"),
    "2": ("Supplydimezzz Business Logistics", "supplydimezzz"),
    "3": ("Genealogy & Historical Research", "genealogy"),
    "4": ("Personal Asset & Ledger Indices", "personal_assets")
}

def log_thought():
    print("\n---------------------------------------------------------")
    print("             SELECT ROUTING VECTOR CATEGORY              ")
    print("---------------------------------------------------------")
    for key, (name, _) in CATEGORIES.items():
        print(f" {key}. {name}")
    print("---------------------------------------------------------")
    cat_choice = input("[?] Select vector for routing entry: ").strip()
    
    if cat_choice not in CATEGORIES:
        print("[!] Invalid category. Aborting entry.")
        input("Press [Enter] to return...")
        return
        
    cat_name, folder = CATEGORIES[cat_choice]
    
    # Sub-specification for Legal Binders to keep the 7-binder array clear
    binder_tag = ""
    if cat_choice == "1":
        binder_tag = input("[?] Enter Binder Number/Title (e.g., Binder 3 - Financials): ").strip()
        binder_tag = f" | {binder_tag}" if binder_tag else ""

    print(f"\n[*] Routing data to -> {cat_name}")
    thought = input("[?] Stream your data/document text: ").strip()
    if not thought:
        return
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = os.path.join(ARCHIVE_DIR, folder, "master_stream.md")
    
    with open(log_file, "a", encoding='utf-8') as f:
        f.write(f"\n### [{timestamp}]{binder_tag}\n> {thought}\n")
    print(f"[+] Entry successfully synchronized into {folder}/master_stream.md.")
    input("\nPress [Enter] to return...")

def search_matrix():
    print("\n---------------------------------------------------------")
    print("             QUERY COGNITIVE ARCHIVE MATRIX              ")
    print("---------------------------------------------------------")
    query = input("[?] Enter keyword, case term, or date to locate: ").strip().lower()
    if not query:
        return
    
    print(f"\n[*] Scanning archive layers for pattern matches: '{query}'...\n")
    found = False
    
    for root, _, files in os.walk(ARCHIVE_DIR):
        for file in files:
            if file.endswith(('.txt', '.md', '.json')):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Split by markdown headers to pull individual entries instead of whole files
                        entries = content.split("### ")
                        for entry in entries:
                            if query in entry.lower():
                                print(f"=========================================================")
                                print(f"MATCH FOUND IN: {file_path}")
                                print(f"=========================================================")
                                print(f"### {entry.strip()}\n")
                                found = True
                except Exception:
                    continue
                    
    if not found:
        print("[!] No matching structural patterns found in current archives.")
    input("\nPress [Enter] to return...")

def main():
    while True:
        os.system('clear')
        print("=========================================================")
        print("         ORB CORE :: ENHANCED THOUGHT MATRIX ENGINE      ")
        print("=========================================================")
        print(" 1. Log and Route Document Entry")
        print(" 2. Query Full Operational Matrix (Deep Search)")
        print(" 3. Return to Master Main Frame")
        print("=========================================================")
        choice = input("- Select vector [1-3]: ").strip()
        
        if choice == '1':
            log_thought()
        elif choice == '2':
            search_matrix()
        elif choice == '3':
            break

if __name__ == "__main__":
    main()
