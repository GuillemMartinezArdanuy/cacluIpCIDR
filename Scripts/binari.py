
def entradaIpAprovar ():
    contadorDe4=0
    try:
        ipTest = input("ip xarxa? exemple 192.168.1.1")
        #print("ipTest dins de funcio es : --------------------> ", ipTest)
        #print("contador ----> ", contadorDe4)
        part=ipTest.split(".")
        #print("PART---> ",part)
        if len(part)==4:
            #print("dins")
            for o in part:
                oInt=int(o)
                #print(o)
                if oInt>=0 and oInt<=255:
                    #print("ok")
                    contadorDe4+=1
                    #print("contador---> ",contadorDe4)
                else:
                    print("valor entre 0 i 255")
                    return entradaIpAprovar()
        else:
            print("format XXX.XXX.XXX.XXX    -->   entre 0 i 255")
            return entradaIpAprovar()
    except:
        print("format XXX.XXX.XXX.XXX    -->   entre 0 i 255")
        return entradaIpAprovar()
    #print("retornemmmmmmm ---> ", ipTest)
    if contadorDe4==4:
        #print("dins de contador de 4 igual a 4 ",contadorDe4)
        #print("retornem ----> ",ipTest)
        return ipTest

    else:
        #print("contador de 4  dins de else que no ha de ser 4 ",contadorDe4)
        #print("dins de else despres de comprobar que contador noes 4")
        return entradaIpAprovar()


def subnetMaskBinari(n,h):
    networkBits=n
    hostBits=h
    subnetMask = ""  # creem la string buida
    # print("tipus subnetMASK--->", type(subnetMask))
    posemPunt = 0  # cada cop que afegim 1 o 0 augmentem arribara a 32 si es multiple de 8 es posa punt

    cuatreOctetsDecimals = ""  # sera la mascara per exemple 255.255.255.0
    octetDecimal = 0  # valor en decimal del octet

    posicioOctet = 8  # iniciem a 8 cada cop el nirem restant

    maskaraBitsLista = []

    maskaraDecimalLista = []

    aAfegirOctetBitsMascara = ""

    while networkBits > 0:
        subnetMask += str(1)
        aAfegirOctetBitsMascara += str(1)
        networkBits -= 1
        posemPunt += 1
        posicioOctet -= 1
        octetDecimal += (2 ** posicioOctet)
        if (posemPunt % 8 == 0 and networkBits >= 0 and posemPunt != 32):
            subnetMask += "."
            cuatreOctetsDecimals += str(octetDecimal) + "."
            maskaraBitsLista.append(aAfegirOctetBitsMascara)
            aAfegirOctetBitsMascara = ""
            maskaraDecimalLista.append(octetDecimal)
            octetDecimal = 0  # reiniciem el valor de octet
            posicioOctet = 8

    # print("octetDecimal abans de entrar al calcul dels 0: "+str(octetDecimal))
    while hostBits > 0:
        subnetMask += str(0)
        aAfegirOctetBitsMascara += "0"
        hostBits -= 1
        posemPunt += 1
        posicioOctet -= 1
        octetDecimal += 0
        if (posemPunt % 8 == 0 and hostBits != 0):
            subnetMask += "."
            cuatreOctetsDecimals += str(octetDecimal) + "."
            maskaraDecimalLista.append(octetDecimal)
            maskaraBitsLista.append(aAfegirOctetBitsMascara)
            octetDecimal = 0  # reiniciem octet
            aAfegirOctetBitsMascara = ""
            posicioOctet = 8

    maskaraDecimalLista.append(octetDecimal)
    maskaraBitsLista.append(aAfegirOctetBitsMascara)
    cuatreOctetsDecimals += str(octetDecimal)

    return subnetMask,maskaraBitsLista,maskaraDecimalLista,cuatreOctetsDecimals


def decimalsAbinari(numeroArab=0): # entra un numero arab (base 10) y et retorna un binari (base 2)
    numeroBinari = ""
    if numeroArab==0:
        return '0'
    while True:
        if (numeroArab % 2==0 and numeroArab!=0):
            #print(numeroArab ," == 0 ")
            numeroBinari+="0"
            numeroArab//=2
        elif(numeroArab % 2==1):
            #print(numeroArab , " == 1 ")
            numeroBinari+="1"
            numeroArab //= 2
        elif (numeroArab==0):            
            return numeroBinari # string


