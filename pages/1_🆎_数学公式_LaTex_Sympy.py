import streamlit as st
import pandas as pd
import numpy as np
# import sympy
from sympy import *

str = [r'x^{2}-y^{2} = \left(x+y\right)\left(x-y\right)',
       r'a_{n}x^{n}+a_{n-1}x^{n-1}+\dotsb + a_{2}x^{2} +a_{1}x + a_{0}',
       r'\sum_{k=0}^{n}a_{k}x^{k}',
       r'ax^{2}+bx+c=0\ (a\neq 0)',
       r'{\sqrt[{n}]{a^{m}}}=(a^{m})^{1/n}=a^{m/n}=(a^{1/n})^{m}=({\sqrt[{n}]{a}})^{m}',
       r'\left({\sqrt {1-x^{2}}}\right)^{2}',
       r'\frac {1}{x+1}+{\frac {1}{x-1}}={\frac {2x}{x^{2}-1}}',
       r'x_{1,2}={\frac {-b\pm {\sqrt {b^{2}-4ac}}}{2a}}',
       r'f(x)=ax^{2}+bx+c~~{\text{ with }}~~a,b,c\in\mathbb {R} ,\ a\neq 0',
       r'f(x_1, x_2) = x_1^2 + x_2^2 + 2x_1x_2',
       r'\log_{b}(xy)=\log_{b}x+\log_{b}y',
       r'\ln(xy)=\ln x+\ln y{\text{ for }} x>0{\text{ and }} y>0',
       r'f(x)=a\exp \left(-{\frac {(xb)^{2}}{2c^{2}}}\right)',
       r'\sin ^{2}\theta +\cos ^{2}\theta =1',
       r'\sin(\alpha \pm \beta )=\sin \alpha \cos \beta \pm\cos \alpha \sin \beta',
       r'\tan(\alpha \pm \beta )=\frac {\tan \alpha \pm \tan\beta }{1\mp \tan \alpha \tan \beta }',
       r'\exp(x)=\sum _{k=0}^{\infty }{\frac{x^{k}}{k!}}=1+x+{\frac {x^{2}}{2}}+{\frac{x^{3}}{6}}+{\frac {x^{4}}{24}}+\cdots',
       r'\left(\sum _{i=0}^{n}a_{i}\right)\left(\sum_{j=0}^{n}b_{j}\right)=\sum _{i=0}^{n}\sum_{j=0}^{n}a_{i}b_{j}',
       r'\exp(x) =\lim _{n\to \infty }\left(1+{\frac{x}{n}}\right)^{n}',
       r'\int _{-\infty }^{\infty }\exp(-x^{2})\mathrm{d}x={\sqrt {\mathrm{\pi} }}',
       r'\mathbf {A} = {\begin{bmatrix} 1 & 2\\ 3& 4 \\ 5 & 6 \end{bmatrix}}',
       r'\mathbf {A}={\begin{bmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots &\vdots &\ddots &\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{bmatrix}}',
       ]

st.set_page_config(page_title="数学公式", page_icon="🆎")

name = st.text_input('LaTeX:')
if name:
    st.latex(name)

name_exp = st.text_input('Sympy:')
if name_exp:
    exp = sympify(name_exp)
    st.write(f"LaTex:", latex(exp))
    st.latex(exp)

st.write('常用的数学表达式')
for i in range(len(str)):
    st.write(f"LaTex {i} : {str[i]}")
    st.latex(str[i])
