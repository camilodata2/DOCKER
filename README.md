# 🐳 a_brief_Docker_course
<h1 aling="center"> What's Docker </h1>
Docker is an open source platform that enables developers to build, deploy, run, update and manage containers—standardized
Executable components that combine application source code with the operating system (OS) libraries and dependencies required to run
That code in any environ# 🐳 a_brief_Docker_course
<h1 aling="center"> What's Docker </h1>
Docker is an open source platform that enables developers to build, deploy, run, update and manage containers—standardized
Executable components that combine application source code with the operating system (OS) libraries and dependencies required to run
That code in any environment.

## 🤤 Install docker on ubunto 
On this subject there are many videos on youtube or any technology platform, but I will give you the steps to make it easier.
just following the steps below
 1. [sudo apt update](#id1)
 2. [sudo apt install apt-transport-https ca-certificates curl software-properties-common](#id2)
 3. [curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg](#id3)
 4. [echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null](#id4)
 5. [sudo apt update](#id5)
 6. [sudo apt install docker-ce docker-ce-cli containerd.io](#id6)
 7. [docker --version](#id7)

### ⚒️ Docker concepts 
1. [BIND MOUNT](#id1)
2. [VOLUME](#id2)
3. [CONTAINER](#id3)

#### 😮‍💨 BIND MOUNT
A bind mount in Docker is a method of mounting a directory from the host machine into a container
It allows you to link a specific directory or file on the host system to a corresponding location within the container
##### 😐 VOLUME
 a volume is a way to persistently store and manage data generated or used by containers
 Volumes provide a mechanism for separating data from the container itself, allowing data to be shared and reused across multiple containers.

###### 🥳 CONTAINER
A Docker container is a lightweight, standalone, and executable package that includes everything needed to run a piece of software
Including the code, runtime, system tools, libraries, and settings.

 <img src="https://miro.medium.com/v2/resize:fit:1079/1*3ds-PdxGGMN-ZzJH95_lsA.png" alt="Texto alternativo" width="500" height="200">



