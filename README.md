# OTIA

OTIA (ok this is a (piece of trash)) is a Python library used for processing images of trash/recycling 
using machine learning and CNNs.

## Installation

Use the package manager (pip) to install otia.
```bash
pip install otia
```

## Usage

```python
import otia.myfunctions

# load the data by binding the images to labels
ims, ls = otia.myfunctions.load_data(DATA_DIRECTORY, ["recycle", "trash"], 128)

# creates a CNN model by processing all images in the set
otia.myfunctions.train_model(imgs, ls, 128, ["recycle", "trash"])

# predict an image based off an already existing model
# predicts whether a piece of trash is trash or recycleable
prediction = otia.myfunctions.predict_image(trash_img, model_path, 128, ["recycle","trash"])
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.