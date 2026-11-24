```python
dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dia_semana = 0  # 0 = lunes, 6 = domingo (1 de enero de 1900 fue lunes)
domingos = 0

for anio in range(1900, 2001):
    es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

    for mes in range(12):
        if anio >= 1901 and dia_semana == 6:
            domingos += 1

        dias_actuales = dias_mes[mes]
        if mes == 1 and es_bisiesto:
            dias_actuales = 29

        dia_semana = (dia_semana + dias_actuales) % 7

print(domingos)

```
