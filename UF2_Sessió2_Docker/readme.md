# M15_UF2 Ciencies Òmiques - Muntatge d'entorns Docker.

### Autor: Pablo Garcia
### Redacció: Miquel Angel Amorós

Avui investigarem i provarem algunes de les imatges que disposa DockerHub per muntar un contenidor amb un entorn de desenvolupament (Python, PHP...)

Al final de la sessió 1 vam muntar un HelloWorld. Repassem:
- Imatge: Fitxers i directoris comprimits que contenen tot el necessari.
- Contenidor: Procés aïllat 
- Virtualitzador: Compartim el Hardware i el Sistema Operatiu del Host.

## Imatges de dockerhub.

DockerHub:
https://hub.docker.com

Important mirar la informació de les imatges.
- Tag: La versió. Si surt **lastest** és que és la última versió.

## Historial dels contenidors arrencats.

Ho hem de fer amb aquesta comanda, per mostrar tots els contenidors arrencats:
docker container ls -a

```sh
(base) mamorosal@pop-os:~$ docker container ls -a
CONTAINER ID   IMAGE                COMMAND                  CREATED      STATUS                    PORTS     NAMES
ebb885dcb2bf   rapidfort/flaskapp   "/bin/sh -c 'uwsgi -…"   2 days ago   Exited (30) 2 days ago              practical_wu
b251529948c0   hello-world          "/hello"                 2 days ago   Exited (0) 2 days ago               bold_meitner
```

Els NAMES que assigan Docker són aleatoris.
El COMMAND és important:

Podem veure més opcions:

```sh
(base) mamorosal@pop-os:~$ docker container ls --help

Usage:  docker container ls [OPTIONS]

List containers

Aliases:
  ls, ps, list

Options:
  -a, --all             Show all containers (default shows just running)
```

Podem posar el nostre nom de contenidor:

```sh
docker container run hello-world -name green-donatello
```


### Eliminar contenidors

**Prune** -> Els elimina tots.
Però guarda l'estat dels contenidors per si volem tornar-lo a aixecar en una altre sessió.


```sh
(base) mamorosal@pop-os:~$ docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
b96422344b6e5906ef57b7a0b068d17f4ba1d655cc9d1b9610136333fa2804cb
ebb885dcb2bf33c6776a84458f4e30cc1260c2f2d1d7dc17bf4e8909366b2ef0
b251529948c031f93955d6c7e3e00f14814dae561768f8834e63420b92e2e5d5
Total reclaimed space: 148.4kB
(base) mamorosal@pop-os:~$ docker container ls -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## Baixem una distro de Linux amb Docker.

Fedora, Ubuntu, Alpine (muy ligera, ideal per a deployment)

Però com a developers, triem Ubuntu, ens la descarreguem:

```sh
(base) mamorosal@pop-os:~$ docker image pull ubuntu 
Using default tag: latest
latest: Pulling from library/ubuntu
6e3729cf69e0: Already exists 
Digest: sha256:27cb6e6ccef575a4698b66f5de06c7ecd61589132d5a91d098f7f3f9285415a9
Status: Downloaded newer image for ubuntu:latest
docker.io/library/ubuntu:latest
```

Si volem, podem eliminar la imatge de hello-world:

```sh
(base) mamorosal@pop-os:~$ docker image rm hello-world:latest
Untagged: hello-world:latest
Untagged: hello-world@sha256:c77be1d3a47d0caf71a82dd893ee61ce01f32fc758031a6ec4cf1389248bb833
Deleted: sha256:feb5d9fea6a5e9606aa995e879d862b825965ba48de054caab5ef356dc6b3412
Deleted: sha256:e07ee1baac5fae6a26f30cabfe54a36d3402f96afda318fe0a96cec4ca393359
```

Ja no podrem crear més contenidors amb aquesta imatge :( ens la hauriem de tornar a baixar.


### Arrenquem la distro d'Ubuntu

Abans, mirem quina versió de PopOS tenim:

```sh
(base) mamorosal@pop-os:~$ uname -a
Linux pop-os 5.17.5-76051705-generic #202204271406~1653440576~22.04~6277a18 SMP PREEMPT Wed May 25 01 x86_64 x86_64 x86_64 GNU/Linux
```

Ara, arrenquem un contenidor d'Ubuntu amb la imatge descarregada. Ocupa molt menys que una ISO.

Què vol dir -it --> 2 paràmetres: -i Interactive - t terminal

```sh
(base) mamorosal@pop-os:~$ docker container run -it ubuntu bash
root@c8c6f009ed71:/# 
```

**Enhorabona, hem entrat com root :D**

Fixeu-vos que el nostre container utilitza el Kernel del Host:

```sh
root@c8c6f009ed71:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@c8c6f009ed71:/# uname -a
Linux c8c6f009ed71 5.17.5-76051705-generic #202204271406~1653440576~22.04~6277a18 SMP PREEMPT Wed May 25 01 x86_64 x86_64 x86_64 GNU/Linux
root@c8c6f009ed71:/# 
```

### Instal·lar programes al nostre contenidor.

Hem de fer un update abans que res.

```sh
root@c8c6f009ed71:/# nano    
bash: nano: command not found
root@c8c6f009ed71:/# sudo apt install nano
bash: sudo: command not found
root@c8c6f009ed71:/# apt update
Get:1 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy InRelease [270 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [114
.....
```sh

Ara ja podem instal·lar i usar programes amb l'apt

```sh
apt install nano
.....
nano
```

Recordeu que per sortir de nano es Ctrl+X, Ctrl+O guardar.

Instal·lem més coses:
```sh
apt install tree
nano
```
