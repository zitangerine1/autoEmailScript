import csv

# Returns an array of tuples of (String, String), which will contain the Company name and their email
def getSponsorList(filepath):
    emailList = []
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # ignore headers
                line_count += 1
            else:
                emailList.append((row[0],row[1]))
                line_count += 1
        print(f'Processed {line_count} addresses.')
    return emailList