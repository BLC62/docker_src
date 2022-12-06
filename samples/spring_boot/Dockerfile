FROM eclipse-temurin:11 

RUN apt-get update && apt-get install -y git maven

WORKDIR /tmp
RUN git clone https://github.com/Aenori/Spring_boot_sample.git && \ 
      rm -Rf Spring_boot_sample/.git && \
      mv Spring_boot_sample /app

WORKDIR /app

CMD ["bash", "-c", "mvn install && mvn spring-boot:run"]

