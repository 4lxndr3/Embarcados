# Valor original
a = 0x6DB7 # Calcula o complemento de bits
complement_value = a ^ 0xFFFF  # O operador ^ realiza a operação XOR bit a bit com 0xFFFF (todos os bits setados)
print(hex(complement_value)) # Imprime o resultado em formato hexadecimal

b = 0xA726 # Valor original de b
# Cálculo do complemento de bits
b_complement = ~b & ((1 << 16) - 1)  # Usando uma máscara de 16 bits
print(hex(b_complement)) # Impressão do resultado em formato hexadecimal

a = 0x6DB7  # 0110 1101 1011 0111
b = 0xA726  # 1010 0111 0010 0110
result_or = a | b  # Bitwise OR
expected_result = 0xEFB7
print("Resultado calculado em hexadecimal:", hex(result_or))
print("Resultado esperado em hexadecimal:", hex(expected_result))
print("Resultado calculado igual ao esperado?", result_or == expected_result)

a = 0b11010101  # 213 em decimal
b = 0b10011011  # 155 em decimal
result_and = a & b  # Bitwise AND
result_or = a | b   # Bitwise OR
result_xor = a ^ b  # Bitwise XOR
result_not_a = ~a   # Bitwise NOT
print("AND:", result_and)
print("OR:", result_or)
print("XOR:", result_xor)
print("NOT a:", result_not_a)

a = 0x6DB7  # 0110 1101 1011 0111
b = 0xA726  # 1010 0111 0010 0110
result_xor = a ^ b  # Bitwise XOR
print("Resultado em hexadecimal:", hex(result_xor))
print("Resultado em decimal:", result_xor)

num1 = 10
num2 = 7

resultado_and = num1 & num2
print("AND:", resultado_and)

resultado_or = num1 | num2
print("OR:", resultado_or)

resultado_xor = num1 ^ num2
print("XOR:", resultado_xor)

def bit_and_mask(num, mask):
    return num & mask
num = 0b101010
mask = 0b001100

resultado_and_mask = bit_and_mask(num, mask)
print("AND usando mascara:", bin(resultado_and_mask))

a = 0x6DB7  # 0110 1101 1011 0111
# Extrair os 6 bits mais à esquerda de a
b = (a >> 10) & 0x3F  # 0x3F é 111111 em binário (6 bits)
# Preencher os 10 bits mais à direita de b com zeros
b <<= 10  # Deslocar os bits à esquerda por 10 posições
print("Valor de b em hexadecimal:", hex(b))


a = 0x6DB7  # 0110 1101 1011 0111
# Transformar os 8 bits mais à esquerda de 'a' em 1s, mantendo os 8 bits mais à direita
b = (a & 0xFF) | 0xFF00  # 0xFF é 11111111 em binário
print("Valor de b em hexadecimal:", hex(b))

a = 0x6DB7  # 0110 1101 1011 0111
# Isolar os 8 bits mais à esquerda de 'a'
upper_bits = (a >> 8) & 0xFF  # Isola os 8 bits mais à esquerda de 'a'
# Criar um valor com os 8 bits mais à esquerda sendo 1s
upper_masked = upper_bits | 0xFF00  # Combina os 8 bits mais à esquerda de 'a' com 0xFF00
# Manter os 8 bits mais à direita de 'a'
lower_bits = a & 0xFF  # Isola os 8 bits mais à direita de 'a'
# Combinar os dois valores para formar 'b'
b = upper_masked | lower_bits
print("Valor de b em hexadecimal:", hex(b))


a = 0x6DB7  # 0110 1101 1011 0111
# Isolar os 8 bits mais à esquerda de 'a'
upper_bits = (a >> 8) & 0xFF
# Inverter os 8 bits menos significativos de 'a'
lower_bits = a & 0xFF  # Isolar os 8 bits menos significativos
inverted_lower_bits = ~lower_bits & 0xFF  # Inverter os bits e aplicar uma máscara para manter apenas 8 bits
# Combinar os valores para formar 'b'
b = (upper_bits << 8) | inverted_lower_bits
print("Valor de b em hexadecimal:", hex(b))

a = 0x6DB7
for _ in range(5):
    print("Valor de a:", hex(a))
    a ^= 0x4


def trocar_bits_menos_significativos(numero, novos_bits):
    # Isolar os bits menos significativos do número
    bits_menos_significativos = numero & 0b11
  # Limpar os bits menos significativos do número
    numero_sem_bits_menos_significativos = numero & ~0b11
    # Adicionar os novos bits menos significativos ao número
    novo_numero = numero_sem_bits_menos_significativos | novos_bits
    return novo_numero
a = 0x6DB7
novos_bits = 0b10  # Novos bits menos significativos
b = trocar_bits_menos_significativos(a, novos_bits)
print("Valor de b em hexadecimal:", hex(b))


def trocar_bits(numero, posicoes, novos_bits):
    mascara = novos_bits << posicoes  # Criar uma máscara com os novos bits deslocados para as posições corretas
    numero_modificado = (numero & ~mascara) | mascara  # Aplicar a máscara para trocar os bits
    return numero_modificado
a = 0x6DB7
posicoes = 3  # Bits 5, 4 e 3 correspondem às posições 5, 4 e 3 a partir da direita
novos_bits = 0b101  # Novos bits que você deseja usar
b = trocar_bits(a, posicoes, novos_bits)
print("Valor de b em hexadecimal:", hex(b))

# Deslocamento à esquerda (<<)
a = 0b1010  # Valor binário 10
deslocamento_esquerda = a << 2  # Deslocar 2 posições à esquerda
print("Deslocamento à esquerda:", bin(deslocamento_esquerda))  # Resultado: 101000 (40 em decimal)
# Deslocamento à direita (>>)
b = 0b110110  # Valor binário 54
deslocamento_direita = b >> 3  # Deslocar 3 posições à direita
print("Deslocamento à direita:", bin(deslocamento_direita))  # Resultado: 110 (6 em decimal)


a = 0b11011010  # Valor binário 218
deslocamento_direita = a >> 3  # Deslocar 3 posições à direita
print("Original:", bin(a))  # Resultado: 0b11011010
print("Deslocado:", bin(deslocamento_direita))  # Resultado: 0b00011011 (27 em decimal)