def main():
        fibonacci = open('fibonacci.txt','w')

        a = 0
        b = 1

        while True:
                fibonacci.write(hex(b)[2:len(hex(b))] + '\n')
                
                a+=b

                fibonacci.write(hex(a)[2:len(hex(a))] + '\n')

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
