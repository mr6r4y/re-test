# Structure Description

            [prev_size_0 8b][size_0 8b]
    p_0 --> [fd_0        8b][bk_0   8b]
            [data_0                16b]
            [prev_size_1 8b]
            ---------------------------
                            [size_1 8b]
    p_1 --> [fd_1        8b][bk_1   8b]

            [data_1                16b]  ==  [fake_chunk]
            ==
            [

              [prev_size_1_2 8b][size_1_2 8b]
    p_1_2 --> [fd_1_2        8b][bk_1_2   8b]

            ]
            ==

            [prev_size_2 8b]
            ---------------------------
                            [size_2 8b]
    p_2 --> [fd_2        8b][bk_2   8b]
            [data_2                16b]
            [prev_size_3 8b]
            ---------------------------
            [wilderness]




            [prev_size_0 8b]
    p_0 --> [size_0 8b] = 0x30 | PREV_IN_USE
            [fd_0        8b][bk_0   8b]
            [data_0                16b]
            [prev_size_1 8b]
            ---------------------------
    p_1 --> [size_1 8b] = 0x30 | PREV_IN_USE
            [fd_1        8b][bk_1   8b]
            [data_1                16b]
            [prev_size_2 8b]
            ---------------------------
    p_2 --> [size_2 8b] = 0x30 | PREV_IN_USE
            [fd_2        8b][bk_2   8b]
            [data_2                16b]
            [prev_size_3 8b]
            ---------------------------
            [wilderness]

# Limitations

* size_0 == prev_size_1
* size_1 == prev_size_2
* p_0 < p_0 + size_0
* p_1 < p_1 + size_1
* p_2 < p_2 + size_2
* size_0/size_1/size_2 >= MINSIZE
* size_0/size_1/size_2 % MALLOC_ALIGNMENT == 0
