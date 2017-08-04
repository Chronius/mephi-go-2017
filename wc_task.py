import sys


def string_count(filename):
    line_count = 0
    with open(filename) as f:
        while(f.readline()):
            line_count += 1
        # or we can do:    
        # for line in f:
        #     line_count += 1
    return line_count


def byte_count(filename):
    with open(filename) as f:
        while(f.read()):
            continue
        return f.tell()


if __name__ == '__main__':
    # use it to align the stdout
    out = ['', '', '']
    total_s = 0
    total_b = 0
    if len(sys.argv) == 1:        
        print("Please, enter filename")
        exit(1)        
    else:
        print("=============================")
        print("filename \tstring\tbytes")
        for arg in sys.argv:
            if arg != sys.argv[0]:
                out[1] = str(string_count(arg))
                out[2] = str(byte_count(arg))                
                if len(arg) > 5:
                    arg = arg[:5] + '..'
                out[0] = arg
                print(out[0] + '\t\t' + out[1] + '\t' + out[2])
                total_s += int(out[1])
                total_b += int(out[2])
        print("-----------------------------")
        print("total\t\t", total_s, '\t', total_b)

        print("=============================")
    sys.stdout.flush()
    exit(0)

main()