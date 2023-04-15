# -----------------Imports----------------- #
import os.path


# -----------------Functions----------------- #
def delete_empty_lines(input_list):
    list_without_empty_lines = input_list.copy()

    list_without_empty_lines.pop(0)
    list_without_empty_lines.pop(0)

    return list_without_empty_lines


def find_id(input_list):
    list_tmp = input_list.copy()
    id_number_of_element = []

    for i_id in range(4):
        if list_tmp[0] != ' ':
            id_number_of_element.append(list_tmp.pop(0))
        else:
            list_tmp.pop(0)
    id_number_of_element = ''.join(id_number_of_element)

    return id_number_of_element


def find_type(input_list):
    list_tmp = input_list.copy()
    type_of_element_to_draw = []

    for i_type in range(5):
        list_tmp.pop(0)

    if list_tmp[0] == 'О':
        for i_type in range(10):
            tmp = list_tmp.pop(0)
            type_of_element_to_draw.append(tmp)
    elif list_tmp[0] == 'Д':
        for i_type in range(9):
            tmp = list_tmp.pop(0)
            type_of_element_to_draw.append(tmp)
    elif list_tmp[0] == 'Л':
        for i_type in range(5):
            tmp = list_tmp.pop(0)
            type_of_element_to_draw.append(tmp)
    type_of_element_to_draw = ''.join(type_of_element_to_draw)

    return type_of_element_to_draw


def find_any_elements(input_list, first_indent, second_indent):
    list_tmp = input_list.copy()
    elements = []
    dictionary = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.']

    for i_elements in range(first_indent):
        list_tmp.pop(0)

    for i_elements in range(second_indent):
        if list_tmp[0] in dictionary:
            elements.append(list_tmp.pop(0))
        else:
            list_tmp.pop(0)
    elements = ''.join(elements)

    return elements


def find_base(input_list):
    list_tmp = input_list.copy()
    base_of_element = []
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.', ',']

    for i_base in range(67):
        list_tmp.pop(0)

    for i_base in range(13):
        if list_tmp[0] in numbers:
            base_of_element.append(list_tmp.pop(0))
        else:
            list_tmp.pop(0)
    base_of_element = ''.join(base_of_element)
    base_of_element = base_of_element.split(',')

    return base_of_element


def split_the_list_circle(input_list, num_of_rows):
    list_tmp = input_list.copy()
    list_circle_items = []

    for num in range(num_of_rows):
        if list_tmp[num][1] == "Окружность":
            list_circle_items.append(list_tmp[num])

    return list_circle_items


def split_the_list_line_odd(input_list, num_of_rows):
    list_tmp = input_list.copy()
    list_odd_items = []

    for num in range(num_of_rows):
        if list_tmp[num][1] == "Линия":
            if num % 2 == 0:
                list_odd_items.append(list_tmp[num])

    return list_odd_items


def split_the_list_line_even(input_list, num_of_rows):
    list_tmp = input_list.copy()
    list_even_items = []

    for num in range(num_of_rows):
        if list_tmp[num][1] == "Линия":
            if num % 2 != 0:
                list_even_items.append(list_tmp[num])

    return list_even_items


def split_the_list_distance(input_list, num_of_rows):
    list_tmp = input_list.copy()
    list_distance_items = []

    for num in range(num_of_rows):
        if list_tmp[num][1] == "Дистанция":
            list_distance_items.append(list_tmp[num])

    return list_distance_items


def find_coordinates_from_base_x(input_list, id_in):
    list_tmp = input_list.copy()
    x0_list_out = []
    search_result = False

    for element in range(len(list_tmp)):
        if list_tmp[element][0] == id_in:
            x0_list_out.append(list_tmp[element][2])
            search_result = True

    return x0_list_out, search_result


def find_coordinates_from_base_y(input_list, id_in):
    list_tmp = input_list.copy()
    y0_list_out = []
    search_result = False

    for element in range(len(list_tmp)):
        if list_tmp[element][0] == id_in:
            y0_list_out.append(list_tmp[element][3])
            search_result = True

    return y0_list_out, search_result


def find_coordinates_from_base_z(input_list, id_in):
    list_tmp = input_list.copy()
    z0_list_out = []
    search_result = False

    for element in range(len(list_tmp)):
        if list_tmp[element][0] == id_in:
            z0_list_out.append(list_tmp[element][4])
            search_result = True

    return z0_list_out, search_result


def list_of_lists_to_list_of_strings(input_list):
    list_tmp = input_list.copy()
    list_with_strings_out = []

    for sublist in list_tmp:
        for item in sublist:
            list_with_strings_out.append(item)

    return list_with_strings_out


