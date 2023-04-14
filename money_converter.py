import PySimpleGUI as sg

layout = [
    [sg.Input(key = "-INPUT-"),
    sg.Spin(["Доллары в рубли","Шекели в рубли","Злотые в рубли"], key = "-UNITS-"),
    sg.Button("Конвертировать", key = "-CONVERT-")],
    [sg.Text("Вывод", key = "-OUTPUT-")]
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
            if unit == "Доллары в рубли":
                output = int(input_value) * 81.29
                output_string = f"{input_value} долларов это {output} рублей"
            elif unit == "Шекели в рубли":
                output = int(input_value) * 22.22
                output_string = f"{input_value} шекелей это {output} рублей"
            elif unit == "Злотые в рубли":
                output = int(input_value) * 19.32
                output_string = f"{input_value} злотых это {output} рублей"
            
        window["-OUTPUT-"].update(output_string)

window.close()