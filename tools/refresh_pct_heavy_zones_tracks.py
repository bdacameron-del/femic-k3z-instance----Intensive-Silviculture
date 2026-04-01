from __future__ import annotations

import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MODEL_ROOT = REPO_ROOT / "models" / "k3z_patchworks_model"
SOURCE_TRACKS = MODEL_ROOT / "tracks_pct_heavy"
TARGET_TRACKS = MODEL_ROOT / "tracks_pct_heavy_zones"
GROUPS_SOURCE = SOURCE_TRACKS / "groups_zones.csv"


def main() -> None:
    if not SOURCE_TRACKS.is_dir():
        raise FileNotFoundError(f"Missing source tracks directory: {SOURCE_TRACKS}")
    if not GROUPS_SOURCE.is_file():
        raise FileNotFoundError(f"Missing zoned groups source: {GROUPS_SOURCE}")

    if TARGET_TRACKS.exists():
        shutil.rmtree(TARGET_TRACKS)
    shutil.copytree(SOURCE_TRACKS, TARGET_TRACKS)
    shutil.copy2(GROUPS_SOURCE, TARGET_TRACKS / "groups.csv")
    print(f"Refreshed {TARGET_TRACKS} from {SOURCE_TRACKS} with {GROUPS_SOURCE.name}")


if __name__ == "__main__":
    main()
