import streamlit as st
import numpy as np
import math
import matplotlib.pyplot as plt

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[100, 200, 300], [400, 500, 600]])
arr3 = np.array([10, 20, 30], ndmin=2)
arr4 = np.zeros((2, 3))
arr5 = np.ones((5, 6))
arr6 = np.random.rand(3, 3)
st.write(arr1)
st.write(arr2)
st.write(arr3)
st.write(arr4)
st.write(arr5)
st.write(arr6)


