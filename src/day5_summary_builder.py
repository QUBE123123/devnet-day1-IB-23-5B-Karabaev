import hashlib, json, os
from pathlib import Path

ART = Path("artifacts/day5")
HASH = "f0c3a881"

def main():
    # Проверка YANG
    tree = (ART / "yang/pyang_tree.txt").read_text()
    yang_ok = "interfaces" in tree

    # Проверка Webex
    with open(ART / "webex/room_create.json") as f:
        room = json.load(f)
    webex_ok = HASH in room["title"]

    summary = {
        "schema_version": "5.0",
        "student": {"name": "Suleimanov Timur", "hash": HASH},
        "checks": {
            "yang_tree_valid": yang_ok,
            "webex_room_contains_hash": webex_ok,
            "pt_ticket_received": (ART / "pt/serviceTicket.txt").exists()
        },
        "validation_passed": yang_ok and webex_ok
    }
    
    with open(ART / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print("Summary created!")

if __name__ == "__main__": main()
