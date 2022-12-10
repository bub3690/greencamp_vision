import argparse
import os
import platform
import sys
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory

sys.path.append(str(FILE.parents[1])+'/yolov5_greencamp')  # yolov5 서브모듈 패스 넣어주기.
print(str(FILE.parents[1])+'/yolov5_greencamp')

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from models.common import DetectMultiBackend


