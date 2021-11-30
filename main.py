import numpy as np
import math


def task1(k, v, n, lam, buf):
    """
    calculates probability of refuse

    Parameters
    ----------
    k: int
        Number of channels
    v: int
        Speed
    n: int
        size of pack
    lam: float
        intensity
    buf: int
        size of buffer
    """
    ro = lam / (v / n)
    m = k * (buf - 1)

    chast = ro ** k / math.factorial(k) * (ro ** m) / (k ** m)
    znam = math.fsum([ro ** j / math.factorial(j) for j in range(k)]) + \
           ro ** k / math.factorial(k) * math.fsum([ro ** s / k ** s for s in range(m)])
    return chast / znam


def task2(k, lam, buf):
    # Количество пакетов
    n_packets = 1000
    # Текущее время
    t = 0
    # текущий размер очереди
    queue = 0
    # Максимальный размер очереди
    m = k * (buf - 1)
    # Интенсивность выходного потока
    mu = 2.08
    # время, когда прибор освободится
    t_free = [0.0]*k
    # Количество потярянных пактеов
    n_lost = 0

    for _ in range(n_packets):
        # время поступления нового пакета
        t += np.random.exponential(scale=1 / lam)
        # количество занятых концентраторов
        n_close = 0
        # проверяем есть, ли очередь
        if queue > 0:
            for i in range(k):
                while t_free[i] < t and queue > 0:
                    # обрабатываем пакеты из очереди до момента t
                    t_free[i] += np.random.exponential(scale=1 / mu)
                    queue -= 1
        for i in range(k):
            if t_free[i] < t:
                t_free[i] = t + np.random.exponential(scale=1 / mu)
                break
            else:
                n_close += 1
        if n_close == k:
            if queue < m:
                queue += 1
            else:
                n_lost += 1
    return n_lost/n_packets


def main():
    np.random.seed(100)
    k = 4
    v = 5000
    buffer = 4
    n = 2400
    lambda_day = 4
    lambda_night = 0.5
    # max_queue = (k * (buffer - 1))
    print("day time probability:", '%.40f' % task1(k, v, n, lambda_day, buffer))
    print("night time probability:", '%.40f' % task1(k, v, n, lambda_night, buffer))

    # Количество повторов в методе Монте-Карло
    n_rep = 1000

    # Вероятность блокировки
    p_refuse = 0

    # Имитационное моделирование
    for i in range(n_rep):
        p_refuse += task2(k, lambda_day, buffer)
    p_refuse /= n_rep
    print("day time probability2:", '%.40f' % p_refuse)


if __name__ == "__main__":
    main()
