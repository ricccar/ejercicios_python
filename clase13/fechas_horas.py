from datetime import datetime, date, timedelta, time
from time import asctime, gmtime, mktime, localtime


d = date(2026, 3, 7)
print(d)

# Fromisoformat
d = date.fromisoformat("2026-11-20")
print(d)


# Fecha y hora actual
ahora = datetime.now()
print(ahora)
print(ahora.year, ahora.month, ahora.day)
print(ahora.strftime("%d/%m/%Y %H:%M"))     # Formato personalizado, lo imprime como yo quiero

# Parsear una fecha desde string
fecha_texto = "25/12/2024"
fecha = datetime.strptime(fecha_texto, "%d/%m/%Y")
print(fecha, type(fecha))

# Operaciones con fechas
hoy = date.today()
cumple = date(1976, 7, 3)
edad = (hoy-cumple).days // 365
print(edad)

# Sumar y restar tiempo
mañana = hoy +timedelta(days=1)
hace_una_semana = hoy - timedelta(weeks=1)
print(f"Mañana es: {mañana}")
print(f"Hace una semana: {hace_una_semana}")


# Time Horas

res = time()        # Por defecto todo 0.
print(res)

hora = time(2,25,56)
hora2 = time(hour=12, minute=51, second=5)
hora3 = time(2, second=12)
print(hora)
print(hora2)
print(hora3)

hora = time.fromisoformat("01:25:58")
print(hora)
print(hora.hour)
print(hora.minute)
print(hora.second)

hora_actual = datetime.now().hour
print(hora_actual)

# Ejemplo de fechas
var = date(2026,12,5)
var2 = timedelta(days=32)
print(var+var2)
var3 = timedelta(days=12, hours=32)
print(var+var3)

# Time
var = gmtime()
var2 = asctime(var)
print(var)
print(var2)

# Similar a ...
varl = localtime()
varl2 = mktime(varl)        # tiempo en posix
varl3 = datetime.fromtimestamp(varl2)
print (varl, varl2, varl3, sep="\n")
