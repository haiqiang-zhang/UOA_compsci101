def main():
    data_dict = {850:["Kim", "Lucy"], 700:["Ken", "Mele"], 450:["Ronald"],1000:["Gill", "Bart"], 200:["Alfonso"]}
    filename = "Output.txt"
    write_data(filename, data_dict)

def write_data(filename, data_dict):
    key_list = list(data_dict.keys())
    key_list.sort()
    key_list.reverse()
    output_stream = open(filename, "w")
    for key in key_list:
        values = data_dict[key]
        values.sort()
        for value in values:
            output_stream.write(value + " - " + str(key) + "\n")
    output_stream.close()

main()