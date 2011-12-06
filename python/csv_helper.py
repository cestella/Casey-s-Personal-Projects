#!/opt/local/bin/python

from optparse import OptionParser
import csv
import sys

def main():
    parser = OptionParser()
    parser.add_option( "-c"
                    , "--columns"
                    , dest="columns"
                    , help="Project onto a set of columns (0-based, like G*d intended)"
                    , metavar="COLS"
                    )
    parser.add_option( "-f"
                    , "--file"
                    , dest="file"
                    , help="CSV File to open"
                    , metavar="FILE"
                    )
    parser.add_option( "-d"
                    , "--delimiter"
                    , dest="delimiter"
                    , help="delimiter to use, default is comma"
                    , metavar="DELIMITER"
                    )

    #parse the CLI options
    (options, args) = parser.parse_args()
    in_file = None 
    if options.file is None:
       #use stdin if we have no other file specified
       in_file = sys.__stdin__
    else:
       in_file = open(options.file, 'rb')

    #default delimiter is ,
    csv_delimiter = ',' 
    if options.delimiter is not None:
        if options.delimiter is 'tab':
            csv_delimiter = '\t'
        else:
            csv_delimiter = options.delimiter
    columns = []
    if options.columns is not None:
        #A little functional programming candy
        columns = map(lambda column: int(column.strip())
                     , options.columns.split(',') 
                     )

    #Create our CSV reader
    #TODO: we really need to pass in what we consider a quote
    cli_reader = csv.reader( in_file
                           , delimiter=csv_delimiter
                           , quotechar='\"'
                           )

    for line in cli_reader:
        out_line = ''
        for i in range(0, len(columns)):
            #iterate over the columns that we wish to output and
            #if within range, print it out
            if columns[i] < len(line):
                out_line += line[columns[i]] + ' '
        print out_line

if __name__ == "__main__":
    main()
