# ![pydruid logo](assets/pdlogo.svg) PyDruid

<div style={text_align: center;}>
<img src="assets/terminal.png">
</div>

PyDruid is the first ever Druid compiler that I wrote. It's basically meant to compile the actual Druid compiler in written in Druid, which is compiled to machine code rather than being a bunch of Python scripts.

## Install
Simply you don't install it. You need just a requeriment to run it, which is Python (and preferably running on Linux). The compiler is called by running the file ```druidc```, in the root directory of the git repository.

## Compile
If you have your Druid source code done, you need pass all the files to the compiler with the ```compile``` option. There's a JSON file containing the compiler default properties in the same path of the git repo, so you can modify the C compiler and its flags. By default, it uses GCC with no flags.
```
$ ./druidc compile example.druid
```
Of course, you need to change ```example.druid``` by all your files. All the dependencies __must__ be satisfied, because the compiler will crash with an error if any dependency is broken, so __make sure__ you import __all__ the required Druid files.

## Other options
The compiler can do more things, such as initializing projects, for example. It basically does everything that the actual Druid compiler does, so if you want to get a list with all the available options, just use the option ```help```.
