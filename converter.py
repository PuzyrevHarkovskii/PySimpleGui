import PySimpleGUI as sg

layout = [
    [sg.Input(key="-INPUT-"),
     sg.Spin(["Километры в метры", "Килограмы в фунты", "Секунды в минуты"], key="-UNITS-"),
     sg.Button("Конвертировать", key="-CONVERT-")],
    [sg.Text("Вывод", key="-OUTPUT-")]
]

window = sg.Window("Converter", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-CONVERT-":
        input_value = values["-INPUT-"]
        if input_value.isnumeric():
            unit = values["-UNITS-"]
            if unit == "Километры в метры":
                output = int(input_value) * 1000
                output_string = f"{input_value} км = {output} м"
            elif unit == "Килограмы в фунты":
                output = int(input_value) * 2.20462
                output_string = f"{input_value} кг = {output} фунтов"
            elif unit == "Секунды в минуты":
                output = int(input_value) / 60
                output_string = f"{input_value} сек = {output} мин"

            window["-OUTPUT-"].update(output_string)

window.close()
