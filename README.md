Multichannel AM transmitter, using GNURADIO with fl2k USB adaptor.
Needs pre-installed osmocom fl2k drives and ffmpeg.
Info here-> https://osmocom.org/projects/osmo-fl2k/wiki and here-> https://ffmpeg.org/

Operation:
1. Open the GnuRadioCompanion with the "am_xmit_multi_noGUI_fl2kUDP.grc" and start execution.

2. Start the "ffmpegURLStreams" script in an open terminal. (chmod 755 for execution)
   
3. Open another terminal and connect the fl2k with the output TCP stream-> "fl2k_tcp -p 25000 -s 8192000"


Connect any receiver to the red output channel of your fl2k. Please protect your device by using DC blocker and filter elements. 

Please obey your local regulations and aviod any unintended transmission or interference of radio services.

Enjoy several AM channels like in the good old days with your AM Radio receivers.


Goal:
-lower CPU load by resigning any form of GUI elements in the gnu radio companion.
-content feed by using web life streams adaped by ffmpeg submitted netcat via UDP 
-motivated by this thread-> https://radio-bastler.de/forum/showthread.php?tid=12946&page=11


Improvments:
Channel adaptation to your personal taste.
Level adjustments
Commit execution into a single script.
