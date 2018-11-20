//
//
// Udp client for recieving data from a udp steam sent out by codemasters f1 2018 game
//
// Author: Kristian Nilssen
//

#include <stdio.h>      /* for printf() and fprintf() */
#include <sys/socket.h> /* for socket(), connect(), sendto(), and recvfrom() */
#include <arpa/inet.h>  /* for sockaddr_in and inet_addr() */
#include <stdlib.h>     /* for atoi() and exit() */
#include <string.h>     /* for memset() */
#include <unistd.h>     /* for close() */
#include <stdint.h>
#include "structs.h"       /* for f1 2018 UDP packet structs  */

#define MAXRECVSTRING 1341
#define HEADERSTRING 21

int main(int argc, char *argv[]) {

  int sock;                         /* Socket */
  struct sockaddr_in broadcastAddr; /* Broadcast Address */
  unsigned short broadcastPort;     /* Port */
  char recvString[MAXRECVSTRING+1]; /* Buffer for received string */
  int recvStringLen;                /* Length of received string */
  char recvString_header[21];

  if (argc != 2)    /* Test for correct number of arguments */
  {
      fprintf(stderr,"Usage: %s <Broadcast Port>\n", argv[0]);
      exit(1);
  }

  broadcastPort = atoi(argv[1]);   /* First arg: broadcast port */

  /* Create a best-effort datagram socket using UDP */
  if ((sock = socket(PF_INET, SOCK_DGRAM, 0)) < 0) {
    perror("cannot create socket\n");
		return 0;
  }


  /* Construct bind structure */
  memset(&broadcastAddr, 0, sizeof(broadcastAddr));   /* Zero out structure */
  broadcastAddr.sin_family = AF_INET;                 /* Internet address family */
  broadcastAddr.sin_addr.s_addr = htonl(INADDR_ANY);  /* Any incoming interface */
  broadcastAddr.sin_port = htons(broadcastPort);      /* Broadcast port */

  /* Bind to the broadcast port */
  if (bind(sock, (struct sockaddr *) &broadcastAddr, sizeof(broadcastAddr)) < 0) {
  	perror("bind failed");
  	return 0;
	}


  // Now loop, receiving data from our udp socket listning for udp packets from f1 2018
  for (;;) {
    recvStringLen = recvfrom(sock, recvString, MAXRECVSTRING, 0, NULL, 0);
    if (recvStringLen > 0) {
      recvString[recvStringLen] = '\0';
      strncpy (recvString_header, recvString, 21);
      struct PacketHeader *packet = (struct PacketHeader *)&recvString_header;
			// printf("Received packet with id: %hhu\n", packet->m_packetId);

      // Switch statement to handle which packet we received
      switch(packet->m_packetId) {
        case 0 :
          printf("Received Motion data packet");
          break;
        case 1 :
          printf("Received Session data packet");
          break;
        case 2 :
          printf("Received Lap data packet");
          break;
        case 3 :
          printf("Received Event packet");
          break;
        case 4 :
          printf("Received Participants packet");
          break;
        case 5 :
          printf("Received Car Setups packet");
          break;
        case 6 :
          printf("Received Car Telemetry packet");
          break;
        case 7 :
          printf("Received Car Status packet");
          break;
      }
		}
  }

}
