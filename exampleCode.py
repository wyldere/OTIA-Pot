from otia.myfunctions import load_data, train_model, predict_image

DATA_DIRECTORY = "/Users/jessevguo/PycharmProjects/OTIA-Pot/trashnet/data/dataset-resized"
CATEGORIES = ["recycle", "trash"]

imgs, labels = load_data(DATA_DIRECTORY, CATEGORIES, 128)
train_model(imgs, labels, 128, CATEGORIES)
print(predict_image("/Users/jessevguo/PycharmProjects/OTIA-Pot/recycle0.png", "/Users/jessevguo/PycharmProjects/OTIA-Pot/trashnet_model.h5", 128, CATEGORIES))
print(predict_image("/Users/jessevguo/PycharmProjects/OTIA-Pot/recycle1.png", "/Users/jessevguo/PycharmProjects/OTIA-Pot/trashnet_model.h5", 128, CATEGORIES))
print(predict_image("/Users/jessevguo/PycharmProjects/OTIA-Pot/trash0.png", "/Users/jessevguo/PycharmProjects/OTIA-Pot/trashnet_model.h5", 128, CATEGORIES))
