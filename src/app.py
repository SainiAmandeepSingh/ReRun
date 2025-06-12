# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 22:01:59 2025

@author: Singh
"""

import streamlit as st
from extractor import extract

st.title("Supermarket Flyer Extractor")

url = st.text_input("Flyer URL")

if st.button("Extract"):
    if url:
        try:
            products = extract(url)
            if products:
                st.json(products)
            else:
                st.write("No products found.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.write("Please enter a URL.")
