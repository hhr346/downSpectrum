'''
Compare the two txts from the website and the server
'''

# f_server = open('./txt/dq1.txt', 'r')
# f_tmp = open('./txt/dq1_tmp.txt', 'r')
# f_web = open('./txt/dq1_all.txt', 'r')

f_server = open('./txt/gf5b.txt', 'r')
# f_tmp = open('./txt/gf5b_tmp.txt', 'r')
f_web = open('./txt/gf5b_all.txt', 'r')

def read_file(file):
    lines = []
    for line in file:
        line = line.rstrip('\n')
        lines.extend([line])
    return lines

f_server = read_file(f_server)
f_web = read_file(f_web)
# f_tmp = read_file(f_tmp)
f_tmp = []

diff = set(f_web) - (set(f_server) | set(f_tmp))
diff = sorted(diff)
f = open('./gf5b_diff.txt', 'w')
for i in diff:
    print(i)
    f.write(i)
    f.write('\n')
