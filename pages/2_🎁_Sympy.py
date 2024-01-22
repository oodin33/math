
import streamlit as st
from sympy import *


st.set_page_config(page_title="Sympy", page_icon="🎁")
st.text_area(   'Sympy 简单说明 :100:',
                "因式分解 ---factor---eg>2*x**5 + 2*x**4*y + 4*x**3 + 4*x**2*y + 2*x + 2*y \n"
                "多项式展开式---expand---eg> (x+y) **3 \n"
                '简化表达式---simplify---eg> (x + x**2)/(x*sin(y)**2 + x*cos(y)**2) \n'
                '合并同类相---collect---eg> a*x*log(x) + b*(x*log(x)), x*log(x) \n'
                'P/Q---collect---eg> (2*x**2 - 2)/(x**2 - 2*x + 1) \n',height=150)

name = st.text_input('因式分解')
if name:
    exp = sympify(name)
    st.latex(exp)
    st.latex(factor(exp))

name = st.text_input('多项式展开式')
if name:
    exp = sympify(name)
    st.latex(exp)
    st.latex(expand(exp))

name = st.text_input('简化表达式')
if name:
    exp = sympify(name)
    st.latex(exp)
    st.latex(simplify(exp))

name = st.text_input('合并同类相')
flag = st.text_input('合并同类相的因变量')
if name and flag:
    exp = sympify(name)
    st.latex(exp)
    st.latex(collect(exp, flag))

name = st.text_input('P/Q')
if name :
    exp = sympify(name)
    st.latex(exp)
    st.latex(cancel(exp))