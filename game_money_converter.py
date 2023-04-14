import PySimpleGUI as sg

layout = [
    
    [sg.Input(key = "-INPUT-"),
     sg.Spin(["Симолионы в рубли", "Крышки Follaut в рубли", "Септимы в рубли"], key = "-UNITS-"),
     sg. Button("Конвертировать", key = "-CONVERT-")],
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
            if unit == "Симолионы в рубли":
                output = int(input_value) * 3 * 164
                output_string = f"{input_value} симолеонов это {output} рублей"
            elif unit == "Крышки Follaut в рубли":
                output = int(input_value) * 1.22 * 81.62
                output_string = f"{input_value} крышек это {output} рублей"
            elif unit == "Септимы в рубли":
                output = int(input_value) / 4 * 81.62
                output_string = f"{input_value} септимов это {output} рублей"
            
            window["-OUTPUT-"].update(output_string)
            
window.close()
            