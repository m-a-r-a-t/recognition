# import multiprocessing
# from pdfminer.high_level import extract_text
# from os import listdir
# from os.path import isfile, join, curdir
# from pathlib import Path


# def convert_pdf_files_to_txt(file_names: list, dir_name: str):
#     for file_name in file_names:
#         print(file_name)
#         new_file = open(f"{dir_name}/{file_name.replace('pdf','txt')}", 'w')
#         text = extract_text('dataset/' + file_name)
#         new_file.write(text)
#         new_file.close()


# dataset_path = Path(curdir, "dataset")
# onlyfiles = [f for f in listdir(dataset_path) if isfile(join(dataset_path, f))]

# NUM_CORE = 12
# count_for_each_proccess = int(len(onlyfiles)/NUM_CORE)

# double_arrays = []

# for i in range(NUM_CORE):
#     if i+1 != NUM_CORE:
#         double_arrays.append(onlyfiles[
#             i*count_for_each_proccess:count_for_each_proccess*(i+1)
#         ])
#     else:
#         double_arrays.append(onlyfiles[
#             i*count_for_each_proccess:
#         ])

# procs = []
# for i in range(NUM_CORE):
#     p = multiprocessing.Process(target=convert_pdf_files_to_txt, args=(double_arrays[i], 'dataset_text'))
#     procs.append(p)
#     p.start()

# [proc.join() for proc in procs]
