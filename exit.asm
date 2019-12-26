section .text
	global _start

_start:

	mov bl, 1
	mov al, 0x1
	int 0x80

