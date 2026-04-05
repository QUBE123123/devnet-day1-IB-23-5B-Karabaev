import json, os, subprocess
from pathlib import Path
import jsonschema

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "day5"
SCHEMA = ROOT / "schemas" / "day5_summary.schema.json"

def jload(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))

def test_day5_summary_and_artifacts():
    env = os.environ.copy()
    # Проверяем наличие токена студента
    assert env.get("STUDENT_TOKEN"), "Забыл сделать export STUDENT_TOKEN!"
    
    # 1. Запуск сборщика summary
    r = subprocess.run(["python3", "src/day5_summary_builder.py"], cwd=str(ROOT), env=env, capture_output=True, text=True)
    assert r.returncode == 0, f"Ошибка сборщика: {r.stderr}"

    # 2. Проверка существования файлов
    assert (ART / "summary.json").exists()
    assert (ART / "yang/pyang_tree.txt").exists()
    assert (ART / "webex/room_create.json").exists()
    assert (ART / "pt/serviceTicket.txt").exists()

    # 3. Валидация по схеме
    summary = jload(ART / "summary.json")
    if SCHEMA.exists():
        schema = jload(SCHEMA)
        jsonschema.validate(instance=summary, schema=schema)

    # 4. Проверка уникальности (хэш f0c3a881 должен быть в Webex)
    with open(ART / "webex/room_create.json") as f:
        room = json.load(f)
    assert "f0c3a881" in room["title"], "Хэш f0c3a881 не найден в названии комнаты Webex!"

    print("\n[SUCCESS] Все проверки Дня 5 пройдены!")
