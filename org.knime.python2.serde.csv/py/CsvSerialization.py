import pandas
import tempfile
import os
import base64


_types_ = None
_eval_types_ = None
_bytes_types_ = None


def init(types):
    global _types_, _eval_types_, _bytes_types_
    _types_ = types
    _eval_types_ = {_types_.BOOLEAN_LIST.value, _types_.BOOLEAN_SET.value, _types_.INTEGER_LIST.value,
                    _types_.INTEGER_SET.value, _types_.LONG_LIST.value, _types_.LONG_SET.value,
                    _types_.DOUBLE_LIST.value, _types_.DOUBLE_SET.value, _types_.STRING_LIST.value,
                    _types_.STRING_SET.value, _types_.BYTES_LIST.value, _types_.BYTES_SET.value}
    _bytes_types_ = {_types_.BYTES.value, _types_.BYTES_LIST.value, _types_.BYTES_SET.value}


def column_names_from_bytes(data_bytes):
    path = data_bytes.decode('utf-8')
    in_file = open(path, 'r')
    try:
        data_frame = pandas.read_csv(in_file, index_col=0, nrows=0, skiprows=2)
    except ValueError:
        data_frame = pandas.DataFrame()
    in_file.close()
    return data_frame.columns.tolist()


def column_types_from_bytes(data_bytes):
    path = data_bytes.decode('utf-8')
    in_file = open(path, 'r')
    types = in_file.readline().strip()[2:].split(',')
    if types == ['']:
        types = []
    column_types = []
    for i in range(len(types)):
        col_type_id = int(types[i])
        column_types.append(_types_(col_type_id))
    in_file.close()
    return column_types


def column_serializers_from_bytes(data_bytes):
    path = data_bytes.decode('utf-8')
    in_file = open(path, 'r')
    types = in_file.readline().strip()[2:].split(',')
    serializers_line = in_file.readline().strip()[2:].split(',')
    serializers = {}
    for part in serializers_line:
        if part != '':
            key_value = part.split('=')
            serializers[key_value[0]] = key_value[1]
    return serializers


def bytes_into_table(table, data_bytes):
    path = data_bytes.decode('utf-8')
    in_file = open(path, 'r')
    types = in_file.readline().strip()[2:].split(',')
    if types == ['']:
        types = []
    serializers_line = in_file.readline().strip()[2:].split(',')
    try:
        names = pandas.read_csv(in_file, index_col=0, nrows=0).columns.tolist()
    except ValueError:
        names = []
    in_file.seek(0)
    # this is commented out because assigning types if a column contains missing values will fail
    # dtypes = {}
    # for i in range(len(names)):
    #     name = names[i]
    #     col_type_id = int(types[i])
    #     if col_type_id == _types_.BOOLEAN.value:
    #         col_type = numpy.bool
    #     elif col_type_id == _types_.INTEGER.value:
    #         col_type = numpy.int32
    #     elif col_type_id == _types_.LONG.value:
    #         col_type = numpy.int64
    #     elif col_type_id == _types_.DOUBLE.value:
    #         col_type = numpy.float64
    #     else:
    #         col_type = numpy.str
    #     dtypes[name] = col_type
    try:
        # data_frame = pandas.read_csv(in_file, index_col=0, skiprows=2, na_values=['MissingCell'], dtype=dtypes)
        data_frame = pandas.read_csv(in_file, index_col=0, skiprows=2, na_values=['MissingCell'])
    except ValueError:
        data_frame = pandas.DataFrame()
    for i in range(len(types)):
        col_type_id = int(types[i])
        if col_type_id in _eval_types_:
            for j in range(len(data_frame)):
                index = data_frame.index[j]
                if str(data_frame[names[i]][index]) != 'nan':
                    data_frame.set_value(index, names[i], eval(data_frame[names[i]][index]))
                else:
                    data_frame.set_value(index, names[i], None)
        if col_type_id == _types_.BYTES.value:
            for j in range(len(data_frame)):
                index = data_frame.index[j]
                if str(data_frame[names[i]][index]) != 'nan':
                    data_frame.set_value(index, names[i], base64.b64decode(data_frame[names[i]][index]))
                else:
                    data_frame.set_value(index, names[i], None)
        elif col_type_id == _types_.BYTES_LIST.value:
            for j in range(len(data_frame)):
                index = data_frame.index[j]
                base64_list = data_frame[names[i]][index]
                if base64_list is not None:
                    bytes_list = []
                    for k in range(len(base64_list)):
                        bytes_value = base64_list[k]
                        if bytes_value:
                            bytes_list.append(base64.b64decode(bytes_value))
                        else:
                            bytes_list.append(None)
                    data_frame.set_value(index, names[i], bytes_list)
        elif col_type_id == _types_.BYTES_SET.value:
            for j in range(len(data_frame)):
                index = data_frame.index[j]
                base64_set = data_frame[names[i]][index]
                if base64_set is not None:
                    bytes_set = set()
                    for value in base64_set:
                        if value:
                            bytes_set.add(base64.b64decode(value))
                        else:
                            bytes_set.add(None)
                    data_frame.set_value(index, names[i], bytes_set)
    table._data_frame = data_frame
    in_file.close()
    os.remove(path)


def table_to_bytes(table):
    path = tempfile.mkstemp(suffix='.csv', prefix='python-to-java-', text=True)[1]
    out_file = open(path, 'w')
    types_line = '#'
    needs_copy = False
    types = []
    for i in range(table.get_number_columns()):
        col_type_id = table.get_type(i).value
        types.append(col_type_id)
        if col_type_id in _bytes_types_:
            needs_copy = True
        types_line += ',' + str(col_type_id)
    serializers_line = '#'
    column_serializers = table.get_column_serializers()
    for serializer_id in column_serializers:
        serializers_line += ',' + serializer_id + '=' + column_serializers[serializer_id]
    out_file.write(types_line + '\n')
    out_file.write(serializers_line + '\n')
    data_frame = table._data_frame
    if needs_copy:
        data_frame = data_frame.copy()
    names = data_frame.columns.tolist()
    for i in range(len(types)):
        col_type_id = int(types[i])
        if col_type_id == _types_.BYTES.value:
            for j in range(len(data_frame)):
                index = data_frame.index[j]
                if data_frame[names[i]][index] is not None:
                    data_frame.set_value(index, names[i], base64.b64encode(data_frame[names[i]][index]))
        elif col_type_id == _types_.BYTES_LIST.value:
            for j in range(len(data_frame)):
                index = data_frame.index[j]
                bytes_list = data_frame[names[i]][index]
                if bytes_list is not None:
                    base64_list = []
                    for k in range(len(bytes_list)):
                        bytes_value = bytes_list[k]
                        if bytes_value:
                            base64_list.append(base64.b64encode(bytes_value))
                        else:
                            base64_list.append(None)
                    data_frame.set_value(index, names[i], base64_list)
        elif col_type_id == _types_.BYTES_SET.value:
            for j in range(len(data_frame)):
                index = data_frame.index[j]
                bytes_set = data_frame[names[i]][index]
                if bytes_set is not None:
                    base64_set = set()
                    for value in bytes_set:
                        if value:
                            base64_set.add(base64.b64encode(value))
                        else:
                            base64_set.add(None)
                    data_frame.set_value(index, names[i], base64_set)
    data_frame.to_csv(out_file, na_rep='MissingCell')
    out_file.close()
    return bytearray(path, 'utf-8')