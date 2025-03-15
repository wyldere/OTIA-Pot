import pytest
from otia.myfunctions import load_data, train_model

DATA_DIRECTORY = "/Users/jessevguo/PycharmProjects/OTIA-Pot/trashnet/data/dataset-resized"
def test_load_data():
    ims, ls = load_data(DATA_DIRECTORY, ["recycle", "trash"], 128)
    assert len(ims) == len(ls), "images and labels should be the same length"

def test_train_model():
    ims, ls = load_data(DATA_DIRECTORY, ["recycle", "trash"], 128)
    train_model(ims, ls, 128, ["recycle", "trash"])
    #assert result is not None, "model training should return a result"