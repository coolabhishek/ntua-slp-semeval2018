import config
from model.params import TASK3_A, TASK3_B
import emoji
from config import QUERY_EXPANSION_METHOD1, QUERY_EXPANSION_METHOD2, QUERY_EXPANSION_METHOD3
import os

TASK = 'a'
# select config by args.task
if TASK == "a":
    model_config = TASK3_A
else:
    model_config = TASK3_B

def create_emotion_from_emoji(x):
    x = emoji.demojize(x, delimiters=(' ',' '))
    return x.replace('_face', ' ')


def parse_train_csv_method_1(data_file):
    """
    Returns:
        X: a list of tweets
        y: a list of labels corresponding to the tweets
    """
    relative_folder = os.path.dirname(os.path.abspath(data_file)).split("/")
    folder_to_write = list()
    flag = False
    for each_part in relative_folder:
        if flag == True:
            folder_to_write.append(each_part)
        if each_part == "datasets":
            flag = True
    file_name = os.path.basename(data_file)
    folder_to_write = QUERY_EXPANSION_METHOD1 + '/'.join(folder_to_write) + '/'
    os.makedirs(folder_to_write, exist_ok=True)
    file_path_to_write = folder_to_write + file_name
    file_to_write = open(file_path_to_write, "w")
    print ("input file", data_file)
    print ("output file", file_path_to_write)

    with open(data_file, 'r') as fd:
        data = [l.strip().split('\t') for l in fd.readlines()][1:]
    for d in data:
        d_emoji = create_emotion_from_emoji(d[2])
        d[2] = d_emoji
        file_to_write.write('\t'.join(d))
        file_to_write.write('\n')
    file_to_write.close()


def parse(task, dataset):
    if task == 'a' and dataset == "train":
        data_file = config.TASK3.TASK_A
    elif task == 'a' and dataset == "gold":
        data_file = config.TASK3.TASK_A_GOLD
    elif task == 'b' and dataset == "train":
        data_file = config.TASK3.TASK_B
    elif task == 'b' and dataset == "gold":
        data_file = config.TASK3.TASK_B_GOLD
    else:
        raise ValueError("Invalid dataset.")

    parse_train_csv_method_1(data_file)



parse(task=TASK, dataset="train")
parse(task=TASK, dataset="gold")