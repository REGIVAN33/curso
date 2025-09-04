# dia hora e ano atual

from datetime import datetime
agora = datetime.now()
segundo_atual = agora.second
minnutos_atual = agora.minute
hora_atual = agora.hour
dia_atual = agora.day
mes_atual = agora.month
ano_atual = agora.year

print(f" São {hora_atual}:{minnutos_atual}.{segundo_atual} horas, do dia {dia_atual}/{mes_atual}/{ano_atual}")