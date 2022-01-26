###############################################################################################
#                                                                                             #
#   Try saving in base 15 instead of 16; use \xff as a delimeter instead of a usable number   #
#                                                                                             #
###############################################################################################

def main():
        from math import floor, log

        open('fibonacci.bin','w').close()
        fibonacci = open('fibonacci.bin','ab')

        a = 0
        b = 1

        length = 0x8000 # The length of each number in bytes

        while True:
                # byte_length_b = floor(log(b, 16))
                # if byte_length_b == 0:
                #         byte_length_b = 1
                # fibonacci.write(bytearray(b.to_bytes(byte_length_b, 'little')).strip(b'\x00') + b'\x00')
                fibonacci.write(bytearray(b.to_bytes(length, 'little')))
                
                a += b

                # byte_length_a = floor(log(a, 16))
                # if byte_length_a == 0:
                #         byte_length_a = 1
                # fibonacci.write(bytearray(a.to_bytes(byte_length_a, 'little')).strip(b'\x00') + b'\x00')
                fibonacci.write(bytearray(a.to_bytes(length, 'little')))

                b += a
                
if __name__ == '__main__':
        from signal import signal, SIGINT
        from sys import exit

        def handler(signal_received, frame):
                exit(0)

        # Tell Python to run the handler() function when SIGINT is received
        signal(SIGINT, handler)

        # Runs main function
        main()