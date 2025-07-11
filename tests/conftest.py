import sys
from pathlib import Path

# Add the src directory to sys.path so tests can import the package without installation
SRC_PATH = Path(__file__).resolve().parents[1] / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))
