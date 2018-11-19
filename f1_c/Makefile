CC=gcc
CFLAGS = -g

all: udp_client

udp_client: udp_client.o
	$(CC) -o udp_client udp_client.o

udp_client.o: udp_client.c

clean:
	rm -f udp_client udp_client.o
