def my_view(request):
    return {'project':'newproject'}
def home_view(request):
    return {'project':'zodiac'}
def zodiac2_view(request):
    import sys
    import sys
    import datetime
    params = sys.argv
    
    dia = int(request.POST.get('dia'))
    mes = int(request.POST.get('mes'))
    anyo = 2000
    data = datetime.date(anyo, mes, dia)
    signe = "prova"
    ari =  datetime.date(anyo, 3, 21)
    tau =  datetime.date(anyo, 4, 21)
    gem =  datetime.date(anyo, 5, 22)
    can =  datetime.date(anyo, 6, 22)
    leo =  datetime.date(anyo, 7, 23)
    vir =  datetime.date(anyo, 8, 23)
    lib =  datetime.date(anyo, 9, 23)
    esc =  datetime.date(anyo, 10, 23)
    sag =  datetime.date(anyo, 11, 23)
    cap =  datetime.date(anyo, 12, 22)
    acu =  datetime.date(anyo, 1, 21)
    pis =  datetime.date(anyo, 2, 20)

    if data>=ari and data < tau:
        signe = "Aries"
	imatge = "aries"
    if data>=tau and data < gem:
        signe =  "Tauro"
	imatge = "tauro"
    if data>=gem and data < can:
        signe =  "Geminis"
	imatge = "gemini"
    if data>=can and data < leo:
        signe =  "Cancer"
	imatge = "cancer"
    if data>=leo and data < vir:
        signe =  "Leo"
	imatge = "leo"
    if data>=vir and data < lib:
        signe =  "Virgo"
	imatge = "virgo"
    if data>=lib and data < esc:
        signe =  "Lliura"
	imatge = "libra"
    if data>=esc and data < sag:
        signe =  "Escorpio"
	imatge = "escorpio"
    if data>=sag and data < cap:
        signe =  "Sagitari"
	imatge = "sagitario"
    if data>=cap and data < acu:
        signe =  "Capricorn"
	imatge = "capricornio"
    if data>=acu and data < pis:
        signe =  "Acuari"
	imatge = "acuario"
    if data>=pis and data < ari:
        signe =  "Piscis"
	imatge = "piscis"

    
    
    return {'project':'zodiac','zodiac':signe,'img':imatge}
