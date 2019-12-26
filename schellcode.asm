
section .text
	global _start
_start:
	push 0x006e6f68
	push 0x7479702f
	push 0x6e69622f
	push 0x7273752f

	mov ebx, esp
	mov ecx, 0
	mov edx, 0
	mov eax, 0xb
	int 0x80
