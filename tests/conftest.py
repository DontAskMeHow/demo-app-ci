import sys
from pathlib import Path

# Add project root so `import app` works even if pytest runs elsewhere.
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
