pealkiri = "{:^80}"
print pealkiri.format("ARVE NR 666")
print ""
fmt1 = "{:<25}{:<30}{:>20}"
print fmt1.format("Arve v2ljastaja", "Arve saaja", "Kuup2ev: 06.11.2013")

fmt2 = "{:<25}{:<26}{:>20}"
print fmt2.format("Lauri Lindmets", "Juku Juku", "Makset2htaeg: 06.12.2013")

fmt3 = "{:<10}{:>25}{:>32}"
print fmt3.format("Reg. Nr. 987654321", "Reg. Nr. 123456789", "Viitenumber 987654321")

print "___________________________________________________________________________"

print ""

fmt4 = "{:<20}{:>35}{:>10}{:>10}"
print fmt4.format("Kauba nimetus", "Kogus", "Hind", "Summa")
print fmt4.format("Viru Valge 1L", "5 tk", "9.99", "49,95")
print fmt4.format("Naine", "3.00 tk", "25", "75")
print fmt4.format("Syletants", "3 tk", "100", "300")

print "___________________________________________________________________________"

print ""

fmt5 = "{:<29}{:<26}{:>20}"
print fmt5.format("LEPAMETSA TANTSUKOLLEDZ OY", "V2IMELA YHIKAS 9-9 65432", "SEB 32592392373463")
fmt6 = "{:<29}{:<21}{:>10}"
print fmt6.format("KMKR EE1010101010", "Tel. +372 56788765", "lepamets@tantsukolledz.ee")
