import csv

def proc_non_csv(filename):
    fi = open(filename, 'rt')

    # initialize "accumulator" variables
    line_no = 0
    subtotal = 0

    for line in fi:
        line = line.rstrip()
        parts = line.split(',')
        if line_no == 0:
            # Print header row (special case)
            print(f"     {parts[0]:<30}{parts[1]:<25}{parts[2]:<15} {parts[-1]:>10}")
        else:
            # General case
            print(f"{line_no:<4}:{parts[0]:<30}{parts[1]:<25}{parts[2]:<15}${parts[-1]:>10}")
            prof = float(parts[-1])
            subtotal += prof
        line_no += 1

    print(f"TOTAL PROFIT:${subtotal:>73.2f}")


def proc_csv(filename):
    fi = open(filename, 'rt')
    rdr = csv.reader(fi)

    # initialize "accumulator" variables
    line_no = 0
    subtotal = 0

    for line in rdr:
        # print(line)
        if line_no == 0:
            # Print header row (special case)
            print(f"     {line[0]:<30}{line[1]:<25}{line[2]:<15} {line[-1]:>10}")
        else:
            # General case
            print(f"{line_no:<4}:{line[0]:<30}{line[1]:<25}{line[2]:<15}${line[-1]:>10}")
            prof = float(line[-1])
            subtotal += prof
        line_no += 1

    print(f"TOTAL PROFIT:${subtotal:>73.2f}")

def proc_csv_filter(filename,region):
    # force region to lower case
    region = region.lower()

    fi = open(filename, 'rt')
    rdr = csv.reader(fi)

    # initialize "accumulator" variables
    line_no = 0
    record_no = 0
    subtotal = 0

    for line in rdr:
        # print(line)
        if line_no == 0:
            # Print header row (special case)
            print(f"     {line[0]:<30}{line[1]:<25}{line[2]:<15} {line[-1]:>10}")
        else:
            if region == line[0].lower():
                # General case (filtered)
                record_no += 1
                print(f"{record_no:< 5}{line_no:<4}:{line[0]:<30}{line[1]:<25}{line[2]:<15}${line[-1]:>10}")
                prof = float(line[-1])
                subtotal += prof
        line_no += 1

    print(f"TOTAL PROFIT:${subtotal:>73.2f}")


def proc_csv_bad_idea(filename):
    fi = open(filename, 'rt')
    rdr = csv.reader(fi)
    # BAD BECAUSE it reads the whole kit and kaboodle into RAM
    all = list(rdr)
    # print(rdr)
    # print(all)
    print(all[0][0])
    print(all[1][0])
    print(all[1][3])


def proc_csv_dict_version(filename):
    fi = open(filename, 'rt')

    drdr = csv.DictReader(fi)

    # initialize "accumulator" variables
    subtotal = 0

    for line in drdr:
        # General case
        print(f"{line['Region']:<30}{line['Country']:<25}{line['Item Type']:<15}${line['Total Profit']:>10}")
        prof = float(line['Total Profit'])
        subtotal += prof

    print(f"TOTAL PROFIT:${subtotal:>73.2f}")


def simple_write(outfilename):
    with open(outfilename, 'wt', newline='') as outfile:
        line = ["Paul","Is","A","Old","Fart"]
        wtr = csv.writer(outfile)
        wtr.writerow(line)
        wtr.writerow(line)
        wtr.writerow(line)
        wtr.writerow(line)


def filter_csv(infilename, region):
    # force region to lower case
    region = region.lower()

    with open(infilename, 'rt') as inputfile:
        rdr = csv.reader(inputfile)

        outfilename = f"{region}.csv"
        with open(outfilename, 'wt', newline='') as outputfile:
            
            wtr = csv.writer(outputfile)

            # initialize "accumulator" variables
            first_line = True

            for line in rdr:
                # print(line)
                if first_line == True:
                    wtr.writerow(line)
                    first_line = False
                else:
                    if region == line[0].lower():
                        wtr.writerow(line)


def main():
    # proc_non_csv('thousand.csv')
    # proc_csv('thousand.csv')
    # proc_csv_filter('thousand.csv','asia')
    # proc_csv_bad_idea('thousand.csv')
    # proc_csv_dict_version('thousand.csv')
    # simple_write('simple.csv')
    filter_csv('thousand.csv', 'asia')

main()
