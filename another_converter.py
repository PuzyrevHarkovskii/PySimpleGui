import PySimpleGUI as sg

layout = [
    [sg.Input(key="-INPUT-"),
    sg.Spin(["Евро в рубли", "Йены в рубли", "Тенге в рубли"], key="UNITS"),
    sg.Button("Конвертировать" ,key = "-CONVERT-")],
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
            if unit == "Евро в рубли":
                output = int(input_value) * 90.18
                output_string = f"{input_value} евро это {output} рублей"
            elif unit == "Йены в рубли":
                output = int(input_value) * 0.61
                output_string = f"{input_value} йен это {output} рублей"
            elif unit == "Тенге в рубли":
                output = int(input_value) * 0.18
                output_string = f"{input_value} тенге это {output} рублей"
            
            window["-OUTPUT-"].update(output_string)
            
window.close()