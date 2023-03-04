import csv

def outputStats (file_name, input_name, output_name, mask, algo, k, kmers_len, superStr_len, tm, tm1, memory):

    header = ['Genome', 'Output File', 'Mask Type', 'Algorithm', 'K', 'Length of k-mers Set', 'Length of SuperString', 'CPU Time', 'Wall-clock time', 'Memory Usage Peak']
    data = [input_name, output_name, mask, algo, str(k), str(kmers_len), str(superStr_len), round(tm, 4), round(tm1, 4), memory[1]]

    with open(file_name, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)