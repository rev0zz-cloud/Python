import sys


def get_mean_size():
    lines = sys.stdin.readlines()[1:]
    if lines:
        size_all, counter = 0, 0
        for line in lines:
            size_all += int(line.split()[4])
            counter += 1
        print(f'Средний размер файла в каталоге: {size_all / counter}')
    else:
        print('В каталоге нет файлов!')

if __name__ == "__main__":
    get_mean_size()
