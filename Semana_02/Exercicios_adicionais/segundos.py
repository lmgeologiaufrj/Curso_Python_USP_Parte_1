segundos = int(
    input("Por favor, entre com o número de segundos que deseja converter: ")
)

dias = segundos // (24 * 3600)

horas = segundos % (24 * 3600) // 3600

minutos = segundos % (24 * 3600) % 3600 // 60

segundos_restantes = segundos % (24 * 3600) % 3600 % 60

print(
    dias,
    "dias,",
    horas,
    "horas,",
    minutos,
    "minutos e",
    segundos_restantes,
    "segundos.",
)
