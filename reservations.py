import datetime as dt


class Reserva():

    def __init__(self, fecha, entrada, salida):
        self.entrada = dt.time(hour=entrada, minute=0)
        self.salida = dt.time(hour=salida, minute=0)
        self.fecha = fecha

    def info(self):
        return f'Fecha: {self.fecha}, check in: {self.entrada} - check out: {self.salida}'


def desplegar_r(all_res):
    for r in all_r:
        print(r.info())


fecha = dt.date(year=2021, month=2, day=14)


r1 = Reserva(8, 10, fecha)
r2 = Reserva(14, 15, fecha)
r3 = Reserva(15, 18, fecha)
r4 = Reserva(18, 20, fecha)

all_r = [r1, r2, r3, r4]

mi_reserva = Reserva(12, 17, fecha)

for i in range(1, len(all_r)):
    r_siguiente = all_r[i]
    r_anterior = all_r[i-1]

    if mi_reserva.entrada >= r_anterior.salida and mi_reserva.salida <= r_siguiente.entrada:
        all_r.insert(i, mi_reserva)
        break


if mi_reserva in all_r:
    print('Tu reserva se realizó con éxito.')
    desplegar_r(all_r)

else:
    print('Lo sentimos, ese espacio ya fue ocupado.')
    desplegar_r(all_r)
