import os
import binascii
import mmap
import struct


# thx: http://stackoverflow.com/questions/22901285/taking-a-hex-file-and-extracting-data

class Parser(object):

    start_of_email = 66  # 66th byte is the 132 character

    # the email_index map in the file starts at the first
    # null sequence of 2 bytes "00 00", so "0000" in our string
    # representation.

    email_index_separator = "0000"

    def __init__(self, filename):

        self.filename = filename

    def get_email_addresses(self):

        # initial address start at byte

        return email_addresses

    def go(self):

        with open(self.filename, 'rb') as fp:
            hex_list = ["{:02x}".format(ord(c)) for c in fp.read()]

            email_indeces = [self.start_of_email]
            first_index_byte_index = 0

            for i, byte in enumerate(hex_list):
                if i < self.start_of_email:
                    continue
                if byte == '00' and hex_list[i+1] == "00":
                    first_index_byte_index = i+2
                    break


            import pdb
            pdb.set_trace()




            # email_map_start_index = ascii_file.find(
            #     self.email_index_separator,
            #     (self.start_of_email*2)
            # ) + len(self.email_index_separator)
            #
            # for two_byte in ascii_file[email_map_start_index:].split('0000'):
            #     try:
            #         # thx: http://stackoverflow.com/questions/30803985/convert-hex-string-to-integer-with-python
            #         int_val = struct.unpack("<h", binascii.unhexlify(two_byte))
            #         print two_byte
            #         print int_val
            #         print binascii.unhexlify(two_byte)
            #
            #         email_indeces.append(int_val)
            #         if int_val >= email_map_start_index:
            #             break
            #     except Exception as e:
            #         print e
            #         email_indeces.append(two_byte)
            #




            # map_index_ascii = ascii_file_sans_header[email_index_start:].split('0000')
            # for ascii_rep in map_index_ascii:
            #     try:
            #         if ascii_rep and int(ascii_rep, 16) < email_index_start:
            #             email_indeces.append(int(ascii_rep, 16))
            #     except ValueError, e:
            #         print e


            # Just keep getting indeces until you hit the max_index_start



            # split on the first sign of 4 null bytes in a row,
            # which indicates the start of the index of emails




