'''
The script aims to extract the basename of the filenames in the dir
'''
import datetime
import glob
import os

dirs = {
    0: '/exports/hhr346/Archive/DQ1/LEVEL1/DQ1_EMI_',
    1: '/exports/hhr346/Archive/GF5B/LEVEL1/GF5B_EMI_',
    2: '/exports/hhr346/Archive/GF5A/LEVEL1/GF5A_EMI_',
    3: '/satellite/d1/GF5B-EFI/LEVEL1/tar/GF5B_EMI_',
    4: '/satellite/d2/DQ1/tmp/DQ1_EMI_',
}

status = 1
dir = dirs[status]

def check_date():
    if status == 0 or status == 4:
        begin = datetime.date(2022, 11, 1)
        f = open('./dq1_tmp.txt', 'w')
    elif status == 1 or status == 3:
        # begin = datetime.date(2021, 10, 20)
        begin = datetime.date(2022, 11, 1)
        f = open('./gf5b.txt', 'w')
        # f.write('The missing part of GF5B')
    elif status == 2:
        begin = datetime.date(2023, 1, 9)
        f.write('The missing part of GF5A')
    # end = datetime.date.today()
    end = datetime.date(2023, 11, 1)
    d = begin
    while d <= end:
        time_target = d.strftime('%Y%m%d')
        d += datetime.timedelta(1)
        files = glob.glob(dir+time_target+'*')
        for file in files:
            name = os.path.splitext(os.path.basename(file))[0]
            print(name)
            f.write(name)
            f.write('\n')
check_date()
