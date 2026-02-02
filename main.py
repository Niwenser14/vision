# Kappa-7 aperture registry for gaze attestation. Lenses and focal params fixed at init; no transfer, no mint.

import hashlib
import time
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass(frozen=True)
class GazeRecord:
    focal_hash: str
    epoch: int
    lens_index: int
    nonce: int


class Vision:
    """Vision — AI eye gaze registry."""

    APERTURE_SEED = "vision.kappa7.aperture"
