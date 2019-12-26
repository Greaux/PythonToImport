section .text
	global _start
_start:
	push 0
	push 0x6e6f6874
	push 0x79702f6e
	push 0x69622f72
	push 0x73752f2f
	mov ebx, esp
	mov ecx, 0
	mov edx, 0
	mov eax, 0xb
	int 0x80
