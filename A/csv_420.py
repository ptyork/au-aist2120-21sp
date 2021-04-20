import csv

def process_text(filename):
    fi = open(filename, 'rt')

    firstline = fi.readline().rstrip()
    headers = firstline.split(',')
    # print(headers)
    print(f"{headers[0]}\t{headers[1]}\t{headers[2]}\t{headers[-1]}")

    for line in fi:
        line = line.rstrip()
        # print(line)
        parts = line.split(',')
        print(f"{parts[0]}\t{parts[1]}\t{parts[2]}\t{parts[-1]}")

    fi.close()

def process_text_by_region(filename, region):
    region = region.upper()

    fi = open(filename, 'rt')

    firstline = fi.readline().rstrip()
    headers = firstline.split(',')
    # print(headers)
    print(f"{headers[0]}\t{headers[1]}\t{headers[2]}\t{headers[-1]}")

    subtotal = 0   # initialize "accumulator" variable
    for line in fi:
        line = line.rstrip()
        # print(line)
        parts = line.split(',')
        if parts[0].upper() == region:
            print(f"{parts[0]}\t{parts[1]}\t{parts[2]}\t$ {parts[-1]}")
            subtotal = subtotal + float(parts[-1])   # add to accumulator

    print(f"TOTAL PROFITS:\t$ {subtotal:.2f}")

    fi.close()


def process_csv(filename):
    with open(filename, 'rt') as fi:
        rdr = csv.reader(fi)
        
        # all = list(rdr)
        # # print(all)
        # print(all[0][0])
        # print(all[1][0])
        # print(all[8][0])
        # print(all[8][-1])
        # return

        for line in rdr:
            print(f"{line[0]}\t{line[1]}\t{line[2]}\t{line[-1]}")


def process_csv2(filename):
    # Demonstrate how to skip the first "header" line
    with open(filename, 'rt') as fi:
        rdr = csv.reader(fi)
        first_line = True
        for line in rdr:
            if first_line == False:
                print(f"{line[0]}\t{line[1]}\t{line[2]}\t{line[-1]}")
            else:
                first_line = False
                continue

def process_csv3(filename):
    # Demonstrate how to skip the first "header" line
    with open(filename, 'rt') as fi:
        rdr = csv.reader(fi)
        row_counter = 0
        for line in rdr:
            if row_counter >= 1:
                print(f"{row_counter}:\t{line[0]}\t{line[1]}\t{line[2]}\t{line[-1]}")
            row_counter += 1


def process_csv_dict_version(filename):
    # Demonstrate how to skip the first "header" line
    with open(filename, 'rt') as fi:
        rdr = csv.DictReader(fi)
        for line in rdr:
            print(f"{line['Region']}\t{line['Country']}\t{line['Item Type']}\t{line['Total Profit']}")


def filter_csv(filename, region):
    first_line = True
    with open(filename, 'rt') as infile:
        outname = f"{region}.csv"
        # Open a second file for WRITING
        # MUST be opened with optional newline='' argument to avoid
        # having an extra newline at the end.
        with open(outname, 'wt', newline='') as outfile:
            rdr = csv.reader(infile)
            wtr = csv.writer(outfile)
            for line in rdr:
                if first_line == True:
                    first_line = False
                    wtr.writerow(line)
                else:
                    if region.upper() == line[0].upper():
                        wtr.writerow(line)

def main():
    # process_text('thousand.csv')
    # process_text_by_region('thousand.csv','Europe')
    # process_csv('thousand.csv')
    # process_csv2('thousand.csv')
    # process_csv3('thousand.csv')
    # process_csv_dict_version('thousand.csv')
    filter_csv('thousand.csv', 'Asia')


main()
