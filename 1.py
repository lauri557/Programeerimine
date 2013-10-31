eesnimi = raw_input('Mis su nimi on:')
perekonnanimi = raw_input('Mis su perekonnanimi on:')

if eesnimi == "Jaan-Edgar" and perekonnanimi == 'Urm':
	print "Sina, v2ike v22nik, oled mulle v6lgu 15 Eurot."
else:
	print "Sinu nimi on " + eesnimi + " " + perekonnanimi

vastus = raw_input('Kas sa maksad 2ra enne 5. Nov?:')

if vastus == "Jah" or "ja" or "jh":
	print "Okey, tore seda kuulda"
else:
	print "Killin sinu 2ra kui ei maksa"
