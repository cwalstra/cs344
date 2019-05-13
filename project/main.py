'''
Created on 22 sty 2018
3D Object Representations for Fine-Grained Categorization
Jonathan Krause, Michael Stark, Jia Deng, Li Fei-Fei
4th IEEE Workshop on 3D Representation and Recognition, at ICCV 2013 (3dRR-13). Sydney, Australia. Dec. 8, 2013.
@author: mgdak
Additions: cwalstra
'''

from pprint import pprint
from keras import backend as K
from utilityFunctions import evaluate, readData, readClasses, dataPreprocessing, serializeModel, prepareDataGenerators

from runFunctions import setLayersToRetrain, initialTraining, finetuningTraining, model

train_data_dir = 'cars_train'
val_data_dir = 'cars_val'
nb_train_samples = 1043
nb_val_samples = 300

def main(args):
    pprint(args)
    if args["process_data"]:
        dataPreprocessing(args["car_ims_dir"], args["car_ims_labels"])

    K.clear_session()

    model(args["learning_rate"],
          args["optimizer_last_layer"],
          args["no_of_epochs"],
          args["batch_size"],
          args["saved_model_name"],
          args["car_ims_dir"],
          args["car_ims_labels"],
          args["model"],
          args["dropout_rate"],
          args["lr_decay"])

args = {}

args["process_data"] = False
args["car_ims_dir"] = "/home/cjw44/allCars/car_ims"
args["car_ims_labels"] = "/home/cjw44/CarData/cars_annos"
args["learning_rate"] = 0.001
args["dropout_rate"] = 0.4
args["lr_decay"] = 0
args["optimizer_last_layer"] = "RMSPROP"  # options: ['ADAGRAD', 'ADADELTA', 'ADAM', 'RMSPROP', 'MOM']
args["model"] = "MyCNN" # options: ['VGG19', 'VGG16', 'InceptionV3', "MyCNN"]
args["no_of_epochs"] = 10
args["batch_size"] = 64
args["saved_model_name"] = "carRecognition"

main(args)