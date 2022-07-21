import matplotlib.pyplot as plt
import numpy as np

delta_t = 0.01
t_max = 50
k = 1
m = 1
x0 = 1
v0 = 0


def a(x): return - (k * x / m)


def Euler(t_max, delta_t, v0, x0, a):
    v = [v0]
    x = [x0]
    t_interval = [0]

    vt = v0
    xt = x0

    for t in np.arange(delta_t, t_max, delta_t):

        new_v = vt + a(xt) * delta_t
        new_x = xt + vt * delta_t

        v.append(new_v)
        x.append(new_x)
        t_interval.append(t)

        xt = new_x
        vt = new_v

    return {"v": v, "x": x, 't': t_interval}


def Verlet(t_max, delta_t, x0, v0, a):

    delta_t2 = delta_t * delta_t
    x1 = x0 + v0 * delta_t + 0.5 * a(x0) * delta_t2

    xt_old = x0
    xt = x1

    position = [x0]
    velocity = [v0]
    time = [0]

    for t in np.arange(delta_t, t_max, delta_t):
        x_next = 2 * xt - xt_old + a(xt) * delta_t2
        vt = (x_next - xt_old) / (2 * delta_t)

        position.append(xt)
        time.append(t)
        velocity.append(vt)
        xt_old = xt
        xt = x_next

    return {"x": position, "t": time, "v": velocity}


euler = Euler(t_max, delta_t, v0, x0, a)
verlet = Verlet(t_max, delta_t, v0, x0, a)


plt.plot(euler["t"], euler["v"])
plt.plot(euler["t"], euler["x"])

plt.plot(verlet["t"], verlet["v"])
plt.plot(verlet["t"], verlet["x"])

plt.legend(["euler v", "euler x", "verlet v", "verlet x"])
plt.show()
