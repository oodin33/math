import streamlit as st

# def modify_bin_file(file_path):
#     # 读取二进制文件
#     with open(file_path, 'rb') as f:
#         bin_data = f.read()
#
#     # 获取二进制数据的大小
#     bin_size = len(bin_data)
#
#     # 如果二进制数据的大小小于0x10000，则将二进制数据的大小修改为0x00000-0x10000，并使用0填充多余的空间
#     if bin_size < 0x10000:
#         bin_data += b'\x00' * (0x10000 - bin_size)
#
#     # 如果二进制数据的大小大于0x10000，则将多余的数据删除
#     elif bin_size > 0x10000:
#         bin_data = bin_data[:0x10000]
#
#     # 将修改后的二进制数据写入文件
#     with open(file_path, 'wb') as f:
#         f.write(bin_data)
bin1_data = b''
bin2_data = b''
bin3_data = b''
bin4_data = b''
bin5_data = b''
bin6_data = b''
flash_bin = b''


def merge_bin_files(bin1_data, bin2_data, bin3_data, bin4_data, bin5_data, bin6_data):
    # 将二进制数据按照指定的地址段进行合并
    merged_data = b''
    # merged_data += bin1_data[0:0x10000]  # isp.bin
    merged_data += bin1_data[0:0x10000]  # isp.bin
    merged_data += b'\xff' * (0x10000 - len(merged_data))

    merged_data += bin2_data[:0x11000 - 0x10000]  # userdata
    merged_data += b'\xff' * (0x11000 - len(merged_data))

    merged_data += bin2_data[:0x12000 - 0x11000]  # factory data
    merged_data += b'\xff' * (0x12000 - len(merged_data))

    merged_data += bin3_data[:0x1b000 - 0x12000]  # cmos
    merged_data += b'\xff' * (0x1b000 - len(merged_data))

    merged_data += b'\xff' * (0x1c000 - len(merged_data))

    merged_data += bin4_data[:0x20000 - 0x1c000]  # tvi
    merged_data += b'\xff' * (0x20000 - len(merged_data))

    merged_data += bin5_data[:0x2c000 - 0x20000]  # font
    merged_data += b'\xff' * (0x2c000 - len(merged_data))

    merged_data += bin6_data[:0x30000 - 0x2c000]  # osd
    merged_data += b'\xff' * (0x30000 - len(merged_data))

    merged_data += bin1_data[:0x40000 - 0x30000]  # isp.bin
    merged_data += b'\xff' * (0x40000 - len(merged_data))
    # 将合并后的二进制数据写入文件
    # with open('merged.bin', 'wb') as f:
    #     f.write(merged_data)
    return merged_data


uploaded_file1 = st.file_uploader("Choose isp.bin", type='bin')
if uploaded_file1 is not None:
    # To read file as bytes:
    bin1_data = uploaded_file1.getvalue()

uploaded_file2 = st.file_uploader("Choose userdata", type='dat')
if uploaded_file2 is not None:
    # To read file as bytes:
    bin2_data = uploaded_file2.getvalue()

uploaded_file3 = st.file_uploader("Choose cmos", type='cmos')
if uploaded_file3 is not None:
    # To read file as bytes:
    bin3_data = uploaded_file3.getvalue()

uploaded_file4 = st.file_uploader("Choose tvi", type='tvi')
if uploaded_file4 is not None:
    # To read file as bytes:
    bin4_data = uploaded_file4.getvalue()

uploaded_file5 = st.file_uploader("Choose font.bin", type='bin')
if uploaded_file5 is not None:
    # To read file as bytes:
    bin5_data = uploaded_file5.getvalue()

uploaded_file6 = st.file_uploader("Choose osd", type='osd')
if uploaded_file6 is not None:
    # To read file as bytes:
    bin6_data = uploaded_file6.getvalue()

if st.button('合成'):
    flash_bin = merge_bin_files(bin1_data, bin2_data, bin3_data, bin4_data, bin5_data, bin6_data)
    st.write('合成完成')

st.download_button('Download binary file', flash_bin)
