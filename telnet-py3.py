#!/usr/bin/env python

# https://stackoverflow.com/questions/47087138/python3-telnet-read-all-doesnt-work

import telnetlib
import time
import socket
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def send_command(remote_conn, cmd):
  remote_conn.write(cmd)
  time.sleep(1)
  return remote_conn.read_very_eager()

def login(remote_conn, username, password):
  output = remote_conn.read_until(b"sername:", TELNET_TIMEOUT)
  remote_conn.write(username.encode('ascii') + b'\n')
  output += remote_conn.read_until(b"ssword:", TELNET_TIMEOUT)
  remote_conn.write(password.encode('ascii') + b'\n')
  return output

def telnet_connect(ip_addr):
  try:
    return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
  except socket.timeout:
    sys.exit("Connection timed-out")

def main():
  ip_addr = '184.105.247.70'
  username = 'pyclass'
  password = '88newclass'

  remote_conn = telnet_connect(ip_addr)
  output = login(remote_conn, username, password)
  print(output.decode('ascii'))
  time.sleep(1)
  output = remote_conn.read_very_eager()

  output = send_command(remote_conn, b'terminal length 0\n')
  output = send_command(remote_conn, b'show version\n')
  print(output.decode('ascii'))

  remote_conn.close

if __name__ == "__main__":
  main()



