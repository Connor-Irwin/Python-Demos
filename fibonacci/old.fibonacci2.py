def main():
        fibonacci = open('fibonacci.txt','w')

        a = 0
        b = 1

        while True:
                new_bString = ""
                new_aString = ""

                bString = str(hex(b)[2:len(hex(b))])

                if len(bString) == 1:
                        bString = "0" + bString
                if len(bString) % 2 != 0:
                        bString = "0" + bString
                for i in range(0, len(bString) - 2):
                        if i % 2 == 0:
                                new_bString += "\\x" + bString[i : i+2]

                print("fibonacci.write('" + new_bString + "')")

                a+=b

                aString = str(hex(a)[2:len(hex(a))])

                if len(aString) == 1:
                        aString = "0" + aString
                if len(aString) % 2 != 0:
                        aString = "0" + aString
                for i in range(0, len(aString) - 2):
                        if i % 2 == 0:
                                new_aString += "\\x" + aString[i : i+2]

                print("fibonacci.write('" + new_aString + "')")

                b+=a

if __name__ == '__main__':
        from signal import signal, SIGINT
        from sys import exit

        def handler(signal_received, frame):
                fibonacci.close()

                exit(0)

        # Runs main function
        main()

        # Tell Python to run the handler() function when SIGINT is recieved
        signal(SIGINT, handler)
