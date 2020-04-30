import os
import binascii
import logging
import mmap
import struct
import itertools

mylogger = logging.getLogger("mylogger")

# thx: http://stackoverflow.com/questions/22901285/taking-a-hex-file-and-extracting-data


class Parser(object):

    start_of_email_index = 66  # 66th byte is the 132 character
    end_of_email = None

    def __init__(self, filename):

        self.filename = filename

    def get_email_addresses(self):

        # initial address start at byte

        return email_addresses

    # https: // docs.python.org / 3.1 / library / itertools.html  # recipes
    def grouper(self, n, iterable, fillvalue=None):
        "grouper(8, ['AB','CD','FG'], 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        return itertools.izip_longest(*args, fillvalue=fillvalue)

    def go(self):

        with open(self.filename, 'rb') as fp:
            hex_list = ["{:02x}".format(ord(c)) for c in fp.read()]

            email_indeces = [self.start_of_email_index]
            first_index_byte_index = 0

            for i, byte in enumerate(hex_list):
                if i < self.start_of_email_index:
                    continue
                # Assume that the first sequence of two null bytes indicates
                # the end of email
                if first_index_byte_index == 0 and byte == '00' and hex_list[i+1] == "00":
                    self.end_of_email_index = first_index_byte_index
                    first_index_byte_index = i+2

            # for each group of four, get the second two bytes and int them
            four_byte_groups = self.grouper(
                4, hex_list[first_index_byte_index:], '00')

            for group in four_byte_groups:
                # for each group of four, get the second two bytes and int them
                hex_rep = binascii.unhexlify(''.join(group[2:]))
                try:
                    int_val = struct.unpack("<h", hex_rep)[0]
                except Exception as e:
                    mylogger.error(
                        "Error processing group %s: %s" % (hex_rep, e))
                    int_val = -1
                    continue

                # their value is the next thing to add to email_indeces
                email_indeces.append(self.start_of_email_index + int_val)

                # once their value is equal to or greater than first_index_byte_index
                # stop, processing
                if int_val+self.start_of_email_index >= first_index_byte_index-2:
                    break

            # We now know that our email address go from byte self.start_of_email
            # to self.end_of_email
            emails_hex = []
            for i, index in enumerate(email_indeces):
                if i == len(email_indeces) - 1:
                    break
                emails_hex.append(hex_list[index:email_indeces[i+1]])

            emails = [binascii.unhexlify(''.join(item)) for item in emails_hex]

            for email in emails:
                print(email)

            # email_map_start_index = ascii_file.find(
            #     self.email_index_separator,
            #     (self.start_of_email*2)
            # ) + len(self.email_index_separator)
            #
            # for two_byte in ascii_file[email_map_start_index:].split('0000'):
            #     try:
            #         # thx: http://stackoverflow.com/questions/30803985/convert-hex-string-to-integer-with-python
            #         int_val = struct.unpack("<i", binascii.unhexlify(two_byte))
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
