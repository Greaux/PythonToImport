section .text 
	global _start
_start:
	xor eax, eax
	xor ebx, ebx
	mov bl,1
	mov al, 0x1
	int 0x80

