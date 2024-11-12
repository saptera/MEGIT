# MEGIT

## Installation

***3.9 <= Python required.***

### Required Packages

- [NumPy](https://numpy.org) `pip install numpy` *(Basic requirements)*
- [SciPy](https://www.scipy.org) `pip install scipy` *(Basic requirements)*
- [OpenCV](https://opencv.org) `pip install opencv-python` *(Video processing)*
- [Shapely](https://shapely.readthedocs.io/en/stable/) `pip install shapely` *(Geometry functions)*
- [Matplotlib](https://matplotlib.org) `pip install matplotlib` *(Plotting functions)*
- [H5Py](https://www.h5py.org) `pip install h5py` *(HDF5 file management)*
- [PySide6](https://www.qt.io/qt-for-python) `pip install PySide6` *(GUI requirements)*

OS dependent scripts can be found in `[install]` directory, which contain auto-install script.

## System Walkthrough

### Interactive GUIs

Run `Zoom_Preprocess.py` to handel zoom-view related preprocessing tasks.

Run `Overview_Preprocess.py` to handel overview related preprocessing tasks.

Run `Corss_Verifier.py` to manually adjust auto-detection results.

### Automated scripts

## Package Structure

```
├── install                 <- OS dependent installation scripts
├── megit                   <- Package source directory
│   ├── gui                     <- GUI sub-directory
│   │   ├── app_*.py               <- Application script
│   │   ├── dgn_*.ui               <- PyQt5 UI raw design files
│   │   ├── dgn_*.py               <- PyQt5 auto-converted UI scripts
│   ├── model                   <- Trained pose estimation models
│   │   ├── overview.model         <- MEGIT overview model
│   ├── batch.py                <- Batch process functions
│   ├── data.py                 <- Data process functions
│   ├── fio.py                  <- File IO functions
│   ├── utils.py                <- Package utility functions
├── Zoom_Preprocess.py      <- MEGIT Zoom-View preprocess GUI
├── Overview_Preprocess.py  <- MEGIT Overview preprocess GUI
├── Cross_Verifier.py       <- Post pose estimation verification GUI
├── LICENSE                 <- AGPL-3.0 license
├── README.md
├── .gitattributes
└── .gitignore
```
