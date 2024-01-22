import streamlit as st
from sympy import *

from sympy import symbols, exp, lambdify
import numpy as np
import matplotlib.pyplot as plt

x1, x2 = symbols('x1 x2')
A = st.slider('A', -10, 10, 10)
x0 =st.slider('x0', -10, 10, 0)
y0 =st.slider('y0', -10, 10, 0)
sx = st.slider('sx', 1, 10, 1)
sy = st.slider('sy', 1, 10, 1)

# 定义符号变量
f_gaussian_x1x2 = A * exp(-(x1 -x0) ** 2/2*sx**2 - (x2-y0) ** 2/2*sy**2)

st.latex(f_gaussian_x1x2)
# 将符号表达式转换为Python函数
f_gaussian_x1x2_fcn = lambdify((x1, x2), f_gaussian_x1x2)

# print(type(f_gaussian_x1x2_fcn))
xx1, xx2 = np.meshgrid(np.linspace(-3, 3, 201),
                       np.linspace(-3, 3, 201))

ff = f_gaussian_x1x2_fcn(xx1, xx2)

# 可视化
fig = plt.figure()

ax = fig.add_subplot(projection='3d')
ax.plot_wireframe(xx1, xx2, ff,
                  rstride=10, cstride=10)
ax.set_proj_type('ortho')
ax.view_init(azim=-120, elev=30)
ax.grid(False)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f(x1,x2)')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-10, 10)
ax.set_box_aspect(aspect=(1, 1, 1))
# fig.savefig('二元高斯函数.svg', format='svg')

st.pyplot(fig)
