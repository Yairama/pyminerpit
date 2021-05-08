import streamlit as st

import numpy as np
import pandas as pd


def create_ubc_arrays():
    tables = {
        'Massive': np.array([4, 4, 3, 3, -49, 0, 0, 1, 1, 0]),
        "Tabular or Platy": np.array([2, 2, 4, 4, 4, 4, 4, 4, 2, 1]),
        "Irregular": np.array([3, 0, 1, 1, -49, 2, 2, 4, 0, 4]),
        "Very Narrow": np.array([1, -49, -10, -49, 4, 4, 4, 3, 1, 4]),
        "Narrow": np.array([2, -49, 1, -49, 3, 3, 4, 4, 1, 3]),
        "Intermediate thickness": np.array([3, 0, 3, 0, 0, 1, 0, 4, 0, 2]),
        "Thick": np.array([4, 3, 4, 4, -49, -49, -49, 1, 2, 0]),
        "Very Thick": np.array([4, 4, 3, 4, -49, -49, -49, 0, 1, 0]),
        "Flat": np.array([3, 3, 2, 1, 4, 4, -49, 1, 4, 2]),
        "Intermediate Plunge": np.array([3, 2, 1, 1, 0, 0, 0, 3, 2, 3]),
        "Steep": np.array([1, 4, 4, 4, -49, -49, 4, 4, 0, 2]),
        "Uniform": np.array([3, 3, 4, 3, 4, 4, 3, 2, 2, 0]),
        "Gradational": np.array([3, 2, 4, 2, 1, 2, 2, 3, 1, 1]),
        "Erratic": np.array([2, 2, 3, 2, 0, 0, 2, 4, 1, 3]),
        "Shallow": np.array([4, 2, 3, 3, 2, 3, 3, 2, 2, 1]),
        "Intermediate depth": np.array([0, 3, 4, 2, 2, 3, 3, 3, 1, 1]),
        "Deep": np.array([-49, 3, 2, 2, 3, 2, 2, 4, 1, 2]),

        "RMR OZ Very Weak = 0-20": np.array([3, 4, 1, 3, 6, -49, 0, 0, 3, 4]),
        "RMR OZ Weak = 20-40": np.array([3, 3, 3, 4, 6, 0, 1, 1, 2, 4]),
        "RMR OZ Medium = 40-60": np.array([3, 2, 4, 3, 4, 3, 3, 2, 1, 1]),
        "RMR OZ Strong = 60-80": np.array([3, 0, 4, 1, 2, 5, 3, 3, 1, 0]),
        "RMR OZ Very Strong = 80-100": np.array([3, -49, 4, 0, 2, 6, 3, 3, 0, 0]),
        "RMR HW Very Weak = 0-20": np.array([2, 3, -49, 4, 6, -49, 0, 3, 0, 4]),
        "RMR HW Weak = 20-40": np.array([3, 3, 0, 4, 5, 0, 0, 5, 0, 4]),
        "RMR HW Medium = 40-60": np.array([4, 3, 3, 3, 4, 3, 2, 4, 2, 1]),
        "RMR HW Strong = 60-80": np.array([4, 2, 4, 2, 3, 5, 4, 3, 3, 0]),
        "RMR HW Very Strong = 80-100": np.array([4, 2, 4, 2, 3, 6, 4, 3, 3, 0]),
        "RMR FW Very Weak = 0-20": np.array([2, 3, 0, 1, 0, 0, 0, 3, 0, 3]),
        "RMR FW Weak = 20-40": np.array([3, 3, 0, 2, 0, 0, 0, 3, 0, 1]),
        "RMR FW Medium = 40-60": np.array([4, 3, 2, 3, 0, 0, 2, 2, 1, 0]),
        "RMR FW Strong = 60-80": np.array([4, 2, 3, 3, 0, 0, 3, 2, 2, 0]),
        "RMR FW Very Strong = 80-100": np.array([4, 2, 3, 3, 0, 0, 3, 2, 2, 0]),

        "RSS OZ Very Weak": np.array([4, 4, 0, 2, 6, 0, 0, 0, 3, 4]),
        "RSS OZ Weak": np.array([3, 2, 2, 3, 5, 0, 1, 1, 2, 3]),
        "RSS OZ Medium": np.array([3, 1, 4, 3, 2, 3, 3, 3, 1, 1]),
        "RSS OZ Strong": np.array([3, 0, 4, 2, 1, 6, 4, 3, 0, 0]),
        "RSS HW Very Weak": np.array([3, 4, 0, 4, 6, 0, 0, 3, 3, 4]),
        "RSS HW Weak": np.array([3, 3, 1, 3, 5, 0, 1, 5, 2, 2]),
        "RSS HW Medium": np.array([4, 2, 4, 2, 2, 2, 3, 4, 2, 1]),
        "RSS HW Strong": np.array([4, 0, 5, 1, 2, 6, 4, 2, 2, 0]),
        "RSS FW Very Weak": np.array([3, 4, 0, 1, 0, 0, 0, 1, 2, 3]),
        "RSS FW Weak": np.array([3, 3, 1, 2, 0, 0, 2, 3, 2, 2]),
        "RSS FW Medium": np.array([4, 2, 3, 2, 0, 0, 3, 2, 1, 0]),
        "RSS FW Strong": np.array([4, 1, 3, 2, 0, 0, 3, 2, 1, 0])}

    return tables


