import os
import sys
import array
import dbs

files = ['xin.dsc']

# allow specifying multiple files on command line
if len(sys.argv) > 1:
    files = sys.argv[1:]

for file in files:
    dsc_array_in = array.array('i')
    dsc_array_out = array.array('i')

    # use frombytes because fromfile requires length
    f_in = open(file, 'rb')
    dsc_array_in.frombytes(f_in.read())
    f_in.close()
	
    # FT Magic
    dsc_array_out.append(0x10120116)

    # dsc_array_in[i] is the command id
    # f2/x scripts start from 18
    i = 18
    while True:
        command = dsc_array_in[i]

        if command == 0x13:  # MOUTH_ANIM
            # modify the third parameter of MOUTH_ANIM
            mouth = dsc_array_in[i + 3]
            dsc_array_in[i + 3] = dbs.x_to_f_mouths.get(mouth, mouth)

        # get properties of the input command
        input_param_cnt = dbs.command_lengths_x[command]
        command_str = dbs.command_to_string_x[command]
        print(command_str)

        # only process output if it's a valid command
        if command_str in dbs.string_to_command_f:
            output_command = dbs.string_to_command_f[command_str]
            dsc_array_out.append(output_command)

            output_param_cnt = dbs.command_lengths_f[output_command]

            for param in range(0, output_param_cnt):
                if param < input_param_cnt:
                    dsc_array_out.append(dsc_array_in[i + 1 + param])
                else:
                    dsc_array_out.append(0)

        i += 1 + input_param_cnt

        if command == 0:
            # stop processing if found END
            break

        if i > len(dsc_array_in):
            break

    file_split = os.path.splitext(file)

    output_name = 'fout.dsc'
    if file != 'xin.dsc':
        output_name = file_split[0] + '_f' + file_split[1]

    f_out = open(output_name, 'wb')
    dsc_array_out.tofile(f_out)
    f_out.close()
