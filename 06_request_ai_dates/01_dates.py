# Trabajando con fechas y horas en Python

from datetime import datetime, timedelta
import locale

# 1. Obtener la fecha y hora actual
now = datetime.now()
print(f"Fecha y hora actual: {now}")

# 2. Crear una fecha y hora específica
specific_date = datetime(2025, 2, 12, 15, 30, 0)
print(f"Fecha y hora específica: {specific_date}")

# 3. Formatear fechas
# método strftime() para formatear fechas
# pasarle el objeto datetime y el formato especificado
# formato:
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

format_date = now.strftime("%A %B %Y %H:%M:%S")
print(f"Fecha formateada: {format_date}")

# 4. Operaciones con fechas (sumar/restar dias, minutos, horas, meses)
yesterday = datetime.now() - timedelta(days=1)
print(f"Ayer: {yesterday}")

tomorrow = datetime.now() + timedelta(days=1)
print(f"Mañana: {tomorrow}")

one_hour_after = datetime.now() + timedelta(hours=1)
print(f"Una hora después: {one_hour_after}")

# 5. Obtener componentes individuales de una fecha
year = now.year
print(year)

month = now.month
print(month)

# 6. Calcular la diferencia entre 2 fechas
date1 = datetime.now()
date2 = datetime(2025, 2, 12, 15, 30, 0)
difference = date2 - date1
print(f"Diferencia entre las fechas: {difference}")


f0 = datetime(2025, 1, 1, 0, 0, 0) 
fE = datetime(2025, 1, 2, 1, 12, 0) 
deltaT = 10

def createTspan(f0,fE,deltaT):
    """ This function creates a time array that starts at f0 and ends at fE with a time step of deltaT.
    f0 = datetime(2025, 1, 1, 0, 0, 0) 
    fE = datetime(2025, 1, 1, 1, 0, 0) 
    deltaT = elapsed time in minutes between measurements.
    Example of use:
    
    The measurement is made every ten mins, starting time [2025,1,1,0,0,0] ending time [2025,1,1,1,0,0]
    f0 = datetime.(2025,1,1,0,0,0)
    fe = datetime(2025,1,1,1,0,0)
    deltaT = 10 (10 minutes each measurement)

    # Result
    tspan = [datetime.datetime(2025, 1, 1, 0, 0), datetime.datetime(2025, 1, 1, 0, 10), datetime.datetime(2025, 1, 1, 0, 20), datetime.datetime(2025, 1, 1, 0, 30), datetime.datetime(2025, 1, 1, 0, 40), datetime.datetime(2025, 1, 1, 0, 50), datetime.datetime(2025, 1, 1, 1, 0)]
    """
    dt = (fE-f0).seconds/(60*deltaT)
    tspan = [f0+timedelta(minutes=deltaT*t) for t in range(0,int(dt)+1)]
    return tspan

tspan = createTspan(f0,fE,deltaT)
print(tspan)

tspan_str = [t.strftime("%Y/%m/%d %H:%M") for idx, t in enumerate(tspan)]

