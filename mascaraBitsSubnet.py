from Scripts.binari import entradaIpAprovar,subnetMaskBinari,deBinariArab,decimalsAbinari,ipArabaBinari,networkAddress,wildcardMask,broadCastAddress,ipBinariarab

#autor : Guillem Ardanuy Martínez

controlEntradaNetworkBits=True


while controlEntradaNetworkBits:

    try:
        networkBits = int(input("quants bits de xarxa vols?") or "10")  # aqui els 1   el or serveix per posar un valor per defecte si el usuari no entra cap valor
        if(networkBits>0 and networkBits<32):
            controlEntradaNetworkBits=False
        else:
            print("de 0 a 32")
    except:
        print("de 0 a 32 nomes numeros siusplau")


ipAprobar=entradaIpAprovar()

#print("EXTRACCIO IP APROBAR ----> ",ipAprobar)

#print("ip a probar ----------------> ",ipAprobar)


hostBits=32-networkBits # els 0

nb=networkBits
hb=hostBits

diccioIPiMascara={"ipDecimal":ipAprobar,"nb":nb,"hb":hb}
print("diccio IP I MASCARA DICCIONARI---------------------> ",diccioIPiMascara,"\n")

calculsSubNeting=subnetMaskBinari(nb,hb)  # guardem el resultat aixi no hem de cridar cada cop la funcio per extreure els valors.

#posem al seulloc les variables de calculs de subneting
subnetMask=calculsSubNeting[0]
maskaraBitsLista=calculsSubNeting[1]
maskaraDecimalLista=calculsSubNeting[2]
cuatreOctetsDecimals=calculsSubNeting[3]
diccioIPiMascara["subnetMaskBinari"]=subnetMask

print("diccioIPiMascaraDiccionari---> ",diccioIPiMascara)

separador="""\n ----------------------------------------------------------------------"""

print("(variable subnetMask STRING)la maskara de subXarxa  en bits es: " +subnetMask)
print("(variable SubnetMask LIST) la maskara de subXarxa en bits es: ",maskaraBitsLista)
print("(variable subnetMask Lista)la maskara de subXarxa  en Decimals es: " ,maskaraDecimalLista)
print("(variable STRING)la mascara de subXarxa en Decimal es: " +cuatreOctetsDecimals+separador)

diccioIPiMascara["subnetMaskArab"]=cuatreOctetsDecimals
diccioIPiMascara["hostsUtils"]=str(2**hb-2)
diccioIPiMascara["subXarxesTotals"]=str(2**nb)

print("els hosts de xarxa es 2 ^ "+str(hb)+" TOTAL DE HOSTS EN LA XARXA: "+ str(2**hb) + "\n s'han de treure el de xarxa i el de broadcast , total utilitzables: "+str(2**hb-2))

print("les subxarxes totals son 2 elevat a "+str(nb)+" = "+str(2**nb)+separador)

print ("IP AMB BINARI: ",ipArabaBinari(ipAprobar))
print("ip amb arab: ",ipAprobar+separador)

diccioIPiMascara["ipBinari"]=ipArabaBinari(ipAprobar)

print("SUBNETMASK (bits de xarxa a 1,hosts a 0): ",subnetMask)
print("SubnetMask amb arab: "+ipBinariarab(subnetMask),separador)
print("wildcardMask: (bits de hosts a 1, xarxa a 0)",wildcardMask(subnetMask))
print("wildcardMask: (bits de hosts a 1, xarxa a 0) amb arab",ipBinariarab(wildcardMask(subnetMask)),separador)

diccioIPiMascara["wildCardMaskBinari"]=wildcardMask(subnetMask)
diccioIPiMascara["wildCardMaskArab"]=ipBinariarab(diccioIPiMascara["wildCardMaskBinari"])

#ipBinari+=decimalsAbinari(k)

print("network adress en BINARI es: ",networkAddress(ipArabaBinari(ipAprobar),subnetMask))
print("network addres en ARAB es : ",ipBinariarab(networkAddress(ipArabaBinari(ipAprobar),subnetMask)),separador)

diccioIPiMascara["networkAddressBinari"]=networkAddress(ipArabaBinari(ipAprobar),subnetMask)
diccioIPiMascara["networkAddressArab"]=ipBinariarab(diccioIPiMascara["networkAddressBinari"])


#print(separador,separador,wildcardMask(subnetMask),separador,separador)

print("broadCastAddres en BINARI: ",broadCastAddress(ipArabaBinari(ipAprobar),wildcardMask(subnetMask)))
print("broadCastAddres en ARAB es: ",ipBinariarab(broadCastAddress(ipArabaBinari(ipAprobar),wildcardMask(subnetMask))),separador)

diccioIPiMascara["broadCastAddressBinari"]=broadCastAddress(ipArabaBinari(ipAprobar),wildcardMask(subnetMask))
diccioIPiMascara["broadCastAddressArab"]=ipBinariarab(diccioIPiMascara["broadCastAddressBinari"])

#print("yeaaaaaaaaah ha de d onar 112.3.2.127 -->", ipBinariarab(broadCastAddress("01110000.00000011.00000010.00000011","00000000.00000000.00000000.01111111")) )


print("whiteMagic")
for k in diccioIPiMascara:
    print(k," --> ",diccioIPiMascara[k])

