class View:
    """
    ***************************
    * A view for a library DB *
    ***************************
    """
    def start(self):
        print('==================================')
        print('= Bienvenido a nuestra libreria! =')
        print('==================================')

    def end(self):
        print('================================')
        print('=        Hasta la vista!       =')
        print('================================')

    def main_menu(self):
        print('================================')
        print('=        Menu Principal        =')
        print('================================')
        print('1. Direcciones')
        print('2. Autores')
        print('3. Libros')
        print('4. Usuarios')
        print('5. Prestamos')
        print('6. Salir')

    def option(self,last):
        print('Selecciona un opcion (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('Opcion no valida!\nIntenta de nuevo')
    
    def ask(self, output):
        print(output, end = '' )
    
    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))
    
    def error(self, err):
        print(' ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))
    
    def dir_menu(self):
        print('*********************')
        print('* -- Submenu Dir -- *')
        print('*********************')
        print('1. Agregar CP')
        print('2. Mostrar CP')
        print('3. Mostrar todos los CPs')
        print('4. Mostrar CPs de una ciudad')
        print('5. Actualizar CP')
        print('6. Borrar CP')
        ##########Direcciones############33
        print('7. Agregar una dirección')
        print('8. Mostrar una dirección')
        print('9. Mostrar todas las direcciones')
        print('10. Mostrar todas las direcciones por CP')
        print('11. Actualizar dirección')
        print('12. Borrar dirección')
        print('13. Regresar')
    
    def show_a_zip(self, record):
        print(f'{record[0]:<6}|{record[1]:<35}|{record[2]:<35}')
    
    def show_zip_header(self, header):
        print(header.center(78,'*'))
        print('CP'.ljust(6)+'|'+'Ciudad'.ljust(35)+'|'+'Estado'.ljust(35))
        print('-'*78)

    def show_zip_midder(self):
        print('-'*78)
    
    def show_zip_footer(self):
        print('-'*78)
    
    ########################    DIRECCIONES #######################
    def show_a_dir(self, record):
        print(f'{record[1]:<25}|{record[2]:<25}|{record[3]:<8}|{record[4]:<8}|{record[5]:<6}')
    
    def show_dir_header(self, header):
        print(header.center(78,'*'))
        print('Calle'.ljust(25)+'|'+'Colonia'.ljust(25)+'|'+'Num Ext'.ljust(8)+'|'+'Num Int'.ljust(8)+'|'+'CP'.ljust(6))
        print('-'*78)

    def show_dir_midder(self):
        print('-'*78)
    
    def show_dir_footer(self):
        print('-'*78)


    def autor_menu(self):
        print('*********************')
        print('* -- Submenu Autor -- *')
        print('*********************')
        print('1. Agregar autor')
        print('2. Mostrar autor')
        print('3. Mostrar todos los autores')
        print('4. Mostrar autores por apellido paterno')
        print('5. Actualizar autor')
        print('6. Borrar autor')
        print('7. Regresar')
    
    def show_a_autor(self, record):
        print('Nombre:', record[1])
        print('Apellido paterno:', record[2])
        print('Apellido materno:', record[3])

    def show_autor_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)

    def show_autor_midder(self):
        print('-'*53)
    
    def show_autor_footer(self):
        print('*'*53)
        
    
    """
    ***********************
    * A view for libros   *
    ***********************
    """
    def libro_menu(self):
        print('**************************')
        print('* -- Submenu Libros   -- *')
        print('**************************')
        print('1. Agregar libro')
        print('2. Mostrar libro')
        print('3. Mostrar todos los libros')
        print('4. Mostrar libros por nombre')
        print('5. Actualizar libro')
        print('6. Borrar libro')
        print('7. Regresar')
    
    def show_a_libro(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Cantidad:', record[2])
        print('Edición:', record[3])
        print('Nombre del autor:', record[5]+ ' '+ record[6])
        
 
    
    def show_libro_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_libro_midder(self):
        print('-'*48)
    
    def show_libro_footer(self):
        print('*'*48)



    """
    ***********************
    * A view for usuarios *
    ***********************
    """
    def usuarios_menu(self):
        print('**************************')
        print('* -- Submenu usuarios -- *')
        print('**************************')
        print('1. Agregar usuario')
        print('2. Mostrar usuario')
        print('3. Mostrar todos los usuarios')
        print('4. Mostrar usuarios por un apellido paterno')
        print('5. Actualizar usuario')
        print('6. Borrar usuario')
        print('7. Regresar')
    
    def show_a_user(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Apellido paterno:', record[2])
        print('Apellido materno:', record[3])
        print('Telefono:', record[4])
        print('Email:', record[5])
        print('Dirección:', record[8]+' #'+record[10]+' Col.'+record[9]+' CP:'+record[7])
        
    
    def show_a_user_brief(self,record):
        print('ID:', record[0])
        print('Nombre:', record[1]+' '+record[2]+' '+record[3])
        print('Dirección:', record[8]+' #'+record[10]+' Col.'+record[9])
        print('Email:', record[5])
        print('Telefono:', record[4])
        

    def show_user_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)

    def show_user_midder(self):
        print('-'*53)
    
    def show_user_footer(self):
        print('*'*53)
    
    """
    ************************
    * A view for prestamos *
    ************************
    """
    
    def prestamo_menu(self):
        print('***************************')
        print('* -- Submenu prestamos -- *')
        print('***************************')
        print('1. Agregar prestamo')
        print('2. Leer prestamo')
        print('3. Leer todas los prestamos')
        print('4. Leer prestamos de un usuario')
        print('5. Actualizar prestamo')
        print('6. Borrar prestamo')
        print('7. Agregar detalles prestamo')
        print('8. Agregar libros al  prestamo')
        print('9. Leer detalles del prestamo')
        print('10. Leer todos los detalles del prestamo')
        print('11. Leer detalles del prestamo por libro')
        print('12. Actualizar un detalle del prestamo')
        print('13. Borrar detalle del prestamo')
        print('14. Regresar')
    
    def show_a_prestamo(self, record):
        print('ID del prestamo:', record[0])
        print('Fecha de prestamo',record[1])
        print('Fecha de devolución:', record[2])
        print('ID usuario: ', record[4])
        #self.show_a_user_brief(record[5:])
    
    def show_prestamo_header(self, header):
        print(header.center(81,'+'))


    def show_prestamo_midder(self):
        print('-'*81)
    
    def show_prestamo_adeudo(self, record):
        print('Aduedo total: '+str(record[3]))

    def show_prestamo_footer(self):
        print('+'*81)

    """
    *******************************
    * A view for prestamo details *
    *******************************
    """
    def show_a_prestamo_details(self, record):
        print(f'{record[0]:<5}|{record[1]:<20}|{record[2]:<20}|{record[3]:<11}')
    
    def show_prestamo_details_header(self):
        print('-'*81)
        print('ID'.ljust(5)+'|'+'ID libro'.ljust(20)+'|'+'Cantidad'.ljust(20)+'|'+'Adeudo total'.ljust(11))
        print('-'*81)

    def show_prestamo_details_footer(self):
        print('-'*81)