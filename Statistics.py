import csv

def outputStats (file_name, input_name, output_name, mask, algo, k, kmers_len, superStr_len, tm, tm1, memory, test):

    header = ['Genome', 'Output File', 'Mask Type', 'Algorithm', 'K', 'Length of k-mers Set', 'Length of SuperString', 'CPU Time', 'Wall-clock time', 'Memory Usage Peak', 'Test Result']
    data = [input_name, output_name, mask, algo, str(k), str(kmers_len), str(superStr_len), round(tm, 4), round(tm1, 4), memory[1], test]

    with open(file_name, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)

#Memory(current, peak). Current memory is the memory the code is currently using and peak memory is the maximum space the program used while executing.