def main(in_path_to_folder="E:/Python_Projects/PyCharm_Projects/Text_Work/Converter/files_to_transform/0390.txt",
         in_color=(255, 255, 255)):
    # -----------------Variables----------------- #
    list_original = []
    list_indexed_chars = []
    list_result = []
    str_to_write = []

    # -----------------Open_txt_Start----------------- #
    path_to_folder = os.path.dirname(in_path_to_folder) + str('/')
    file_name = os.path.basename(in_path_to_folder)
    raw_file_name = os.path.splitext(os.path.basename(in_path_to_folder))[0]
    script_file_name = raw_file_name + str('.scr')

    cwd = os.getcwd()
    if not os.path.isdir(cwd + str('/') + str("output_scripts")):
        os.makedirs(cwd + str('/') + str("output_scripts"))
    path_to_script = cwd + str('/') + str("output_scripts") + str('/')

    path_to_file = (path_to_folder + file_name)
    infile = open(path_to_file, "r")
    for line in infile.readlines():
        list_original.append(line)

    # -----------------Delete_1st_and_2nd_Columns----------------- #
    list_only_data = delete_empty_lines(list_original)

    # -----------------Nums_of_Columns----------------- #
    number_of_rows = len(list_only_data)

    # -----------------Main_Program----------------- #
    default_color = (0, 0, 0)
    if in_color is None:
        color = default_color
    else:
        color = ','.join(map(str, in_color))
    str_to_write.append("COLOR Truecolor " + str(color) + " \n\n")
    print("COLOR " + str(color))

    for row in range(number_of_rows):
        list_indexed_lines = list_only_data[row]
        for columns in list_indexed_lines:
            for char in columns:
                list_indexed_chars.append(char)
        id_of_element = find_id(list_indexed_chars)
        type_of_element = find_type(list_indexed_chars)
        if type_of_element == 'Дистанция':
            list_out = [id_of_element, type_of_element, find_any_elements(list_indexed_chars, 15, 15),
                        find_any_elements(list_indexed_chars, 30, 13), find_any_elements(list_indexed_chars, 43, 11),
                        find_any_elements(list_indexed_chars, 54, 13), find_base(list_indexed_chars)]
        else:
            list_out = [id_of_element, type_of_element, find_any_elements(list_indexed_chars, 15, 15),
                        find_any_elements(list_indexed_chars, 30, 13), find_any_elements(list_indexed_chars, 43, 11),
                        find_any_elements(list_indexed_chars, 54, 13)]
        list_result.append(list_out)
        del list_indexed_lines
        list_indexed_chars.clear()

    list_circle = split_the_list_circle(list_result, number_of_rows)

    number_of_list_circle = len(list_circle)
    for i in range(number_of_list_circle):
        str_to_write.append("_.circle _non ")
        str_to_write.append(list_circle[i][2])
        str_to_write.append(",")
        str_to_write.append(list_circle[i][3])
        str_to_write.append(",")
        str_to_write.append(list_circle[i][4])
        str_to_write.append(" ")
        str_to_write.append("D")
        str_to_write.append(" ")
        str_to_write.append(list_circle[i][5])
        str_to_write.append("\n")

    list_line_odd = split_the_list_line_odd(list_result, number_of_rows)
    list_line_even = split_the_list_line_even(list_result, number_of_rows)

    number_of_list_line_odd = len(list_line_odd)
    number_of_list_line_even = len(list_line_even)
    number_of_list_line = number_of_list_line_odd + number_of_list_line_even
    for i in range(number_of_list_line_odd):
        str_to_write.append("_.line _non ")
        str_to_write.append(list_line_odd[i][2])
        str_to_write.append(",")
        str_to_write.append(list_line_odd[i][3])
        str_to_write.append(",")
        str_to_write.append(list_line_odd[i][4])
        str_to_write.append(" ")
        str_to_write.append(list_line_even[i][2])
        str_to_write.append(",")
        str_to_write.append(list_line_even[i][3])
        str_to_write.append(",")
        str_to_write.append(list_line_even[i][4])
        str_to_write.append(" \n")

    list_distance = split_the_list_distance(list_result, number_of_rows)

    x0_list = []
    y0_list = []
    x1_list = []
    y1_list = []
    z0_list = []
    z1_list = []

    number_of_list_distance = len(list_distance)
    for i in range(number_of_list_distance):

        str_to_write.append("_.line _non ")

        id_search_0 = list_distance[i][6][0]
        id_search_1 = list_distance[i][6][1]

        # Search list circle for distance indexes
        x0, search = find_coordinates_from_base_x(list_circle, id_search_0)
        if search:
            x0_list.append(x0)
        y0, search = find_coordinates_from_base_y(list_circle, id_search_0)
        if search:
            y0_list.append(y0)
        z0, search = find_coordinates_from_base_z(list_circle, id_search_0)
        if search:
            z0_list.append(z0)

        x1, search = find_coordinates_from_base_x(list_circle, id_search_1)
        if search:
            x1_list.append(x1)
        y1, search = find_coordinates_from_base_y(list_circle, id_search_1)
        if search:
            y1_list.append(y1)
        z1, search = find_coordinates_from_base_z(list_circle, id_search_1)
        if search:
            z1_list.append(z1)

        x0_list_of_strings = list_of_lists_to_list_of_strings(x0_list)
        y0_list_of_strings = list_of_lists_to_list_of_strings(y0_list)
        x1_list_of_strings = list_of_lists_to_list_of_strings(x1_list)
        y1_list_of_strings = list_of_lists_to_list_of_strings(y1_list)
        z0_list_of_strings = list_of_lists_to_list_of_strings(z0_list)
        z1_list_of_strings = list_of_lists_to_list_of_strings(z1_list)

        str_to_write.append(x0_list_of_strings[i])
        str_to_write.append(",")
        str_to_write.append(y0_list_of_strings[i])
        str_to_write.append(",")
        str_to_write.append(z0_list_of_strings[i])
        str_to_write.append(" ")
        str_to_write.append(x1_list_of_strings[i])
        str_to_write.append(",")
        str_to_write.append(y1_list_of_strings[i])
        str_to_write.append(",")
        str_to_write.append(z1_list_of_strings[i])
        str_to_write.append(" \n")

    if os.path.isfile(path_to_script + script_file_name):
        open(path_to_script + script_file_name, 'w').close()
        with open(path_to_script + script_file_name, 'a') as f:
            for line in str_to_write:
                f.write(line)
    else:
        with open(path_to_script + script_file_name, 'a') as f:
            for line in str_to_write:
                f.write(line)

    print("Done!")
    return number_of_rows, number_of_list_circle, number_of_list_line, number_of_list_distance


if __name__ == '__main__':
    main()
