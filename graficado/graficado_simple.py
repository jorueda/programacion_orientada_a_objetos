from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado_simple.html')
    figura = figure()

    total_valores = int(input("¿Cuántos valores quieres graficar? "))
    x_valores = list(range(total_valores))
    y_valores = []

    for contador in x_valores:
        valor = int(input(f'Valor y para la posición {contador}: '))
        y_valores.append(valor)

    figura.line(x_valores, y_valores, line_width=2)
    show(figura)