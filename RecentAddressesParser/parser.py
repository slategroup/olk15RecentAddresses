import os
import binascii
import mmap


# thx: http://stackoverflow.com/questions/22901285/taking-a-hex-file-and-extracting-data

class Parser(object):

    start_of_email = 66

    # This is kind gross
    email_index_separator = "000000"

    def __init__(self, filename):

        self.filename = filename

    def get_email_addresses(self):

        # initial address start at byte

        return email_addresses

    def go(self):

        with open(self.filename, 'rb') as fp:
            ascii_file = binascii.hexlify(fp.read())
            hex_list= ["{:02x}".format(ord(c)) for c in fp.read()]

            # Throw out the header (up to 66)
            hex_list = hex_list[self.start_of_email:]

            # same with ascii representation
            ascii_file_sans_header = ascii_file[(self.start_of_email*2):]

            email_end = ascii_file_sans_header.find(self.email_index_separator)
            email_index_start = email_end + len(self.email_index_separator)

            email_indeces = []

            # build the map index by starting at map_index_start


            # THE START OF THE INDEX IS BAD AND THROWS IT ALL OFF
            #                    OR
            # THIS IS BIG VS LITTLE ENDIAN, BUT I DON'T THINK SO


            # Once you find a sequence of email_index_separator, you know that a list of indeces
            # separated by groups of '000000' will tell you the delimeters of the email
            # addresses before email_index_start
            map_index_ascii = ascii_file_sans_header[email_index_start:].split('0000')
            for ascii_rep in map_index_ascii:
                try:
                    if ascii_rep and int(ascii_rep, 16) < email_index_start:
                        email_indeces.append(int(ascii_rep, 16))
                except ValueError, e:
                    print e


            # Just keep getting indeces until you hit the max_index_start

            import pdb
            pdb.set_trace()


            # split on the first sign of 4 null bytes in a row,
            # which indicates the start of the index of emails




