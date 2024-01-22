import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

# sin_y = np.sin(x_array)
# cos_y = np.cos(x_array)

if st.button('复位'):
    st.rerun()

name = st.text_input('初等函数')
if name:
    exp = sympify(name)
    st.latex(exp)
    x = symbols('x')
    ff = lambdify(x, exp)

    x_array = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    sin_y = ff(x_array)

    fig1, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x_array, sin_y, color='b', linewidth=2)

    # ax.plot(x_array, cos_y, label='cos(x)', color='r', linewidth=2)

    # ax.set_title('sin')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    ax.legend()

    # ax.set_xlim(-2*np.pi, 2*np.pi)
    # ax.set_ylim(-1.5, 1.5)

    st.pyplot(fig1)

name1 = st.text_input('隐性函数')

if st.button('心形函数'):
    name1 = '(x ** 2 +(  (y-abs(x)**(2/3)) ** 2) -1) '
if st.button('sin(x)*x+sin(y)*y -1'):
    name1 = 'sin(x)*x+sin(y)*y -1'

if name1:
    exp = sympify(name1)
    st.latex(exp)
    x, y = symbols('x y')
    ff = lambdify((x, y), exp)

    x = np.linspace(-30, 30, 1000)
    y = np.linspace(-30, 30, 1000)
    fig2, ax = plt.subplots(figsize=(8, 6))
    # 构造网格
    x, y = np.meshgrid(x, y)
    # z = 0.5 * x - 0.3 * np.log1p(x) + 0.3 * y - 0.1 * np.log1p(y) - 1
    z = ff(x, y)

    ax.contour(x, y, z, 0,colors='r')
    ax.axis('equal')

    # plt.show()
    st.pyplot(fig2)


name2 = st.text_input('极坐标')
A = st.slider('A', 1, 10, 5)
if st.button('电风扇'):
    name2 = f'cos({A}*x)'
if name2:
    exp = sympify(name2)
    st.latex(exp)
    x = symbols('x')
    ff = lambdify(x, exp)

    # fig3, ax = plt.subplots(figsize=(8, 6))
    fig3 = plt.figure()

    x_array = np.linspace(0, 2 * np.pi, 1000)
    sin_y = ff(x_array)

    # 绘制极坐标图
    plt.polar(x_array, sin_y)

    st.pyplot(fig3)