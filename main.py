import os
from datetime import datetime
from config import NICHES, OUTPUT_DIR

os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_short(niche):
    print(f"[{datetime.now()}] Generating {niche} short...")
    with open(f"{OUTPUT_DIR}/{niche}_latest.md", "w") as f:
        f.write(f"# Sample {niche} Short\nGenerated at {datetime.now()}\n\nHook: This one trick changes everything!\n\nContent coming soon...")
    print(f"✅ {niche} placeholder created")

if __name__ == "__main__":
    for niche in NICHES.keys():
        generate_short(niche)
    print("✅ Pipeline run complete! Check output/ folder.")