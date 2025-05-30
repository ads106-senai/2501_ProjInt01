import time
from datetime import datetime
from clp import CLP

#Como executar a cada 5 seg por tempo 
myclp = CLP('10.104.2.43')
myclp.connect( )

start_time = time.time()
end_time = start_time + 180

hora_inicial = datetime.now()
print(f"Hora inicial das medições: {hora_inicial.strftime('%Y-%m-%d %H:%M:%S')}")

while time.time() < end_time:
    resultado=myclp.read("TEMPO")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Tempo = {resultado.value}")
    time.sleep(5)

hora_final = datetime.now()
print(f"Hora final das medições: {hora_final.strftime('%Y-%m-%d %H:%M:%S')}")
print("Leitura concluída após 3 minutos.")
