import math
import numpy as np
import matplotlib.pyplot as plt


# Переменные:
# alpha - угол положения между двумя точками
# beta - угол ориентации мобильного робота
# distance - расстояние между точками


def input_coordinates():
    coordinates_arr = []
    locale_count = 0
    while True:
        coordinates_arr += [input('Введите координаты точки №' + str(locale_count + 1) + ': ')]
        if len(coordinates_arr[locale_count].split(' ')) > 2:
            break
        locale_count += 1
    return coordinates_arr


def calculation_alpha_angle(x0, x1, y0, y1):
    alpha = 0
    if y0 < y1 and x0 == x1:
        alpha = 0
    if y0 < y1 and x0 < x1:
        alpha = math.degrees(math.atan((x1 - x0) / (y1 - y0)))
    if y0 == y1 and x0 < x1:
        alpha = 90
    if y0 > y1 and x0 < x1:
        alpha = 90 + math.degrees(math.atan((y0 - y1) / (x1 - x0)))
    if y0 > y1 and x0 == x1:
        alpha = 180
    if y0 > y1 and x0 > x1:
        alpha = 180 + math.degrees(math.atan((x0 - x1) / (y0 - y1)))
    if y0 == y1 and x0 > x1:
        alpha = 270
    if y0 < y1 and x0 > x1:
        alpha = 270 + math.degrees(math.atan((y1 - y0) / (x0 - x1)))
    return alpha


def calculation_beta_angles(beta, alpha):
    if beta == alpha:
        beta = alpha
    if (beta > alpha) and (alpha >= (beta - 180)):
        beta = (beta - alpha) * (-1)
    if alpha >= (beta + 180):
        beta = (beta + (360 - alpha)) * (-1)
    if alpha < (beta - 180):
        beta = ((360 - beta) + alpha)
    if (alpha > beta) and (alpha < (beta + 180)):
        beta = alpha - beta
    return beta


def calculation_beta_angle_last(beta, alpha):
    beta_last = 0
    if beta == alpha:
        beta_last = alpha
    if (beta > alpha) and (alpha >= (beta - 180)):
        beta_last = (beta - alpha) * (-1)
    if alpha >= (beta + 180):
        beta_last = (beta + (360 - alpha)) * (-1)
    if alpha < (beta - 180):
        beta_last = ((360 - beta) + alpha)
    if (alpha > beta) and (alpha < (beta + 180)):
        beta_last = alpha - beta
    return beta_last


def output(count, x0, x1, y0, y1, distance, alpha, beta):
    print('____________________________________________')
    print('Пара точек № ' + str(count + 1))
    print('Координаты первой точки (' + str(x0) + ';' + str(y0) + ')')
    print('Координаты второй точки (' + str(x1) + ';' + str(y1) + ')')
    print('Расстояние между точками S=' + str(distance))
    print('Угол между точками: ' + str(alpha))
    print('Угол поворота в первой точке: ' + str(beta))


def calculation_all_info(coordinates_arr, x0, y0, beta):
    # Задаем массивы
    distance_arr = []
    alpha_arr = []
    beta_arr = []
    locale_count = 0
    while locale_count < int(len(coordinates_arr)):
        if int(len(coordinates_arr[locale_count].split(' '))) > 2:
            # Обозначим вторую точку и последний угол положения двух точек.
            x1 = int(coordinates_arr[locale_count].split(' ')[0])
            y1 = int(coordinates_arr[locale_count].split(' ')[1])
            alpha_last = float(coordinates_arr[locale_count].split()[2])

            # Найдем дистанцию между двумя точками.
            distance_arr += [round((((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5), 3)]

            # Найдем углы alpha, beta в первой точке.
            alpha_arr += [calculation_alpha_angle(x0, x1, y0, y1)]
            beta_arr += [calculation_beta_angles(beta, alpha_arr[locale_count])]

            # Последний угол beta (во второй точке) совпадает с углом alpha в первой точке. Найдем его
            beta_last = alpha_arr[locale_count]
            # Найдем последний угол ориентации робота.
            beta_last = calculation_beta_angle_last(beta_last, alpha_last)

            # Выведем на печать данные для этого шага
            output(locale_count, x0, x1, y0, y1, distance_arr[locale_count], alpha_arr[locale_count], beta_arr[locale_count])
            print('Угол конечной ориентации: ' + str(alpha_last))
            print('Угол поворота в конечной точке: ' + str(beta_last))
        else:
            # Обозначим вторую точку.
            x1 = int(coordinates_arr[locale_count].split(' ')[0])
            y1 = int(coordinates_arr[locale_count].split(' ')[1])

            # Найдем дистанцию между двумя точками.
            distance_arr += [round((((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5), 1)]

            # Найдем углы alpha, beta в первой точке.
            alpha_arr += [calculation_alpha_angle(x0, x1, y0, y1)]
            beta_arr += [calculation_beta_angles(beta, alpha_arr[locale_count])]

            # Выведем на печать данные для этого шага
            output(locale_count, x0, x1, y0, y1, distance_arr[locale_count], alpha_arr[locale_count], beta_arr[locale_count])

        # Перезаписываем данные. Сдвигаемся на одну точку вперед.
        beta = alpha_arr[locale_count]
        x0 = x1
        y0 = y1
        locale_count += 1
    return distance_arr, alpha_arr, beta_arr


def image(x0, y0, coordinates_arr, distance_arr, alpha_arr):
    x = [x0]
    y = [y0]

    locale_count = 0
    while locale_count < len(coordinates_arr):
        x += coordinates_arr[locale_count].split(' ')[0]
        y += coordinates_arr[locale_count].split(' ')[1]
        locale_count += 1

    print(x)
    print(y)
    plt.plot(x, y)
    locale_count = 0
    while locale_count < len(distance_arr):
        locale_distance = 0
        while locale_distance <= distance_arr[locale_count]:
            dx = (int(y[locale_count + 1]) - int(y[locale_count])) * locale_distance / distance_arr[locale_count]
            dy = (int(x[locale_count + 1]) - int(x[locale_count])) * locale_distance / distance_arr[locale_count]

            plt.plot(x[locale_count] + dx, y[locale_count] + dy, color="purple", marker='o', markersize=5)

            plt.draw()
            plt.pause(0.1)
            locale_distance += 0.01

        locale_count += 1
    plt.pause(30)
    # plt.close()


def main():
    # Введем начальные координаты.
    start_info = input('Введите координаты начальной точки и угол ориентации робота: ')
    start_x = int(start_info.split(' ')[0])
    start_y = int(start_info.split(' ')[1])
    start_beta = int(start_info.split()[2])

    # Введем координаты точек для перемещения.
    coordinates_arr = input_coordinates()

    # Рассчитаем углы alpha, beta, расстояние между точками.
    # На входе отправляем начальные данные.
    # На выходе получаем массивы с данными для расстояния, углами alpha и beta между точками.
    distance_arr, alpha_arr, beta_arr = calculation_all_info(coordinates_arr, start_x, start_y, start_beta)

    # Работаем с визуализацией
    # image(start_x, start_y, coordinates_arr, distance_arr, alpha_arr)


main()
