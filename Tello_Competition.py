# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....


print("\nOlivia Strombeck, Corbin Hanson")
print("Program Name: Tello Drones Hoop Competition")
print("Date: 3.26.2025")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command', 1)
        sendmsg('takeoff')


        # Commit Message: First hoop - Stable
        sendmsg('forward 200', 8)

        # Commit Message: Second Hoop - Stable - ascend to third hoop
        #              X Y Z  x2 y2 z2 Speedh
        def speed_value
        sendmsg(speed_value = speed)
        sendmsg(speed=50)

        sendmsg('curve 10 0 0 10 15 10')
        #sendmsg ('curve -1 00 0 100 100 0 50', speed = 50)
        # Commit Message: Third Hoop - Stable


        # Commit Message: Final Hoop - Stable


        sendmsg('land')

        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()

