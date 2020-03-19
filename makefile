do_all:
		make -j 3  test1 test2 test4 test3   

test1:
			ip=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
test2:
			xhost + 

test4:
			socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$(DISPLAY)\"

test3:
			docker run -it  -e DISPLAY=$(ip):0 -v /tmp/.X11-unix:/tmp/.X11-unix  28b542bb8774

