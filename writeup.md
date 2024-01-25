level0: ghidra => exe level0 423, /bin/sh as level1, cat /home/user/level1/.pass
	pass: 1fe8a524fa4bec01ca4ea2a869af2a02260d4a7d5fe7e7c24d8617e6dca12d3a

level1: ghidra analysis to get payload and offset => craft_payload to tmp, cat /tmp/payload - | ./level1, cat /home/user/level2/.pass
	pass: 53a4a712787f40ec66c3c26c1f4b164dcad5552b038bb0addd69bf5bf6fa8e77

level2: same as 1 with craft_payload2
	pass: 492deb0e7d14c4b5695173cca843c4384fe52d0857c2b0718e1a521a4d33ec02

level3: same as 1 with craft_payload3
	pass: b209ea91ad69ef36f2cf0fcbbc24c739fd10464cf545b20bea8572ebdc3c36fa

level4: same as 1 with craft_payload4, ./level4 < /tmp/payload
	pass: 0f99ba5e9c446258a69b290407a6c60859e9c2d25b26575cafc9ae6d75e9456a

level5: same as 1 with craft_payload5
	pass: d3b7bf1025225bd715fa8ccb54ef06ca70b9125ac855aeab4878217177f41a31

level6:	same as 1 with craft_payload6, payload as argument
	pass: f73dcb7a06f60e3ccc608990b0a046359d42a1a0489ffeefd0d9cb2d7c9cb82d

level7: same as 1 with craft_payload7, payload and payload 2 as argument : ./level7 $(cat /tmp/payload) $(cat /tmp/payload2)
	pass: 5684af5cb4c8679958be4abe6373147ab52d95768e047820bf382e44fa8d8fb9

level8: exec level8 entry: auth 0123456789abcdef, then service 0123456789abcdef, then login then cat /home/user/level9/.pass
	pass: c542e581c5ba5162a85f767996e3247ed619ef6c6f7b76a59435545dc6259f8a

level9: same as 6 with craft_payload9, cat /home/user/bonus0/.pass
	pass: f3f0004b6f364cb5a4147e9ef827fa922a4861408845c26b6971ad770d906728