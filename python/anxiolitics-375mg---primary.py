# K Windfuhr, D While, N Kapur, D M Ashcroft, E Kontopantelis, M J Carr, J Shaw, L Applyby, R T Webb, 2024.

import sys, csv, re

codes = [{"code":"65546020","system":"multilex"},{"code":"63765020","system":"multilex"},{"code":"72416020","system":"multilex"},{"code":"59210020","system":"multilex"},{"code":"60510020","system":"multilex"},{"code":"62715020","system":"multilex"},{"code":"64484020","system":"multilex"},{"code":"75692020","system":"multilex"},{"code":"59594020","system":"multilex"},{"code":"91009020","system":"multilex"},{"code":"63881020","system":"multilex"},{"code":"65832020","system":"multilex"},{"code":"479021","system":"multilex"},{"code":"64733020","system":"multilex"},{"code":"63436020","system":"multilex"},{"code":"59784020","system":"multilex"},{"code":"59236020","system":"multilex"},{"code":"60509020","system":"multilex"},{"code":"72417020","system":"multilex"},{"code":"59237020","system":"multilex"},{"code":"59785020","system":"multilex"},{"code":"59209020","system":"multilex"},{"code":"59593020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anxiolitics-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anxiolitics-375mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anxiolitics-375mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anxiolitics-375mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
