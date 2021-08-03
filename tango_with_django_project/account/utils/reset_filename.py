import random
import time

def random_str():
    num_set = [chr(i) for i in range(48, 58)]
    char_set = [chr(i) for i in range(97, 123)]
    total_set = num_set + char_set
    bits = 14
    value_set = "".join(random.sample(total_set, bits))
    return value_set + str(int(time.time()))

def custom_file_name(file_name):
    file_type = str(file_name).split(".")[-1]
    new_file_name = random_str().upper()

    return ".".join([new_file_name,file_type])