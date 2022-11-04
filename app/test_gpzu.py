from ml.parser import GPZU_parser

p = GPZU_parser(files_paths=['ml/dataset/RU77101000-040954-GPZU.pdf'])

data = p.parse()
p.to_excel('./', 'test')
print(data)
