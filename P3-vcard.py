import csv

with open('contacts.csv', mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        full_name = row['Full Name']
        phone = row['Phone']
        email = row['Email']
        org = row['Organization']

        vcard = """BEGIN:VCARD
FN:{full_name}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
ORG:{org}
END:VCARD
"""

        filename = full_name.replace(" ", "_") + ".vcf"
        with open(filename, "w") as vcf_file:
            vcf_file.write(vcard)

        print("vCard created:",filename)
