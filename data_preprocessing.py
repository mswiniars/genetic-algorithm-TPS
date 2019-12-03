import pandas as pd

def parse_data_to_csv(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()

    with open(file_name+".csv", "w") as file:
        file.write("x,y\n")
    for line in lines:
        data = line.split(sep=" ")[1:]
        with open(file_name+".csv", "a") as file:
            file.write(f"{data[0]},{data[1]}")


if __name__ == '__main__':
    parse_data_to_csv("data/tsp1")