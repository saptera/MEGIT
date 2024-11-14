# MEGIT

Data analysis package for modified elevated gap interaction test (MEGIT)

## Installation

***3.9 <= Python required.***

### Required Packages

- [NumPy](https://numpy.org/) `pip install numpy` *(Basic requirements)*
- [SciPy](https://scipy.org/) `pip install scipy` *(Basic requirements)*
- [OpenCV](https://opencv.org/) `pip install opencv-python` *(Video processing)*
- [Shapely](https://shapely.readthedocs.io/en/stable/) `pip install shapely` *(Geometry functions)*
- [Matplotlib](https://matplotlib.org/) `pip install matplotlib` *(Plotting functions)*
- [H5Py](https://www.h5py.org/) `pip install h5py` *(HDF5 file management)*
- [PySide6](https://www.qt.io/qt-for-python) `pip install PySide6` *(GUI requirements)*

OS dependent scripts can be found in `[install]` directory, which contain auto-install script for aforementioned packages.

- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)

TensorFlow and Keras installation are hardware dependent, please refer to the linked official sites for optimized deployment.

## System Walkthrough

For Window users, simply run `MEGIT.bat` for the guided data pipeline.

### Step 1: Zoomview Preprocess GUI

In this GUI, user can adjust frame brightness/contrast, flip frames, as well as label frames with frame number.

*Detailed tool tips are integrated in the GUI.*

### Step 2: Overview Preprocess GUI

In this GUI, user can adjust frame brightness/contrast, and label frames with frame number. More important, user can define required ROI for MEGIT.

*Detailed tool tips are integrated in the GUI.*

### Step 3: Model Based Pose Estimation

*This is an automated SCRIPT rather than a GUI. This option was chosen to enable higher process efficiency and easier integration into other programs.*

*All possible parameters can be accessed with `MEGIT.bat`, allowing easier usage.*

This script reads data from the overview preprocessed frame and make predictions of "nose", "left ear", and "right ear" of a mouse.

The default model was trained using our [OptiFlex](https://github.com/saptera/OptiFlex) package. User can customize new models with this package.

This script also support models trained with TensorFlow.

***All available data will be processed at one call, refer the data structure section for more info.***

### Step 4: Cross Detection

*This is an automated SCRIPT rather than a GUI. This option was chosen to enable higher process efficiency and easier integration into other programs.*

*All possible parameters can be accessed with `MEGIT.bat`, allowing easier usage.*

This script post process the HeatMap predictions acquired from the model inference, and detect the actual cross with the data.

***All available data will be processed at one call, refer the data structure section for more info.***

### Step 5: Manual Cross Validation GUI

In this GUI, user check and validate the results from the automated steps.

*Detailed tool tips is integrated in the GUI.*

## Recommended Data Structure

```
├── base folder    <- This folder can have arbitrary name
├── animal data 1    <- Animal identifier is suggested for these folders
    -- All path/file names in this section CANNOT be changed --
│   ├── obj            <- Object test group folder
│   │   ├── *.avi        <- [AVI] Preprocessed zoomview video (from step-1)
│   │   ├── *.frm        <- [HDF5] Preprocessed frames of this group (from step-2)
│   │   ├── *.roi        <- [JSON] Region of interest information (from step-2)
│   │   ├── *.hml        <- [HDF5] HeatMap predictions from model (from step-3)
│   │   ├── *.ait        <- [CJSH] Average intensty information of each ROI (from step-4)
│   │   ├── *.rjl        <- [CJSH] Raw JSON label direct from HeatMap predictions (from step-4)
│   │   ├── *.jsl        <- [CJSH] Augmented JSON label combining intensity detection and raw JSON (from step-4)
│   │   ├── *.csv        <- [CSV] Cross detection results (from step-4)
│   │   ├── *_vld.csv    <- [CSV] Validated cross detection results (from step-5)
│   ├── juv            <- Juvenile test group folder
│   │   ├── ...           <- Same as [obj]
│   ├── byj            <- By juvenile group folder
│   │   ├── ...           <- Same as [obj]
    -----------------------------------------------------------
├── animal data 2
├── ...
└── ...
```

*If all steps are finished with the MEGIT data pipeline, this structure is automatically established.*

## Package Structure

```
├── install             <- OS dependent installation scripts
├── megit               <- Package source directory
│   ├── gui                 <- GUI sub-package
│   │   ├── app_*.py           <- Application script
│   │   ├── dgn_*.ui           <- PyQt5 UI raw design files
│   │   ├── dgn_*.py           <- PyQt5 auto-converted UI scripts
│   ├── model               <- Model related sub-package
│   │   ├── pred.py            <- Model inference related functions
│   │   ├── overview.model     <- MEGIT overview model
│   ├── script               <- Automated scripts sub-folder
│   │   ├── preproc_zoom.py    <- Zoomview preprocess GUI caller
│   │   ├── preproc_over.py    <- Overview preprocess GUI caller
│   │   ├── model_pred.py      <- Model pose estimation script
│   │   ├── crs_det.py         <- Post pose estimation cross dection script
│   │   ├── crs_vld.py         <- Post cross dection manual verification GUI caller
│   ├── batch.py            <- Batch process functions
│   ├── data.py             <- Data process functions
│   ├── fio.py              <- File IO functions
│   ├── utils.py            <- Package utility functions
├── MEGIT_Win.bat       <- MEGIT data pipeline caller for Windows
├── LICENSE             <- AGPL-3.0 license
├── README.md
├── .gitattributes
└── .gitignore
```
