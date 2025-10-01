# Функции поиска числа
def fast_guess_num(num: int, sp: list[int]) -> list:
    """
    Данная функция реализует базовый метод бинарного поиска.

    :param num: Искомое число
    :param sp: Заданный список
    :param cnt: Счетчик для поиска количества операций. cnt = 0
    :return: возвращает список из искомого числа и количества операций
    """
    cnt = 0
    l = 0
    r = len(sp)
    while (r - l) != 1:
        mid = (r + l) // 2
        if num < sp[mid]:
            r = mid
            if sp[mid] == num:
                break
        else:
            l = mid
        cnt += 1
    if cnt == 0:
        return [sp[l], cnt + 1]
    cnt -= 1
    return [sp[l], cnt]


def guess_num(num: int, sp: list[int]) -> list:
    """
    Данная функция реализует поиск числа перебором.

    :param num: Искомое число
    :param sp: Заданный список
    :param cnt: Счетчик для поиска количества операций. cnt = 0
    :return: возвращает список из искомого числа и количества операций
    """
    cnt = 0
    for i in sp:
        if num == i:
            return [num, cnt + 1]
        else:
            cnt += 1
