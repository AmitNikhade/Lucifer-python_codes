import cdata.tally as mod
conn = mod.connect("Url='http://localhost:9000'")
cur = conn.cursor()

cmpname = input("Enter Company Name: ").split()
cmpstr = ''

for c in cmpname:
    cmpstr += c
    cmpstr = cmpstr+' '

ncmpstr = cmpstr.rstrip()
print("\n", ncmpstr)

cur.execute(
    f"SELECT CreditAmount,DebitAmount FROM Report_BankGroupSummary where Name='{ncmpstr}' ")
Res = cur.fetchall()
for r in Res:
    print("Credit Amount: ", r[0], "\n")
    print("Debit Amount: ", r[1], "\n")
