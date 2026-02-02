# Kappa-7 aperture registry for gaze attestation. Lenses and focal params fixed at init; no transfer, no mint.

import hashlib
import time
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass(frozen=True)
class GazeRecord:
