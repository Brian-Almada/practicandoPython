# Strings

my_string =  'My String'
my_other_string = "otro string"

my_strings = my_string, my_other_string

print(my_string + " " + my_other_string)
print(my_string + " " + my_other_string)
print(my_string + " y " + my_other_string)

my_new_line_string = 'Este es un \n salto de línea'
print(my_new_line_string)

my_tab_string = '\t Este es un texto con tabulación'
print(my_tab_string)

my_scape_string = '\\t Este es un texto \\n con escapado'
print(my_scape_string)

# Formateo

name, surname, age = 'Brian', 'Almada', 32

print('Mi nombre es {}, mi apellido es {} y mi edad es de {} años'.format(name, surname, age))
print('Mi nombre es %s, mi apellido es %s y mi edad es de %d años' %(name, surname, age))
print(f'Mi nombre es {name}, mi apellido es {surname} y mi edad es de {age} años')