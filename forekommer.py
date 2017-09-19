def forekommer(tekst, bokstav):
    teller = 0
    for elem in tekst:
        if elem == bokstav:
            teller += 1
    return teller

def uten_repetisjon(tekst):
    nyTekst = []
    for elem in tekst:
        if elem not in nyTekst:
            nyTekst.append(elem)
    
    return nyTekst

def antallForskjellige(tekst):
    nyTekst = uten_repetisjon(tekst)
    return len(nyTekst)


tekst = "abcabcabcabcabc"

print(forekommer(tekst, "a"))
print(uten_repetisjon(tekst))
print(antallForskjellige(tekst))

    
