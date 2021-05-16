<div align="center">
    <img src="../assets/pdlogo.svg" title="Druid" width=70%>
</div>

# Compile Druid

## ![](../assets/worm.svg) Requirements
You need the following software in order to compile Druid.
- ```python3```
- ```git```
- ```gcc```

### Install on Debian-based distros
```
# apt install python3 git gcc
```

### Install on Arch-based distros
```
# pacman -S python git gcc
```

## ![](../assets/worm.svg) Clone the Druid repository
```
$ git clone https://github.com/sergiolabora/DruidLang.git
```

## ![](../assets/worm.svg) Compile
Navigate to the git repository and open a terminal there. Then, allow execution to the file ```setup``` and run it with the compile option.

```
$ chmod +x setup
$ ./setup compile
```

During this process, the PyDruid repository will be downloaded, so you __need__ internet conection.

## ![](../assets/worm.svg) Install
Like compiling, but using ```install``` instead of ```compile``` and running as root.

```
# ./setup install
```