def create_gui():
    st.title('Mining Method Selector')
    st.write("Ranking of geometry/grade distribution for different mining methods")

    general_shape_cb = st.selectbox('General Shape:', ('Massive', 'Tabular or Platy', 'Irregular'))
    general_shape_array = ubc_tables.get(general_shape_cb)

    ore_thickness_cb = st.selectbox('Ore Thickness:', ('Very Narrow', 'Narrow', 'Intermediate thickness',
                                                       'Thick', 'Very Thick'))
    ore_thickness_array = ubc_tables.get(ore_thickness_cb)

    ore_plunge_cb = st.selectbox('Ore Plunge:', ('Flat', 'Intermediate Plunge', 'Steep'))
    ore_plunge_array = ubc_tables.get(ore_plunge_cb)

    grade_distribution_cb = st.selectbox('Grade Distribution:', ('Uniform', 'Gradational', 'Erratic'))
    grade_distribution_array = ubc_tables.get(grade_distribution_cb)

    depth_cb = st.selectbox('Depth:', ('Shallow', 'Intermediate depth', 'Deep'))
    depth_array = ubc_tables.get(depth_cb)

    rmr_oz_cb = st.selectbox('RMR Ore Zone:', ('RMR OZ Very Weak = 0-20', 'RMR OZ Weak = 20-40',
                                               'RMR OZ Medium = 40-60', 'RMR OZ Strong = 60-80',
                                               'RMR OZ Very Strong = 80-100'))
    rmr_oz_array = ubc_tables.get(rmr_oz_cb)

    rmr_hw_cb = st.selectbox('RMR Hanging Wall:', ('RMR HW Very Weak = 0-20', 'RMR HW Weak = 20-40',
                                                   'RMR HW Medium = 40-60', 'RMR HW Strong = 60-80',
                                                   'RMR HW Very Strong = 80-100'))
    rmr_hw_array = ubc_tables.get(rmr_hw_cb)

    rmr_fw_cb = st.selectbox('RMR FootWall:', ('RMR FW Very Weak = 0-20', 'RMR FW Weak = 20-40',
                                               'RMR FW Medium = 40-60', 'RMR FW Strong = 60-80',
                                               'RMR FW Very Strong = 80-100'))
    rmr_fw_array = ubc_tables.get(rmr_fw_cb)

    rss_oz_cb = st.selectbox('RSS Ore Zone:', ('RSS OZ Very Weak', 'RSS OZ Weak',
                                               'RSS OZ Medium', 'RSS OZ Strong'))
    rss_oz_array = ubc_tables.get(rss_oz_cb)

    rss_hw_cb = st.selectbox('RSS Hanging Wall:', ('RSS HW Very Weak', 'RSS HW Weak',
                                                   'RSS HW Medium', 'RSS HW Strong'))
    rss_hw_array = ubc_tables.get(rss_hw_cb)

    rss_fw_cb = st.selectbox('RSS FootWall:', ('RSS FW Very Weak', 'RSS FW Weak',
                                               'RSS FW Medium', 'RSS FW Strong'))
    rss_fw_array = ubc_tables.get(rss_fw_cb)


    df_result = pd.DataFrame(general_shape_array + ore_thickness_array + ore_plunge_array + grade_distribution_array
                              + depth_array + rmr_oz_array + rmr_hw_array + rmr_fw_array + rss_oz_array + rss_hw_array + rss_fw_array
                              , columns=['Values'], index=['Open Pit mining', 'Block Caving', 'Sublevel Stoping',
                                          'Sublevel Caving', 'LongWall Mining', 'Room and Pillar', 'Shirinkage stoping',
                                          'Cut and fill', 'Top slicing', 'Square set'])

    st.bar_chart(df_result, width = 6000)

    df_result_table = pd.DataFrame({'lab':['Open Pit mining', 'Block Caving', 'Sublevel Stoping',
                                             'Sublevel Caving', 'LongWall Mining', 'Room and Pillar',
                                             'Shirinkage stoping',
                                             'Cut and fill', 'Top slicing', 'Square set'],'val':general_shape_array + ore_thickness_array + ore_plunge_array + grade_distribution_array
                               + depth_array + rmr_oz_array + rmr_hw_array + rmr_fw_array + rss_oz_array + rss_hw_array + rss_fw_array
                               })


    st.write(df_result_table)


if __name__ == "__main__":
    ubc_tables = create_ubc_arrays();
    create_gui()
