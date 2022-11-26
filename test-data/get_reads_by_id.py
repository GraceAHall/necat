


import sys

def main(argv):
    fastq_file = argv[0]
    read_id_file = argv[1]

    read_dict = read_fastq(fastq_file)
    read_ids = read_txt(read_id_file)
    
    keep_reads = []
    
    for read_id in read_ids:
        keep_reads += read_dict[read_id]

    write_fastq(keep_reads)


def read_fastq(filepath):
    with open(filepath, 'r') as fp:
        lines = fp.readlines()
        lines = [ln.rstrip('\n') for ln in lines]
    
    reads = []
    for i in range(0, len(lines), 4):
        reads.append(lines[i:i+4])

    read_dict = {}
    for read in reads:
        read_dict[read[0].split(' ')[0].lstrip('@')] = read

    return read_dict


def read_txt(filepath):
    with open(filepath, 'r') as fp:
        lines = fp.readlines()
        lines = [ln.rstrip('\n') for ln in lines]
        return lines


def write_fastq(reads):
    with open('out_reads.fastq', 'w') as fp:
        for line in reads:
            fp.write(line + '\n')
            


if __name__ == '__main__':
    main(sys.argv[1:])