docker-machine create --driver virtualbox manager1
for it in $(seq 1 6); do
  docker-machine create --driver virtualbox manager$it;
done  