def deBinariArab(numeroBinari): # entra un numero binari (base 2) i et retorna un numero arab (base 10)
    numeroBinari=numeroBinari[::-1] # girem aixi anirem del 0 al 128
    numeroArab=0
    exponencial=1
    for e in numeroBinari:
        if e==" ":
            pass
        elif int(e)==1:
            #print("1")
            numeroArab+=exponencial;
        elif int(e)==0:
            #print("0")
            pass

        else:
            print("EL BINARI NOMES POT TENIR 0 o 1 !!!!")
            break
        exponencial*=2  # multipliquem per 2
    return numeroArab # int

#print("en decimal es : ", decimalsAbinari(255)[::-1])
#print(deBinariArab('11101111'))

def ipArabaBinari(ipArab="112.3.2.3"): #entra una ip en numeros arabs(base10), i et retorna una ip en format binari (base 2)
    contadordePunts = 3
    ipArab = ipArab.split(".")
    ipBinari = ""
    for k in ipArab:
        #print(k)
        resBinari=decimalsAbinari(int(k))
       # print("BINARI ",str(resBinari)," K ", k)
        faltaDigitsPer8= 8 - len(resBinari)
        if(faltaDigitsPer8>0):
            ipBinari+=(faltaDigitsPer8*"0")+str(resBinari[::-1])
            contadordePunts-=1
        else:
            ipBinari+=resBinari[::-1]
            contadordePunts-=1
        if contadordePunts>=0:
            ipBinari+="."
    return ipBinari


#transformem una ip binari de entrada amb una ip arab de sortida
def ipBinariarab(ipBinari="01110000.00000011.00000010.00000011"):
    ipArab=" "
    ipBinari=ipBinari.split(".")
    numeroPunts=3
    for e in ipBinari:
       # print ( "e: ",e," ipBinari ", ipBinari, " ipBinari de e: " , "\n ipBinari[-1]: ", ipBinari[-1])
        ipArab+=str(deBinariArab(e))
        if numeroPunts>0:
            ipArab+="."
            numeroPunts-=1
        else:
            return ipArab

def wildcardMask(subnetMask="11111111.11111111.11111111.10000000"): # entra una mascara de subxarxa y et reotrna el wildmask (inversio 0 --> 1 , 1 --> 0)
    wildCMask=" "
    for e in range(len(subnetMask)):
        if(subnetMask[e]=="0"):
            wildCMask+="1"
        elif(subnetMask[e]=="1"):
            wildCMask+="0"
        elif(subnetMask[e]=="."):
            wildCMask+="."
        else:
            raise(excepction)
    return wildCMask
            


#entra una ip en format Binari, i la seva submascara ,i et retorna la adresa de xarxa
def networkAddress(ipAddresBinari='01110000.00000011.00000010.00000011',subnetMaskBinari='11111111.11111111.11111111.1000000'):
   # print("ipaddresBinari ",ipAddresBinari," subnetMask ",subnetMaskBinari)
    ind=0
    netAddress=" "
    #print(ipAddresBinari,"\n",subnetMaskBinari)
    if (len(ipAddresBinari)==len(subnetMaskBinari)):
        for e in range(len(ipAddresBinari)):
            #print(ipAddresBinari[e],subnetMaskBinari[e])
            if (ipAddresBinari[e]=="."):
                netAddress+="."
            elif(ipAddresBinari[e]=="1" and subnetMaskBinari[e]=="1" ):
                netAddress+="1"
            else:
                netAddress+="0"
    else:
        raise
    return netAddress


#entra la ipAddress en format binari, i la wildCardMask (inversa de subxarxaMask)
def broadCastAddress(ipAddress="01110000.00000011.00000010.00000011",wildCardMask="00000000.00000000.00000000.01111111"):
    broadCAddress=" "
    #print("wildCardMask -----------> ",wildCardMask)
   # print("dins broadcast --> ipAddres : ",ipAddress," len: ",len(ipAddress.strip()))
    #print("dins broadcast --> wildCard : ", wildCardMask," len: ",len(wildCardMask.strip()))
    ipAddress=ipAddress.strip()
    wildCardMask=wildCardMask.strip()
    if (len(ipAddress)==len(wildCardMask)): # eliminem posibles espais que poden donar a errors
     #   print("dins if len==len")
        for e in range(len(ipAddress)):
            #print(ipAddress[e]," --> ",wildCardMask[e])
            #print(ipAddresBinari[e],subnetMaskBinari[e])
            if (ipAddress[e]=="."):
                broadCAddress+="."
            elif(ipAddress[e]=="1" or wildCardMask[e]=="1" ):
                broadCAddress+="1"
            elif(ipAddress[e]=="0"  or wildCardMask[e]=="0"):
                broadCAddress+="0"
        #print("broadcast BINARI----> ",broadCAddress)
    return broadCAddress # surt string bc binari
