import sys
import csv
import process


def read_csv_file(file_name):
    csv_rows = []
    try:
        with open(file_name, 'rt', encoding='windows 1250') as csv_input:
            reader = csv.reader(csv_input, delimiter=';')
            for row in reader:
                csv_rows.append(row)
            # Checking headers
            check_header(csv_rows[0])
        print('Working on file: ' + file_name + '\n')

        return csv_rows

    except FileNotFoundError:
        print('File you\'re trying to read does not exist.')
        sys.exit(0)
    except UnicodeDecodeError:
        print('It\'s not even a text file!')
        sys.exit(0)
    except ValueError:
        print('Not all headers found')
    except Exception as ex:
        print('Unexpected type of exception: "', ex, '" occurred in read_csv_file method.')
        sys.exit(0)


def check_header(header_row):
        for columnHeader in header_row:
            if columnHeader in process.__HEADERS__:
                process.__HEADERS__[columnHeader] = header_row.index(columnHeader)
        for value in process.__HEADERS__.values():
            # show header and index ...
            if value is '':
                print('Header not found.')
                sys.exit(0)