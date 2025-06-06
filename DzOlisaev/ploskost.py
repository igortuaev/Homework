#Задание 18.

#1 Написать функцию, которая рисует на экране оси координат x и y с числовыми обозначениями.
def draw_coordinates(xcenter: int = 512, ycenter: int = 512, grid_step: int = 40, grid_range: int = 10) -> None:
    '''
    Функция "draw_coordinates" рисует координатную сетку с осями X и Y, с рисками и числовыми подписями.
    Входные данные:
        - "xcenter" - координата центра по оси X, тип данных - int.
        - "ycenter" - координата центра по оси Y, тип данных - int.
        - "grid_step" - расстояние между рисками на осях, тип данных - int.
        - "grid_range" - количество рисок в положительном и отрицательном 
          направлениях на каждой оси, тип данных - int. 
    Выходные данные:
        - Функция cоздаёт графическое окно с координатной 
          сеткой, отображая оси X и Y, точки начала координат, риски и числовые 
          подписи.
    '''
    import tkinter as tk
    main_window = tk.Tk()
    main_window.title('Координатная плоскость')
    main_window.geometry('1024x1024')
    canvas = tk.Canvas(main_window, width=1024, height=1024, bg='brown1')
    canvas.pack()
    canvas.create_line(0, ycenter, 1024, ycenter, fill='cornsilk1', width=2)
    canvas.create_line(xcenter, 0, xcenter, 1024, fill='cornsilk1', width=2)
    canvas.create_line(1024, ycenter, 1004, ycenter - 10, fill='cornsilk1', width=2)
    canvas.create_line(1024, ycenter, 1004, ycenter + 10, fill='cornsilk1', width=2)
    canvas.create_line(xcenter, 0, xcenter - 10, 20, fill='cornsilk1', width=3)
    canvas.create_line(xcenter, 0, xcenter + 10, 20, fill='cornsilk1', width=3)
    canvas.create_text(1004, ycenter - 20, text="X", fill="cornsilk1", font=("Arial", 12, "bold"))
    canvas.create_text(xcenter + 20, 20, text="Y", fill="cornsilk1", font=("Arial", 12, "bold"))
    canvas.create_oval(xcenter - 5, ycenter - 5, xcenter + 5, ycenter + 5, fill='cornsilk1', outline='cornsilk1')
    canvas.create_text(xcenter - 10, ycenter + 10, text="0", fill="cornsilk1", font=("Arial", 14, "bold"))
    for i in range(1, grid_range + 1):
        canvas.create_line(xcenter + i * grid_step, ycenter - 5, xcenter + i * grid_step, ycenter + 5, fill='cornsilk1')
        canvas.create_text(xcenter + i * grid_step, ycenter + 15, text=str(i), fill='cornsilk1', font=("Arial", 10, "bold"))
        canvas.create_line(xcenter - i * grid_step, ycenter - 5, xcenter - i * grid_step, ycenter + 5, fill='cornsilk1')
        canvas.create_text(xcenter - i * grid_step, ycenter + 15, text=str(-i), fill='cornsilk1', font=("Arial", 10, "bold"))
    for i in range(1, grid_range + 1):
        canvas.create_line(xcenter - 5, ycenter - i * grid_step, xcenter + 5, ycenter - i * grid_step, fill='cornsilk1')
        canvas.create_text(xcenter + 15, ycenter - i * grid_step, text=str(i), fill='cornsilk1', font=("Arial", 10, "bold"))
        canvas.create_line(xcenter - 5, ycenter + i * grid_step, xcenter + 5, ycenter + i * grid_step, fill='cornsilk1')
        canvas.create_text(xcenter + 15, ycenter + i * grid_step, text=str(-i), fill='cornsilk1', font=("Arial", 10, "bold"))
    main_window.mainloop()

if __name__ == "__main__":
    draw_coordinates(xcenter=512, ycenter=512, grid_step=45, grid_range=10)