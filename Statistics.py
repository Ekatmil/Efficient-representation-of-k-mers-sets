import csv

def outputStats (file_name, input_name, output_name, mask, algo, k, kmers_len, superStr_len, tm, memory):
    # if output_name == False:
    #     output_name = ""

    header = ['Genome', 'Output File', 'Mask Type', 'Algorithm', 'K', 'Length of k-mers Set', 'Length of SuperString', 'Time', 'Memory Consumption']
    data = [input_name, output_name, mask, algo, str(k), str(kmers_len), str(superStr_len), tm, memory]
    with open(file_name, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)

        
        # statistics = str
        # input = str
        # output = str
        # binary mask = bool
        # algorithm = str 
        # config.k = int
        # len (arr_saved) = int
        # len (superStr) = int
        # time = int 