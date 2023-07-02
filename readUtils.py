import csv

# TODO Implement skipping empty rows

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
            # If the row is empty, skip it
            # Or accept a placeholder value - if it's there, skip it
            # Or check if there is an "@" in the string.
            else:
                emailList.append((row[0], row[1]))
                line_count += 1
        print(f'Processed {line_count} addresses.')
    return emailList